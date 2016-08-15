# coding: utf-8

"""
VolumeCopyCreationDescriptor.py

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


class VolumeCopyCreationDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeCopyCreationDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'source_volume': 'str',  # (required parameter)
            'target_volume': 'str',  # (required parameter)
            'idle_target_write_prot': 'bool',  # (required parameter)
            'copy_priority': 'str',  # (required parameter)
            'disable_snapshot': 'bool',  # (required parameter)
            'pg_ref': 'str'
        }

        self.attribute_map = {
            'source_volume': 'sourceVolume',  # (required parameter)
            'target_volume': 'targetVolume',  # (required parameter)
            'idle_target_write_prot': 'idleTargetWriteProt',  # (required parameter)
            'copy_priority': 'copyPriority',  # (required parameter)
            'disable_snapshot': 'disableSnapshot',  # (required parameter)
            'pg_ref': 'pgRef'
        }

        self._source_volume = None
        self._target_volume = None
        self._idle_target_write_prot = None
        self._copy_priority = None
        self._disable_snapshot = None
        self._pg_ref = None

    @property
    def source_volume(self):
        """
        Gets the source_volume of this VolumeCopyCreationDescriptor.
        The source volume reference.

        :return: The source_volume of this VolumeCopyCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._source_volume

    @source_volume.setter
    def source_volume(self, source_volume):
        """
        Sets the source_volume of this VolumeCopyCreationDescriptor.
        The source volume reference.

        :param source_volume: The source_volume of this VolumeCopyCreationDescriptor.
        :type: str
        """
        self._source_volume = source_volume

    @property
    def target_volume(self):
        """
        Gets the target_volume of this VolumeCopyCreationDescriptor.
        The target volume reference.

        :return: The target_volume of this VolumeCopyCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._target_volume

    @target_volume.setter
    def target_volume(self, target_volume):
        """
        Sets the target_volume of this VolumeCopyCreationDescriptor.
        The target volume reference.

        :param target_volume: The target_volume of this VolumeCopyCreationDescriptor.
        :type: str
        """
        self._target_volume = target_volume

    @property
    def idle_target_write_prot(self):
        """
        Gets the idle_target_write_prot of this VolumeCopyCreationDescriptor.
        Apply write protection to target volume when copy is idle (true/false).

        :return: The idle_target_write_prot of this VolumeCopyCreationDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._idle_target_write_prot

    @idle_target_write_prot.setter
    def idle_target_write_prot(self, idle_target_write_prot):
        """
        Sets the idle_target_write_prot of this VolumeCopyCreationDescriptor.
        Apply write protection to target volume when copy is idle (true/false).

        :param idle_target_write_prot: The idle_target_write_prot of this VolumeCopyCreationDescriptor.
        :type: bool
        """
        self._idle_target_write_prot = idle_target_write_prot

    @property
    def copy_priority(self):
        """
        Gets the copy_priority of this VolumeCopyCreationDescriptor.
        Importance of copy operation.

        :return: The copy_priority of this VolumeCopyCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._copy_priority

    @copy_priority.setter
    def copy_priority(self, copy_priority):
        """
        Sets the copy_priority of this VolumeCopyCreationDescriptor.
        Importance of copy operation.

        :param copy_priority: The copy_priority of this VolumeCopyCreationDescriptor.
        :type: str
        """
        allowed_values = ["priority0", "priority1", "priority2", "priority3", "priority4", "__UNDEFINED"]
        if copy_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `copy_priority`, must be one of {0}"
                .format(allowed_values)
            )
        self._copy_priority = copy_priority

    @property
    def disable_snapshot(self):
        """
        Gets the disable_snapshot of this VolumeCopyCreationDescriptor.
        When true, this indicates that the source snapshot should be disabled when the physical copy operation is complete. This field is only set to true when the volume copy is a clone.

        :return: The disable_snapshot of this VolumeCopyCreationDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._disable_snapshot

    @disable_snapshot.setter
    def disable_snapshot(self, disable_snapshot):
        """
        Sets the disable_snapshot of this VolumeCopyCreationDescriptor.
        When true, this indicates that the source snapshot should be disabled when the physical copy operation is complete. This field is only set to true when the volume copy is a clone.

        :param disable_snapshot: The disable_snapshot of this VolumeCopyCreationDescriptor.
        :type: bool
        """
        self._disable_snapshot = disable_snapshot

    @property
    def pg_ref(self):
        """
        Gets the pg_ref of this VolumeCopyCreationDescriptor.
        For clones based on PiT Groups, this will identify the PiT Group.

        :return: The pg_ref of this VolumeCopyCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._pg_ref

    @pg_ref.setter
    def pg_ref(self, pg_ref):
        """
        Sets the pg_ref of this VolumeCopyCreationDescriptor.
        For clones based on PiT Groups, this will identify the PiT Group.

        :param pg_ref: The pg_ref of this VolumeCopyCreationDescriptor.
        :type: str
        """
        self._pg_ref = pg_ref

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

