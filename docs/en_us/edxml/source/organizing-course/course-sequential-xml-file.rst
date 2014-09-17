.. _Course Sequential XML Files:

############################
Course Sequential XML Files
############################

A course sequential file:

* Defines the display name and release date for the sequential, or subsection.
* Organizes units within the sequential.
  
See:
* `Create Course Sequential Files`_
* `Sequential File Elements`_
* `sequential Element Attributes`_
* `Example Sequential File`_


*******************************
Create Course Sequential Files
*******************************

You create a course sequential XML file in the ``sequential`` directory for
each subsection in your course.

The name of the sequential file must match the value of the @url_name attribute
of the ``sequential`` element in the chapter XML file.

For example, if the chapter file contains:

.. code-block:: xml
  
    <chapter display_name="Example Week 2: Get Interactive">
        <sequential url_name="simulations"/>
        . . .
    </chapter>

You create the file ``sequential/simulations.xml`` to define the sequential.


*************************************
Sequential File Elements
************************************* 

The root element of the sequential file is ``sequential``. 

The ``sequential`` element contains one or more child ``vertical`` elements.

======================
``vertical`` Element
======================

The ``vertical`` element references a vertical, or unit, in the subsection.

The ``vertical`` element contains one attribute:

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``url_name``
     - The unique identifier for the vertical. The url_name must be the name
       of the vertical XML file (without the ``.xml`` extension).


*************************************
``sequential`` Element Attributes
*************************************

.. list-table::
   :widths: 10 70
   :header-rows: 1

   * - Attribute
     - Meaning
   * - ``display_name``
     - The value that is displayed to students as the name of the sequential,
       or subsection.
   * - ``start``
     - The date and time, in UTC, that the sequential is released to students.
       Before this date and time, students do not see the sequential.
   * - ``graded``
     - Whether the sequential is a graded subsection; ``true`` or ``false``.
   * - ``format``
     - If the sequential is graded, the assignment type.
   * - ``graceperiod``
     - If the sequential is graded, the number of seconds in the grace period.
   * - ``rerandomize``
     - TBP
   * - ``showanswer``
     - TBP
   * - ``xqa_key``
     - TBP


*************************************
Example Sequential File
*************************************

The following example shows a sequential with three verticals, or units:

.. code-block:: xml
  
  <sequential display_name="Lesson 1">
      <vertical url_name="Lesson_1_Unit_1"/>
      <vertical url_name="Lesson_1_Unit_2"/>
  </sequential>

