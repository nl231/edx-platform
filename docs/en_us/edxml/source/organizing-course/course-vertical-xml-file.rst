.. _Course Vertical XML Files:

############################
Course Vertical XML Files
############################

A course vertical file:

* Defines the display name for the vertical, or unit.
* Organizes components and other verticals in the vertical.

See:
* `Create Course Vertical Files`_
* `Vertical File Elements`_
* `vertical Element Attributes`_
* `Example Vertical File`_


*******************************
Create Course Vertical Files
*******************************

You create a course vertical XML file in the ``vertical`` directory for each
unit in your course.

The name of the vertical file must match the value of the @url_name attribute
of ``vertical`` element in the sequential XML file.

For example, if the sequential file contains:

.. code-block:: xml

  <sequential display_name="Lesson 1">
      <vertical url_name="Lesson_1_Unit_1"/>
      . . .
  </sequential>

You create the file ``vertical/Lesson_1_Unit_1.xml`` to define the vertical.


*************************************
Vertical File Elements
************************************* 

The root element of the vertical file is ``vertical``. 

The ``vertical`` element contains one or more child elements for each component
in the vertical.

.. note:: 
 A vertical element can also contain a vertical element. You can nest
 verticals, or units, recursively.

==============================
``vertical`` Element Children
==============================

Child elements or ``vertical`` refer to components in your course.  The edX
Platform supports a wide range of components, including custom XBlocks.

Types of supported components include:

table with type/xml element/link

*************************************
``vertical`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - The value that is displayed to students as the name of the sequential,
       or subsection.
   
release status??


*************************************
Example Vertical File
*************************************

The following example shows a vertical with three components:

.. code-block:: xml
  
  <vertical display_name="Lesson_1_Unit_1">
      <html url_name="Introduction"/>
      <video url_name="Unit_1_Video"/>
  </vertical>

