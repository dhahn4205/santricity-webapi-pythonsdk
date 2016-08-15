# coding: utf-8

"""
HostSpecificNVSRAMUpdateDescriptor.py

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


class HostSpecificNVSRAMUpdateDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HostSpecificNVSRAMUpdateDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'region_id': 'str',  # (required parameter)
            'offset': 'int',  # (required parameter)
            'region_data': 'str',  # (required parameter)
            'host_index': 'int'
        }

        self.attribute_map = {
            'region_id': 'regionId',  # (required parameter)
            'offset': 'offset',  # (required parameter)
            'region_data': 'regionData',  # (required parameter)
            'host_index': 'hostIndex'
        }

        self._region_id = None
        self._offset = None
        self._region_data = None
        self._host_index = None

    @property
    def region_id(self):
        """
        Gets the region_id of this HostSpecificNVSRAMUpdateDescriptor.
        The region of NVSRAM to update.

        :return: The region_id of this HostSpecificNVSRAMUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this HostSpecificNVSRAMUpdateDescriptor.
        The region of NVSRAM to update.

        :param region_id: The region_id of this HostSpecificNVSRAMUpdateDescriptor.
        :type: str
        """
        allowed_values = ["allRegions", "nonUserConfigData", "subsystemId", "subsystemFaultData", "driveFaultData", "hostManagedData", "hostInterfaceData", "userConfigData", "bootpData", "extUserConfigData", "hostTypeDependentData", "__UNDEFINED"]
        if region_id not in allowed_values:
            raise ValueError(
                "Invalid value for `region_id`, must be one of {0}"
                .format(allowed_values)
            )
        self._region_id = region_id

    @property
    def offset(self):
        """
        Gets the offset of this HostSpecificNVSRAMUpdateDescriptor.
        The offset into the region to update.

        :return: The offset of this HostSpecificNVSRAMUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this HostSpecificNVSRAMUpdateDescriptor.
        The offset into the region to update.

        :param offset: The offset of this HostSpecificNVSRAMUpdateDescriptor.
        :type: int
        """
        self._offset = offset

    @property
    def region_data(self):
        """
        Gets the region_data of this HostSpecificNVSRAMUpdateDescriptor.
        The data to write to NVSRAM.

        :return: The region_data of this HostSpecificNVSRAMUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._region_data

    @region_data.setter
    def region_data(self, region_data):
        """
        Sets the region_data of this HostSpecificNVSRAMUpdateDescriptor.
        The data to write to NVSRAM.

        :param region_data: The region_data of this HostSpecificNVSRAMUpdateDescriptor.
        :type: str
        """
        self._region_data = region_data

    @property
    def host_index(self):
        """
        Gets the host_index of this HostSpecificNVSRAMUpdateDescriptor.
        Host Type Index mapped by SPM.

        :return: The host_index of this HostSpecificNVSRAMUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._host_index

    @host_index.setter
    def host_index(self, host_index):
        """
        Sets the host_index of this HostSpecificNVSRAMUpdateDescriptor.
        Host Type Index mapped by SPM.

        :param host_index: The host_index of this HostSpecificNVSRAMUpdateDescriptor.
        :type: int
        """
        self._host_index = host_index

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
