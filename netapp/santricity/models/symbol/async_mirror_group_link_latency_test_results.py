# coding: utf-8

"""
AsyncMirrorGroupLinkLatencyTestResults.py

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


class AsyncMirrorGroupLinkLatencyTestResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncMirrorGroupLinkLatencyTestResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'min_latency_in_microseconds': 'int',  # (required parameter)
            'max_latency_in_microseconds': 'int',  # (required parameter)
            'avg_latency_in_microseconds': 'int'
        }

        self.attribute_map = {
            'min_latency_in_microseconds': 'minLatencyInMicroseconds',  # (required parameter)
            'max_latency_in_microseconds': 'maxLatencyInMicroseconds',  # (required parameter)
            'avg_latency_in_microseconds': 'avgLatencyInMicroseconds'
        }

        self._min_latency_in_microseconds = None
        self._max_latency_in_microseconds = None
        self._avg_latency_in_microseconds = None

    @property
    def min_latency_in_microseconds(self):
        """
        Gets the min_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The minimum latency measured in microseconds.

        :return: The min_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._min_latency_in_microseconds

    @min_latency_in_microseconds.setter
    def min_latency_in_microseconds(self, min_latency_in_microseconds):
        """
        Sets the min_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The minimum latency measured in microseconds.

        :param min_latency_in_microseconds: The min_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :type: int
        """
        self._min_latency_in_microseconds = min_latency_in_microseconds

    @property
    def max_latency_in_microseconds(self):
        """
        Gets the max_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The maximum latency measured in microseconds.

        :return: The max_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._max_latency_in_microseconds

    @max_latency_in_microseconds.setter
    def max_latency_in_microseconds(self, max_latency_in_microseconds):
        """
        Sets the max_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The maximum latency measured in microseconds.

        :param max_latency_in_microseconds: The max_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :type: int
        """
        self._max_latency_in_microseconds = max_latency_in_microseconds

    @property
    def avg_latency_in_microseconds(self):
        """
        Gets the avg_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The average latency measured in microseconds.

        :return: The avg_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :rtype: int
        :required/optional: required
        """
        return self._avg_latency_in_microseconds

    @avg_latency_in_microseconds.setter
    def avg_latency_in_microseconds(self, avg_latency_in_microseconds):
        """
        Sets the avg_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        The average latency measured in microseconds.

        :param avg_latency_in_microseconds: The avg_latency_in_microseconds of this AsyncMirrorGroupLinkLatencyTestResults.
        :type: int
        """
        self._avg_latency_in_microseconds = avg_latency_in_microseconds

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

