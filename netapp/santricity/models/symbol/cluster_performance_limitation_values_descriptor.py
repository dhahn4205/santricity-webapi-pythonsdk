# coding: utf-8

"""
ClusterPerformanceLimitationValuesDescriptor.py

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


class ClusterPerformanceLimitationValuesDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterPerformanceLimitationValuesDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cluster_ref': 'str',  # (required parameter)
            'max_iops_on_cluster': 'int',  # (required parameter)
            'max_m_bs_on_cluster': 'int'
        }

        self.attribute_map = {
            'cluster_ref': 'clusterRef',  # (required parameter)
            'max_iops_on_cluster': 'maxIopsOnCluster',  # (required parameter)
            'max_m_bs_on_cluster': 'maxMBsOnCluster'
        }

        self._cluster_ref = None
        self._max_iops_on_cluster = None
        self._max_m_bs_on_cluster = None

    @property
    def cluster_ref(self):
        """
        Gets the cluster_ref of this ClusterPerformanceLimitationValuesDescriptor.
        This is the reference to the cluster for which the performance parameters apply.

        :return: The cluster_ref of this ClusterPerformanceLimitationValuesDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._cluster_ref

    @cluster_ref.setter
    def cluster_ref(self, cluster_ref):
        """
        Sets the cluster_ref of this ClusterPerformanceLimitationValuesDescriptor.
        This is the reference to the cluster for which the performance parameters apply.

        :param cluster_ref: The cluster_ref of this ClusterPerformanceLimitationValuesDescriptor.
        :type: str
        """
        self._cluster_ref = cluster_ref

    @property
    def max_iops_on_cluster(self):
        """
        Gets the max_iops_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        This is the maximum number of IOPs allowed for the cluster. The controller firmware will limit the number of IOPs for a cluster to this value. A value of CLUSTER_PERFORMANCE_LIMIT_DEFAULT_VALUE (0) means that no performance limitations have been placed on the cluster.

        :return: The max_iops_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._max_iops_on_cluster

    @max_iops_on_cluster.setter
    def max_iops_on_cluster(self, max_iops_on_cluster):
        """
        Sets the max_iops_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        This is the maximum number of IOPs allowed for the cluster. The controller firmware will limit the number of IOPs for a cluster to this value. A value of CLUSTER_PERFORMANCE_LIMIT_DEFAULT_VALUE (0) means that no performance limitations have been placed on the cluster.

        :param max_iops_on_cluster: The max_iops_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        :type: int
        """
        self._max_iops_on_cluster = max_iops_on_cluster

    @property
    def max_m_bs_on_cluster(self):
        """
        Gets the max_m_bs_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        This is the maximum number of MB per second that will be supported on the cluster. The controller firmware will limit the throughput for the cluster to this value. A value of CLUSTER_PERFORMANCE_LIMIT_DEFAULT_VALUE (0) means that no throughput limitations exist on the cluster.

        :return: The max_m_bs_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._max_m_bs_on_cluster

    @max_m_bs_on_cluster.setter
    def max_m_bs_on_cluster(self, max_m_bs_on_cluster):
        """
        Sets the max_m_bs_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        This is the maximum number of MB per second that will be supported on the cluster. The controller firmware will limit the throughput for the cluster to this value. A value of CLUSTER_PERFORMANCE_LIMIT_DEFAULT_VALUE (0) means that no throughput limitations exist on the cluster.

        :param max_m_bs_on_cluster: The max_m_bs_on_cluster of this ClusterPerformanceLimitationValuesDescriptor.
        :type: int
        """
        self._max_m_bs_on_cluster = max_m_bs_on_cluster

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

