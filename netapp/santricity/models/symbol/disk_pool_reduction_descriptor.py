# coding: utf-8

"""
DiskPoolReductionDescriptor.py

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


class DiskPoolReductionDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DiskPoolReductionDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volume_group_ref': 'str',  # (required parameter)
            'drive_ref': 'list[str]'
        }

        self.attribute_map = {
            'volume_group_ref': 'volumeGroupRef',  # (required parameter)
            'drive_ref': 'driveRef'
        }

        self._volume_group_ref = None
        self._drive_ref = None

    @property
    def volume_group_ref(self):
        """
        Gets the volume_group_ref of this DiskPoolReductionDescriptor.
        The disk pool undergoing the capacity reduction.

        :return: The volume_group_ref of this DiskPoolReductionDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._volume_group_ref

    @volume_group_ref.setter
    def volume_group_ref(self, volume_group_ref):
        """
        Sets the volume_group_ref of this DiskPoolReductionDescriptor.
        The disk pool undergoing the capacity reduction.

        :param volume_group_ref: The volume_group_ref of this DiskPoolReductionDescriptor.
        :type: str
        """
        self._volume_group_ref = volume_group_ref

    @property
    def drive_ref(self):
        """
        Gets the drive_ref of this DiskPoolReductionDescriptor.
        The drives to be removed.

        :return: The drive_ref of this DiskPoolReductionDescriptor.
        :rtype: list[str]
        :required/optional: required
        """
        return self._drive_ref

    @drive_ref.setter
    def drive_ref(self, drive_ref):
        """
        Sets the drive_ref of this DiskPoolReductionDescriptor.
        The drives to be removed.

        :param drive_ref: The drive_ref of this DiskPoolReductionDescriptor.
        :type: list[str]
        """
        self._drive_ref = drive_ref

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

