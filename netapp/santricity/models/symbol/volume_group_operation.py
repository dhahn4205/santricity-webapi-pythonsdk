# coding: utf-8

"""
VolumeGroupOperation.py

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


class VolumeGroupOperation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeGroupOperation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volume_group_ref': 'str',  # (required parameter)
            'group_percent_complete': 'int',  # (required parameter)
            'group_time_to_completion': 'int',  # (required parameter)
            'volume_ref': 'str',  # (required parameter)
            'volume_percent_complete': 'int',  # (required parameter)
            'volume_time_to_completion': 'int'
        }

        self.attribute_map = {
            'volume_group_ref': 'volumeGroupRef',  # (required parameter)
            'group_percent_complete': 'groupPercentComplete',  # (required parameter)
            'group_time_to_completion': 'groupTimeToCompletion',  # (required parameter)
            'volume_ref': 'volumeRef',  # (required parameter)
            'volume_percent_complete': 'volumePercentComplete',  # (required parameter)
            'volume_time_to_completion': 'volumeTimeToCompletion'
        }

        self._volume_group_ref = None
        self._group_percent_complete = None
        self._group_time_to_completion = None
        self._volume_ref = None
        self._volume_percent_complete = None
        self._volume_time_to_completion = None

    @property
    def volume_group_ref(self):
        """
        Gets the volume_group_ref of this VolumeGroupOperation.
        Reference to the volume group.

        :return: The volume_group_ref of this VolumeGroupOperation.
        :rtype: str
        :required/optional: required
        """
        return self._volume_group_ref

    @volume_group_ref.setter
    def volume_group_ref(self, volume_group_ref):
        """
        Sets the volume_group_ref of this VolumeGroupOperation.
        Reference to the volume group.

        :param volume_group_ref: The volume_group_ref of this VolumeGroupOperation.
        :type: str
        """
        self._volume_group_ref = volume_group_ref

    @property
    def group_percent_complete(self):
        """
        Gets the group_percent_complete of this VolumeGroupOperation.
        Completion percentage for volume group. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :return: The group_percent_complete of this VolumeGroupOperation.
        :rtype: int
        :required/optional: required
        """
        return self._group_percent_complete

    @group_percent_complete.setter
    def group_percent_complete(self, group_percent_complete):
        """
        Sets the group_percent_complete of this VolumeGroupOperation.
        Completion percentage for volume group. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :param group_percent_complete: The group_percent_complete of this VolumeGroupOperation.
        :type: int
        """
        self._group_percent_complete = group_percent_complete

    @property
    def group_time_to_completion(self):
        """
        Gets the group_time_to_completion of this VolumeGroupOperation.
        Estimated time in minutes to complete the volume group. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :return: The group_time_to_completion of this VolumeGroupOperation.
        :rtype: int
        :required/optional: required
        """
        return self._group_time_to_completion

    @group_time_to_completion.setter
    def group_time_to_completion(self, group_time_to_completion):
        """
        Sets the group_time_to_completion of this VolumeGroupOperation.
        Estimated time in minutes to complete the volume group. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :param group_time_to_completion: The group_time_to_completion of this VolumeGroupOperation.
        :type: int
        """
        self._group_time_to_completion = group_time_to_completion

    @property
    def volume_ref(self):
        """
        Gets the volume_ref of this VolumeGroupOperation.
        Reference to the volume currently being processed.

        :return: The volume_ref of this VolumeGroupOperation.
        :rtype: str
        :required/optional: required
        """
        return self._volume_ref

    @volume_ref.setter
    def volume_ref(self, volume_ref):
        """
        Sets the volume_ref of this VolumeGroupOperation.
        Reference to the volume currently being processed.

        :param volume_ref: The volume_ref of this VolumeGroupOperation.
        :type: str
        """
        self._volume_ref = volume_ref

    @property
    def volume_percent_complete(self):
        """
        Gets the volume_percent_complete of this VolumeGroupOperation.
        Completion percentage for volume currently being processed. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :return: The volume_percent_complete of this VolumeGroupOperation.
        :rtype: int
        :required/optional: required
        """
        return self._volume_percent_complete

    @volume_percent_complete.setter
    def volume_percent_complete(self, volume_percent_complete):
        """
        Sets the volume_percent_complete of this VolumeGroupOperation.
        Completion percentage for volume currently being processed. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :param volume_percent_complete: The volume_percent_complete of this VolumeGroupOperation.
        :type: int
        """
        self._volume_percent_complete = volume_percent_complete

    @property
    def volume_time_to_completion(self):
        """
        Gets the volume_time_to_completion of this VolumeGroupOperation.
        Estimated time in minutes to complete the volume currently being processed. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :return: The volume_time_to_completion of this VolumeGroupOperation.
        :rtype: int
        :required/optional: required
        """
        return self._volume_time_to_completion

    @volume_time_to_completion.setter
    def volume_time_to_completion(self, volume_time_to_completion):
        """
        Sets the volume_time_to_completion of this VolumeGroupOperation.
        Estimated time in minutes to complete the volume currently being processed. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :param volume_time_to_completion: The volume_time_to_completion of this VolumeGroupOperation.
        :type: int
        """
        self._volume_time_to_completion = volume_time_to_completion

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

