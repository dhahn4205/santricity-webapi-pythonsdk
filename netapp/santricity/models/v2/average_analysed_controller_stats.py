# coding: utf-8

"""
AverageAnalysedControllerStats.py

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


class AverageAnalysedControllerStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AverageAnalysedControllerStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',  # (required parameter)
            'iops_read': 'AverageAnalysedValue',  # (required parameter)
            'iops_write': 'AverageAnalysedValue',  # (required parameter)
            'throughput_read': 'AverageAnalysedValue',  # (required parameter)
            'throughput_write': 'AverageAnalysedValue',  # (required parameter)
            'cpu_utilization': 'AverageAnalysedValue',  # (required parameter)
            'headroom_pct': 'AverageAnalysedValue'
        }

        self.attribute_map = {
            'id': 'id',  # (required parameter)
            'iops_read': 'iopsRead',  # (required parameter)
            'iops_write': 'iopsWrite',  # (required parameter)
            'throughput_read': 'throughputRead',  # (required parameter)
            'throughput_write': 'throughputWrite',  # (required parameter)
            'cpu_utilization': 'cpuUtilization',  # (required parameter)
            'headroom_pct': 'headroomPct'
        }

        self._id = None
        self._iops_read = None
        self._iops_write = None
        self._throughput_read = None
        self._throughput_write = None
        self._cpu_utilization = None
        self._headroom_pct = None

    @property
    def id(self):
        """
        Gets the id of this AverageAnalysedControllerStats.


        :return: The id of this AverageAnalysedControllerStats.
        :rtype: str
        :required/optional: required
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AverageAnalysedControllerStats.


        :param id: The id of this AverageAnalysedControllerStats.
        :type: str
        """
        self._id = id

    @property
    def iops_read(self):
        """
        Gets the iops_read of this AverageAnalysedControllerStats.


        :return: The iops_read of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._iops_read

    @iops_read.setter
    def iops_read(self, iops_read):
        """
        Sets the iops_read of this AverageAnalysedControllerStats.


        :param iops_read: The iops_read of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._iops_read = iops_read

    @property
    def iops_write(self):
        """
        Gets the iops_write of this AverageAnalysedControllerStats.


        :return: The iops_write of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._iops_write

    @iops_write.setter
    def iops_write(self, iops_write):
        """
        Sets the iops_write of this AverageAnalysedControllerStats.


        :param iops_write: The iops_write of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._iops_write = iops_write

    @property
    def throughput_read(self):
        """
        Gets the throughput_read of this AverageAnalysedControllerStats.


        :return: The throughput_read of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._throughput_read

    @throughput_read.setter
    def throughput_read(self, throughput_read):
        """
        Sets the throughput_read of this AverageAnalysedControllerStats.


        :param throughput_read: The throughput_read of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._throughput_read = throughput_read

    @property
    def throughput_write(self):
        """
        Gets the throughput_write of this AverageAnalysedControllerStats.


        :return: The throughput_write of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._throughput_write

    @throughput_write.setter
    def throughput_write(self, throughput_write):
        """
        Sets the throughput_write of this AverageAnalysedControllerStats.


        :param throughput_write: The throughput_write of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._throughput_write = throughput_write

    @property
    def cpu_utilization(self):
        """
        Gets the cpu_utilization of this AverageAnalysedControllerStats.


        :return: The cpu_utilization of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """
        Sets the cpu_utilization of this AverageAnalysedControllerStats.


        :param cpu_utilization: The cpu_utilization of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._cpu_utilization = cpu_utilization

    @property
    def headroom_pct(self):
        """
        Gets the headroom_pct of this AverageAnalysedControllerStats.


        :return: The headroom_pct of this AverageAnalysedControllerStats.
        :rtype: AverageAnalysedValue
        :required/optional: required
        """
        return self._headroom_pct

    @headroom_pct.setter
    def headroom_pct(self, headroom_pct):
        """
        Sets the headroom_pct of this AverageAnalysedControllerStats.


        :param headroom_pct: The headroom_pct of this AverageAnalysedControllerStats.
        :type: AverageAnalysedValue
        """
        self._headroom_pct = headroom_pct

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

