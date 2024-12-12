=====================================
From concept to realization Tutorial
=====================================

**Goal:** This tutorial will walk you through the steps create a new 'robosapiensIO' application and generate skeleton code, ready for implementing your own trustworthy self-adaptive application, based on the RoboSAPIENS Adaptive Platform.

**Tutorial level:** Intermediate

**Time:** 20 minutes

.. contents:: Contents
   :depth: 2
   :local:


Background
----------

To develop on top of the RoboSAPIENS Adaptive Platform, we use standalone application packages that contain everything needed to develop, build, deploy and run the adaptive application.
This means that everything needed to go from conceptual design to realization and eventually deployment is contained within the package.

Prerequisites
-------------

- **rpio CLI**: Ensure that the `rpio` command-line tool is installed and available on your system.
- **robosapiensio package**: Ensure that the `robosapiensio` python package is installed in your python, either system-wide or in python virtual environement. Installation instructions can be found `here <../../installation/methods/pypi.html>`_

Tasks
-----

1. **Run the Package Creation Command**

   Open a terminal in the folder you want to create the new robosapiensIO application package, with name ``newPackage`` and run the following command:

   .. code-block:: bash

        rpio package --create -n "newPackage" --verbose

Here's what each argument in the command does:

   - ``package --create``: Specifies that a new package should be created.
   - ``-n "newPackage"``: Sets the name of the new package to ``newPackage``.
   - ``--verbose``: Enables detailed output during the package creation process.

2. **Verify Package Structure**

   Navigate to the directory where the ``newPackage`` package was created and check its structure to confirm that all necessary files and folders have been set up correctly:

   .. code-block:: bash

        cd newPackage
        ls


3. **Check the newly created robosapiensIO package**

   You can check that the newly created package is a valid robosapiensIO package, run:

   .. code-block:: bash

     rpio package --check


Here's what each argument in the command does:

   - ``package --check``: Check if the current directory is a valid robosapiensIO package.


4. **Developing the adaptive application design**

   Within the newly generated application package ``newPackage``, a folder is provided to develop the AADL design, namely `/Design`. Within this folder, the following design files are required:

   - **LogicalArchitecture.aadl:** modeling the MAPLE-K components. Instructions how to model can be found `here <../basics/aadl_gettingStarted.html>`_.
   - **messages.aadl:** modeling the custom messages. Instructions how to model can be found `here <../basics/aadl_gettingStarted.html>`_.
   - **PhysicalArchitecture.aadl:** modeling the compute architecture. Instructions how to model can be found here !TODO!
   - **system.aadl:** modeling the logical-physical mapping architecture. Instructions how to model can be found here !TODO!

   .. warning::

    This tutorial focusses on the workflows instead of implementing the self-adaptive application design.
    Therefore the design file of the ``hello world`` example is provided as ``json file``.
    Please download the hello world design file (:download:`download<files/design.json>`) and put in the `/Design` folder.

5. **Running the code generators**

   With the AADL design implemented (``Design/design.json`` available), we can trigger de code generation using the ``AADL2CODE`` transformation.
   Open a terminal in the folder ``newPackage`` and run:

   .. code-block:: bash

     python Workflows/AADL2CODE.py

   This will pop-up a window to run the ``AADL2CODE transformation`` as shown below

   .. image:: files/aadl2code_workflow.png
   :width: 400
   :alt: aadl2code workflow

   alternatively, the ``AADL2CODE transformation`` can also be triggered using the `rpio` command-line tool.
   Open a terminal in the folder ``newPackage`` and run:

   .. code-block:: bash

     rpio transformation --aadl2code

   This will also pop-up the same window to run the ``AADL2CODE transformation``.

6. **Inspect the generated code skeletons**

7. **Inspect the generated deployment methods**

Summary
-------

You have successfully created a new ``robosapiensIO`` package using the `rpio` command-line tool, added an AADL design, based on the hellow world example and generated code skeletons, configurations and deployment methods.
This package is now ready for further development. Please check the ``hello world`` example for an implemented example.