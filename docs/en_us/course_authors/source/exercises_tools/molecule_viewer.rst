.. _Molecule Viewer:

#######################
Molecule Viewer Tool
#######################

Students can use the molecule viewer to see three-dimensional representations of molecules. 



The molecule editor incorporates JSmol, a JavaScript-based molecular viewer from Jmol. (You don't need to download this tool; Studio uses it automatically.) For more information about JSmol, see `JSmol <http://sourceforge.net/projects/jsmol/>`_.



.. _Create the Molecule Viewer:

*******************************
Create the Molecule Viewer Tool
*******************************

.. note:: Before you begin:

  * Make sure you have a tool that can compress files into a .zip folder.

  * Make sure you have permission to upload files to a third-party file hosting site such as Amazon Web Services Simple Storage Service (AWS S3). When you create the molecule viewer, you'll upload a .zip file to the file hosting site. 


To create the molecule viewer tool, you'll download and edit some files, upload the files to a file hosting site, and then create a component in Studio that references those files.

#. Download and edit files and folders, and then upload the file for the molecule viewer tool.

   #. Create or download a .mol file for the molecule that you want to show. You can download a variety of .mol files from the `BioTopics website <http://www.biotopics.co.uk/jsmol/molecules>`_. 
   #. Download the `MoleculeViewerFiles.zip <http://files.edx.org/MoleculeViewerFiles.zip>`_ file from edX.
   #. Unzip the `MoleculeViewerFiles.zip <http://files.edx.org/MoleculeViewerFiles.zip>`_ file that you've downloaded.

      When you unzip the file, you'll see a **MoleculeViewerFiles** folder that contains the following folders and files:

	    * data (folder)
	    * j2s (folder)
	    * js (folder)
	    * MoleculeViewer.html (file)

   4. Add the .mol file that you downloaded to the **data** folder.
   #. In a text editor, open the MoleculeViewer.html file.
   #. In line 19 of the MoleculeViewer.html file, change **Example.mol** to the name of your .mol file. For example, the line for your file may look like the following:

  		``script: "set antialiasDisplay; background black; load data/Glucose.mol;"``

   7. Save the MoleculeViewer.html file.
   #. Upload the entire **MoleculeViewerFiles** folder to your file hosting site. This folder must contain the following folders and files:

	    * data (folder): In step 1.4, you added a .mol file to this folder.
	    * j2s (folder)
	    * js (folder)
	    * MoleculeViewer.html (file): In step 1.6, you changed line 19 in this file.
   
      .. note:: Uploading this folder may take several minutes, even over a fast connection.

2. Create a component for the molecule viewer tool in Studio.

   #. In Studio, open the unit where you want to add the molecule viewer.
   #. Under **Add New Component**, click **HTML**, and then click **IFrame**.
   #. In the component editor that opens, replace the existing content with the text that you want.
   #. In the toolbar, click **HTML**.
   #. In the **HTML Source Code** box, enter the following line in the place where you want the molecule viewer to appear:

      ``<iframe name="moleculeiframe" src="https://path_to_folder/MoleculeViewer.html" width="500" height="500"></iframe>``

   6. Replace ``path_to_file`` with the URL of your file hosting site. For example, the line may look like the following:

      ``<iframe name="moleculeiframe" src="https://myfiles.example.com/MoleculeViewer.html" width="500" height="500"></iframe>``

   7. Click **OK** to close the **HTML Source Code** box, and then click **Save** to save the component.
   #. Click **Preview** to see your component as a student would see it.