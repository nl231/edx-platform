from django.contrib.auth.models import User
from rest_framework import serializers

from course_groups.cohorts import is_course_cohorted
from course_groups.models import CourseUserGroup
from notification_prefs import NOTIFICATION_PREF_KEY
from lang_pref import LANGUAGE_KEY
from student.models import UserProfile
from user_api.models import UserPreference


# N.B. This is designed to work well with prefetch_related and select_related,
# which require the use of all() instead of get() or filter()
class NotifierUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("get_name")
    preferences = serializers.SerializerMethodField("get_preferences")
    course_info = serializers.SerializerMethodField("get_course_info")

    def get_name(self, user):
        return user.profile.name

    def get_preferences(self, user):
        return {
            pref.key: pref.value
            for pref
            in user.preferences.all()
            if pref.key in [LANGUAGE_KEY, NOTIFICATION_PREF_KEY]
        }

    def get_course_info(self, user):
        cohort_id_map = {
            cohort.course_id: cohort.id
            for cohort in user.course_groups.all()
        }
        see_all_cohorts_set = {
            role.course_id
            for role in user.roles.all()
            for perm in role.permissions.all() if perm.name == "see_all_cohorts"
        }
        return {
            enrollment.course_id.to_deprecated_string(): {
                "cohort_id": cohort_id_map.get(enrollment.course_id),
                "see_all_cohorts": (
                    enrollment.course_id in see_all_cohorts_set or
                    not is_course_cohorted(enrollment.course_id)
                ),
            }
            for enrollment in user.courseenrollment_set.all()
        }

    class Meta:
        model = User
        # This list is the minimal set required by the notification service
        fields = ("id", "email", "name", "preferences", "course_info")
        read_only_fields = ("id", "email")
