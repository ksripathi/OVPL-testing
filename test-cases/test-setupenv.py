import os
import sys
import json
import unittest
from envsetup import *
from settings import get_subnet

class TestEnvSetup(unittest.TestCase):
    def setUp(self):
        self.e=EnvSetUp()

    def test_no_proxy(self):
        self.no_proxy=self.e.no_proxy
        assert(self.no_proxy == "10.2.58.128,10.2.58.129,10.2.58.130,10.2.58.131,10.2.58.132,10.2.58.133,10.2.58.134,10.2.58.135,10.2.58.136,10.2.58.137,10.2.58.138,10.2.58.139,10.2.58.140,10.2.58.141,10.2.58.142,10.2.58.143,localhost,10.2.58.129")

    def test_http_proxy(self):
	self.http_proxy=self.e.http_proxy
        assert(self.http_proxy == "http://proxy.iiit.ac.in:8080")

    def test_https_proxy(self):
        self.https_proxy=self.e.https_proxy
        assert(self.https_proxy == "https://proxy.iiit.ac.in:8080")

    def test_environment_set(self):
        self.env = self.a.set_environment()
        assert(self.a.os.environ[https_proxy] == "http://proxy.iiit.ac.in:8080")

    def setUp(self):
        print 'TearDown is Invoked'

if __name__ == "__main__":
    unittest.main()
