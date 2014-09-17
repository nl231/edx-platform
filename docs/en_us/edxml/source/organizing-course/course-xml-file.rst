.. _The course.xml File:

##########################
The ``course.xml`` File
##########################

You begin developing a course with a ``course.xml`` file, which you place in the top level directory.

See:

* `course.xml File Elements`_
* `course Element Attributes`_
* `course Element Attributes and Course URLS`_

*************************************
``course.xml`` File Elements
*************************************

The root element of the ``course.xml`` file is ``course``. 

The ``course`` element does not contain any child elements.

For example, the ``course.xml`` file for the edX Demo course contains:

.. code-block:: xml
  
  <course url_name="Demo_Course" org="edX" course="DemoX"/>


*************************************
``course`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The value in the course URL path directly after the domain,
       organization, and course name. The url_name must also be the name of the course outline XML file (without the ``.xml`` extension).
   * - ``org``
     - The organization sponsoring the course. This value is in the course URL
       path, following the domain and ``/courses/``.
   * - ``course``
     - The name of the course. This value is in the course URL
       path, following the organization.


**********************************************
``course`` Element Attributes and Course URLS
**********************************************

The attributes of the ``course`` element are used to construct URLs in the
course.  The following course URL shows where these values are used:

.. code-block:: html
  
  http://my-edx-server.org/courses/<@org value>/<@course value>/<@url value>/info

For example:

.. code-block:: html
  
  http://my-edx-server.org/courses/edX/DemoX/Demo_Course/info
