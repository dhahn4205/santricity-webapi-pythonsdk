# coding: utf-8

"""
PITConsistencyGroupAddMemberDescriptor.py

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


class PITConsistencyGroupAddMemberDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PITConsistencyGroupAddMemberDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cg_ref': 'str',  # (required parameter)
            'base_volume': 'str',  # (required parameter)
            'repository_candidate': 'ConcatVolumeCreationDescriptor'
        }

        self.attribute_map = {
            'cg_ref': 'cgRef',  # (required parameter)
            'base_volume': 'baseVolume',  # (required parameter)
            'repository_candidate': 'repositoryCandidate'
        }

        self._cg_ref = None
        self._base_volume = None
        self._repository_candidate = None

    @property
    def cg_ref(self):
        """
        Gets the cg_ref of this PITConsistencyGroupAddMemberDescriptor.
        The consistency group to which you will add the member.

        :return: The cg_ref of this PITConsistencyGroupAddMemberDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._cg_ref

    @cg_ref.setter
    def cg_ref(self, cg_ref):
        """
        Sets the cg_ref of this PITConsistencyGroupAddMemberDescriptor.
        The consistency group to which you will add the member.

        :param cg_ref: The cg_ref of this PITConsistencyGroupAddMemberDescriptor.
        :type: str
        """
        self._cg_ref = cg_ref

    @property
    def base_volume(self):
        """
        Gets the base_volume of this PITConsistencyGroupAddMemberDescriptor.
        The member base volume to add to the consistency group.

        :return: The base_volume of this PITConsistencyGroupAddMemberDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._base_volume

    @base_volume.setter
    def base_volume(self, base_volume):
        """
        Sets the base_volume of this PITConsistencyGroupAddMemberDescriptor.
        The member base volume to add to the consistency group.

        :param base_volume: The base_volume of this PITConsistencyGroupAddMemberDescriptor.
        :type: str
        """
        self._base_volume = base_volume

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this PITConsistencyGroupAddMemberDescriptor.
        The repository volume candidate for the consistency group PITGroup repository.

        :return: The repository_candidate of this PITConsistencyGroupAddMemberDescriptor.
        :rtype: ConcatVolumeCreationDescriptor
        :required/optional: required
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this PITConsistencyGroupAddMemberDescriptor.
        The repository volume candidate for the consistency group PITGroup repository.

        :param repository_candidate: The repository_candidate of this PITConsistencyGroupAddMemberDescriptor.
        :type: ConcatVolumeCreationDescriptor
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

