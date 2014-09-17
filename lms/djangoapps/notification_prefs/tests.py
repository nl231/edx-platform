import json

from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from mock import Mock, patch

from course_groups.models import CourseUserGroup
from django_comment_common.models import Role, Permission
from lang_pref import LANGUAGE_KEY
from notification_prefs import NOTIFICATION_PREF_KEY
from notification_prefs.views import (
    ajax_enable,
    ajax_disable,
    ajax_status,
    set_subscription,
    UsernameCipher,
    NotifierUsersListView,
)
from student.tests.factories import UserFactory, CourseEnrollmentFactory
from edxmako.tests import mako_middleware_process_request
from user_api.models import UserPreference
from util.testing import UrlResetMixin
from xmodule.modulestore.tests.factories import CourseFactory


TEST_API_KEY = "test_api_key"


@override_settings(SECRET_KEY="test secret key")
class NotificationPrefViewTest(UrlResetMixin, TestCase):
    INITIALIZATION_VECTOR = "\x00" * 16

    @classmethod
    def setUpClass(cls):
        # Make sure global state is set up appropriately
        Client().get("/")

    @patch.dict("django.conf.settings.FEATURES", {"ENABLE_DISCUSSION_SERVICE": True})
    def setUp(self):
        super(NotificationPrefViewTest, self).setUp()
        self.user = UserFactory.create(username="testuser")
        # Tokens are intentionally hard-coded instead of computed to help us
        # avoid breaking existing links.
        self.tokens = {
            self.user: "AAAAAAAAAAAAAAAAAAAAAA8mMQo96FZfb1YKv1R5X6s=",
            # Username with length equal to AES block length to test padding
            UserFactory.create(username="sixteencharsuser"):
            "AAAAAAAAAAAAAAAAAAAAAPxPWCuI2Ay9TATBVnfw7eIj-hUh6erQ_-VkbDqHqm8D",
            # Even longer username
            UserFactory.create(username="thisusernameissoveryverylong"):
            "AAAAAAAAAAAAAAAAAAAAAPECbYqPI7_W4mRF8LbTaHuHt3tNXPggZ1Bke-zDyEiZ",
            # Non-ASCII username
            UserFactory.create(username=u"\u4e2d\u56fd"):
            "AAAAAAAAAAAAAAAAAAAAAMjfGAhZKIZsI3L-Z7nflTA="
        }
        self.request_factory = RequestFactory()

    def create_prefs(self):
        """Create all test preferences in the database"""
        for (user, token) in self.tokens.items():
            UserPreference.objects.create(user=user, key=NOTIFICATION_PREF_KEY, value=token)

    def assertPrefValid(self, user):
        """Ensure that the correct preference for the user is persisted"""
        pref = UserPreference.objects.get(user=user, key=NOTIFICATION_PREF_KEY)
        self.assertTrue(pref)  # check exists and only 1 (.get)
        # now coerce username to utf-8 encoded str, since we test with non-ascii unicdoe above and
        # the unittest framework has hard time coercing to unicode.
        # decrypt also can't take a unicode input, so coerce its input to str
        self.assertEqual(str(user.username.encode('utf-8')), UsernameCipher().decrypt(str(pref.value)))

    def assertNotPrefExists(self, user):
        """Ensure that the user does not have a persisted preference"""
        self.assertFalse(
            UserPreference.objects.filter(user=user, key=NOTIFICATION_PREF_KEY).exists()
        )


class AjaxViewsTest(NotificationPrefViewTest):
    # AJAX status view

    def test_ajax_status_get_0(self):
        request = self.request_factory.get("dummy")
        request.user = self.user
        response = ajax_status(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"status":0})

    def test_ajax_status_get_1(self):
        self.create_prefs()
        request = self.request_factory.get("dummy")
        request.user = self.user
        response = ajax_status(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"status":1})

    def test_ajax_status_post(self):
        request = self.request_factory.post("dummy")
        request.user = self.user
        response = ajax_status(request)
        self.assertEqual(response.status_code, 405)

    def test_ajax_status_anon_user(self):
        request = self.request_factory.get("dummy")
        request.user = AnonymousUser()
        self.assertRaises(PermissionDenied, ajax_status, request)

    # AJAX enable view

    def test_ajax_enable_get(self):
        request = self.request_factory.get("dummy")
        request.user = self.user
        response = ajax_enable(request)
        self.assertEqual(response.status_code, 405)
        self.assertNotPrefExists(self.user)

    def test_ajax_enable_anon_user(self):
        request = self.request_factory.post("dummy")
        request.user = AnonymousUser()
        self.assertRaises(PermissionDenied, ajax_enable, request)
        self.assertNotPrefExists(self.user)

    @patch("Crypto.Random.new")
    def test_ajax_enable_success(self, mock_random_new):
        mock_stream = Mock()
        mock_stream.read.return_value = self.INITIALIZATION_VECTOR
        mock_random_new.return_value = mock_stream

        def test_user(user):
            request = self.request_factory.post("dummy")
            request.user = user
            response = ajax_enable(request)
            self.assertEqual(response.status_code, 204)
            self.assertPrefValid(user)

        for user in self.tokens.keys():
            test_user(user)

    def test_ajax_enable_already_enabled(self):
        self.create_prefs()
        request = self.request_factory.post("dummy")
        request.user = self.user
        response = ajax_enable(request)
        self.assertEqual(response.status_code, 204)
        self.assertPrefValid(self.user)

    def test_ajax_enable_distinct_values(self):
        request = self.request_factory.post("dummy")
        request.user = self.user
        ajax_enable(request)
        other_user = UserFactory.create()
        request.user = other_user
        ajax_enable(request)
        self.assertNotEqual(
            UserPreference.objects.get(user=self.user, key=NOTIFICATION_PREF_KEY).value,
            UserPreference.objects.get(user=other_user, key=NOTIFICATION_PREF_KEY).value
        )

    # AJAX disable view

    def test_ajax_disable_get(self):
        self.create_prefs()
        request = self.request_factory.get("dummy")
        request.user = self.user
        response = ajax_disable(request)
        self.assertEqual(response.status_code, 405)
        self.assertPrefValid(self.user)

    def test_ajax_disable_anon_user(self):
        self.create_prefs()
        request = self.request_factory.post("dummy")
        request.user = AnonymousUser()
        self.assertRaises(PermissionDenied, ajax_disable, request)
        self.assertPrefValid(self.user)

    def test_ajax_disable_success(self):
        self.create_prefs()
        request = self.request_factory.post("dummy")
        request.user = self.user
        response = ajax_disable(request)
        self.assertEqual(response.status_code, 204)
        self.assertNotPrefExists(self.user)

    def test_ajax_disable_already_disabled(self):
        request = self.request_factory.post("dummy")
        request.user = self.user
        response = ajax_disable(request)
        self.assertEqual(response.status_code, 204)
        self.assertNotPrefExists(self.user)


class SetSubscriptionTest(NotificationPrefViewTest):
    def test_unsubscribe_post(self):
        request = self.request_factory.post("dummy")
        response = set_subscription(request, "dummy", subscribe=False)
        self.assertEqual(response.status_code, 405)

    def test_unsubscribe_invalid_token(self):
        def test_invalid_token(token, message):
            request = self.request_factory.get("dummy")
            self.assertRaisesRegexp(Http404, "^{}$".format(message), set_subscription, request, token, False)

        # Invalid base64 encoding
        test_invalid_token("ZOMG INVALID BASE64 CHARS!!!", "base64url")
        test_invalid_token("Non-ASCII\xff", "base64url")
        test_invalid_token(self.tokens[self.user][:-1], "base64url")

        # Token not long enough to contain initialization vector
        test_invalid_token("AAAAAAAAAAA=", "initialization_vector")

        # Token length not a multiple of AES block length
        test_invalid_token(self.tokens[self.user][:-4], "aes")

        # Invalid padding (ends in 0 byte)
        # Encrypted value: "testuser" + "\x00" * 8
        test_invalid_token("AAAAAAAAAAAAAAAAAAAAAMoazRI7ePLjEWXN1N7keLw=", "padding")

        # Invalid padding (ends in byte > 16)
        # Encrypted value: "testusertestuser"
        test_invalid_token("AAAAAAAAAAAAAAAAAAAAAC6iLXGhjkFytJoJSBJZzJ4=", "padding")

        # Invalid padding (entire string is padding)
        # Encrypted value: "\x10" * 16
        test_invalid_token("AAAAAAAAAAAAAAAAAAAAANRGw8HDEmlcLVFawgY9wI8=", "padding")

        # Nonexistent user
        # Encrypted value: "nonexistentuser\x01"
        test_invalid_token("AAAAAAAAAAAAAAAAAAAAACpyUxTGIrUjnpuUsNi7mAY=", "username")

    def test_unsubscribe_success(self):
        self.create_prefs()

        def test_user(user):
            request = self.request_factory.get("dummy")
            request.user = AnonymousUser()

            mako_middleware_process_request(request)
            response = set_subscription(request, self.tokens[user], subscribe=False)
            self.assertEqual(response.status_code, 200)
            self.assertNotPrefExists(user)

        for user in self.tokens.keys():
            test_user(user)

    def test_unsubscribe_twice(self):
        self.create_prefs()
        request = self.request_factory.get("dummy")
        request.user = AnonymousUser()

        mako_middleware_process_request(request)
        set_subscription(request, self.tokens[self.user], False)
        response = set_subscription(request, self.tokens[self.user], subscribe=False)
        self.assertEqual(response.status_code, 200)
        self.assertNotPrefExists(self.user)

    def test_resubscribe_success(self):
        def test_user(user):
            # start without a pref key
            self.assertFalse(UserPreference.objects.filter(user=user, key=NOTIFICATION_PREF_KEY))
            request = self.request_factory.get("dummy")
            request.user = AnonymousUser()

            mako_middleware_process_request(request)
            response = set_subscription(request, self.tokens[user], subscribe=True)
            self.assertEqual(response.status_code, 200)
            self.assertPrefValid(user)

        for user in self.tokens.keys():
            test_user(user)


@override_settings(EDX_API_KEY=TEST_API_KEY)
class NotifierUsersListViewTest(NotificationPrefViewTest):
    def setUp(self):
        super(NotifierUsersListViewTest, self).setUp()
        self.moderator = UserFactory.create(username="testmoderator")
        self.tokens[self.moderator] = "AAAAAAAAAAAAAAAAAAAAAJHMWxIpsgP14ZTocoW4bvY="
        self.create_prefs()
        self.cohorted_course = CourseFactory.create(
            number="Cohorts101",
            cohort_config={"cohorted": True}
        )
        self.non_cohorted_course = CourseFactory.create(number="NoCohorts101")
        moderator_perm = Permission(name="see_all_cohorts")
        moderator_perm.save()
        for course in [self.cohorted_course, self.non_cohorted_course]:
            for user in [self.user, self.moderator]:
                CourseEnrollmentFactory.create(user=user, course_id=course.id)
            moderator_role = Role(name="Moderator", course_id=course.id)
            moderator_role.save()
            moderator_role.permissions.add(moderator_perm)
            self.moderator.roles.add(moderator_role)

    def _get_results(self):
        request = RequestFactory().get("dummy", HTTP_X_EDX_API_KEY=TEST_API_KEY)
        response = NotifierUsersListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            set(response.data.keys()),
            {"count", "next", "previous", "results"}
        )
        return response.data["results"]

    def _assert_user_correct(self, results, user_obj, expected_course_info):
        result_user = next((result for result in results if result["id"] == user_obj.id), None)
        self.assertEqual(
            set(result_user.keys()),
            {"id", "email", "name", "preferences", "course_info"}
        )
        self.assertEqual(result_user["email"], user_obj.email)
        self.assertEqual(result_user["name"], user_obj.profile.name)
        self.assertEqual(
            set(result_user["preferences"].keys()),
            {NOTIFICATION_PREF_KEY} # TODO: Should also set and check for LANGUAGE_KEY
        )
        self.assertEqual(result_user["course_info"], expected_course_info)

    def test_without_api_key(self):
        request = RequestFactory().get("dummy")
        response = NotifierUsersListView.as_view()(request)
        self.assertEqual(response.status_code, 403)

    def test_get_without_cohorts_assigned(self):
        results = self._get_results()

        self._assert_user_correct(
            results,
            self.user,
            {
                self.cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": False,
                },
                self.non_cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": True,
                },
            }
        )
        self._assert_user_correct(
            results,
            self.moderator,
            {
                self.cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": True,
                },
                self.non_cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": True,
                },
            }
        )

    def test_get_with_cohorts_assigned(self):
        cohort = CourseUserGroup(
            name="Test Cohort",
            course_id=self.cohorted_course.id,
            group_type=CourseUserGroup.COHORT
        )
        cohort.save()
        for user in [self.user, self.moderator]:
            cohort.users.add(user)

        results = self._get_results()

        self._assert_user_correct(
            results,
            self.user,
            {
                self.cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": cohort.id,
                    "see_all_cohorts": False,
                },
                self.non_cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": True,
                },
            }
        )
        self._assert_user_correct(
            results,
            self.moderator,
            {
                self.cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": cohort.id,
                    "see_all_cohorts": True,
                },
                self.non_cohorted_course.id.to_deprecated_string(): {
                    "cohort_id": None,
                    "see_all_cohorts": True,
                },
            }
        )

    # Test cases:
    #   No enrollments?
    #   Different enrollments per user?
    #   Moderator in some but not all enrolled courses?
    #   Exclusion of excess preferences
    #   Pagination
