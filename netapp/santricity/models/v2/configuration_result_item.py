# coding: utf-8

"""
ConfigurationResultItem.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class ConfigurationResultItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConfigurationResultItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'system_key': 'str',  
            'success': 'bool',  
            'response': 'CallResponse'
        }

        self.attribute_map = {
            'system_key': 'systemKey',  
            'success': 'success',  
            'response': 'response'
        }

        self._system_key = None
        self._success = None
        self._response = None

    @property
    def system_key(self):
        """
        Gets the system_key of this ConfigurationResultItem.
        The key from the csv file  for the storage system

        :return: The system_key of this ConfigurationResultItem.
        :rtype: str
        :required/optional: optional
        """
        return self._system_key

    @system_key.setter
    def system_key(self, system_key):
        """
        Sets the system_key of this ConfigurationResultItem.
        The key from the csv file  for the storage system

        :param system_key: The system_key of this ConfigurationResultItem.
        :type: str
        """
        self._system_key = system_key

    @property
    def success(self):
        """
        Gets the success of this ConfigurationResultItem.
        True if the configuration did not have any reported errors

        :return: The success of this ConfigurationResultItem.
        :rtype: bool
        :required/optional: optional
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ConfigurationResultItem.
        True if the configuration did not have any reported errors

        :param success: The success of this ConfigurationResultItem.
        :type: bool
        """
        self._success = success

    @property
    def response(self):
        """
        Gets the response of this ConfigurationResultItem.
        If the operation did not succeed, this properties has the error information

        :return: The response of this ConfigurationResultItem.
        :rtype: CallResponse
        :required/optional: optional
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this ConfigurationResultItem.
        If the operation did not succeed, this properties has the error information

        :param response: The response of this ConfigurationResultItem.
        :type: CallResponse
        """
        self._response = response

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

