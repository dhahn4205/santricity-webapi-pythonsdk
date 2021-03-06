# coding: utf-8

"""
ThinVolumeRepositoryExpansionHistoryData.py

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


class ThinVolumeRepositoryExpansionHistoryData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ThinVolumeRepositoryExpansionHistoryData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volume_ref': 'str',  # (required parameter)
            'type': 'str',  # (required parameter)
            'start_time': 'int',  # (required parameter)
            'pre_expansion_capacity_in_bytes': 'int',  # (required parameter)
            'post_expansion_capacity_in_bytes': 'int'
        }

        self.attribute_map = {
            'volume_ref': 'volumeRef',  # (required parameter)
            'type': 'type',  # (required parameter)
            'start_time': 'startTime',  # (required parameter)
            'pre_expansion_capacity_in_bytes': 'preExpansionCapacityInBytes',  # (required parameter)
            'post_expansion_capacity_in_bytes': 'postExpansionCapacityInBytes'
        }

        self._volume_ref = None
        self._type = None
        self._start_time = None
        self._pre_expansion_capacity_in_bytes = None
        self._post_expansion_capacity_in_bytes = None

    @property
    def volume_ref(self):
        """
        Gets the volume_ref of this ThinVolumeRepositoryExpansionHistoryData.
        A reference to the thin volume.

        :return: The volume_ref of this ThinVolumeRepositoryExpansionHistoryData.
        :rtype: str
        :required/optional: required
        """
        return self._volume_ref

    @volume_ref.setter
    def volume_ref(self, volume_ref):
        """
        Sets the volume_ref of this ThinVolumeRepositoryExpansionHistoryData.
        A reference to the thin volume.

        :param volume_ref: The volume_ref of this ThinVolumeRepositoryExpansionHistoryData.
        :type: str
        """
        self._volume_ref = volume_ref

    @property
    def type(self):
        """
        Gets the type of this ThinVolumeRepositoryExpansionHistoryData.
        The type of expansion.

        :return: The type of this ThinVolumeRepositoryExpansionHistoryData.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ThinVolumeRepositoryExpansionHistoryData.
        The type of expansion.

        :param type: The type of this ThinVolumeRepositoryExpansionHistoryData.
        :type: str
        """
        allowed_values = ["expansionTypeUnknown", "expansionTypeManual", "expansionTypeAutomatic", "contractionTypeAutomatic", "__UNDEFINED"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def start_time(self):
        """
        Gets the start_time of this ThinVolumeRepositoryExpansionHistoryData.
        The start timestamp of expansion operation, in seconds since January 1, 1970.

        :return: The start_time of this ThinVolumeRepositoryExpansionHistoryData.
        :rtype: int
        :required/optional: required
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ThinVolumeRepositoryExpansionHistoryData.
        The start timestamp of expansion operation, in seconds since January 1, 1970.

        :param start_time: The start_time of this ThinVolumeRepositoryExpansionHistoryData.
        :type: int
        """
        self._start_time = start_time

    @property
    def pre_expansion_capacity_in_bytes(self):
        """
        Gets the pre_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        The repository capacity before expansion (in bytes).

        :return: The pre_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        :rtype: int
        :required/optional: required
        """
        return self._pre_expansion_capacity_in_bytes

    @pre_expansion_capacity_in_bytes.setter
    def pre_expansion_capacity_in_bytes(self, pre_expansion_capacity_in_bytes):
        """
        Sets the pre_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        The repository capacity before expansion (in bytes).

        :param pre_expansion_capacity_in_bytes: The pre_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        :type: int
        """
        self._pre_expansion_capacity_in_bytes = pre_expansion_capacity_in_bytes

    @property
    def post_expansion_capacity_in_bytes(self):
        """
        Gets the post_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        The repository capacity after expansion (in bytes).

        :return: The post_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        :rtype: int
        :required/optional: required
        """
        return self._post_expansion_capacity_in_bytes

    @post_expansion_capacity_in_bytes.setter
    def post_expansion_capacity_in_bytes(self, post_expansion_capacity_in_bytes):
        """
        Sets the post_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        The repository capacity after expansion (in bytes).

        :param post_expansion_capacity_in_bytes: The post_expansion_capacity_in_bytes of this ThinVolumeRepositoryExpansionHistoryData.
        :type: int
        """
        self._post_expansion_capacity_in_bytes = post_expansion_capacity_in_bytes

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

