# coding: utf-8

"""
IbPointInTimeStatistics.py

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


class IbPointInTimeStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IbPointInTimeStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time_of_reading': 'int',  # (required parameter)
            'ib_tca_statistics': 'list[IbTcaStatistics]',  # (required parameter)
            'ib_rdma_channel_statistics': 'list[IbRdmaChannelStatistics]'
        }

        self.attribute_map = {
            'time_of_reading': 'timeOfReading',  # (required parameter)
            'ib_tca_statistics': 'ibTcaStatistics',  # (required parameter)
            'ib_rdma_channel_statistics': 'ibRdmaChannelStatistics'
        }

        self._time_of_reading = None
        self._ib_tca_statistics = None
        self._ib_rdma_channel_statistics = None

    @property
    def time_of_reading(self):
        """
        Gets the time_of_reading of this IbPointInTimeStatistics.
        A timestamp, expressed as number of seconds since midnight GMT on January 1, 1970, which is the time at which the statistics were read by the controller firmware.

        :return: The time_of_reading of this IbPointInTimeStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._time_of_reading

    @time_of_reading.setter
    def time_of_reading(self, time_of_reading):
        """
        Sets the time_of_reading of this IbPointInTimeStatistics.
        A timestamp, expressed as number of seconds since midnight GMT on January 1, 1970, which is the time at which the statistics were read by the controller firmware.

        :param time_of_reading: The time_of_reading of this IbPointInTimeStatistics.
        :type: int
        """
        self._time_of_reading = time_of_reading

    @property
    def ib_tca_statistics(self):
        """
        Gets the ib_tca_statistics of this IbPointInTimeStatistics.
        An array of structures containing the IB TCA statistics, one structure per TCA (i.e., InfiniBand host board).

        :return: The ib_tca_statistics of this IbPointInTimeStatistics.
        :rtype: list[IbTcaStatistics]
        :required/optional: required
        """
        return self._ib_tca_statistics

    @ib_tca_statistics.setter
    def ib_tca_statistics(self, ib_tca_statistics):
        """
        Sets the ib_tca_statistics of this IbPointInTimeStatistics.
        An array of structures containing the IB TCA statistics, one structure per TCA (i.e., InfiniBand host board).

        :param ib_tca_statistics: The ib_tca_statistics of this IbPointInTimeStatistics.
        :type: list[IbTcaStatistics]
        """
        self._ib_tca_statistics = ib_tca_statistics

    @property
    def ib_rdma_channel_statistics(self):
        """
        Gets the ib_rdma_channel_statistics of this IbPointInTimeStatistics.
        An array of structures containing the IB RDMA channel statistics, one structure per RDMA channel.

        :return: The ib_rdma_channel_statistics of this IbPointInTimeStatistics.
        :rtype: list[IbRdmaChannelStatistics]
        :required/optional: required
        """
        return self._ib_rdma_channel_statistics

    @ib_rdma_channel_statistics.setter
    def ib_rdma_channel_statistics(self, ib_rdma_channel_statistics):
        """
        Sets the ib_rdma_channel_statistics of this IbPointInTimeStatistics.
        An array of structures containing the IB RDMA channel statistics, one structure per RDMA channel.

        :param ib_rdma_channel_statistics: The ib_rdma_channel_statistics of this IbPointInTimeStatistics.
        :type: list[IbRdmaChannelStatistics]
        """
        self._ib_rdma_channel_statistics = ib_rdma_channel_statistics

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

