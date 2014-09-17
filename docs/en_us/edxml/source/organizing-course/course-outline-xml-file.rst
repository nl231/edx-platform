.. _The Course Outline XML File:

############################
The Course Outline XML File
############################

The course outline file:

* Defines common settings for your course.
* Organizes sections, or chapters, in your course.
  
See:
* `Create the Course Outline File`_
* `The Course Outline File Elements`_
* `course Element Attributes`_
* `Example Course Outline File`_

*******************************
Create the Course Outline File
*******************************

You create the course outline XML file in the ``course`` directory.

The name of the course outline file must match the value of the @url attribute
of the ``course`` element in the ``courses.xml`` file.

For example, if the ``course.xml`` file contains:

.. code-block:: xml
  
  <course url_name="Demo_Course" org="edX" course="DemoX"/>

You create the file ``course/Demo_Course.xml``.

*************************************
The Course Outline File Elements
************************************* 

The root element of the ``course.xml`` file is ``course``. 

The ``course`` element contains the following child elements:

* One or more ``chapter`` elements.
* Optionally, a ``wiki`` element.

================
chapter Element
================

The ``chapter`` element references a chapter, or section, in the course.

The ``chapter`` element contains one attribute.

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The unique identifier for the chapter. The url_name must be the name of
       the chapter XML file (without the ``.xml`` extension).

================
wiki Element
================

The ``wiki`` element defines the wiki used in the course.

.. note:: 
  The edX Platform uses a single wiki for all courses, but you can segment the
  wiki by course by using a unique value for the ``slug`` attribute in the
  ``wiki`` element.

The ``wiki`` element contains one attribute.

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``slug``
     - The unique identifier for the segment of the wiki to use in this course.
       Students in the course only see this segment of the wiki.


*************************************
``course`` Element Attributes
*************************************

WE NEED COMPLETE ADVANCED SETTINGS DOCUMENTATION TO DO THIS

*************************************
Example Course Outline File
*************************************

The following example shows a course outline file with three chapters
(sections) and a course wiki:

.. code-block:: xml
  
  <course advanced_modules="[&quot;annotatable&quot;,
      &quot;combinedopenended&quot;, &quot;peergrading&quot;, &quot;lti&quot;,
      &quot;word_cloud&quot;]" display_name="Manual Smoke Test Course 1"
      lti_passports="[&quot;ims:12345:secret&quot;]"
      pdf_textbooks="[{&quot;tab_title&quot;: &quot;An Example Paper&quot;,
      &quot;id&quot;: &quot;0An_Example_Paper&quot;, &quot;chapters&quot;:
      [{&quot;url&quot;: &quot;/static/1.pdf&quot;, &quot;title&quot;:
      &quot;Introduction &quot;}]}]" show_calculator="true" show_chat="true"
      start="2014-06-26T00:00:00Z"> 
      <chapter url_name="a64a6f63f75d430aa71e6ce113c5b4d2"/> 
      <chapter url_name="d68c2861c10a4c9d92a679b4cfc0f924"/> 
      <chapter url_name="ab97a6dbfafd48868c36bed4c8c5391d"/> 
      <wiki slug="ManTestX.ManTest1.2014"/> 
  </course>

