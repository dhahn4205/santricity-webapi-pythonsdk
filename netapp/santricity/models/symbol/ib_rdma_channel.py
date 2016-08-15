# coding: utf-8

"""
IbRdmaChannel.py

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


class IbRdmaChannel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IbRdmaChannel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'endpoints': 'IbRdmaChannelEndpoints',  # (required parameter)
            'maximum_rdma_message_size': 'int',  # (required parameter)
            'path_maximum_transmission_unit': 'int',  # (required parameter)
            'maximum_queue_depth': 'int',  # (required parameter)
            'channel_state': 'str'
        }

        self.attribute_map = {
            'endpoints': 'endpoints',  # (required parameter)
            'maximum_rdma_message_size': 'maximumRdmaMessageSize',  # (required parameter)
            'path_maximum_transmission_unit': 'pathMaximumTransmissionUnit',  # (required parameter)
            'maximum_queue_depth': 'maximumQueueDepth',  # (required parameter)
            'channel_state': 'channelState'
        }

        self._endpoints = None
        self._maximum_rdma_message_size = None
        self._path_maximum_transmission_unit = None
        self._maximum_queue_depth = None
        self._channel_state = None

    @property
    def endpoints(self):
        """
        Gets the endpoints of this IbRdmaChannel.
        This field identifies the RDMA channel by identifying its initiator and target endpoints.

        :return: The endpoints of this IbRdmaChannel.
        :rtype: IbRdmaChannelEndpoints
        :required/optional: required
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this IbRdmaChannel.
        This field identifies the RDMA channel by identifying its initiator and target endpoints.

        :param endpoints: The endpoints of this IbRdmaChannel.
        :type: IbRdmaChannelEndpoints
        """
        self._endpoints = endpoints

    @property
    def maximum_rdma_message_size(self):
        """
        Gets the maximum_rdma_message_size of this IbRdmaChannel.
        The maximum supported RDMA message size or this RDMA channel.

        :return: The maximum_rdma_message_size of this IbRdmaChannel.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_rdma_message_size

    @maximum_rdma_message_size.setter
    def maximum_rdma_message_size(self, maximum_rdma_message_size):
        """
        Sets the maximum_rdma_message_size of this IbRdmaChannel.
        The maximum supported RDMA message size or this RDMA channel.

        :param maximum_rdma_message_size: The maximum_rdma_message_size of this IbRdmaChannel.
        :type: int
        """
        self._maximum_rdma_message_size = maximum_rdma_message_size

    @property
    def path_maximum_transmission_unit(self):
        """
        Gets the path_maximum_transmission_unit of this IbRdmaChannel.
        The maximum supported transmission unit for the path associated with the RDMA channel.

        :return: The path_maximum_transmission_unit of this IbRdmaChannel.
        :rtype: int
        :required/optional: required
        """
        return self._path_maximum_transmission_unit

    @path_maximum_transmission_unit.setter
    def path_maximum_transmission_unit(self, path_maximum_transmission_unit):
        """
        Sets the path_maximum_transmission_unit of this IbRdmaChannel.
        The maximum supported transmission unit for the path associated with the RDMA channel.

        :param path_maximum_transmission_unit: The path_maximum_transmission_unit of this IbRdmaChannel.
        :type: int
        """
        self._path_maximum_transmission_unit = path_maximum_transmission_unit

    @property
    def maximum_queue_depth(self):
        """
        Gets the maximum_queue_depth of this IbRdmaChannel.
        The maximum supported queue depth for this RDMA channel.

        :return: The maximum_queue_depth of this IbRdmaChannel.
        :rtype: int
        :required/optional: required
        """
        return self._maximum_queue_depth

    @maximum_queue_depth.setter
    def maximum_queue_depth(self, maximum_queue_depth):
        """
        Sets the maximum_queue_depth of this IbRdmaChannel.
        The maximum supported queue depth for this RDMA channel.

        :param maximum_queue_depth: The maximum_queue_depth of this IbRdmaChannel.
        :type: int
        """
        self._maximum_queue_depth = maximum_queue_depth

    @property
    def channel_state(self):
        """
        Gets the channel_state of this IbRdmaChannel.
        The current state of this RDMA channel.

        :return: The channel_state of this IbRdmaChannel.
        :rtype: str
        :required/optional: required
        """
        return self._channel_state

    @channel_state.setter
    def channel_state(self, channel_state):
        """
        Sets the channel_state of this IbRdmaChannel.
        The current state of this RDMA channel.

        :param channel_state: The channel_state of this IbRdmaChannel.
        :type: str
        """
        allowed_values = ["uninitialized", "connecting", "connected", "disconnecting", "disconnected", "__UNDEFINED"]
        if channel_state not in allowed_values:
            raise ValueError(
                "Invalid value for `channel_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._channel_state = channel_state

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

