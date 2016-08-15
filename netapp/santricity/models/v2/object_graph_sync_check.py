# coding: utf-8

"""
ObjectGraphSyncCheck.py

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


class ObjectGraphSyncCheck(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ObjectGraphSyncCheck - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'result': 'str',  # (required parameter)
            'type': 'str',  # (required parameter)
            'severity_level': 'str',  # (required parameter)
            'cfw_match': 'bool',  # (required parameter)
            'nvsram_match': 'bool',  # (required parameter)
            'successful': 'bool'
        }

        self.attribute_map = {
            'result': 'result',  # (required parameter)
            'type': 'type',  # (required parameter)
            'severity_level': 'severityLevel',  # (required parameter)
            'cfw_match': 'cfwMatch',  # (required parameter)
            'nvsram_match': 'nvsramMatch',  # (required parameter)
            'successful': 'successful'
        }

        self._result = None
        self._type = None
        self._severity_level = None
        self._cfw_match = None
        self._nvsram_match = None
        self._successful = None

    @property
    def result(self):
        """
        Gets the result of this ObjectGraphSyncCheck.


        :return: The result of this ObjectGraphSyncCheck.
        :rtype: str
        :required/optional: required
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this ObjectGraphSyncCheck.


        :param result: The result of this ObjectGraphSyncCheck.
        :type: str
        """
        allowed_values = ["ok", "notCompleted", "failedDataRetrieval", "failed"]
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result`, must be one of {0}"
                .format(allowed_values)
            )
        self._result = result

    @property
    def type(self):
        """
        Gets the type of this ObjectGraphSyncCheck.


        :return: The type of this ObjectGraphSyncCheck.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ObjectGraphSyncCheck.


        :param type: The type of this ObjectGraphSyncCheck.
        :type: str
        """
        allowed_values = ["melEventCheck", "cntrlSyncCheck", "storageDeviceAccessible", "spmDatabaseVerification", "validPassword", "configurationDatabaseCheck", "objectGraphSyncCheck", "nvsramMatches", "volumeGroupsComplete", "controllerStatusOptimal", "hotSparesInUse", "failedDrivesPresent", "driveCheck", "missingVolumes", "exclusiveOperations"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def severity_level(self):
        """
        Gets the severity_level of this ObjectGraphSyncCheck.


        :return: The severity_level of this ObjectGraphSyncCheck.
        :rtype: str
        :required/optional: required
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        """
        Sets the severity_level of this ObjectGraphSyncCheck.


        :param severity_level: The severity_level of this ObjectGraphSyncCheck.
        :type: str
        """
        allowed_values = ["unknown", "low", "medium", "high", "fatal"]
        if severity_level not in allowed_values:
            raise ValueError(
                "Invalid value for `severity_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._severity_level = severity_level

    @property
    def cfw_match(self):
        """
        Gets the cfw_match of this ObjectGraphSyncCheck.


        :return: The cfw_match of this ObjectGraphSyncCheck.
        :rtype: bool
        :required/optional: required
        """
        return self._cfw_match

    @cfw_match.setter
    def cfw_match(self, cfw_match):
        """
        Sets the cfw_match of this ObjectGraphSyncCheck.


        :param cfw_match: The cfw_match of this ObjectGraphSyncCheck.
        :type: bool
        """
        self._cfw_match = cfw_match

    @property
    def nvsram_match(self):
        """
        Gets the nvsram_match of this ObjectGraphSyncCheck.


        :return: The nvsram_match of this ObjectGraphSyncCheck.
        :rtype: bool
        :required/optional: required
        """
        return self._nvsram_match

    @nvsram_match.setter
    def nvsram_match(self, nvsram_match):
        """
        Sets the nvsram_match of this ObjectGraphSyncCheck.


        :param nvsram_match: The nvsram_match of this ObjectGraphSyncCheck.
        :type: bool
        """
        self._nvsram_match = nvsram_match

    @property
    def successful(self):
        """
        Gets the successful of this ObjectGraphSyncCheck.


        :return: The successful of this ObjectGraphSyncCheck.
        :rtype: bool
        :required/optional: optional
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this ObjectGraphSyncCheck.


        :param successful: The successful of this ObjectGraphSyncCheck.
        :type: bool
        """
        self._successful = successful

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

