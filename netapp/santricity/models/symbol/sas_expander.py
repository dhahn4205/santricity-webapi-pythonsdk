# coding: utf-8

"""
SasExpander.py

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


class SasExpander(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SasExpander - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expander_ref': 'str',  # (required parameter)
            'parent': 'SasExpanderParent',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'device_name': 'str',  # (required parameter)
            'vendor_id': 'str',  # (required parameter)
            'product_id': 'str',  # (required parameter)
            'fw_version': 'str',  # (required parameter)
            'expander_ports': 'list[SasPort]',  # (required parameter)
            'domain_number': 'int',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'expander_ref': 'expanderRef',  # (required parameter)
            'parent': 'parent',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'device_name': 'deviceName',  # (required parameter)
            'vendor_id': 'vendorId',  # (required parameter)
            'product_id': 'productId',  # (required parameter)
            'fw_version': 'fwVersion',  # (required parameter)
            'expander_ports': 'expanderPorts',  # (required parameter)
            'domain_number': 'domainNumber',  # (required parameter)
            'id': 'id'
        }

        self._expander_ref = None
        self._parent = None
        self._channel = None
        self._device_name = None
        self._vendor_id = None
        self._product_id = None
        self._fw_version = None
        self._expander_ports = None
        self._domain_number = None
        self._id = None

    @property
    def expander_ref(self):
        """
        Gets the expander_ref of this SasExpander.
        The reference value that uniquely identifies the SAS expander.

        :return: The expander_ref of this SasExpander.
        :rtype: str
        :required/optional: required
        """
        return self._expander_ref

    @expander_ref.setter
    def expander_ref(self, expander_ref):
        """
        Sets the expander_ref of this SasExpander.
        The reference value that uniquely identifies the SAS expander.

        :param expander_ref: The expander_ref of this SasExpander.
        :type: str
        """
        self._expander_ref = expander_ref

    @property
    def parent(self):
        """
        Gets the parent of this SasExpander.
        The reference value that uniquely identifies the parent (controller or ESM) of the SAS expander.

        :return: The parent of this SasExpander.
        :rtype: SasExpanderParent
        :required/optional: required
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SasExpander.
        The reference value that uniquely identifies the parent (controller or ESM) of the SAS expander.

        :param parent: The parent of this SasExpander.
        :type: SasExpanderParent
        """
        self._parent = parent

    @property
    def channel(self):
        """
        Gets the channel of this SasExpander.
        The drive channel location of the expander

        :return: The channel of this SasExpander.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this SasExpander.
        The drive channel location of the expander

        :param channel: The channel of this SasExpander.
        :type: int
        """
        self._channel = channel

    @property
    def device_name(self):
        """
        Gets the device_name of this SasExpander.
        The SAS address that is the expander device name

        :return: The device_name of this SasExpander.
        :rtype: str
        :required/optional: required
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """
        Sets the device_name of this SasExpander.
        The SAS address that is the expander device name

        :param device_name: The device_name of this SasExpander.
        :type: str
        """
        self._device_name = device_name

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this SasExpander.
        The Inquiry vendor identification string for the SAS expander.

        :return: The vendor_id of this SasExpander.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this SasExpander.
        The Inquiry vendor identification string for the SAS expander.

        :param vendor_id: The vendor_id of this SasExpander.
        :type: str
        """
        self._vendor_id = vendor_id

    @property
    def product_id(self):
        """
        Gets the product_id of this SasExpander.
        The Inquiry product identification string for the SAS expander.

        :return: The product_id of this SasExpander.
        :rtype: str
        :required/optional: required
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this SasExpander.
        The Inquiry product identification string for the SAS expander.

        :param product_id: The product_id of this SasExpander.
        :type: str
        """
        self._product_id = product_id

    @property
    def fw_version(self):
        """
        Gets the fw_version of this SasExpander.
        The version of the firmware on the SAS expander.

        :return: The fw_version of this SasExpander.
        :rtype: str
        :required/optional: required
        """
        return self._fw_version

    @fw_version.setter
    def fw_version(self, fw_version):
        """
        Sets the fw_version of this SasExpander.
        The version of the firmware on the SAS expander.

        :param fw_version: The fw_version of this SasExpander.
        :type: str
        """
        self._fw_version = fw_version

    @property
    def expander_ports(self):
        """
        Gets the expander_ports of this SasExpander.
        List of ports that are part of this expander.

        :return: The expander_ports of this SasExpander.
        :rtype: list[SasPort]
        :required/optional: required
        """
        return self._expander_ports

    @expander_ports.setter
    def expander_ports(self, expander_ports):
        """
        Sets the expander_ports of this SasExpander.
        List of ports that are part of this expander.

        :param expander_ports: The expander_ports of this SasExpander.
        :type: list[SasPort]
        """
        self._expander_ports = expander_ports

    @property
    def domain_number(self):
        """
        Gets the domain_number of this SasExpander.
        The domain number identifies which SAS domain this element is a part of. Domain numbers are arbitrarily assigned by the firmware and are consistent on a per controller basis -- but not across controllers. So, the contents of domains will be consistent across controllers but the number identifying a particular domain may not be.

        :return: The domain_number of this SasExpander.
        :rtype: int
        :required/optional: required
        """
        return self._domain_number

    @domain_number.setter
    def domain_number(self, domain_number):
        """
        Sets the domain_number of this SasExpander.
        The domain number identifies which SAS domain this element is a part of. Domain numbers are arbitrarily assigned by the firmware and are consistent on a per controller basis -- but not across controllers. So, the contents of domains will be consistent across controllers but the number identifying a particular domain may not be.

        :param domain_number: The domain_number of this SasExpander.
        :type: int
        """
        self._domain_number = domain_number

    @property
    def id(self):
        """
        Gets the id of this SasExpander.


        :return: The id of this SasExpander.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SasExpander.


        :param id: The id of this SasExpander.
        :type: str
        """
        self._id = id

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

