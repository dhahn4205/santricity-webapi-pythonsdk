# coding: utf-8

"""
ChannelDiagInterfaceDepResults.py

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


class ChannelDiagInterfaceDepResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ChannelDiagInterfaceDepResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interface_type': 'str',  # (required parameter)
            'fc_results': 'ChannelDiagFcDependentResults',  
            'sas_results': 'ChannelDiagSasDependentResults'
        }

        self.attribute_map = {
            'interface_type': 'interfaceType',  # (required parameter)
            'fc_results': 'fcResults',  
            'sas_results': 'sasResults'
        }

        self._interface_type = None
        self._fc_results = None
        self._sas_results = None

    @property
    def interface_type(self):
        """
        Gets the interface_type of this ChannelDiagInterfaceDepResults.
        This enumeration defines the different I/O interface types that may be reported as part of the configuration information associated with a controller.

        :return: The interface_type of this ChannelDiagInterfaceDepResults.
        :rtype: str
        :required/optional: required
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """
        Sets the interface_type of this ChannelDiagInterfaceDepResults.
        This enumeration defines the different I/O interface types that may be reported as part of the configuration information associated with a controller.

        :param interface_type: The interface_type of this ChannelDiagInterfaceDepResults.
        :type: str
        """
        allowed_values = ["notImplemented", "scsi", "fc", "sata", "sas", "iscsi", "ib", "fcoe", "__UNDEFINED"]
        if interface_type not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._interface_type = interface_type

    @property
    def fc_results(self):
        """
        Gets the fc_results of this ChannelDiagInterfaceDepResults.
        A set of Fibre-Channel-specific drive channel diagnostic results. This field is present only if interfaceType is set to IO_IF_FC.

        :return: The fc_results of this ChannelDiagInterfaceDepResults.
        :rtype: ChannelDiagFcDependentResults
        :required/optional: optional
        """
        return self._fc_results

    @fc_results.setter
    def fc_results(self, fc_results):
        """
        Sets the fc_results of this ChannelDiagInterfaceDepResults.
        A set of Fibre-Channel-specific drive channel diagnostic results. This field is present only if interfaceType is set to IO_IF_FC.

        :param fc_results: The fc_results of this ChannelDiagInterfaceDepResults.
        :type: ChannelDiagFcDependentResults
        """
        self._fc_results = fc_results

    @property
    def sas_results(self):
        """
        Gets the sas_results of this ChannelDiagInterfaceDepResults.
        A set of SAS-specific drive channel diagnostic results. This field is present only if interfaceType is set to IO_IF_SAS.

        :return: The sas_results of this ChannelDiagInterfaceDepResults.
        :rtype: ChannelDiagSasDependentResults
        :required/optional: optional
        """
        return self._sas_results

    @sas_results.setter
    def sas_results(self, sas_results):
        """
        Sets the sas_results of this ChannelDiagInterfaceDepResults.
        A set of SAS-specific drive channel diagnostic results. This field is present only if interfaceType is set to IO_IF_SAS.

        :param sas_results: The sas_results of this ChannelDiagInterfaceDepResults.
        :type: ChannelDiagSasDependentResults
        """
        self._sas_results = sas_results

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

