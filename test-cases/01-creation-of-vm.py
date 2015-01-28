import sys
import netaddr
import json
import re
from subprocess import call


import AdapterServer
from AdapterServer import *

import CentOSVZAdapter
from CentOSVZAdapter import __all__

import settings

class CreateContainer(unittest.TestCase):
    def setUp(self):
        self.adapter_spec = json.loads(open("../../config/config.json").read())
        self.adapter_name = self.adapter_spec['CENTOSVZADAPTER']['ADAPTER_NAME']
        self.module = __import__(self.adapter_name)
        self.AdapterClass = getattr(self.module, self.adapter_name)
        self.adapter_instance = self.AdapterClass()
        self.lab_spec=json.loads(open("labspec.json").read())
    def test_vm_creation(self):
        self.vm_id = self.adapter_instance.create_vm(self.lab_spec)
        self.ip_addr = CentOSVZAdapter.get_vm_ip(self.vm_id)
        self.m = re.match(r'[0-9]+.[0-9]+.([0-9]+).([0-9]+)', self.ip_addr)
        self.temp_vm_id = self.m.group(1) + self.m.group(2)
        self.assertEqual(self.temp_vm_id, self.vm_id)
    def tearDown(self):
        call(["vzctl", "stop", self.vm_id])
        call(["vzctl", "destroy",self.vm_id])

if __name__ == "__main__":
    unittest.main()



