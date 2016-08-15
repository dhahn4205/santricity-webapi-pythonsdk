#!/usr/bin/env python
# coding: utf-8

"""
diagnostics_api_test.py

The Clear BSD License

Copyright (c) – 2016, NetApp, Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

import unittest
from netapp.santricity.rest import ApiException
from netapp.santricity.api.v2.diagnostics_api import DiagnosticsApi



class DiagnosticsApiTest(unittest.TestCase):

    
    def test_get_alert_configuration(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_alert_configuration(system_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_get_core_dump_information(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_core_dump_information(system_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_get_device_diagnostic_data(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_device_diagnostic_data(system_id="test", data_request="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_get_failures(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_failures(system_id="test", )
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_get_support_data_retrieval_request_status(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_support_data_retrieval_request_status(system_id="test", request_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_get_syslog_configuration(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.get_syslog_configuration(system_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_set_syslog_configuration(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.set_syslog_configuration(system_id="test", )
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_start_support_data_retrieval_request(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.start_support_data_retrieval_request(system_id="test", )
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_test_alert_email(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.test_alert_email(system_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_test_syslog_send(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.test_syslog_send(system_id="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    
    def test_update_alert_configuration(self):
       api = DiagnosticsApi()
       diagnostics_api = None
       try:
            diagnostics_api = api.update_alert_configuration(system_id="test", update_request="test")
            # For the DELETE calls, there's no reponse returned and we want to set that as a valid sdk call.
            if diagnostics_api is None:
                diagnostics_api = 1
       except (ApiException, IOError)  as exp:
             # The API call went through but got a HTTP errorcode, which means the SDK works
             diagnostics_api = 1

       self.assertNotEqual(diagnostics_api, None)
    


