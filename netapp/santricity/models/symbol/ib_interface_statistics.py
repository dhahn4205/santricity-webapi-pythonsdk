# coding: utf-8

"""
IbInterfaceStatistics.py

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


class IbInterfaceStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IbInterfaceStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interface_ref': 'str',  # (required parameter)
            'symbol_errors': 'int',  # (required parameter)
            'recovered_link_errors': 'int',  # (required parameter)
            'unrecovered_link_errors': 'int',  # (required parameter)
            'rx_packet_errors': 'int',  # (required parameter)
            'rx_ebp_delimited_packets': 'int',  # (required parameter)
            'tx_port_down_packet_discards': 'int',  # (required parameter)
            'tx_constraint_error_packet_discards': 'int',  # (required parameter)
            'rx_constraint_error_packet_discards': 'int',  # (required parameter)
            'rx_subnet_management_dropped_packets': 'int',  # (required parameter)
            'tx_total_bytes': 'int',  # (required parameter)
            'rx_total_bytes': 'int',  # (required parameter)
            'tx_total_packets': 'int',  # (required parameter)
            'rx_total_packets': 'int',  # (required parameter)
            'tx_wait_time': 'int',  # (required parameter)
            'tx_unicast_total_packets': 'int',  # (required parameter)
            'rx_unicast_total_packets': 'int',  # (required parameter)
            'tx_multicast_total_packets': 'int',  # (required parameter)
            'rx_multicast_total_packets': 'int'
        }

        self.attribute_map = {
            'interface_ref': 'interfaceRef',  # (required parameter)
            'symbol_errors': 'symbolErrors',  # (required parameter)
            'recovered_link_errors': 'recoveredLinkErrors',  # (required parameter)
            'unrecovered_link_errors': 'unrecoveredLinkErrors',  # (required parameter)
            'rx_packet_errors': 'rxPacketErrors',  # (required parameter)
            'rx_ebp_delimited_packets': 'rxEbpDelimitedPackets',  # (required parameter)
            'tx_port_down_packet_discards': 'txPortDownPacketDiscards',  # (required parameter)
            'tx_constraint_error_packet_discards': 'txConstraintErrorPacketDiscards',  # (required parameter)
            'rx_constraint_error_packet_discards': 'rxConstraintErrorPacketDiscards',  # (required parameter)
            'rx_subnet_management_dropped_packets': 'rxSubnetManagementDroppedPackets',  # (required parameter)
            'tx_total_bytes': 'txTotalBytes',  # (required parameter)
            'rx_total_bytes': 'rxTotalBytes',  # (required parameter)
            'tx_total_packets': 'txTotalPackets',  # (required parameter)
            'rx_total_packets': 'rxTotalPackets',  # (required parameter)
            'tx_wait_time': 'txWaitTime',  # (required parameter)
            'tx_unicast_total_packets': 'txUnicastTotalPackets',  # (required parameter)
            'rx_unicast_total_packets': 'rxUnicastTotalPackets',  # (required parameter)
            'tx_multicast_total_packets': 'txMulticastTotalPackets',  # (required parameter)
            'rx_multicast_total_packets': 'rxMulticastTotalPackets'
        }

        self._interface_ref = None
        self._symbol_errors = None
        self._recovered_link_errors = None
        self._unrecovered_link_errors = None
        self._rx_packet_errors = None
        self._rx_ebp_delimited_packets = None
        self._tx_port_down_packet_discards = None
        self._tx_constraint_error_packet_discards = None
        self._rx_constraint_error_packet_discards = None
        self._rx_subnet_management_dropped_packets = None
        self._tx_total_bytes = None
        self._rx_total_bytes = None
        self._tx_total_packets = None
        self._rx_total_packets = None
        self._tx_wait_time = None
        self._tx_unicast_total_packets = None
        self._rx_unicast_total_packets = None
        self._tx_multicast_total_packets = None
        self._rx_multicast_total_packets = None

    @property
    def interface_ref(self):
        """
        Gets the interface_ref of this IbInterfaceStatistics.
        A reference to the interface for which the statistics apply.

        :return: The interface_ref of this IbInterfaceStatistics.
        :rtype: str
        :required/optional: required
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """
        Sets the interface_ref of this IbInterfaceStatistics.
        A reference to the interface for which the statistics apply.

        :param interface_ref: The interface_ref of this IbInterfaceStatistics.
        :type: str
        """
        self._interface_ref = interface_ref

    @property
    def symbol_errors(self):
        """
        Gets the symbol_errors of this IbInterfaceStatistics.
        The number of symbol errors.

        :return: The symbol_errors of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._symbol_errors

    @symbol_errors.setter
    def symbol_errors(self, symbol_errors):
        """
        Sets the symbol_errors of this IbInterfaceStatistics.
        The number of symbol errors.

        :param symbol_errors: The symbol_errors of this IbInterfaceStatistics.
        :type: int
        """
        self._symbol_errors = symbol_errors

    @property
    def recovered_link_errors(self):
        """
        Gets the recovered_link_errors of this IbInterfaceStatistics.
        The number of recovered link errors.

        :return: The recovered_link_errors of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._recovered_link_errors

    @recovered_link_errors.setter
    def recovered_link_errors(self, recovered_link_errors):
        """
        Sets the recovered_link_errors of this IbInterfaceStatistics.
        The number of recovered link errors.

        :param recovered_link_errors: The recovered_link_errors of this IbInterfaceStatistics.
        :type: int
        """
        self._recovered_link_errors = recovered_link_errors

    @property
    def unrecovered_link_errors(self):
        """
        Gets the unrecovered_link_errors of this IbInterfaceStatistics.
        The number of unrecovered link errors.

        :return: The unrecovered_link_errors of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._unrecovered_link_errors

    @unrecovered_link_errors.setter
    def unrecovered_link_errors(self, unrecovered_link_errors):
        """
        Sets the unrecovered_link_errors of this IbInterfaceStatistics.
        The number of unrecovered link errors.

        :param unrecovered_link_errors: The unrecovered_link_errors of this IbInterfaceStatistics.
        :type: int
        """
        self._unrecovered_link_errors = unrecovered_link_errors

    @property
    def rx_packet_errors(self):
        """
        Gets the rx_packet_errors of this IbInterfaceStatistics.
        The number of packets containing an error that have been received on the port.

        :return: The rx_packet_errors of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_packet_errors

    @rx_packet_errors.setter
    def rx_packet_errors(self, rx_packet_errors):
        """
        Sets the rx_packet_errors of this IbInterfaceStatistics.
        The number of packets containing an error that have been received on the port.

        :param rx_packet_errors: The rx_packet_errors of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_packet_errors = rx_packet_errors

    @property
    def rx_ebp_delimited_packets(self):
        """
        Gets the rx_ebp_delimited_packets of this IbInterfaceStatistics.
        The total number of packets with End Bad Packet delimiter that have been received on the port.

        :return: The rx_ebp_delimited_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_ebp_delimited_packets

    @rx_ebp_delimited_packets.setter
    def rx_ebp_delimited_packets(self, rx_ebp_delimited_packets):
        """
        Sets the rx_ebp_delimited_packets of this IbInterfaceStatistics.
        The total number of packets with End Bad Packet delimiter that have been received on the port.

        :param rx_ebp_delimited_packets: The rx_ebp_delimited_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_ebp_delimited_packets = rx_ebp_delimited_packets

    @property
    def tx_port_down_packet_discards(self):
        """
        Gets the tx_port_down_packet_discards of this IbInterfaceStatistics.
        The number of outbound packets discarded because the port is either down or congested.

        :return: The tx_port_down_packet_discards of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_port_down_packet_discards

    @tx_port_down_packet_discards.setter
    def tx_port_down_packet_discards(self, tx_port_down_packet_discards):
        """
        Sets the tx_port_down_packet_discards of this IbInterfaceStatistics.
        The number of outbound packets discarded because the port is either down or congested.

        :param tx_port_down_packet_discards: The tx_port_down_packet_discards of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_port_down_packet_discards = tx_port_down_packet_discards

    @property
    def tx_constraint_error_packet_discards(self):
        """
        Gets the tx_constraint_error_packet_discards of this IbInterfaceStatistics.
        The number of outbound packets discarded because either (1) the packet is a raw datagram, (2) the packet has a wrong partition key, or (3) the packet has a bad transport header version.

        :return: The tx_constraint_error_packet_discards of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_constraint_error_packet_discards

    @tx_constraint_error_packet_discards.setter
    def tx_constraint_error_packet_discards(self, tx_constraint_error_packet_discards):
        """
        Sets the tx_constraint_error_packet_discards of this IbInterfaceStatistics.
        The number of outbound packets discarded because either (1) the packet is a raw datagram, (2) the packet has a wrong partition key, or (3) the packet has a bad transport header version.

        :param tx_constraint_error_packet_discards: The tx_constraint_error_packet_discards of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_constraint_error_packet_discards = tx_constraint_error_packet_discards

    @property
    def rx_constraint_error_packet_discards(self):
        """
        Gets the rx_constraint_error_packet_discards of this IbInterfaceStatistics.
        The number of inbound packets discarded because either (1) the packet is a raw datagram, (2) the packet has a wrong partition key, or (3) the packet has a bad transport header version.

        :return: The rx_constraint_error_packet_discards of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_constraint_error_packet_discards

    @rx_constraint_error_packet_discards.setter
    def rx_constraint_error_packet_discards(self, rx_constraint_error_packet_discards):
        """
        Sets the rx_constraint_error_packet_discards of this IbInterfaceStatistics.
        The number of inbound packets discarded because either (1) the packet is a raw datagram, (2) the packet has a wrong partition key, or (3) the packet has a bad transport header version.

        :param rx_constraint_error_packet_discards: The rx_constraint_error_packet_discards of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_constraint_error_packet_discards = rx_constraint_error_packet_discards

    @property
    def rx_subnet_management_dropped_packets(self):
        """
        Gets the rx_subnet_management_dropped_packets of this IbInterfaceStatistics.
        The number of virtual lane 15 packets dropped due to resource limitations (e.g., lack of buffers) in the port.

        :return: The rx_subnet_management_dropped_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_subnet_management_dropped_packets

    @rx_subnet_management_dropped_packets.setter
    def rx_subnet_management_dropped_packets(self, rx_subnet_management_dropped_packets):
        """
        Sets the rx_subnet_management_dropped_packets of this IbInterfaceStatistics.
        The number of virtual lane 15 packets dropped due to resource limitations (e.g., lack of buffers) in the port.

        :param rx_subnet_management_dropped_packets: The rx_subnet_management_dropped_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_subnet_management_dropped_packets = rx_subnet_management_dropped_packets

    @property
    def tx_total_bytes(self):
        """
        Gets the tx_total_bytes of this IbInterfaceStatistics.
        The number of bytes transmitted at the port on all virtual lanes.

        :return: The tx_total_bytes of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_total_bytes

    @tx_total_bytes.setter
    def tx_total_bytes(self, tx_total_bytes):
        """
        Sets the tx_total_bytes of this IbInterfaceStatistics.
        The number of bytes transmitted at the port on all virtual lanes.

        :param tx_total_bytes: The tx_total_bytes of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_total_bytes = tx_total_bytes

    @property
    def rx_total_bytes(self):
        """
        Gets the rx_total_bytes of this IbInterfaceStatistics.
        The number of bytes received at the port on all virtual lanes.

        :return: The rx_total_bytes of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_total_bytes

    @rx_total_bytes.setter
    def rx_total_bytes(self, rx_total_bytes):
        """
        Sets the rx_total_bytes of this IbInterfaceStatistics.
        The number of bytes received at the port on all virtual lanes.

        :param rx_total_bytes: The rx_total_bytes of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_total_bytes = rx_total_bytes

    @property
    def tx_total_packets(self):
        """
        Gets the tx_total_packets of this IbInterfaceStatistics.
        The number of packets transmitted at the port on all virtual lanes.

        :return: The tx_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_total_packets

    @tx_total_packets.setter
    def tx_total_packets(self, tx_total_packets):
        """
        Sets the tx_total_packets of this IbInterfaceStatistics.
        The number of packets transmitted at the port on all virtual lanes.

        :param tx_total_packets: The tx_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_total_packets = tx_total_packets

    @property
    def rx_total_packets(self):
        """
        Gets the rx_total_packets of this IbInterfaceStatistics.
        The number of packets received at the port on all virtual lanes.

        :return: The rx_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_total_packets

    @rx_total_packets.setter
    def rx_total_packets(self, rx_total_packets):
        """
        Sets the rx_total_packets of this IbInterfaceStatistics.
        The number of packets received at the port on all virtual lanes.

        :param rx_total_packets: The rx_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_total_packets = rx_total_packets

    @property
    def tx_wait_time(self):
        """
        Gets the tx_wait_time of this IbInterfaceStatistics.
        The number of microseconds during which the port had data to transmit, but none was sent because of insufficient credits or due to arbitration.

        :return: The tx_wait_time of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_wait_time

    @tx_wait_time.setter
    def tx_wait_time(self, tx_wait_time):
        """
        Sets the tx_wait_time of this IbInterfaceStatistics.
        The number of microseconds during which the port had data to transmit, but none was sent because of insufficient credits or due to arbitration.

        :param tx_wait_time: The tx_wait_time of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_wait_time = tx_wait_time

    @property
    def tx_unicast_total_packets(self):
        """
        Gets the tx_unicast_total_packets of this IbInterfaceStatistics.
        Total number of unicast packets transmitted on all VLs from the port. This may include unicast packets with errors and excludes link packets.

        :return: The tx_unicast_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_unicast_total_packets

    @tx_unicast_total_packets.setter
    def tx_unicast_total_packets(self, tx_unicast_total_packets):
        """
        Sets the tx_unicast_total_packets of this IbInterfaceStatistics.
        Total number of unicast packets transmitted on all VLs from the port. This may include unicast packets with errors and excludes link packets.

        :param tx_unicast_total_packets: The tx_unicast_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_unicast_total_packets = tx_unicast_total_packets

    @property
    def rx_unicast_total_packets(self):
        """
        Gets the rx_unicast_total_packets of this IbInterfaceStatistics.
        Total number of unicast packets, including unicast packets containing errors, and excluding link packets, received from all VLs on the port.

        :return: The rx_unicast_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_unicast_total_packets

    @rx_unicast_total_packets.setter
    def rx_unicast_total_packets(self, rx_unicast_total_packets):
        """
        Sets the rx_unicast_total_packets of this IbInterfaceStatistics.
        Total number of unicast packets, including unicast packets containing errors, and excluding link packets, received from all VLs on the port.

        :param rx_unicast_total_packets: The rx_unicast_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_unicast_total_packets = rx_unicast_total_packets

    @property
    def tx_multicast_total_packets(self):
        """
        Gets the tx_multicast_total_packets of this IbInterfaceStatistics.
        Total number of multicast packets transmitted on all VLs from the port. This may include multicast packets with errors.

        :return: The tx_multicast_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_multicast_total_packets

    @tx_multicast_total_packets.setter
    def tx_multicast_total_packets(self, tx_multicast_total_packets):
        """
        Sets the tx_multicast_total_packets of this IbInterfaceStatistics.
        Total number of multicast packets transmitted on all VLs from the port. This may include multicast packets with errors.

        :param tx_multicast_total_packets: The tx_multicast_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._tx_multicast_total_packets = tx_multicast_total_packets

    @property
    def rx_multicast_total_packets(self):
        """
        Gets the rx_multicast_total_packets of this IbInterfaceStatistics.
        Total number of multicast packets, including multicast packets containing errors received from all VLs on the port.

        :return: The rx_multicast_total_packets of this IbInterfaceStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_multicast_total_packets

    @rx_multicast_total_packets.setter
    def rx_multicast_total_packets(self, rx_multicast_total_packets):
        """
        Sets the rx_multicast_total_packets of this IbInterfaceStatistics.
        Total number of multicast packets, including multicast packets containing errors received from all VLs on the port.

        :param rx_multicast_total_packets: The rx_multicast_total_packets of this IbInterfaceStatistics.
        :type: int
        """
        self._rx_multicast_total_packets = rx_multicast_total_packets

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

