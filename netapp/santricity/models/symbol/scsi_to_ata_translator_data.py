# coding: utf-8

"""
ScsiToAtaTranslatorData.py

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


class ScsiToAtaTranslatorData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScsiToAtaTranslatorData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'vendor_id': 'str',  # (required parameter)
            'product_id': 'str',  # (required parameter)
            'product_rev_level': 'str',  # (required parameter)
            'sat_type': 'str'
        }

        self.attribute_map = {
            'vendor_id': 'vendorId',  # (required parameter)
            'product_id': 'productId',  # (required parameter)
            'product_rev_level': 'productRevLevel',  # (required parameter)
            'sat_type': 'satType'
        }

        self._vendor_id = None
        self._product_id = None
        self._product_rev_level = None
        self._sat_type = None

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this ScsiToAtaTranslatorData.
        The vendor identification string.

        :return: The vendor_id of this ScsiToAtaTranslatorData.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this ScsiToAtaTranslatorData.
        The vendor identification string.

        :param vendor_id: The vendor_id of this ScsiToAtaTranslatorData.
        :type: str
        """
        self._vendor_id = vendor_id

    @property
    def product_id(self):
        """
        Gets the product_id of this ScsiToAtaTranslatorData.
        The product identification string.

        :return: The product_id of this ScsiToAtaTranslatorData.
        :rtype: str
        :required/optional: required
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ScsiToAtaTranslatorData.
        The product identification string.

        :param product_id: The product_id of this ScsiToAtaTranslatorData.
        :type: str
        """
        self._product_id = product_id

    @property
    def product_rev_level(self):
        """
        Gets the product_rev_level of this ScsiToAtaTranslatorData.
        The product revision level string. When no interposer card is available, this string is set to \"----\" (four dashes).

        :return: The product_rev_level of this ScsiToAtaTranslatorData.
        :rtype: str
        :required/optional: required
        """
        return self._product_rev_level

    @product_rev_level.setter
    def product_rev_level(self, product_rev_level):
        """
        Sets the product_rev_level of this ScsiToAtaTranslatorData.
        The product revision level string. When no interposer card is available, this string is set to \"----\" (four dashes).

        :param product_rev_level: The product_rev_level of this ScsiToAtaTranslatorData.
        :type: str
        """
        self._product_rev_level = product_rev_level

    @property
    def sat_type(self):
        """
        Gets the sat_type of this ScsiToAtaTranslatorData.
        This field identifies the type of the SCSI-to-ATA translation hardware. Note that if this field is set to SAT_TYPE_UNKNOWN, the string in the productId field will have zero length, and the string in the productRevLevel field will be set to \"----\" (four dashes).

        :return: The sat_type of this ScsiToAtaTranslatorData.
        :rtype: str
        :required/optional: required
        """
        return self._sat_type

    @sat_type.setter
    def sat_type(self, sat_type):
        """
        Sets the sat_type of this ScsiToAtaTranslatorData.
        This field identifies the type of the SCSI-to-ATA translation hardware. Note that if this field is set to SAT_TYPE_UNKNOWN, the string in the productId field will have zero length, and the string in the productRevLevel field will be set to \"----\" (four dashes).

        :param sat_type: The sat_type of this ScsiToAtaTranslatorData.
        :type: str
        """
        allowed_values = ["unknown", "driveCruResident", "controllerResident", "enclosureSlotResident", "__UNDEFINED"]
        if sat_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sat_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._sat_type = sat_type

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
