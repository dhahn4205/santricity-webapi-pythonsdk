# coding: utf-8

"""
SasPort.py

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


class SasPort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SasPort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent': 'SasPortProviderDevice',  # (required parameter)
            'attached_device': 'SasAttachedDevice',  # (required parameter)
            'state': 'str',  # (required parameter)
            'miswire_type': 'str',  # (required parameter)
            'channel_port_ref': 'str',  # (required parameter)
            'sas_phys': 'list[SasPhy]',  # (required parameter)
            'port_type_data': 'SasPortTypeData',  # (required parameter)
            'port_mode': 'str',  # (required parameter)
            'domain_number': 'int',  # (required parameter)
            'attached_channel_port_ref': 'str',  # (required parameter)
            'discovery_status': 'int'
        }

        self.attribute_map = {
            'parent': 'parent',  # (required parameter)
            'attached_device': 'attachedDevice',  # (required parameter)
            'state': 'state',  # (required parameter)
            'miswire_type': 'miswireType',  # (required parameter)
            'channel_port_ref': 'channelPortRef',  # (required parameter)
            'sas_phys': 'sasPhys',  # (required parameter)
            'port_type_data': 'portTypeData',  # (required parameter)
            'port_mode': 'portMode',  # (required parameter)
            'domain_number': 'domainNumber',  # (required parameter)
            'attached_channel_port_ref': 'attachedChannelPortRef',  # (required parameter)
            'discovery_status': 'discoveryStatus'
        }

        self._parent = None
        self._attached_device = None
        self._state = None
        self._miswire_type = None
        self._channel_port_ref = None
        self._sas_phys = None
        self._port_type_data = None
        self._port_mode = None
        self._domain_number = None
        self._attached_channel_port_ref = None
        self._discovery_status = None

    @property
    def parent(self):
        """
        Gets the parent of this SasPort.
        The device on which the port resides.

        :return: The parent of this SasPort.
        :rtype: SasPortProviderDevice
        :required/optional: required
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SasPort.
        The device on which the port resides.

        :param parent: The parent of this SasPort.
        :type: SasPortProviderDevice
        """
        self._parent = parent

    @property
    def attached_device(self):
        """
        Gets the attached_device of this SasPort.
        An indication of what device is attached to this port.

        :return: The attached_device of this SasPort.
        :rtype: SasAttachedDevice
        :required/optional: required
        """
        return self._attached_device

    @attached_device.setter
    def attached_device(self, attached_device):
        """
        Sets the attached_device of this SasPort.
        An indication of what device is attached to this port.

        :param attached_device: The attached_device of this SasPort.
        :type: SasAttachedDevice
        """
        self._attached_device = attached_device

    @property
    def state(self):
        """
        Gets the state of this SasPort.
        The state of the SAS port.

        :return: The state of this SasPort.
        :rtype: str
        :required/optional: required
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this SasPort.
        The state of the SAS port.

        :param state: The state of this SasPort.
        :type: str
        """
        allowed_values = ["unknown", "optimal", "degraded", "failed", "__UNDEFINED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def miswire_type(self):
        """
        Gets the miswire_type of this SasPort.
        The type of miswire involving this port (or \"none\").

        :return: The miswire_type of this SasPort.
        :rtype: str
        :required/optional: required
        """
        return self._miswire_type

    @miswire_type.setter
    def miswire_type(self, miswire_type):
        """
        Sets the miswire_type of this SasPort.
        The type of miswire involving this port (or \"none\").

        :param miswire_type: The miswire_type of this SasPort.
        :type: str
        """
        allowed_values = ["none", "topology", "ctlrHostPort", "ctlrDrivePortToHost", "esm", "ctlrDrivePortToEndDevice", "__UNDEFINED"]
        if miswire_type not in allowed_values:
            raise ValueError(
                "Invalid value for `miswire_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._miswire_type = miswire_type

    @property
    def channel_port_ref(self):
        """
        Gets the channel_port_ref of this SasPort.
        A reference to the channel port object identifying the external connector associated with this port. If the port is not associated with an external connector, then this field is set to a null SYMbol ref.

        :return: The channel_port_ref of this SasPort.
        :rtype: str
        :required/optional: required
        """
        return self._channel_port_ref

    @channel_port_ref.setter
    def channel_port_ref(self, channel_port_ref):
        """
        Sets the channel_port_ref of this SasPort.
        A reference to the channel port object identifying the external connector associated with this port. If the port is not associated with an external connector, then this field is set to a null SYMbol ref.

        :param channel_port_ref: The channel_port_ref of this SasPort.
        :type: str
        """
        self._channel_port_ref = channel_port_ref

    @property
    def sas_phys(self):
        """
        Gets the sas_phys of this SasPort.
        A list of PHYs associated with this port.

        :return: The sas_phys of this SasPort.
        :rtype: list[SasPhy]
        :required/optional: required
        """
        return self._sas_phys

    @sas_phys.setter
    def sas_phys(self, sas_phys):
        """
        Sets the sas_phys of this SasPort.
        A list of PHYs associated with this port.

        :param sas_phys: The sas_phys of this SasPort.
        :type: list[SasPhy]
        """
        self._sas_phys = sas_phys

    @property
    def port_type_data(self):
        """
        Gets the port_type_data of this SasPort.
        Information about a SAS port that is type-dependent.

        :return: The port_type_data of this SasPort.
        :rtype: SasPortTypeData
        :required/optional: required
        """
        return self._port_type_data

    @port_type_data.setter
    def port_type_data(self, port_type_data):
        """
        Sets the port_type_data of this SasPort.
        Information about a SAS port that is type-dependent.

        :param port_type_data: The port_type_data of this SasPort.
        :type: SasPortTypeData
        """
        self._port_type_data = port_type_data

    @property
    def port_mode(self):
        """
        Gets the port_mode of this SasPort.
        The SAS port connection mode.

        :return: The port_mode of this SasPort.
        :rtype: str
        :required/optional: required
        """
        return self._port_mode

    @port_mode.setter
    def port_mode(self, port_mode):
        """
        Sets the port_mode of this SasPort.
        The SAS port connection mode.

        :param port_mode: The port_mode of this SasPort.
        :type: str
        """
        allowed_values = ["unknown", "internal", "externalIn", "externalOut", "endDevice", "open", "__UNDEFINED"]
        if port_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `port_mode`, must be one of {0}"
                .format(allowed_values)
            )
        self._port_mode = port_mode

    @property
    def domain_number(self):
        """
        Gets the domain_number of this SasPort.
        The domain number identifies which SAS domain this element is a part of. Domain numbers are arbitrarily assigned by the firmware and are consistent on a per controller basis -- but not across controllers. So, the contents of domains will be consistent across controllers but the number identifying a particular domain may not be.

        :return: The domain_number of this SasPort.
        :rtype: int
        :required/optional: required
        """
        return self._domain_number

    @domain_number.setter
    def domain_number(self, domain_number):
        """
        Sets the domain_number of this SasPort.
        The domain number identifies which SAS domain this element is a part of. Domain numbers are arbitrarily assigned by the firmware and are consistent on a per controller basis -- but not across controllers. So, the contents of domains will be consistent across controllers but the number identifying a particular domain may not be.

        :param domain_number: The domain_number of this SasPort.
        :type: int
        """
        self._domain_number = domain_number

    @property
    def attached_channel_port_ref(self):
        """
        Gets the attached_channel_port_ref of this SasPort.
        This ref identifies the connector on the attached device for a drive channel who's external port is connected to another device.

        :return: The attached_channel_port_ref of this SasPort.
        :rtype: str
        :required/optional: required
        """
        return self._attached_channel_port_ref

    @attached_channel_port_ref.setter
    def attached_channel_port_ref(self, attached_channel_port_ref):
        """
        Sets the attached_channel_port_ref of this SasPort.
        This ref identifies the connector on the attached device for a drive channel who's external port is connected to another device.

        :param attached_channel_port_ref: The attached_channel_port_ref of this SasPort.
        :type: str
        """
        self._attached_channel_port_ref = attached_channel_port_ref

    @property
    def discovery_status(self):
        """
        Gets the discovery_status of this SasPort.
        This element contains the status of the SAS discovery - the status is a bit field and could indicate a successful discovery or could indicate one or more failure conditions (indicated by one or more error flags being set).

        :return: The discovery_status of this SasPort.
        :rtype: int
        :required/optional: required
        """
        return self._discovery_status

    @discovery_status.setter
    def discovery_status(self, discovery_status):
        """
        Sets the discovery_status of this SasPort.
        This element contains the status of the SAS discovery - the status is a bit field and could indicate a successful discovery or could indicate one or more failure conditions (indicated by one or more error flags being set).

        :param discovery_status: The discovery_status of this SasPort.
        :type: int
        """
        self._discovery_status = discovery_status

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

