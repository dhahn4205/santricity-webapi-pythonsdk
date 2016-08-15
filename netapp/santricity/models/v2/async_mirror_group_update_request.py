# coding: utf-8

"""
AsyncMirrorGroupUpdateRequest.py

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


class AsyncMirrorGroupUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',  
            'sync_interval_minutes': 'int',  
            'recovery_warn_threshold_minutes': 'int',  
            'repo_utilization_warn_threshold': 'int',  
            'sync_warn_threshold_minutes': 'int'
        }

        self.attribute_map = {
            'name': 'name',  
            'sync_interval_minutes': 'syncIntervalMinutes',  
            'recovery_warn_threshold_minutes': 'recoveryWarnThresholdMinutes',  
            'repo_utilization_warn_threshold': 'repoUtilizationWarnThreshold',  
            'sync_warn_threshold_minutes': 'syncWarnThresholdMinutes'
        }

        self._name = None
        self._sync_interval_minutes = None
        self._recovery_warn_threshold_minutes = None
        self._repo_utilization_warn_threshold = None
        self._sync_warn_threshold_minutes = None

    @property
    def name(self):
        """
        Gets the name of this AsyncMirrorGroupUpdateRequest.


        :return: The name of this AsyncMirrorGroupUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AsyncMirrorGroupUpdateRequest.


        :param name: The name of this AsyncMirrorGroupUpdateRequest.
        :type: str
        """
        self._name = name

    @property
    def sync_interval_minutes(self):
        """
        Gets the sync_interval_minutes of this AsyncMirrorGroupUpdateRequest.
        Sync interval (minutes)

        :return: The sync_interval_minutes of this AsyncMirrorGroupUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._sync_interval_minutes

    @sync_interval_minutes.setter
    def sync_interval_minutes(self, sync_interval_minutes):
        """
        Sets the sync_interval_minutes of this AsyncMirrorGroupUpdateRequest.
        Sync interval (minutes)

        :param sync_interval_minutes: The sync_interval_minutes of this AsyncMirrorGroupUpdateRequest.
        :type: int
        """
        self._sync_interval_minutes = sync_interval_minutes

    @property
    def recovery_warn_threshold_minutes(self):
        """
        Gets the recovery_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        Recovery point warning threshold (minutes)

        :return: The recovery_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._recovery_warn_threshold_minutes

    @recovery_warn_threshold_minutes.setter
    def recovery_warn_threshold_minutes(self, recovery_warn_threshold_minutes):
        """
        Sets the recovery_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        Recovery point warning threshold (minutes)

        :param recovery_warn_threshold_minutes: The recovery_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        :type: int
        """
        self._recovery_warn_threshold_minutes = recovery_warn_threshold_minutes

    @property
    def repo_utilization_warn_threshold(self):
        """
        Gets the repo_utilization_warn_threshold of this AsyncMirrorGroupUpdateRequest.
        Recovery point warning threshold (percentage)

        :return: The repo_utilization_warn_threshold of this AsyncMirrorGroupUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._repo_utilization_warn_threshold

    @repo_utilization_warn_threshold.setter
    def repo_utilization_warn_threshold(self, repo_utilization_warn_threshold):
        """
        Sets the repo_utilization_warn_threshold of this AsyncMirrorGroupUpdateRequest.
        Recovery point warning threshold (percentage)

        :param repo_utilization_warn_threshold: The repo_utilization_warn_threshold of this AsyncMirrorGroupUpdateRequest.
        :type: int
        """
        self._repo_utilization_warn_threshold = repo_utilization_warn_threshold

    @property
    def sync_warn_threshold_minutes(self):
        """
        Gets the sync_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.


        :return: The sync_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._sync_warn_threshold_minutes

    @sync_warn_threshold_minutes.setter
    def sync_warn_threshold_minutes(self, sync_warn_threshold_minutes):
        """
        Sets the sync_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.


        :param sync_warn_threshold_minutes: The sync_warn_threshold_minutes of this AsyncMirrorGroupUpdateRequest.
        :type: int
        """
        self._sync_warn_threshold_minutes = sync_warn_threshold_minutes

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

