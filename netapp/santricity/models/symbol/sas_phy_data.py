# coding: utf-8

"""
SasPhyData.py

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


class SasPhyData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SasPhyData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phy_identifier': 'int',  # (required parameter)
            'is_valid': 'bool',  # (required parameter)
            'current_speed': 'str',  # (required parameter)
            'maximum_speed': 'str',  # (required parameter)
            'error_counts': 'SasPhyErrorCounts'
        }

        self.attribute_map = {
            'phy_identifier': 'phyIdentifier',  # (required parameter)
            'is_valid': 'isValid',  # (required parameter)
            'current_speed': 'currentSpeed',  # (required parameter)
            'maximum_speed': 'maximumSpeed',  # (required parameter)
            'error_counts': 'errorCounts'
        }

        self._phy_identifier = None
        self._is_valid = None
        self._current_speed = None
        self._maximum_speed = None
        self._error_counts = None

    @property
    def phy_identifier(self):
        """
        Gets the phy_identifier of this SasPhyData.
        A number in the range 0 - 127 that is the PHY identifier.

        :return: The phy_identifier of this SasPhyData.
        :rtype: int
        :required/optional: required
        """
        return self._phy_identifier

    @phy_identifier.setter
    def phy_identifier(self, phy_identifier):
        """
        Sets the phy_identifier of this SasPhyData.
        A number in the range 0 - 127 that is the PHY identifier.

        :param phy_identifier: The phy_identifier of this SasPhyData.
        :type: int
        """
        self._phy_identifier = phy_identifier

    @property
    def is_valid(self):
        """
        Gets the is_valid of this SasPhyData.
        When false, an indication that, though the associated attached device exists, the rest of the data in the structure could not be obtained.

        :return: The is_valid of this SasPhyData.
        :rtype: bool
        :required/optional: required
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this SasPhyData.
        When false, an indication that, though the associated attached device exists, the rest of the data in the structure could not be obtained.

        :param is_valid: The is_valid of this SasPhyData.
        :type: bool
        """
        self._is_valid = is_valid

    @property
    def current_speed(self):
        """
        Gets the current_speed of this SasPhyData.
        The current negotiated physical link rate for the PHY.

        :return: The current_speed of this SasPhyData.
        :rtype: str
        :required/optional: required
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        """
        Sets the current_speed of this SasPhyData.
        The current negotiated physical link rate for the PHY.

        :param current_speed: The current_speed of this SasPhyData.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "__UNDEFINED"]
        if current_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `current_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._current_speed = current_speed

    @property
    def maximum_speed(self):
        """
        Gets the maximum_speed of this SasPhyData.
        The hardware maximum physical link rate for the PHY.

        :return: The maximum_speed of this SasPhyData.
        :rtype: str
        :required/optional: required
        """
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, maximum_speed):
        """
        Sets the maximum_speed of this SasPhyData.
        The hardware maximum physical link rate for the PHY.

        :param maximum_speed: The maximum_speed of this SasPhyData.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "__UNDEFINED"]
        if maximum_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `maximum_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._maximum_speed = maximum_speed

    @property
    def error_counts(self):
        """
        Gets the error_counts of this SasPhyData.
        A collection of PHY error count values.

        :return: The error_counts of this SasPhyData.
        :rtype: SasPhyErrorCounts
        :required/optional: required
        """
        return self._error_counts

    @error_counts.setter
    def error_counts(self, error_counts):
        """
        Sets the error_counts of this SasPhyData.
        A collection of PHY error count values.

        :param error_counts: The error_counts of this SasPhyData.
        :type: SasPhyErrorCounts
        """
        self._error_counts = error_counts

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

