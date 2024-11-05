=====================================
Create robosapiensIO package Tutorial
=====================================

**Goal:** This tutorial will walk you through the steps create a new 'robosapiensIO' application package using the rpio CLI

**Tutorial level:** Beginner

**Time:** 5 minutes

.. contents:: Contents
   :depth: 2
   :local:


Background
----------

To develop on top of the RoboSAPIENS Adaptive Platform, we use standalone application packages that contain everything needed to develop, build, deploy and run the adaptive application.
Using the rpio command line tool, a new robosapiensIO package can be created, the starting point for each self-adaptive application using the RoboSAPIENS Adaptive Platform.

Prerequisites
-------------

- **rpio CLI**: Ensure that the `rpio` command-line tool is installed and available on your system.

Tasks
-----

1. **Run the Package Creation Command**

   Open a terminal in the folder you want to create the new robosapiensIO application package, with name 'newPackage,' and run the following command:

   .. tabs::

       .. group-tab:: Linux

          .. code-block:: bash

            rpio package --create -n "newPackage" --verbose

       .. group-tab:: macOS

          .. code-block:: console

            rpio package --create -n "newPackage" --verbose

       .. group-tab:: Windows

          .. code-block:: console

            rpio package --create -n "newPackage" --verbose

Here's what each argument in the command does:

   - ``package --create``: Specifies that a new package should be created.
   - ``-n "newPackage"``: Sets the name of the new package to ``newPackage``.
   - ``--verbose``: Enables detailed output during the package creation process.

2. **Verify Package Structure**

   Navigate to the directory where the ``test`` package was created and check its structure to confirm that all necessary files and folders have been set up correctly:

   .. tabs::

       .. group-tab:: Linux

          .. code-block:: bash

            cd newPackage
            ls

       .. group-tab:: macOS

          .. code-block:: console

            cd newPackage
            ls

       .. group-tab:: Windows

          .. code-block:: console

            cd newPackage
            ls

3. **Check the newly created robosapiensIO package**

   You can check that the newly created package is a valid robosapiensIO package, run:

   .. tabs::

       .. group-tab:: Linux

          .. code-block:: bash

            rpio package --check

       .. group-tab:: macOS

          .. code-block:: console

            rpio package --check

       .. group-tab:: Windows

          .. code-block:: console

            rpio package --check

Here's what each argument in the command does:

   - ``package --check``: Check if the current directory is a valid robosapiensIO package.

Summary
-------

You have successfully created a new ``robosapiensIO`` package using the ``rpio`` CLI. The package is now ready for further development.