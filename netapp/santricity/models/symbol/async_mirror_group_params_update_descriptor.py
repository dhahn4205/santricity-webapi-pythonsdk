# coding: utf-8

"""
AsyncMirrorGroupParamsUpdateDescriptor.py

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


class AsyncMirrorGroupParamsUpdateDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupParamsUpdateDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_label': 'str',  # (required parameter)
            'sync_interval_minutes': 'int',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'int',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'int',  # (required parameter)
            'repository_utilization_warn_threshold': 'int',  # (required parameter)
            'group_ref': 'str'
        }

        self.attribute_map = {
            'group_label': 'groupLabel',  # (required parameter)
            'sync_interval_minutes': 'syncIntervalMinutes',  # (required parameter)
            'sync_completion_time_alert_threshold_minutes': 'syncCompletionTimeAlertThresholdMinutes',  # (required parameter)
            'recovery_point_age_alert_threshold_minutes': 'recoveryPointAgeAlertThresholdMinutes',  # (required parameter)
            'repository_utilization_warn_threshold': 'repositoryUtilizationWarnThreshold',  # (required parameter)
            'group_ref': 'groupRef'
        }

        self._group_label = None
        self._sync_interval_minutes = None
        self._sync_completion_time_alert_threshold_minutes = None
        self._recovery_point_age_alert_threshold_minutes = None
        self._repository_utilization_warn_threshold = None
        self._group_ref = None

    @property
    def group_label(self):
        """
        Gets the group_label of this AsyncMirrorGroupParamsUpdateDescriptor.
        The user defined label for the mirror group.

        :return: The group_label of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._group_label

    @group_label.setter
    def group_label(self, group_label):
        """
        Sets the group_label of this AsyncMirrorGroupParamsUpdateDescriptor.
        The user defined label for the mirror group.

        :param group_label: The group_label of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: str
        """
        self._group_label = group_label

    @property
    def sync_interval_minutes(self):
        """
        Gets the sync_interval_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The synchronization interval (in minutes).

        :return: The sync_interval_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._sync_interval_minutes

    @sync_interval_minutes.setter
    def sync_interval_minutes(self, sync_interval_minutes):
        """
        Sets the sync_interval_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The synchronization interval (in minutes).

        :param sync_interval_minutes: The sync_interval_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: int
        """
        self._sync_interval_minutes = sync_interval_minutes

    @property
    def sync_completion_time_alert_threshold_minutes(self):
        """
        Gets the sync_completion_time_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete.

        :return: The sync_completion_time_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._sync_completion_time_alert_threshold_minutes

    @sync_completion_time_alert_threshold_minutes.setter
    def sync_completion_time_alert_threshold_minutes(self, sync_completion_time_alert_threshold_minutes):
        """
        Sets the sync_completion_time_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete.

        :param sync_completion_time_alert_threshold_minutes: The sync_completion_time_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: int
        """
        self._sync_completion_time_alert_threshold_minutes = sync_completion_time_alert_threshold_minutes

    @property
    def recovery_point_age_alert_threshold_minutes(self):
        """
        Gets the recovery_point_age_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The recovery point age objective (in minutes). The user is notified via needs-attention when age of last good recovery point exceeds this value.

        :return: The recovery_point_age_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._recovery_point_age_alert_threshold_minutes

    @recovery_point_age_alert_threshold_minutes.setter
    def recovery_point_age_alert_threshold_minutes(self, recovery_point_age_alert_threshold_minutes):
        """
        Sets the recovery_point_age_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        The recovery point age objective (in minutes). The user is notified via needs-attention when age of last good recovery point exceeds this value.

        :param recovery_point_age_alert_threshold_minutes: The recovery_point_age_alert_threshold_minutes of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: int
        """
        self._recovery_point_age_alert_threshold_minutes = recovery_point_age_alert_threshold_minutes

    @property
    def repository_utilization_warn_threshold(self):
        """
        Gets the repository_utilization_warn_threshold of this AsyncMirrorGroupParamsUpdateDescriptor.
        The repository utilization warning threshold (0-100 percent). A needs attention condition will be generated if percent of repository capacity currently utilized exceeds this threshold.

        :return: The repository_utilization_warn_threshold of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._repository_utilization_warn_threshold

    @repository_utilization_warn_threshold.setter
    def repository_utilization_warn_threshold(self, repository_utilization_warn_threshold):
        """
        Sets the repository_utilization_warn_threshold of this AsyncMirrorGroupParamsUpdateDescriptor.
        The repository utilization warning threshold (0-100 percent). A needs attention condition will be generated if percent of repository capacity currently utilized exceeds this threshold.

        :param repository_utilization_warn_threshold: The repository_utilization_warn_threshold of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: int
        """
        self._repository_utilization_warn_threshold = repository_utilization_warn_threshold

    @property
    def group_ref(self):
        """
        Gets the group_ref of this AsyncMirrorGroupParamsUpdateDescriptor.
        A reference to the Async Mirror Group whose parameters are being updated.

        :return: The group_ref of this AsyncMirrorGroupParamsUpdateDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._group_ref

    @group_ref.setter
    def group_ref(self, group_ref):
        """
        Sets the group_ref of this AsyncMirrorGroupParamsUpdateDescriptor.
        A reference to the Async Mirror Group whose parameters are being updated.

        :param group_ref: The group_ref of this AsyncMirrorGroupParamsUpdateDescriptor.
        :type: str
        """
        self._group_ref = group_ref

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

