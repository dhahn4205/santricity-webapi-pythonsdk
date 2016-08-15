# coding: utf-8

"""
EthernetPortStatistics.py

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


class EthernetPortStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EthernetPortStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interfaces': 'list[str]',  # (required parameter)
            'bytes_transmitted': 'int',  # (required parameter)
            'bytes_received': 'int',  # (required parameter)
            'packets_transmitted': 'int',  # (required parameter)
            'packets_received': 'int',  # (required parameter)
            'carrier_sense_errors': 'int',  # (required parameter)
            'single_collision_frames': 'int',  # (required parameter)
            'multiple_collision_frames': 'int',  # (required parameter)
            'late_collisions': 'int',  # (required parameter)
            'deferred_transmissions': 'int',  # (required parameter)
            'frame_too_longs': 'int',  # (required parameter)
            'tx_multicast_frame_count': 'int',  # (required parameter)
            'tx_broadcast_frame_count': 'int',  # (required parameter)
            'tx_pause_frame_count': 'int',  # (required parameter)
            'tx_control_frame_count': 'int',  # (required parameter)
            'tx_frame_excess_deferral_count': 'int',  # (required parameter)
            'tx_frame_abort_count': 'int',  # (required parameter)
            'tx_frame_collision_count': 'int',  # (required parameter)
            'tx_frame_dropped_count': 'int',  # (required parameter)
            'tx_jumbo_frame_count': 'int',  # (required parameter)
            'rx_unknown_control_frame_count': 'int',  # (required parameter)
            'rx_pause_frame_count': 'int',  # (required parameter)
            'rx_control_frame_count': 'int',  # (required parameter)
            'rx_frame_length_error_count': 'int',  # (required parameter)
            'rx_jabber_count': 'int',  # (required parameter)
            'rx_frame_droped_count': 'int',  # (required parameter)
            'rx_frame_crc_error_count': 'int',  # (required parameter)
            'rx_frame_encoding_error_count': 'int',  # (required parameter)
            'rx_small_frame_error_count': 'int',  # (required parameter)
            'rx_multicast_frame_count': 'int',  # (required parameter)
            'rx_broadcast_frame_count': 'int'
        }

        self.attribute_map = {
            'interfaces': 'interfaces',  # (required parameter)
            'bytes_transmitted': 'bytesTransmitted',  # (required parameter)
            'bytes_received': 'bytesReceived',  # (required parameter)
            'packets_transmitted': 'packetsTransmitted',  # (required parameter)
            'packets_received': 'packetsReceived',  # (required parameter)
            'carrier_sense_errors': 'carrierSenseErrors',  # (required parameter)
            'single_collision_frames': 'singleCollisionFrames',  # (required parameter)
            'multiple_collision_frames': 'multipleCollisionFrames',  # (required parameter)
            'late_collisions': 'lateCollisions',  # (required parameter)
            'deferred_transmissions': 'deferredTransmissions',  # (required parameter)
            'frame_too_longs': 'frameTooLongs',  # (required parameter)
            'tx_multicast_frame_count': 'txMulticastFrameCount',  # (required parameter)
            'tx_broadcast_frame_count': 'txBroadcastFrameCount',  # (required parameter)
            'tx_pause_frame_count': 'txPauseFrameCount',  # (required parameter)
            'tx_control_frame_count': 'txControlFrameCount',  # (required parameter)
            'tx_frame_excess_deferral_count': 'txFrameExcessDeferralCount',  # (required parameter)
            'tx_frame_abort_count': 'txFrameAbortCount',  # (required parameter)
            'tx_frame_collision_count': 'txFrameCollisionCount',  # (required parameter)
            'tx_frame_dropped_count': 'txFrameDroppedCount',  # (required parameter)
            'tx_jumbo_frame_count': 'txJumboFrameCount',  # (required parameter)
            'rx_unknown_control_frame_count': 'rxUnknownControlFrameCount',  # (required parameter)
            'rx_pause_frame_count': 'rxPauseFrameCount',  # (required parameter)
            'rx_control_frame_count': 'rxControlFrameCount',  # (required parameter)
            'rx_frame_length_error_count': 'rxFrameLengthErrorCount',  # (required parameter)
            'rx_jabber_count': 'rxJabberCount',  # (required parameter)
            'rx_frame_droped_count': 'rxFrameDropedCount',  # (required parameter)
            'rx_frame_crc_error_count': 'rxFrameCrcErrorCount',  # (required parameter)
            'rx_frame_encoding_error_count': 'rxFrameEncodingErrorCount',  # (required parameter)
            'rx_small_frame_error_count': 'rxSmallFrameErrorCount',  # (required parameter)
            'rx_multicast_frame_count': 'rxMulticastFrameCount',  # (required parameter)
            'rx_broadcast_frame_count': 'rxBroadcastFrameCount'
        }

        self._interfaces = None
        self._bytes_transmitted = None
        self._bytes_received = None
        self._packets_transmitted = None
        self._packets_received = None
        self._carrier_sense_errors = None
        self._single_collision_frames = None
        self._multiple_collision_frames = None
        self._late_collisions = None
        self._deferred_transmissions = None
        self._frame_too_longs = None
        self._tx_multicast_frame_count = None
        self._tx_broadcast_frame_count = None
        self._tx_pause_frame_count = None
        self._tx_control_frame_count = None
        self._tx_frame_excess_deferral_count = None
        self._tx_frame_abort_count = None
        self._tx_frame_collision_count = None
        self._tx_frame_dropped_count = None
        self._tx_jumbo_frame_count = None
        self._rx_unknown_control_frame_count = None
        self._rx_pause_frame_count = None
        self._rx_control_frame_count = None
        self._rx_frame_length_error_count = None
        self._rx_jabber_count = None
        self._rx_frame_droped_count = None
        self._rx_frame_crc_error_count = None
        self._rx_frame_encoding_error_count = None
        self._rx_small_frame_error_count = None
        self._rx_multicast_frame_count = None
        self._rx_broadcast_frame_count = None

    @property
    def interfaces(self):
        """
        Gets the interfaces of this EthernetPortStatistics.
        The interface(s) for which the statistics apply. In some cases, the statistics may be aggregated across multiple interfaces. Even though this is shown as an array, it will only be a single instance.

        :return: The interfaces of this EthernetPortStatistics.
        :rtype: list[str]
        :required/optional: required
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this EthernetPortStatistics.
        The interface(s) for which the statistics apply. In some cases, the statistics may be aggregated across multiple interfaces. Even though this is shown as an array, it will only be a single instance.

        :param interfaces: The interfaces of this EthernetPortStatistics.
        :type: list[str]
        """
        self._interfaces = interfaces

    @property
    def bytes_transmitted(self):
        """
        Gets the bytes_transmitted of this EthernetPortStatistics.
        The total number of bytes transmitted.

        :return: The bytes_transmitted of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._bytes_transmitted

    @bytes_transmitted.setter
    def bytes_transmitted(self, bytes_transmitted):
        """
        Sets the bytes_transmitted of this EthernetPortStatistics.
        The total number of bytes transmitted.

        :param bytes_transmitted: The bytes_transmitted of this EthernetPortStatistics.
        :type: int
        """
        self._bytes_transmitted = bytes_transmitted

    @property
    def bytes_received(self):
        """
        Gets the bytes_received of this EthernetPortStatistics.
        The total number of bytes received.

        :return: The bytes_received of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._bytes_received

    @bytes_received.setter
    def bytes_received(self, bytes_received):
        """
        Sets the bytes_received of this EthernetPortStatistics.
        The total number of bytes received.

        :param bytes_received: The bytes_received of this EthernetPortStatistics.
        :type: int
        """
        self._bytes_received = bytes_received

    @property
    def packets_transmitted(self):
        """
        Gets the packets_transmitted of this EthernetPortStatistics.
        Total number of packets transmitted.

        :return: The packets_transmitted of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._packets_transmitted

    @packets_transmitted.setter
    def packets_transmitted(self, packets_transmitted):
        """
        Sets the packets_transmitted of this EthernetPortStatistics.
        Total number of packets transmitted.

        :param packets_transmitted: The packets_transmitted of this EthernetPortStatistics.
        :type: int
        """
        self._packets_transmitted = packets_transmitted

    @property
    def packets_received(self):
        """
        Gets the packets_received of this EthernetPortStatistics.
        Total number of packets received.

        :return: The packets_received of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._packets_received

    @packets_received.setter
    def packets_received(self, packets_received):
        """
        Sets the packets_received of this EthernetPortStatistics.
        Total number of packets received.

        :param packets_received: The packets_received of this EthernetPortStatistics.
        :type: int
        """
        self._packets_received = packets_received

    @property
    def carrier_sense_errors(self):
        """
        Gets the carrier_sense_errors of this EthernetPortStatistics.
        The number of times the carrier sense condition was lost or never asserted when attempting to transmit a frame.

        :return: The carrier_sense_errors of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._carrier_sense_errors

    @carrier_sense_errors.setter
    def carrier_sense_errors(self, carrier_sense_errors):
        """
        Sets the carrier_sense_errors of this EthernetPortStatistics.
        The number of times the carrier sense condition was lost or never asserted when attempting to transmit a frame.

        :param carrier_sense_errors: The carrier_sense_errors of this EthernetPortStatistics.
        :type: int
        """
        self._carrier_sense_errors = carrier_sense_errors

    @property
    def single_collision_frames(self):
        """
        Gets the single_collision_frames of this EthernetPortStatistics.
        The number of successfully-transmitted frames for which transmission is inhibited by a single collision.

        :return: The single_collision_frames of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._single_collision_frames

    @single_collision_frames.setter
    def single_collision_frames(self, single_collision_frames):
        """
        Sets the single_collision_frames of this EthernetPortStatistics.
        The number of successfully-transmitted frames for which transmission is inhibited by a single collision.

        :param single_collision_frames: The single_collision_frames of this EthernetPortStatistics.
        :type: int
        """
        self._single_collision_frames = single_collision_frames

    @property
    def multiple_collision_frames(self):
        """
        Gets the multiple_collision_frames of this EthernetPortStatistics.
        The number of successfully-transmitted frames for which transmission is inhibited by multiple collisions.

        :return: The multiple_collision_frames of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._multiple_collision_frames

    @multiple_collision_frames.setter
    def multiple_collision_frames(self, multiple_collision_frames):
        """
        Sets the multiple_collision_frames of this EthernetPortStatistics.
        The number of successfully-transmitted frames for which transmission is inhibited by multiple collisions.

        :param multiple_collision_frames: The multiple_collision_frames of this EthernetPortStatistics.
        :type: int
        """
        self._multiple_collision_frames = multiple_collision_frames

    @property
    def late_collisions(self):
        """
        Gets the late_collisions of this EthernetPortStatistics.
        The number of times a collision is detected later than 512 bit-times into the transmission of a packet.

        :return: The late_collisions of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._late_collisions

    @late_collisions.setter
    def late_collisions(self, late_collisions):
        """
        Sets the late_collisions of this EthernetPortStatistics.
        The number of times a collision is detected later than 512 bit-times into the transmission of a packet.

        :param late_collisions: The late_collisions of this EthernetPortStatistics.
        :type: int
        """
        self._late_collisions = late_collisions

    @property
    def deferred_transmissions(self):
        """
        Gets the deferred_transmissions of this EthernetPortStatistics.
        The number of frames for which the first transmission attempt is delayed because the medium is busy.

        :return: The deferred_transmissions of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._deferred_transmissions

    @deferred_transmissions.setter
    def deferred_transmissions(self, deferred_transmissions):
        """
        Sets the deferred_transmissions of this EthernetPortStatistics.
        The number of frames for which the first transmission attempt is delayed because the medium is busy.

        :param deferred_transmissions: The deferred_transmissions of this EthernetPortStatistics.
        :type: int
        """
        self._deferred_transmissions = deferred_transmissions

    @property
    def frame_too_longs(self):
        """
        Gets the frame_too_longs of this EthernetPortStatistics.
        The number of received frames that exceed the maximum permitted frame size.

        :return: The frame_too_longs of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._frame_too_longs

    @frame_too_longs.setter
    def frame_too_longs(self, frame_too_longs):
        """
        Sets the frame_too_longs of this EthernetPortStatistics.
        The number of received frames that exceed the maximum permitted frame size.

        :param frame_too_longs: The frame_too_longs of this EthernetPortStatistics.
        :type: int
        """
        self._frame_too_longs = frame_too_longs

    @property
    def tx_multicast_frame_count(self):
        """
        Gets the tx_multicast_frame_count of this EthernetPortStatistics.
        The number of multicast frames transmitted over the interface.

        :return: The tx_multicast_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_multicast_frame_count

    @tx_multicast_frame_count.setter
    def tx_multicast_frame_count(self, tx_multicast_frame_count):
        """
        Sets the tx_multicast_frame_count of this EthernetPortStatistics.
        The number of multicast frames transmitted over the interface.

        :param tx_multicast_frame_count: The tx_multicast_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_multicast_frame_count = tx_multicast_frame_count

    @property
    def tx_broadcast_frame_count(self):
        """
        Gets the tx_broadcast_frame_count of this EthernetPortStatistics.
        The number of broadcast frames transmitted over the interface.

        :return: The tx_broadcast_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_broadcast_frame_count

    @tx_broadcast_frame_count.setter
    def tx_broadcast_frame_count(self, tx_broadcast_frame_count):
        """
        Sets the tx_broadcast_frame_count of this EthernetPortStatistics.
        The number of broadcast frames transmitted over the interface.

        :param tx_broadcast_frame_count: The tx_broadcast_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_broadcast_frame_count = tx_broadcast_frame_count

    @property
    def tx_pause_frame_count(self):
        """
        Gets the tx_pause_frame_count of this EthernetPortStatistics.
        The number of pause frames transmitted over the interface.

        :return: The tx_pause_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_pause_frame_count

    @tx_pause_frame_count.setter
    def tx_pause_frame_count(self, tx_pause_frame_count):
        """
        Sets the tx_pause_frame_count of this EthernetPortStatistics.
        The number of pause frames transmitted over the interface.

        :param tx_pause_frame_count: The tx_pause_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_pause_frame_count = tx_pause_frame_count

    @property
    def tx_control_frame_count(self):
        """
        Gets the tx_control_frame_count of this EthernetPortStatistics.
        The number of control frames transmitted over the interface.

        :return: The tx_control_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_control_frame_count

    @tx_control_frame_count.setter
    def tx_control_frame_count(self, tx_control_frame_count):
        """
        Sets the tx_control_frame_count of this EthernetPortStatistics.
        The number of control frames transmitted over the interface.

        :param tx_control_frame_count: The tx_control_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_control_frame_count = tx_control_frame_count

    @property
    def tx_frame_excess_deferral_count(self):
        """
        Gets the tx_frame_excess_deferral_count of this EthernetPortStatistics.
        The number of frames which experienced deferred transmission for an excessive period of time.

        :return: The tx_frame_excess_deferral_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_frame_excess_deferral_count

    @tx_frame_excess_deferral_count.setter
    def tx_frame_excess_deferral_count(self, tx_frame_excess_deferral_count):
        """
        Sets the tx_frame_excess_deferral_count of this EthernetPortStatistics.
        The number of frames which experienced deferred transmission for an excessive period of time.

        :param tx_frame_excess_deferral_count: The tx_frame_excess_deferral_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_frame_excess_deferral_count = tx_frame_excess_deferral_count

    @property
    def tx_frame_abort_count(self):
        """
        Gets the tx_frame_abort_count of this EthernetPortStatistics.
        The number of aborts that occurred while transmitting.

        :return: The tx_frame_abort_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_frame_abort_count

    @tx_frame_abort_count.setter
    def tx_frame_abort_count(self, tx_frame_abort_count):
        """
        Sets the tx_frame_abort_count of this EthernetPortStatistics.
        The number of aborts that occurred while transmitting.

        :param tx_frame_abort_count: The tx_frame_abort_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_frame_abort_count = tx_frame_abort_count

    @property
    def tx_frame_collision_count(self):
        """
        Gets the tx_frame_collision_count of this EthernetPortStatistics.
        The number of frames that could not be sent due to a single or multiple collisions.

        :return: The tx_frame_collision_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_frame_collision_count

    @tx_frame_collision_count.setter
    def tx_frame_collision_count(self, tx_frame_collision_count):
        """
        Sets the tx_frame_collision_count of this EthernetPortStatistics.
        The number of frames that could not be sent due to a single or multiple collisions.

        :param tx_frame_collision_count: The tx_frame_collision_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_frame_collision_count = tx_frame_collision_count

    @property
    def tx_frame_dropped_count(self):
        """
        Gets the tx_frame_dropped_count of this EthernetPortStatistics.
        The number of frames that were dropped because the transmit FIFO was full.

        :return: The tx_frame_dropped_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_frame_dropped_count

    @tx_frame_dropped_count.setter
    def tx_frame_dropped_count(self, tx_frame_dropped_count):
        """
        Sets the tx_frame_dropped_count of this EthernetPortStatistics.
        The number of frames that were dropped because the transmit FIFO was full.

        :param tx_frame_dropped_count: The tx_frame_dropped_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_frame_dropped_count = tx_frame_dropped_count

    @property
    def tx_jumbo_frame_count(self):
        """
        Gets the tx_jumbo_frame_count of this EthernetPortStatistics.
        The number of jumbo frames transmitted over the interface.

        :return: The tx_jumbo_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._tx_jumbo_frame_count

    @tx_jumbo_frame_count.setter
    def tx_jumbo_frame_count(self, tx_jumbo_frame_count):
        """
        Sets the tx_jumbo_frame_count of this EthernetPortStatistics.
        The number of jumbo frames transmitted over the interface.

        :param tx_jumbo_frame_count: The tx_jumbo_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._tx_jumbo_frame_count = tx_jumbo_frame_count

    @property
    def rx_unknown_control_frame_count(self):
        """
        Gets the rx_unknown_control_frame_count of this EthernetPortStatistics.
        The number of control frames received with unknown op codes.

        :return: The rx_unknown_control_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_unknown_control_frame_count

    @rx_unknown_control_frame_count.setter
    def rx_unknown_control_frame_count(self, rx_unknown_control_frame_count):
        """
        Sets the rx_unknown_control_frame_count of this EthernetPortStatistics.
        The number of control frames received with unknown op codes.

        :param rx_unknown_control_frame_count: The rx_unknown_control_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_unknown_control_frame_count = rx_unknown_control_frame_count

    @property
    def rx_pause_frame_count(self):
        """
        Gets the rx_pause_frame_count of this EthernetPortStatistics.
        The number of pause frames received over the interface.

        :return: The rx_pause_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_pause_frame_count

    @rx_pause_frame_count.setter
    def rx_pause_frame_count(self, rx_pause_frame_count):
        """
        Sets the rx_pause_frame_count of this EthernetPortStatistics.
        The number of pause frames received over the interface.

        :param rx_pause_frame_count: The rx_pause_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_pause_frame_count = rx_pause_frame_count

    @property
    def rx_control_frame_count(self):
        """
        Gets the rx_control_frame_count of this EthernetPortStatistics.
        The number of control frames received over the interface.

        :return: The rx_control_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_control_frame_count

    @rx_control_frame_count.setter
    def rx_control_frame_count(self, rx_control_frame_count):
        """
        Sets the rx_control_frame_count of this EthernetPortStatistics.
        The number of control frames received over the interface.

        :param rx_control_frame_count: The rx_control_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_control_frame_count = rx_control_frame_count

    @property
    def rx_frame_length_error_count(self):
        """
        Gets the rx_frame_length_error_count of this EthernetPortStatistics.
        The number of frames received with 802.3 frame length errors.

        :return: The rx_frame_length_error_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_frame_length_error_count

    @rx_frame_length_error_count.setter
    def rx_frame_length_error_count(self, rx_frame_length_error_count):
        """
        Sets the rx_frame_length_error_count of this EthernetPortStatistics.
        The number of frames received with 802.3 frame length errors.

        :param rx_frame_length_error_count: The rx_frame_length_error_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_frame_length_error_count = rx_frame_length_error_count

    @property
    def rx_jabber_count(self):
        """
        Gets the rx_jabber_count of this EthernetPortStatistics.
        The number of jabber errors detected.

        :return: The rx_jabber_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_jabber_count

    @rx_jabber_count.setter
    def rx_jabber_count(self, rx_jabber_count):
        """
        Sets the rx_jabber_count of this EthernetPortStatistics.
        The number of jabber errors detected.

        :param rx_jabber_count: The rx_jabber_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_jabber_count = rx_jabber_count

    @property
    def rx_frame_droped_count(self):
        """
        Gets the rx_frame_droped_count of this EthernetPortStatistics.
        Received frames that were dropped.

        :return: The rx_frame_droped_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_frame_droped_count

    @rx_frame_droped_count.setter
    def rx_frame_droped_count(self, rx_frame_droped_count):
        """
        Sets the rx_frame_droped_count of this EthernetPortStatistics.
        Received frames that were dropped.

        :param rx_frame_droped_count: The rx_frame_droped_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_frame_droped_count = rx_frame_droped_count

    @property
    def rx_frame_crc_error_count(self):
        """
        Gets the rx_frame_crc_error_count of this EthernetPortStatistics.
        The number of frames received and discarded with a CRC error.

        :return: The rx_frame_crc_error_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_frame_crc_error_count

    @rx_frame_crc_error_count.setter
    def rx_frame_crc_error_count(self, rx_frame_crc_error_count):
        """
        Sets the rx_frame_crc_error_count of this EthernetPortStatistics.
        The number of frames received and discarded with a CRC error.

        :param rx_frame_crc_error_count: The rx_frame_crc_error_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_frame_crc_error_count = rx_frame_crc_error_count

    @property
    def rx_frame_encoding_error_count(self):
        """
        Gets the rx_frame_encoding_error_count of this EthernetPortStatistics.
        The number of frames received with encoding errors.

        :return: The rx_frame_encoding_error_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_frame_encoding_error_count

    @rx_frame_encoding_error_count.setter
    def rx_frame_encoding_error_count(self, rx_frame_encoding_error_count):
        """
        Sets the rx_frame_encoding_error_count of this EthernetPortStatistics.
        The number of frames received with encoding errors.

        :param rx_frame_encoding_error_count: The rx_frame_encoding_error_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_frame_encoding_error_count = rx_frame_encoding_error_count

    @property
    def rx_small_frame_error_count(self):
        """
        Gets the rx_small_frame_error_count of this EthernetPortStatistics.
        The number of frames received that are smaller than the minimum size allowed (64 bytes).

        :return: The rx_small_frame_error_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_small_frame_error_count

    @rx_small_frame_error_count.setter
    def rx_small_frame_error_count(self, rx_small_frame_error_count):
        """
        Sets the rx_small_frame_error_count of this EthernetPortStatistics.
        The number of frames received that are smaller than the minimum size allowed (64 bytes).

        :param rx_small_frame_error_count: The rx_small_frame_error_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_small_frame_error_count = rx_small_frame_error_count

    @property
    def rx_multicast_frame_count(self):
        """
        Gets the rx_multicast_frame_count of this EthernetPortStatistics.
        The number of multicast frames received over the interface.

        :return: The rx_multicast_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_multicast_frame_count

    @rx_multicast_frame_count.setter
    def rx_multicast_frame_count(self, rx_multicast_frame_count):
        """
        Sets the rx_multicast_frame_count of this EthernetPortStatistics.
        The number of multicast frames received over the interface.

        :param rx_multicast_frame_count: The rx_multicast_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_multicast_frame_count = rx_multicast_frame_count

    @property
    def rx_broadcast_frame_count(self):
        """
        Gets the rx_broadcast_frame_count of this EthernetPortStatistics.
        The number of broadcast frames received over the interface.

        :return: The rx_broadcast_frame_count of this EthernetPortStatistics.
        :rtype: int
        :required/optional: required
        """
        return self._rx_broadcast_frame_count

    @rx_broadcast_frame_count.setter
    def rx_broadcast_frame_count(self, rx_broadcast_frame_count):
        """
        Sets the rx_broadcast_frame_count of this EthernetPortStatistics.
        The number of broadcast frames received over the interface.

        :param rx_broadcast_frame_count: The rx_broadcast_frame_count of this EthernetPortStatistics.
        :type: int
        """
        self._rx_broadcast_frame_count = rx_broadcast_frame_count

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

