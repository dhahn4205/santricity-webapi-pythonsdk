# coding: utf-8

"""
KeyValueTag.py

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


class KeyValueTag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        KeyValueTag - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key_value_tag_ref': 'str',  # (required parameter)
            'key': 'str',  # (required parameter)
            'value': 'str'
        }

        self.attribute_map = {
            'key_value_tag_ref': 'keyValueTagRef',  # (required parameter)
            'key': 'key',  # (required parameter)
            'value': 'value'
        }

        self._key_value_tag_ref = None
        self._key = None
        self._value = None

    @property
    def key_value_tag_ref(self):
        """
        Gets the key_value_tag_ref of this KeyValueTag.
        The unique handle for a key-value object contained within this structure.

        :return: The key_value_tag_ref of this KeyValueTag.
        :rtype: str
        :required/optional: required
        """
        return self._key_value_tag_ref

    @key_value_tag_ref.setter
    def key_value_tag_ref(self, key_value_tag_ref):
        """
        Sets the key_value_tag_ref of this KeyValueTag.
        The unique handle for a key-value object contained within this structure.

        :param key_value_tag_ref: The key_value_tag_ref of this KeyValueTag.
        :type: str
        """
        self._key_value_tag_ref = key_value_tag_ref

    @property
    def key(self):
        """
        Gets the key of this KeyValueTag.
        The key is a fixed length, opaque byte sequence that stores user-defined data.

        :return: The key of this KeyValueTag.
        :rtype: str
        :required/optional: required
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this KeyValueTag.
        The key is a fixed length, opaque byte sequence that stores user-defined data.

        :param key: The key of this KeyValueTag.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        Gets the value of this KeyValueTag.
        The value is a fixed length opaque byte sequence that stores user-defined data.

        :return: The value of this KeyValueTag.
        :rtype: str
        :required/optional: required
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this KeyValueTag.
        The value is a fixed length opaque byte sequence that stores user-defined data.

        :param value: The value of this KeyValueTag.
        :type: str
        """
        self._value = value

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

