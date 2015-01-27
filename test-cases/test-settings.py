#+Title: Test Cases for settings file
#+Authors: Prakash B Hegade and Amulya Sri
#+Date: 01 December 2014

* Description

* Identifying the Dependencies :
As the test scenario will be implemented in Python, we need to import
all the necessary modules. We firstly import all the required Python
modules. 

We would need the methods from =sys=, =netaddr=, =json= and =unittest= modules.

#+BEGIN_SRC python

import os
import sys
import netaddr
import json
import unittest

#+END_SRC

As the scenario is to test =settings= module, we would need to import
functionalities from =envsetup= and =settings= file.

#+BEGIN_SRC python

from envsetup import *
import settings
from settings import *

#+END_SRC

* Defining the Test Class :

A test class in python can be created by subclassing
=unittest.TestCase=.  The test class created primarily holds two
predefined methods namely =setUp= and =tearDown= and the test
cases. Method =setUp= holds the stub creation and =tearDown=
releases all the held resources.

#+BEGIN_SRC python
class TestSettings(unittest.TestCase):
#+END_SRC

When we define =setUp= method, test runner runs this method prior to
every test case. As no initialization is required, we keep the =setUp=
empty.

#+BEGIN_SRC python
    def setUp(self):
        print 'Calling setUp method ...'
#+END_SRC

The first test case is to test the value of =VM-Manager-Script= in
=settings.py= file.

#+BEGIN_SRC python
    def test_vm_manager_script(self):
        self.vm_manager_script=settings.VM_MANAGER_SCRIPT
        print 'Checking VMManager Script '
        print 'VMManger Script is ', self.vm_manager_script
        assert(self.vm_manager_script == "VMManagerServer.py VMManager")
#+END_SRC

The second test case is to test the value of =VM-Manager-Script=. The
assertion statement at the end of the test case checks and raises
=AssertionError= if the value is not matching with the original value.

#+BEGIN_SRC python
    def test_vm_manager_server_path(self):
        self.vm_manager_server=settings.VMMANAGERSERVER_PATH
        print 'Checking VM Manager Server Path'
        print 'VMManager Server Path is ', self.vm_manager_server
        assert(self.vm_manager_server == "/root/ovpl/src/VMManager/")
#+END_SRC

The following test case is to check the functionality of the method,
=get_subnet()= in =settings= file. 

#+BEGIN_SRC python
    def test_subnet(self):
        self.subnet=settings.get_subnet()
        print 'Checking Subnet value'
        print 'Subnet is ', self.subnet
        assert(self.subnet == "['10.2.58.128/28']")
#+END_SRC

We next test the functionality of =get_test_lab_id()= in =settings=
file. 
#+BEGIN_SRC python
    def test_labid(self):
        self.labid=settings.get_test_lab_id()
        print 'Checking Lab id'
        print 'Labid is ', self.labid
        assert(self.labid == "engg01")
#+END_SRC

Now we test the functionality of =get_test_os()= method in =settings= file.
#+BEGIN_SRC python
    def test_test_os(self):
        self.os=settings.get_test_os()
        print 'Checking OS'
        print 'OS is ', self.os
        assert(self.os == "Ubuntu")
#+END_SRC

The following test case tests the functionality of
=get_test_os_version()= in =settings= file.

#+BEGIN_SRC python
    def test_os_version(self):
        self.os_version=settings.get_test_os_version()
        print 'Checking OS Version'
        print 'OS Version is ', self.os_version
        assert(self.os_version == "12.04")
#+END_SRC

The method, =get_adapter_hostname()= returns the hostname of the
adapter. We test the functionality of this method, in the following test case.

#+BEGIN_SRC python
    def test_adapter_hostname(self):
        self.adapter_hostname=settings.get_adapter_hostname()
        print 'Checking Adapter Host Name'
        print 'Adapter Host Name is', self.adapter_hostname
        assert(self.adapter_hostname == "vlabs.ac.in")
#+END_SRC

The next test case is to check value of =VM-Manager-Port= from the
=settings= file.

#+BEGIN_SRC python
    def test_vm_manager_port(self):
        self.vm_manager_port=settings.VM_MANAGER_PORT
        print 'Checking VM Manager Port Number'
        print 'VMManager Port is ', self.vm_manager_port
        assert(self.vm_manager_port == "9089")
#+END_SRC

The test cases are invoked from the main method. The =Main= first
calls the =SetUp= method and creates the stub, invokes it prior to the
execution of test cases and then calls the =tearDown= method after
every test case execution.

#+BEGIN_SRC python
if __name__ == "__main__":
    unittest.main() # run all tests
#+END_SRC

