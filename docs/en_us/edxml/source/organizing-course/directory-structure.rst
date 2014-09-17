.. _edXML Directory Structure:

##########################
edXML Directory Structure
##########################

See:

* `Top Level Directory`_
* `about Directory`_
* `annotabable Directory`_
* `chapter Directory`_
* `course Directory`_
* `html Directory`_
* `info Directory`_
* `policies Directory`_
* `problems Directory`_
* `sequential Directory`_
* `static Directory`_
* `tabs Directory`_
* `vertical Directory`_
* `video Directory`_

********************
Top Level Directory
********************

All files and sub-directories that comprise your edXML course are stored within
a single directory.

For example, the edX Platform contains a directory called `manual-testing-
complete`_ that contains a course with all component types for testing
purposes:

IMAGE

Following are descriptions of each directory in the course. You should set up
these directories in preparation for developing your course content.


********************
about Directory
********************

The ``about`` directory contains:

* ``overview.html``, which contains the content for the course overview page
  students see the the Learning Management System (LMS).

* ``short_description.html``, which contains the content for the course in the
  course list.

See :ref:`The Course About Pages` for more information.


**********************
annotabable Directory
**********************

The ``annotabable`` directory contains an XML file for each Annotation component you use in your course.

If you do not need Annotation components in the course, you do not need to create this directory.


********************
chapter Directory
********************

The ``chapter`` directory contains an XML file for each section in the course.

See :ref:`Course Chapter XML Files` for more information.

********************
course Directory
********************

The ``course`` directory contains an XML file the specifies the course settings
and the chapters (sections) in the courseware.

See :ref:`The Course Outline XML File` for more information.


********************
html Directory
********************

The ``html`` directory contains an XML and HTML file for each HTML component in
the course.

If you do not need HTML components in the course, you do not need to create
this directory.

See :ref:`HTML Components` for more information.

********************
info Directory
********************

The ``info`` directory contains:

* ``handouts.html``, which contains the contain for the Course Handouts page in the course.

* ``updates.html``, which contains the course updates students see when opening a course.

********************
policies Directory
********************

The ``policies`` directory contains:

* ``grading_policy.json``, which defines how student work is graded in the
  course.

* ``policy.json``, which defines various settings in the course.

* ``assets.json``, which defines all files used in the course, such as images.
  
See :ref:`Course Policies` for more information.

********************
problems Directory
********************

The ``problems`` directory contains an XML file for each problem component you
use in your course.

If you do not need problem components in the course, you do not need to create
this directory.

See :ref:`Problems and Tools` for more information.

********************
sequential Directory
********************

The ``sequential`` directory contains an XML file for each subsection in your
course.

See :ref:`Course Sequential XML Files` for more information.

********************
static Directory
********************

The ``static`` directory contains the files used in your course, such as images
or PDFs.

See :ref:`Course Sequential XML Files` for more information.

********************
tabs Directory
********************

The ``tabs`` directory contains an HTML file for each page you add to your
course.

See :ref:`Course Pages` for more information.


********************
vertical Directory
********************

The ``vertical`` directory contains an XML file for each unit in your course.

See :ref:`Course Vertical XML Files` for more information.


********************
video Directory
********************

The ``video`` directory contains an XML file for each video component you use
in your course.

If you do not need video components in the course, you do not need to create
this directory.

See :ref:`Video Components` for more information.

 .. include:: ../links.rst