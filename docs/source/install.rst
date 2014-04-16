Installation
============

This is a guide on how to install BinPy on your computer.


Linux
-----

.. note::
   We support python 2.6, 2.7, 3.2, 3.3 and pypy. If you have any of these
   versions of python you are good to go.

**Dependencies**

We have two dependencies *setuptools* and *ipython*.
setuptools is used to facilitate installation and ipython
is used to provide a separate shell for BinPy.

To install dependencies

.. code-block:: sh

   sudo apt-get install setuptools ipython-notebook  # Debian OS

   sudo yum install python-ipython-notebook # Fedora or CenOS


**Install with pip**

To install pip on debian os

.. code-block:: sh

   sudo apt-get install python-pip

To install pip on fedora or cent os

.. code-block:: sh

   sudo yum -y install python-pip

To get the latest stable version of BinPy

.. code-block:: sh

   pip install BinPy

To get the development version of BinPy

.. code-block:: sh

   pip install https://github.com/BinPy/BinPy/zipball/master

**Install with git**

To install git on your system

.. code-block:: sh

   sudo apt-get install git  # Debian OS

   sudo yum install git-core  # Fedora or CentOS

To get the latest stable version of BinPy

.. code-block:: sh

   git clone https://github.com/BinPy/BinPy
   cd BinPy/
   sudo python setup.py install

To get the development version of BinPy

.. code-block:: sh

   git clone -b develop https://github.com/BinPy/BinPy
   cd BinPy/
   sudo python setup.py install

Windows
-------

To install dependencies(setuptools and ipython) you can check the following links.

* https://pypi.python.org/pypi/setuptools#windows-8-powershell
* http://ipython.org/install.html

To install BinPy on windows you can use our windows installer.

.. note::

   We generate windows installer only for stable release. To get the development version, you'll have to use git.

.. hint::

   If you have the `git cygwin` or you have the `github for windows`
   , you can clone the development branch of our repository from
   https://github.com/BinPy/BinPy.

To install it you will have to run the following commands

.. code-block:: sh

   cd BinPy/
   python setup.py install
