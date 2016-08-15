# coding: utf-8

"""
CVCandidateResponse.py

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


class CVCandidateResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CVCandidateResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'raid_level_match': 'bool',  
            'same_pool': 'bool',  
            'candidate': 'ConcatVolumeCandidate',  
            'volume_group_id': 'str',  
            'capacity_match': 'bool',  
            'qos_match': 'bool',  
            'disk_pool': 'bool',  
            'capacity': 'int',  
            'base_mappable_object_id': 'str',  
            'candidate_type': 'str',  
            'security_match': 'bool',  
            'da_match': 'bool',  
            'drive_type_match': 'bool',  
            'existing_candidate': 'bool'
        }

        self.attribute_map = {
            'raid_level_match': 'raidLevelMatch',  
            'same_pool': 'samePool',  
            'candidate': 'candidate',  
            'volume_group_id': 'volumeGroupId',  
            'capacity_match': 'capacityMatch',  
            'qos_match': 'qosMatch',  
            'disk_pool': 'diskPool',  
            'capacity': 'capacity',  
            'base_mappable_object_id': 'baseMappableObjectId',  
            'candidate_type': 'candidateType',  
            'security_match': 'securityMatch',  
            'da_match': 'daMatch',  
            'drive_type_match': 'driveTypeMatch',  
            'existing_candidate': 'existingCandidate'
        }

        self._raid_level_match = None
        self._same_pool = None
        self._candidate = None
        self._volume_group_id = None
        self._capacity_match = None
        self._qos_match = None
        self._disk_pool = None
        self._capacity = None
        self._base_mappable_object_id = None
        self._candidate_type = None
        self._security_match = None
        self._da_match = None
        self._drive_type_match = None
        self._existing_candidate = None

    @property
    def raid_level_match(self):
        """
        Gets the raid_level_match of this CVCandidateResponse.


        :return: The raid_level_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._raid_level_match

    @raid_level_match.setter
    def raid_level_match(self, raid_level_match):
        """
        Sets the raid_level_match of this CVCandidateResponse.


        :param raid_level_match: The raid_level_match of this CVCandidateResponse.
        :type: bool
        """
        self._raid_level_match = raid_level_match

    @property
    def same_pool(self):
        """
        Gets the same_pool of this CVCandidateResponse.


        :return: The same_pool of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._same_pool

    @same_pool.setter
    def same_pool(self, same_pool):
        """
        Sets the same_pool of this CVCandidateResponse.


        :param same_pool: The same_pool of this CVCandidateResponse.
        :type: bool
        """
        self._same_pool = same_pool

    @property
    def candidate(self):
        """
        Gets the candidate of this CVCandidateResponse.


        :return: The candidate of this CVCandidateResponse.
        :rtype: ConcatVolumeCandidate
        :required/optional: optional
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """
        Sets the candidate of this CVCandidateResponse.


        :param candidate: The candidate of this CVCandidateResponse.
        :type: ConcatVolumeCandidate
        """
        self._candidate = candidate

    @property
    def volume_group_id(self):
        """
        Gets the volume_group_id of this CVCandidateResponse.


        :return: The volume_group_id of this CVCandidateResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, volume_group_id):
        """
        Sets the volume_group_id of this CVCandidateResponse.


        :param volume_group_id: The volume_group_id of this CVCandidateResponse.
        :type: str
        """
        self._volume_group_id = volume_group_id

    @property
    def capacity_match(self):
        """
        Gets the capacity_match of this CVCandidateResponse.


        :return: The capacity_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._capacity_match

    @capacity_match.setter
    def capacity_match(self, capacity_match):
        """
        Sets the capacity_match of this CVCandidateResponse.


        :param capacity_match: The capacity_match of this CVCandidateResponse.
        :type: bool
        """
        self._capacity_match = capacity_match

    @property
    def qos_match(self):
        """
        Gets the qos_match of this CVCandidateResponse.


        :return: The qos_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._qos_match

    @qos_match.setter
    def qos_match(self, qos_match):
        """
        Sets the qos_match of this CVCandidateResponse.


        :param qos_match: The qos_match of this CVCandidateResponse.
        :type: bool
        """
        self._qos_match = qos_match

    @property
    def disk_pool(self):
        """
        Gets the disk_pool of this CVCandidateResponse.


        :return: The disk_pool of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._disk_pool

    @disk_pool.setter
    def disk_pool(self, disk_pool):
        """
        Sets the disk_pool of this CVCandidateResponse.


        :param disk_pool: The disk_pool of this CVCandidateResponse.
        :type: bool
        """
        self._disk_pool = disk_pool

    @property
    def capacity(self):
        """
        Gets the capacity of this CVCandidateResponse.


        :return: The capacity of this CVCandidateResponse.
        :rtype: int
        :required/optional: optional
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this CVCandidateResponse.


        :param capacity: The capacity of this CVCandidateResponse.
        :type: int
        """
        self._capacity = capacity

    @property
    def base_mappable_object_id(self):
        """
        Gets the base_mappable_object_id of this CVCandidateResponse.


        :return: The base_mappable_object_id of this CVCandidateResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._base_mappable_object_id

    @base_mappable_object_id.setter
    def base_mappable_object_id(self, base_mappable_object_id):
        """
        Sets the base_mappable_object_id of this CVCandidateResponse.


        :param base_mappable_object_id: The base_mappable_object_id of this CVCandidateResponse.
        :type: str
        """
        self._base_mappable_object_id = base_mappable_object_id

    @property
    def candidate_type(self):
        """
        Gets the candidate_type of this CVCandidateResponse.


        :return: The candidate_type of this CVCandidateResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._candidate_type

    @candidate_type.setter
    def candidate_type(self, candidate_type):
        """
        Sets the candidate_type of this CVCandidateResponse.


        :param candidate_type: The candidate_type of this CVCandidateResponse.
        :type: str
        """
        allowed_values = ["unknown", "newVol", "existingVols", "expansion", "__UNDEFINED"]
        if candidate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `candidate_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._candidate_type = candidate_type

    @property
    def security_match(self):
        """
        Gets the security_match of this CVCandidateResponse.
        True if the drive security settings for the base pool and the candidate's pool match.

        :return: The security_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._security_match

    @security_match.setter
    def security_match(self, security_match):
        """
        Sets the security_match of this CVCandidateResponse.
        True if the drive security settings for the base pool and the candidate's pool match.

        :param security_match: The security_match of this CVCandidateResponse.
        :type: bool
        """
        self._security_match = security_match

    @property
    def da_match(self):
        """
        Gets the da_match of this CVCandidateResponse.
        True if the DataAssurance settings for the base and the candidate match.

        :return: The da_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._da_match

    @da_match.setter
    def da_match(self, da_match):
        """
        Sets the da_match of this CVCandidateResponse.
        True if the DataAssurance settings for the base and the candidate match.

        :param da_match: The da_match of this CVCandidateResponse.
        :type: bool
        """
        self._da_match = da_match

    @property
    def drive_type_match(self):
        """
        Gets the drive_type_match of this CVCandidateResponse.
        True if the drives for the base pool and the candidate's pool match.

        :return: The drive_type_match of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._drive_type_match

    @drive_type_match.setter
    def drive_type_match(self, drive_type_match):
        """
        Sets the drive_type_match of this CVCandidateResponse.
        True if the drives for the base pool and the candidate's pool match.

        :param drive_type_match: The drive_type_match of this CVCandidateResponse.
        :type: bool
        """
        self._drive_type_match = drive_type_match

    @property
    def existing_candidate(self):
        """
        Gets the existing_candidate of this CVCandidateResponse.
        True if the repository candidate is based on an existing volume and does not require a volume creation to occur.

        :return: The existing_candidate of this CVCandidateResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._existing_candidate

    @existing_candidate.setter
    def existing_candidate(self, existing_candidate):
        """
        Sets the existing_candidate of this CVCandidateResponse.
        True if the repository candidate is based on an existing volume and does not require a volume creation to occur.

        :param existing_candidate: The existing_candidate of this CVCandidateResponse.
        :type: bool
        """
        self._existing_candidate = existing_candidate

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

