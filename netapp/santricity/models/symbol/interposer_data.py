# coding: utf-8

"""
InterposerData.py

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


class InterposerData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InterposerData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'vendor_id': 'str',  # (required parameter)
            'product_id': 'str',  # (required parameter)
            'revision': 'str',  # (required parameter)
            'device_wwn': 'str',  # (required parameter)
            'serial_number': 'str',  # (required parameter)
            'part_number': 'str',  # (required parameter)
            'drive_fw_version': 'str'
        }

        self.attribute_map = {
            'vendor_id': 'vendorID',  # (required parameter)
            'product_id': 'productID',  # (required parameter)
            'revision': 'revision',  # (required parameter)
            'device_wwn': 'deviceWWN',  # (required parameter)
            'serial_number': 'serialNumber',  # (required parameter)
            'part_number': 'partNumber',  # (required parameter)
            'drive_fw_version': 'driveFwVersion'
        }

        self._vendor_id = None
        self._product_id = None
        self._revision = None
        self._device_wwn = None
        self._serial_number = None
        self._part_number = None
        self._drive_fw_version = None

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this InterposerData.
        This data is a variable length ASCII text string containing the vendor identification of the interposer.

        :return: The vendor_id of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this InterposerData.
        This data is a variable length ASCII text string containing the vendor identification of the interposer.

        :param vendor_id: The vendor_id of this InterposerData.
        :type: str
        """
        self._vendor_id = vendor_id

    @property
    def product_id(self):
        """
        Gets the product_id of this InterposerData.
        This data is a variable length ASCII text string containing the product identification of the interposer.

        :return: The product_id of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this InterposerData.
        This data is a variable length ASCII text string containing the product identification of the interposer.

        :param product_id: The product_id of this InterposerData.
        :type: str
        """
        self._product_id = product_id

    @property
    def revision(self):
        """
        Gets the revision of this InterposerData.
        This data is a variable length ASCII text string that represents the current version, or revision level, of the interposer.

        :return: The revision of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this InterposerData.
        This data is a variable length ASCII text string that represents the current version, or revision level, of the interposer.

        :param revision: The revision of this InterposerData.
        :type: str
        """
        self._revision = revision

    @property
    def device_wwn(self):
        """
        Gets the device_wwn of this InterposerData.
        This data represents the device name of the interposer.

        :return: The device_wwn of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._device_wwn

    @device_wwn.setter
    def device_wwn(self, device_wwn):
        """
        Sets the device_wwn of this InterposerData.
        This data represents the device name of the interposer.

        :param device_wwn: The device_wwn of this InterposerData.
        :type: str
        """
        self._device_wwn = device_wwn

    @property
    def serial_number(self):
        """
        Gets the serial_number of this InterposerData.
        This data is a variable length ASCII text string that represents the serial number of the interposer.

        :return: The serial_number of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this InterposerData.
        This data is a variable length ASCII text string that represents the serial number of the interposer.

        :param serial_number: The serial_number of this InterposerData.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def part_number(self):
        """
        Gets the part_number of this InterposerData.
        This data is a variable length ASCII text string that represents the part number of the interposer.

        :return: The part_number of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this InterposerData.
        This data is a variable length ASCII text string that represents the part number of the interposer.

        :param part_number: The part_number of this InterposerData.
        :type: str
        """
        self._part_number = part_number

    @property
    def drive_fw_version(self):
        """
        Gets the drive_fw_version of this InterposerData.
        4 bytes left-justified ASCII drive firmware version as retrieved from the drive's standard INQUIRY data, followed by 4 blank bytes.

        :return: The drive_fw_version of this InterposerData.
        :rtype: str
        :required/optional: required
        """
        return self._drive_fw_version

    @drive_fw_version.setter
    def drive_fw_version(self, drive_fw_version):
        """
        Sets the drive_fw_version of this InterposerData.
        4 bytes left-justified ASCII drive firmware version as retrieved from the drive's standard INQUIRY data, followed by 4 blank bytes.

        :param drive_fw_version: The drive_fw_version of this InterposerData.
        :type: str
        """
        self._drive_fw_version = drive_fw_version

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

