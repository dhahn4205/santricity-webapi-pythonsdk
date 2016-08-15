# coding: utf-8

"""
RepairPolicy.py

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


class RepairPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RepairPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'removal_data': 'ComponentRemovalData',  # (required parameter)
            'replacement_method': 'str'
        }

        self.attribute_map = {
            'removal_data': 'removalData',  # (required parameter)
            'replacement_method': 'replacementMethod'
        }

        self._removal_data = None
        self._replacement_method = None

    @property
    def removal_data(self):
        """
        Gets the removal_data of this RepairPolicy.
        This field contains the removal data for the component. This primary piece of data is a removal method. Additional \"ready-to-remove\" attributes may be defined, depending on the removal method.

        :return: The removal_data of this RepairPolicy.
        :rtype: ComponentRemovalData
        :required/optional: required
        """
        return self._removal_data

    @removal_data.setter
    def removal_data(self, removal_data):
        """
        Sets the removal_data of this RepairPolicy.
        This field contains the removal data for the component. This primary piece of data is a removal method. Additional \"ready-to-remove\" attributes may be defined, depending on the removal method.

        :param removal_data: The removal_data of this RepairPolicy.
        :type: ComponentRemovalData
        """
        self._removal_data = removal_data

    @property
    def replacement_method(self):
        """
        Gets the replacement_method of this RepairPolicy.
        This field defines the \"replacement method\" for the component.

        :return: The replacement_method of this RepairPolicy.
        :rtype: str
        :required/optional: required
        """
        return self._replacement_method

    @replacement_method.setter
    def replacement_method(self, replacement_method):
        """
        Sets the replacement_method of this RepairPolicy.
        This field defines the \"replacement method\" for the component.

        :param replacement_method: The replacement_method of this RepairPolicy.
        :type: str
        """
        allowed_values = ["parent", "self", "__UNDEFINED"]
        if replacement_method not in allowed_values:
            raise ValueError(
                "Invalid value for `replacement_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._replacement_method = replacement_method

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

