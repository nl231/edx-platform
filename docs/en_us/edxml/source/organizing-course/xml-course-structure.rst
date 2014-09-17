.. edXML Course Structure:

##########################
edXML Course Structure
##########################

As you develop your course in edXML, you start by creating the structure of the
courseware.

*************************************
Understanding Course Building Blocks
*************************************

Before you begin building your edXML course, you should understand the building
blocks of an edX course.

* Each course starts with a course outline, which contains one or more
  sections.

* Course sections are at the top level of your course and typically represent
  a time period.

* A section contains one or more subsections. Course subsections are parts of a
  section, and usually represent a topic or other organizing principle.

* A subsection contains one or more units.

* Course units are lessons in a subsection that students view as single pages.
  A unit contains one or more components. Course components are objects within
  units that contain your actual course content.

********************
The course.xml File
********************

Each course starts with a ``course.xml`` file, which is located in the top level directory.

The``course.xml`` file has one element, ``course``, which defines the main URL for the course, the course name, and the organization.

For example, the ``course.xml`` file for the edX Demo course is:

.. code-block:: xml
  
  <course url_name="Demo_Course" org="edX" course="DemoX"/>

The ``course`` element does not contain any child elements.


==========================
course element attributes
==========================

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The value in the course URL path directly after the domain,
       organization, and course name.
   * - ``org``
     - The organization sponsoring the course. This value is in the course URL
       path, following the domain and ``/courses/``.
   * - ``course``
     - The name of the course. This value is in the course URL
       path, following the organization`.


==========================================
course element attributes and course URLS
==========================================

The attributes of the ``course`` element are used to construct URLs in the
course.  For example, the following course URL shows where these values are used:

.. code-block:: html
  
  http://my-edx-server.org/courses/@org/@course/@url/info



****************************
The Course Outline XML File
****************************




************************
Course Section XML Files
************************



****************************
Course Subsection XML Files
****************************



****************************
Course Unit XML Files
****************************
