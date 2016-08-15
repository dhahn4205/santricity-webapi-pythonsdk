# coding: utf-8

"""
VolumeTypeParameters.py

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


class VolumeTypeParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeTypeParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volume_type': 'str',  # (required parameter)
            'capacity_provisioning_details': 'ThinVolumeCapacityProvisioningDetails'
        }

        self.attribute_map = {
            'volume_type': 'volumeType',  # (required parameter)
            'capacity_provisioning_details': 'capacityProvisioningDetails'
        }

        self._volume_type = None
        self._capacity_provisioning_details = None

    @property
    def volume_type(self):
        """
        Gets the volume_type of this VolumeTypeParameters.
        This enumeration is used to identify the capacity provisioning of a volume.

        :return: The volume_type of this VolumeTypeParameters.
        :rtype: str
        :required/optional: required
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """
        Sets the volume_type of this VolumeTypeParameters.
        This enumeration is used to identify the capacity provisioning of a volume.

        :param volume_type: The volume_type of this VolumeTypeParameters.
        :type: str
        """
        allowed_values = ["unknown", "thinProvisioned", "thickProvisioned", "__UNDEFINED"]
        if volume_type not in allowed_values:
            raise ValueError(
                "Invalid value for `volume_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._volume_type = volume_type

    @property
    def capacity_provisioning_details(self):
        """
        Gets the capacity_provisioning_details of this VolumeTypeParameters.
        This field is returned if the value of returnCode is equal to RETCODE_OK.

        :return: The capacity_provisioning_details of this VolumeTypeParameters.
        :rtype: ThinVolumeCapacityProvisioningDetails
        :required/optional: optional
        """
        return self._capacity_provisioning_details

    @capacity_provisioning_details.setter
    def capacity_provisioning_details(self, capacity_provisioning_details):
        """
        Sets the capacity_provisioning_details of this VolumeTypeParameters.
        This field is returned if the value of returnCode is equal to RETCODE_OK.

        :param capacity_provisioning_details: The capacity_provisioning_details of this VolumeTypeParameters.
        :type: ThinVolumeCapacityProvisioningDetails
        """
        self._capacity_provisioning_details = capacity_provisioning_details

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

