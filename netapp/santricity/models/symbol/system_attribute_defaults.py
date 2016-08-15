# coding: utf-8

"""
SystemAttributeDefaults.py

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


class SystemAttributeDefaults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SystemAttributeDefaults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'disk_pool_default_attributes': 'DiskPoolDefaultAttributes',  # (required parameter)
            'thin_vol_default_attributes': 'ThinVolumeDefaultAttributes',  # (required parameter)
            'pit_groups_default_attributes': 'PITGroupsDefaultAttributes',  # (required parameter)
            'arvm_default_attributes': 'ARVMDefaultAttributes',  # (required parameter)
            'concat_default_attributes': 'ConcatVolumeDefaultAttributes',  # (required parameter)
            'snmp_agent_default_attributes': 'EmbeddedSNMPAgentDefaultAttributes',  # (required parameter)
            'statistics_default_attributes': 'CumulativeStatisticsDefaultAttributes'
        }

        self.attribute_map = {
            'disk_pool_default_attributes': 'diskPoolDefaultAttributes',  # (required parameter)
            'thin_vol_default_attributes': 'thinVolDefaultAttributes',  # (required parameter)
            'pit_groups_default_attributes': 'pitGroupsDefaultAttributes',  # (required parameter)
            'arvm_default_attributes': 'arvmDefaultAttributes',  # (required parameter)
            'concat_default_attributes': 'concatDefaultAttributes',  # (required parameter)
            'snmp_agent_default_attributes': 'snmpAgentDefaultAttributes',  # (required parameter)
            'statistics_default_attributes': 'statisticsDefaultAttributes'
        }

        self._disk_pool_default_attributes = None
        self._thin_vol_default_attributes = None
        self._pit_groups_default_attributes = None
        self._arvm_default_attributes = None
        self._concat_default_attributes = None
        self._snmp_agent_default_attributes = None
        self._statistics_default_attributes = None

    @property
    def disk_pool_default_attributes(self):
        """
        Gets the disk_pool_default_attributes of this SystemAttributeDefaults.
        Default Disk Pool feature attributes.

        :return: The disk_pool_default_attributes of this SystemAttributeDefaults.
        :rtype: DiskPoolDefaultAttributes
        :required/optional: required
        """
        return self._disk_pool_default_attributes

    @disk_pool_default_attributes.setter
    def disk_pool_default_attributes(self, disk_pool_default_attributes):
        """
        Sets the disk_pool_default_attributes of this SystemAttributeDefaults.
        Default Disk Pool feature attributes.

        :param disk_pool_default_attributes: The disk_pool_default_attributes of this SystemAttributeDefaults.
        :type: DiskPoolDefaultAttributes
        """
        self._disk_pool_default_attributes = disk_pool_default_attributes

    @property
    def thin_vol_default_attributes(self):
        """
        Gets the thin_vol_default_attributes of this SystemAttributeDefaults.
        Default Thin Volume feature attributes.

        :return: The thin_vol_default_attributes of this SystemAttributeDefaults.
        :rtype: ThinVolumeDefaultAttributes
        :required/optional: required
        """
        return self._thin_vol_default_attributes

    @thin_vol_default_attributes.setter
    def thin_vol_default_attributes(self, thin_vol_default_attributes):
        """
        Sets the thin_vol_default_attributes of this SystemAttributeDefaults.
        Default Thin Volume feature attributes.

        :param thin_vol_default_attributes: The thin_vol_default_attributes of this SystemAttributeDefaults.
        :type: ThinVolumeDefaultAttributes
        """
        self._thin_vol_default_attributes = thin_vol_default_attributes

    @property
    def pit_groups_default_attributes(self):
        """
        Gets the pit_groups_default_attributes of this SystemAttributeDefaults.
        Default PiT Groups feature attributes.

        :return: The pit_groups_default_attributes of this SystemAttributeDefaults.
        :rtype: PITGroupsDefaultAttributes
        :required/optional: required
        """
        return self._pit_groups_default_attributes

    @pit_groups_default_attributes.setter
    def pit_groups_default_attributes(self, pit_groups_default_attributes):
        """
        Sets the pit_groups_default_attributes of this SystemAttributeDefaults.
        Default PiT Groups feature attributes.

        :param pit_groups_default_attributes: The pit_groups_default_attributes of this SystemAttributeDefaults.
        :type: PITGroupsDefaultAttributes
        """
        self._pit_groups_default_attributes = pit_groups_default_attributes

    @property
    def arvm_default_attributes(self):
        """
        Gets the arvm_default_attributes of this SystemAttributeDefaults.
        Default ARVM feature attributes.

        :return: The arvm_default_attributes of this SystemAttributeDefaults.
        :rtype: ARVMDefaultAttributes
        :required/optional: required
        """
        return self._arvm_default_attributes

    @arvm_default_attributes.setter
    def arvm_default_attributes(self, arvm_default_attributes):
        """
        Sets the arvm_default_attributes of this SystemAttributeDefaults.
        Default ARVM feature attributes.

        :param arvm_default_attributes: The arvm_default_attributes of this SystemAttributeDefaults.
        :type: ARVMDefaultAttributes
        """
        self._arvm_default_attributes = arvm_default_attributes

    @property
    def concat_default_attributes(self):
        """
        Gets the concat_default_attributes of this SystemAttributeDefaults.
        Default ConcatVolume feature attributes.

        :return: The concat_default_attributes of this SystemAttributeDefaults.
        :rtype: ConcatVolumeDefaultAttributes
        :required/optional: required
        """
        return self._concat_default_attributes

    @concat_default_attributes.setter
    def concat_default_attributes(self, concat_default_attributes):
        """
        Sets the concat_default_attributes of this SystemAttributeDefaults.
        Default ConcatVolume feature attributes.

        :param concat_default_attributes: The concat_default_attributes of this SystemAttributeDefaults.
        :type: ConcatVolumeDefaultAttributes
        """
        self._concat_default_attributes = concat_default_attributes

    @property
    def snmp_agent_default_attributes(self):
        """
        Gets the snmp_agent_default_attributes of this SystemAttributeDefaults.
        Default/maximum attributes for the embedded SNMP agent.

        :return: The snmp_agent_default_attributes of this SystemAttributeDefaults.
        :rtype: EmbeddedSNMPAgentDefaultAttributes
        :required/optional: required
        """
        return self._snmp_agent_default_attributes

    @snmp_agent_default_attributes.setter
    def snmp_agent_default_attributes(self, snmp_agent_default_attributes):
        """
        Sets the snmp_agent_default_attributes of this SystemAttributeDefaults.
        Default/maximum attributes for the embedded SNMP agent.

        :param snmp_agent_default_attributes: The snmp_agent_default_attributes of this SystemAttributeDefaults.
        :type: EmbeddedSNMPAgentDefaultAttributes
        """
        self._snmp_agent_default_attributes = snmp_agent_default_attributes

    @property
    def statistics_default_attributes(self):
        """
        Gets the statistics_default_attributes of this SystemAttributeDefaults.
        Specifies the low and high statistical sampling attributes supported by this array.

        :return: The statistics_default_attributes of this SystemAttributeDefaults.
        :rtype: CumulativeStatisticsDefaultAttributes
        :required/optional: required
        """
        return self._statistics_default_attributes

    @statistics_default_attributes.setter
    def statistics_default_attributes(self, statistics_default_attributes):
        """
        Sets the statistics_default_attributes of this SystemAttributeDefaults.
        Specifies the low and high statistical sampling attributes supported by this array.

        :param statistics_default_attributes: The statistics_default_attributes of this SystemAttributeDefaults.
        :type: CumulativeStatisticsDefaultAttributes
        """
        self._statistics_default_attributes = statistics_default_attributes

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
