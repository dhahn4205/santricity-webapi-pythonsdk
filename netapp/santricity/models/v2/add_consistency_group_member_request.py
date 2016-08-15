# coding: utf-8

"""
AddConsistencyGroupMemberRequest.py

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


class AddConsistencyGroupMemberRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AddConsistencyGroupMemberRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volume_id': 'str',  # (required parameter)
            'repository_pool_id': 'str',  
            'scan_media': 'bool',  
            'validate_parity': 'bool',  
            'repository_percent': 'float',  
            'repository_candidate': 'ConcatVolumeCandidate'
        }

        self.attribute_map = {
            'volume_id': 'volumeId',  # (required parameter)
            'repository_pool_id': 'repositoryPoolId',  
            'scan_media': 'scanMedia',  
            'validate_parity': 'validateParity',  
            'repository_percent': 'repositoryPercent',  
            'repository_candidate': 'repositoryCandidate'
        }

        self._volume_id = None
        self._repository_pool_id = None
        self._scan_media = None
        self._validate_parity = None
        self._repository_percent = None
        self._repository_candidate = None

    @property
    def volume_id(self):
        """
        Gets the volume_id of this AddConsistencyGroupMemberRequest.
        The member volume ref

        :return: The volume_id of this AddConsistencyGroupMemberRequest.
        :rtype: str
        :required/optional: required
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this AddConsistencyGroupMemberRequest.
        The member volume ref

        :param volume_id: The volume_id of this AddConsistencyGroupMemberRequest.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def repository_pool_id(self):
        """
        Gets the repository_pool_id of this AddConsistencyGroupMemberRequest.
        The repository volume pool

        :return: The repository_pool_id of this AddConsistencyGroupMemberRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._repository_pool_id

    @repository_pool_id.setter
    def repository_pool_id(self, repository_pool_id):
        """
        Sets the repository_pool_id of this AddConsistencyGroupMemberRequest.
        The repository volume pool

        :param repository_pool_id: The repository_pool_id of this AddConsistencyGroupMemberRequest.
        :type: str
        """
        self._repository_pool_id = repository_pool_id

    @property
    def scan_media(self):
        """
        Gets the scan_media of this AddConsistencyGroupMemberRequest.


        :return: The scan_media of this AddConsistencyGroupMemberRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._scan_media

    @scan_media.setter
    def scan_media(self, scan_media):
        """
        Sets the scan_media of this AddConsistencyGroupMemberRequest.


        :param scan_media: The scan_media of this AddConsistencyGroupMemberRequest.
        :type: bool
        """
        self._scan_media = scan_media

    @property
    def validate_parity(self):
        """
        Gets the validate_parity of this AddConsistencyGroupMemberRequest.


        :return: The validate_parity of this AddConsistencyGroupMemberRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._validate_parity

    @validate_parity.setter
    def validate_parity(self, validate_parity):
        """
        Sets the validate_parity of this AddConsistencyGroupMemberRequest.


        :param validate_parity: The validate_parity of this AddConsistencyGroupMemberRequest.
        :type: bool
        """
        self._validate_parity = validate_parity

    @property
    def repository_percent(self):
        """
        Gets the repository_percent of this AddConsistencyGroupMemberRequest.


        :return: The repository_percent of this AddConsistencyGroupMemberRequest.
        :rtype: float
        :required/optional: optional
        """
        return self._repository_percent

    @repository_percent.setter
    def repository_percent(self, repository_percent):
        """
        Sets the repository_percent of this AddConsistencyGroupMemberRequest.


        :param repository_percent: The repository_percent of this AddConsistencyGroupMemberRequest.
        :type: float
        """
        self._repository_percent = repository_percent

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this AddConsistencyGroupMemberRequest.


        :return: The repository_candidate of this AddConsistencyGroupMemberRequest.
        :rtype: ConcatVolumeCandidate
        :required/optional: optional
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this AddConsistencyGroupMemberRequest.


        :param repository_candidate: The repository_candidate of this AddConsistencyGroupMemberRequest.
        :type: ConcatVolumeCandidate
        """
        self._repository_candidate = repository_candidate

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

