# coding: utf-8

"""
PITGroupCreationDescriptor.py

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


class PITGroupCreationDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PITGroupCreationDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'base_volume': 'str',  # (required parameter)
            'pit_group_label': 'str',  # (required parameter)
            'repository_candidate': 'ConcatVolumeCreationDescriptor',  # (required parameter)
            'rep_full_policy': 'str',  # (required parameter)
            'full_warn_threshold': 'int',  # (required parameter)
            'auto_delete_limit': 'int',  # (required parameter)
            'rollback_priority': 'str',  # (required parameter)
            'pit_schedule': 'OptionalScheduleCreationDescriptor'
        }

        self.attribute_map = {
            'base_volume': 'baseVolume',  # (required parameter)
            'pit_group_label': 'pitGroupLabel',  # (required parameter)
            'repository_candidate': 'repositoryCandidate',  # (required parameter)
            'rep_full_policy': 'repFullPolicy',  # (required parameter)
            'full_warn_threshold': 'fullWarnThreshold',  # (required parameter)
            'auto_delete_limit': 'autoDeleteLimit',  # (required parameter)
            'rollback_priority': 'rollbackPriority',  # (required parameter)
            'pit_schedule': 'pitSchedule'
        }

        self._base_volume = None
        self._pit_group_label = None
        self._repository_candidate = None
        self._rep_full_policy = None
        self._full_warn_threshold = None
        self._auto_delete_limit = None
        self._rollback_priority = None
        self._pit_schedule = None

    @property
    def base_volume(self):
        """
        Gets the base_volume of this PITGroupCreationDescriptor.
        The base volume for this PiT Group.

        :return: The base_volume of this PITGroupCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._base_volume

    @base_volume.setter
    def base_volume(self, base_volume):
        """
        Sets the base_volume of this PITGroupCreationDescriptor.
        The base volume for this PiT Group.

        :param base_volume: The base_volume of this PITGroupCreationDescriptor.
        :type: str
        """
        self._base_volume = base_volume

    @property
    def pit_group_label(self):
        """
        Gets the pit_group_label of this PITGroupCreationDescriptor.
        The user-assigned PiT Group label.

        :return: The pit_group_label of this PITGroupCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._pit_group_label

    @pit_group_label.setter
    def pit_group_label(self, pit_group_label):
        """
        Sets the pit_group_label of this PITGroupCreationDescriptor.
        The user-assigned PiT Group label.

        :param pit_group_label: The pit_group_label of this PITGroupCreationDescriptor.
        :type: str
        """
        self._pit_group_label = pit_group_label

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this PITGroupCreationDescriptor.
        The volume candidate for the repository.

        :return: The repository_candidate of this PITGroupCreationDescriptor.
        :rtype: ConcatVolumeCreationDescriptor
        :required/optional: required
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this PITGroupCreationDescriptor.
        The volume candidate for the repository.

        :param repository_candidate: The repository_candidate of this PITGroupCreationDescriptor.
        :type: ConcatVolumeCreationDescriptor
        """
        self._repository_candidate = repository_candidate

    @property
    def rep_full_policy(self):
        """
        Gets the rep_full_policy of this PITGroupCreationDescriptor.
        Behavior on repository full condition.

        :return: The rep_full_policy of this PITGroupCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._rep_full_policy

    @rep_full_policy.setter
    def rep_full_policy(self, rep_full_policy):
        """
        Sets the rep_full_policy of this PITGroupCreationDescriptor.
        Behavior on repository full condition.

        :param rep_full_policy: The rep_full_policy of this PITGroupCreationDescriptor.
        :type: str
        """
        allowed_values = ["unknown", "failbasewrites", "purgepit", "__UNDEFINED"]
        if rep_full_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `rep_full_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._rep_full_policy = rep_full_policy

    @property
    def full_warn_threshold(self):
        """
        Gets the full_warn_threshold of this PITGroupCreationDescriptor.
        The repository utilization warning threshold percentage.

        :return: The full_warn_threshold of this PITGroupCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._full_warn_threshold

    @full_warn_threshold.setter
    def full_warn_threshold(self, full_warn_threshold):
        """
        Sets the full_warn_threshold of this PITGroupCreationDescriptor.
        The repository utilization warning threshold percentage.

        :param full_warn_threshold: The full_warn_threshold of this PITGroupCreationDescriptor.
        :type: int
        """
        self._full_warn_threshold = full_warn_threshold

    @property
    def auto_delete_limit(self):
        """
        Gets the auto_delete_limit of this PITGroupCreationDescriptor.
        The auto-delete setting for PiT Group. A non-zero value indicates auto delete is enabled and the limit should be set to the value specified.

        :return: The auto_delete_limit of this PITGroupCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._auto_delete_limit

    @auto_delete_limit.setter
    def auto_delete_limit(self, auto_delete_limit):
        """
        Sets the auto_delete_limit of this PITGroupCreationDescriptor.
        The auto-delete setting for PiT Group. A non-zero value indicates auto delete is enabled and the limit should be set to the value specified.

        :param auto_delete_limit: The auto_delete_limit of this PITGroupCreationDescriptor.
        :type: int
        """
        self._auto_delete_limit = auto_delete_limit

    @property
    def rollback_priority(self):
        """
        Gets the rollback_priority of this PITGroupCreationDescriptor.
        Importance of rollback operation.

        :return: The rollback_priority of this PITGroupCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._rollback_priority

    @rollback_priority.setter
    def rollback_priority(self, rollback_priority):
        """
        Sets the rollback_priority of this PITGroupCreationDescriptor.
        Importance of rollback operation.

        :param rollback_priority: The rollback_priority of this PITGroupCreationDescriptor.
        :type: str
        """
        allowed_values = ["highest", "high", "medium", "low", "lowest", "__UNDEFINED"]
        if rollback_priority not in allowed_values:
            raise ValueError(
                "Invalid value for `rollback_priority`, must be one of {0}"
                .format(allowed_values)
            )
        self._rollback_priority = rollback_priority

    @property
    def pit_schedule(self):
        """
        Gets the pit_schedule of this PITGroupCreationDescriptor.
        An optional PiT schedule to be created with the new PITGroup. The target object is empty in this structure (unknown because not yet created, assigned by this creation method).

        :return: The pit_schedule of this PITGroupCreationDescriptor.
        :rtype: OptionalScheduleCreationDescriptor
        :required/optional: required
        """
        return self._pit_schedule

    @pit_schedule.setter
    def pit_schedule(self, pit_schedule):
        """
        Sets the pit_schedule of this PITGroupCreationDescriptor.
        An optional PiT schedule to be created with the new PITGroup. The target object is empty in this structure (unknown because not yet created, assigned by this creation method).

        :param pit_schedule: The pit_schedule of this PITGroupCreationDescriptor.
        :type: OptionalScheduleCreationDescriptor
        """
        self._pit_schedule = pit_schedule

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

