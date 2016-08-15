# coding: utf-8

"""
IscsiTargetUpdateRequest.py

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


class IscsiTargetUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiTargetUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alias': 'str',  
            'enable_chap_authentication': 'bool',  
            'chap_secret': 'str'
        }

        self.attribute_map = {
            'alias': 'alias',  
            'enable_chap_authentication': 'enableChapAuthentication',  
            'chap_secret': 'chapSecret'
        }

        self._alias = None
        self._enable_chap_authentication = None
        self._chap_secret = None

    @property
    def alias(self):
        """
        Gets the alias of this IscsiTargetUpdateRequest.
        The iSCSI target alias.

        :return: The alias of this IscsiTargetUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this IscsiTargetUpdateRequest.
        The iSCSI target alias.

        :param alias: The alias of this IscsiTargetUpdateRequest.
        :type: str
        """
        self._alias = alias

    @property
    def enable_chap_authentication(self):
        """
        Gets the enable_chap_authentication of this IscsiTargetUpdateRequest.
        Enable Challenge-Handshake Authentication Protocol (CHAP), defaults to false.

        :return: The enable_chap_authentication of this IscsiTargetUpdateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._enable_chap_authentication

    @enable_chap_authentication.setter
    def enable_chap_authentication(self, enable_chap_authentication):
        """
        Sets the enable_chap_authentication of this IscsiTargetUpdateRequest.
        Enable Challenge-Handshake Authentication Protocol (CHAP), defaults to false.

        :param enable_chap_authentication: The enable_chap_authentication of this IscsiTargetUpdateRequest.
        :type: bool
        """
        self._enable_chap_authentication = enable_chap_authentication

    @property
    def chap_secret(self):
        """
        Gets the chap_secret of this IscsiTargetUpdateRequest.
        Enable Challenge-Handshake Authentication Protocol (CHAP) using the provided password. A      secure password will be generated and returned if CHAP is enabled and this field is not provided.

        :return: The chap_secret of this IscsiTargetUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """
        Sets the chap_secret of this IscsiTargetUpdateRequest.
        Enable Challenge-Handshake Authentication Protocol (CHAP) using the provided password. A      secure password will be generated and returned if CHAP is enabled and this field is not provided.

        :param chap_secret: The chap_secret of this IscsiTargetUpdateRequest.
        :type: str
        """
        self._chap_secret = chap_secret

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
