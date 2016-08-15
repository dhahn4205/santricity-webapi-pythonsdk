# coding: utf-8

"""
AsyncMirrorGroupAddPrimaryMemberDescriptor.py

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


class AsyncMirrorGroupAddPrimaryMemberDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupAddPrimaryMemberDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_ref': 'str',  # (required parameter)
            'local_volume': 'str',  # (required parameter)
            'remote_password': 'RemoteArrayAuthenticator',  # (required parameter)
            'repository_candidate': 'ConcatVolumeCreationDescriptor'
        }

        self.attribute_map = {
            'group_ref': 'groupRef',  # (required parameter)
            'local_volume': 'localVolume',  # (required parameter)
            'remote_password': 'remotePassword',  # (required parameter)
            'repository_candidate': 'repositoryCandidate'
        }

        self._group_ref = None
        self._local_volume = None
        self._remote_password = None
        self._repository_candidate = None

    @property
    def group_ref(self):
        """
        Gets the group_ref of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The AMG to which the member will be added.

        :return: The group_ref of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._group_ref

    @group_ref.setter
    def group_ref(self, group_ref):
        """
        Sets the group_ref of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The AMG to which the member will be added.

        :param group_ref: The group_ref of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :type: str
        """
        self._group_ref = group_ref

    @property
    def local_volume(self):
        """
        Gets the local_volume of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The member local volume to add to the AMG.

        :return: The local_volume of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._local_volume

    @local_volume.setter
    def local_volume(self, local_volume):
        """
        Sets the local_volume of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The member local volume to add to the AMG.

        :param local_volume: The local_volume of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :type: str
        """
        self._local_volume = local_volume

    @property
    def remote_password(self):
        """
        Gets the remote_password of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The password for remote array. This is required to make sure the SYMbol client has authenticated the users access privileges to both the primary and secondary array.

        :return: The remote_password of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :rtype: RemoteArrayAuthenticator
        :required/optional: required
        """
        return self._remote_password

    @remote_password.setter
    def remote_password(self, remote_password):
        """
        Sets the remote_password of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The password for remote array. This is required to make sure the SYMbol client has authenticated the users access privileges to both the primary and secondary array.

        :param remote_password: The remote_password of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :type: RemoteArrayAuthenticator
        """
        self._remote_password = remote_password

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The repository volume candidate for the mirror repository on the primary array.

        :return: The repository_candidate of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        :rtype: ConcatVolumeCreationDescriptor
        :required/optional: required
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
        The repository volume candidate for the mirror repository on the primary array.

        :param repository_candidate: The repository_candidate of this AsyncMirrorGroupAddPrimaryMemberDescriptor.
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
