##########################
edXML Directory Structure
##########################



********************
Top Level Directory
********************

All files and sub-directories that comprise your edXML course are stored within
a single directory.

For example, the edX Platform contains a directory called 
`manual-testing-complete`_ that contains a course with all component types for testing purposes:

IMAGE

Following are descriptions of each directory in the course. You should set up these directories in preparation for developing your course content.


********************
about Directory
********************

The ''about'' directory contains:

* ''overview.html'', which contains the content for the course overview page
  students see the the Learning Management System (LMS).

* ''short_description.html'', which contains the content for the course in the
  course list.



**********************
annotabable Directory
**********************

The ''annotabable'' directory contains an XML file for each Annotation component you use in your course.

If you do not need Annotation components in the course, you do not need to create this directory.


********************
chapter Directory
********************

The ''chapter'' directory contains an XML file for each section in the course.

********************
course Directory
********************

The ''course'' directory contains an XML file the specifies the course settings and the chapters (sections) in the courseware.

********************
html Directory
********************

The ''html'' directory contains an XML and HTML file for each HTML component in the course.

If you do not need HTML components in the course, you do not need to create this directory.


********************
html Directory
********************

The ''html'' directory contains an XML and HTML file for each HTML component in the course.

If you do not need HTML components in the course, you do not need to create this directory.

********************
info Directory
********************

The ''info'' directory contains:

* ''handouts.html'', which contains the contain for the Course Handouts page in the course.

* ''updates.html'', which contains the course updates students see when opening a course.

********************
policies Directory
********************

The ''policies'' directory contains:

* ''grading_policy.json'', which defines how student work is graded in the course.

* ''policy.json'', which defines various settings in the course.

* ''assets.json'', which defines all files used in the course, such as images.

********************
problems Directory
********************

The ''problems'' directory contains an XML file for each problem component you use in your course.

If you do not need problem components in the course, you do not need to create this directory.

********************
sequential Directory
********************

The ''sequential'' directory contains an XML file for each subsection in your course.

********************
static Directory
********************

The ''static'' directory contains the files used in your course, such as images or PDFs.

********************
tabs Directory
********************

The ''tabs'' directory contains an HTML file for each page you add to your course.


********************
veritical Directory
********************

The ''veritical'' directory contains an XML file for each unit in your course.


********************
video Directory
********************

The ''video'' directory contains an XML file for each video component you use in your course.

If you do not need video components in the course, you do not need to create this directory.

 .. include:: ../links.rst