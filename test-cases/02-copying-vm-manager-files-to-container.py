import os
import sys
import netaddr
import json
import unittest
import re
import subprocess
from subprocess import call

import AdapterServer
from AdapterServer import *

import settings
from settings import *

import CentOSVZAdapter
from CentOSVZAdapter import __all__

import Controller
from Controller import *

class TestCopyFiles(unittest.TestCase):

     def setUp(self):
        self.adapter_spec     = json.loads(open("../../config/config.json").read())
        self.adapter_name     = self.adapter_spec['CENTOSVZADAPTER']['ADAPTER_NAME']
        self.module           = __import__(self.adapter_name)
        self.AdapterClass     = getattr(self.module, self.adapter_name)
        self.adapter_instance = self.AdapterClass()
        self.lab_spec =json.loads(open("../../scripts/labspec.json").read())
     def test_copy_source(self):
        self.vm_id = self.adapter_instance.create_vm(self.lab_spec)
        CentOSVZAdapter.copy_ovpl_source(self.vm_id)
        CentOSVZAdapter.copy_lab_source(self.vm_id)
        ovpl_path="/vz/root/"+self.vm_id+"/root/ovpl"
        assert(os.path.exists(ovpl_path) == True)
     def tearDown(self):
        call(["vzctl", "stop", self.vm_id])
        call(["vzctl", "destroy",self.vm_id])

if __name__ == "__main__":
    unittest.main()
