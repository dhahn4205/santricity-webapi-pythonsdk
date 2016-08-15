# coding: utf-8

"""
KeyIDInfo.py

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


class KeyIDInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        KeyIDInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lock_key_id': 'str',  # (required parameter)
            'pass_phrase': 'str'
        }

        self.attribute_map = {
            'lock_key_id': 'lockKeyID',  # (required parameter)
            'pass_phrase': 'passPhrase'
        }

        self._lock_key_id = None
        self._pass_phrase = None

    @property
    def lock_key_id(self):
        """
        Gets the lock_key_id of this KeyIDInfo.
        This is the lock Key ID. Whenever a lock key is initialized or changed, a new lock key ID is generated. The lock key ID can be set to a value set by the user, or the controller can generate a lock key. The lock key ID is written to all security-enabled drives that use the referenced lock key. Note that the lock key ID can be read at any time from the disk drive, even if the drive is locked.

        :return: The lock_key_id of this KeyIDInfo.
        :rtype: str
        :required/optional: required
        """
        return self._lock_key_id

    @lock_key_id.setter
    def lock_key_id(self, lock_key_id):
        """
        Sets the lock_key_id of this KeyIDInfo.
        This is the lock Key ID. Whenever a lock key is initialized or changed, a new lock key ID is generated. The lock key ID can be set to a value set by the user, or the controller can generate a lock key. The lock key ID is written to all security-enabled drives that use the referenced lock key. Note that the lock key ID can be read at any time from the disk drive, even if the drive is locked.

        :param lock_key_id: The lock_key_id of this KeyIDInfo.
        :type: str
        """
        self._lock_key_id = lock_key_id

    @property
    def pass_phrase(self):
        """
        Gets the pass_phrase of this KeyIDInfo.
        The Pass Phrase is an alphanumeric string that is used to provide a human-compatible method of generating a lock key (for MegaRAID controllers) or for securely wrapping the lock key (external controllers). The controller firmware places no restrictions on the Pass Phrase, but for improved security, the management application will place the following requirements on a Pass Phrase used for any purpose:

        :return: The pass_phrase of this KeyIDInfo.
        :rtype: str
        :required/optional: required
        """
        return self._pass_phrase

    @pass_phrase.setter
    def pass_phrase(self, pass_phrase):
        """
        Sets the pass_phrase of this KeyIDInfo.
        The Pass Phrase is an alphanumeric string that is used to provide a human-compatible method of generating a lock key (for MegaRAID controllers) or for securely wrapping the lock key (external controllers). The controller firmware places no restrictions on the Pass Phrase, but for improved security, the management application will place the following requirements on a Pass Phrase used for any purpose:

        :param pass_phrase: The pass_phrase of this KeyIDInfo.
        :type: str
        """
        self._pass_phrase = pass_phrase

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

