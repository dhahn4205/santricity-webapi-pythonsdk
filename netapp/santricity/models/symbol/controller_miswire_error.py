# coding: utf-8

"""
ControllerMiswireError.py

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


class ControllerMiswireError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ControllerMiswireError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'port_ref_a': 'str',  # (required parameter)
            'port_ref_b': 'str',  # (required parameter)
            'port_refs': 'list[str]'
        }

        self.attribute_map = {
            'port_ref_a': 'portRefA',  # (required parameter)
            'port_ref_b': 'portRefB',  # (required parameter)
            'port_refs': 'portRefs'
        }

        self._port_ref_a = None
        self._port_ref_b = None
        self._port_refs = None

    @property
    def port_ref_a(self):
        """
        Gets the port_ref_a of this ControllerMiswireError.
        A reference to one of the drive channel ports involved in a controller miswire.

        :return: The port_ref_a of this ControllerMiswireError.
        :rtype: str
        :required/optional: required
        """
        return self._port_ref_a

    @port_ref_a.setter
    def port_ref_a(self, port_ref_a):
        """
        Sets the port_ref_a of this ControllerMiswireError.
        A reference to one of the drive channel ports involved in a controller miswire.

        :param port_ref_a: The port_ref_a of this ControllerMiswireError.
        :type: str
        """
        self._port_ref_a = port_ref_a

    @property
    def port_ref_b(self):
        """
        Gets the port_ref_b of this ControllerMiswireError.
        A reference to one of the drive channel ports involved in a controller miswire.

        :return: The port_ref_b of this ControllerMiswireError.
        :rtype: str
        :required/optional: required
        """
        return self._port_ref_b

    @port_ref_b.setter
    def port_ref_b(self, port_ref_b):
        """
        Sets the port_ref_b of this ControllerMiswireError.
        A reference to one of the drive channel ports involved in a controller miswire.

        :param port_ref_b: The port_ref_b of this ControllerMiswireError.
        :type: str
        """
        self._port_ref_b = port_ref_b

    @property
    def port_refs(self):
        """
        Gets the port_refs of this ControllerMiswireError.
        The two drive channel ports on one controller that are participating in the miswire condition.

        :return: The port_refs of this ControllerMiswireError.
        :rtype: list[str]
        :required/optional: required
        """
        return self._port_refs

    @port_refs.setter
    def port_refs(self, port_refs):
        """
        Sets the port_refs of this ControllerMiswireError.
        The two drive channel ports on one controller that are participating in the miswire condition.

        :param port_refs: The port_refs of this ControllerMiswireError.
        :type: list[str]
        """
        self._port_refs = port_refs

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

