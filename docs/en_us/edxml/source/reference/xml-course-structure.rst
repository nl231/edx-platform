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

Each course starts with a course.xml file, which is located in the top level directory.

The course.xml file has one element, ''course''.

For example, the course.xml file for the edX Demo course is:

.. code-block:: xml
  
  <course url_name="Demo_Course" org="edX" course="DemoX"/>


===================
course attributes
===================




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
