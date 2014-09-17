.. _Course Chapter XML Files:

############################
Course Chapter XML Files
############################

A course chapter file:

* Defines the display name and release date for the chapter
* Organizes subsections within the chapter.
  
See:
* `Create Course Chapter Files`_
* `Chapter File Elements`_
* `chapter Element Attributes`_
* `Example Chapter File`_

*******************************
Create Course Chapter Files
*******************************

You create a course chapter XML file in the ``chapter`` directory for each
chapter, or section, in your course.

The name of the chapter file must match the value of the @url_name attribute of
``chapter`` element in the course outline XML file.

For example, if the course outline file contains:

.. code-block:: xml
  
    <course> 
      <chapter url_name="exam_review"/> 
      . . .
    </course>

You create the file ``chapter/exam_review.xml`` to define the chapter.


*************************************
Chapter File Elements
************************************* 

The root element of the chapter file is ``chapter``. 

The ``chapter`` element contains one or more child ``sequential`` elements.

======================
``sequential`` Element
======================

The ``sequential`` element references a sequential, or subsection, in the
course.

The ``sequential`` element contains one attribute:

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The unique identifier for the sequential. The url_name must be the name
       of the sequential XML file (without the ``.xml`` extension).


*************************************
``chapter`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - The value that is displayed to students as the name of the chapter, or
       section.
   * - ``start``
     - The date and time, in UTC, that the chapter is released to students.
       Before this date and time, students do not see the chapter.

*************************************
Example Chapter File
*************************************

The following example shows a chapter with three sequentials, or subsections. :

.. code-block:: xml
  
  <chapter display_name="Example Week 2: Get Interactive">
      <sequential url_name="simulations"/>
      <sequential url_name="graded_simulations"/>
      <sequential url_name="simulations_review"/>
  </chapter>

