# coding: utf-8

"""
SupportCRU.py

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


class SupportCRU(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SupportCRU - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'support_cru_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'manufacturer_date': 'int',  # (required parameter)
            'vendor_name': 'str',  # (required parameter)
            'vendor_pn': 'str',  # (required parameter)
            'vendor_sn': 'str',  # (required parameter)
            'fru_type': 'str',  # (required parameter)
            'ready_to_remove': 'bool',  # (required parameter)
            'rtr_attributes': 'RTRAttributes',  # (required parameter)
            'configured_components': 'list[str]',  # (required parameter)
            'type': 'str',  # (required parameter)
            'repair_policy': 'RepairPolicy',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'support_cru_ref': 'supportCRURef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'manufacturer_date': 'manufacturerDate',  # (required parameter)
            'vendor_name': 'vendorName',  # (required parameter)
            'vendor_pn': 'vendorPN',  # (required parameter)
            'vendor_sn': 'vendorSN',  # (required parameter)
            'fru_type': 'fruType',  # (required parameter)
            'ready_to_remove': 'readyToRemove',  # (required parameter)
            'rtr_attributes': 'rtrAttributes',  # (required parameter)
            'configured_components': 'configuredComponents',  # (required parameter)
            'type': 'type',  # (required parameter)
            'repair_policy': 'repairPolicy',  # (required parameter)
            'id': 'id'
        }

        self._support_cru_ref = None
        self._status = None
        self._physical_location = None
        self._manufacturer_date = None
        self._vendor_name = None
        self._vendor_pn = None
        self._vendor_sn = None
        self._fru_type = None
        self._ready_to_remove = None
        self._rtr_attributes = None
        self._configured_components = None
        self._type = None
        self._repair_policy = None
        self._id = None

    @property
    def support_cru_ref(self):
        """
        Gets the support_cru_ref of this SupportCRU.
        The reference for this physical support CRU.

        :return: The support_cru_ref of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._support_cru_ref

    @support_cru_ref.setter
    def support_cru_ref(self, support_cru_ref):
        """
        Sets the support_cru_ref of this SupportCRU.
        The reference for this physical support CRU.

        :param support_cru_ref: The support_cru_ref of this SupportCRU.
        :type: str
        """
        self._support_cru_ref = support_cru_ref

    @property
    def status(self):
        """
        Gets the status of this SupportCRU.
        The operational status of the support CRU.

        :return: The status of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SupportCRU.
        The operational status of the support CRU.

        :param status: The status of this SupportCRU.
        :type: str
        """
        allowed_values = ["unknown", "optimal", "failed", "removed", "noinput", "incorrectConfig", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def physical_location(self):
        """
        Gets the physical_location of this SupportCRU.
        The physical location of the support CRU. The parent reference in Location identifies the tray containing the CRU, and the position field is the parent-relative/like-component relative slot number of the CRU, starting at one.

        :return: The physical_location of this SupportCRU.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this SupportCRU.
        The physical location of the support CRU. The parent reference in Location identifies the tray containing the CRU, and the position field is the parent-relative/like-component relative slot number of the CRU, starting at one.

        :param physical_location: The physical_location of this SupportCRU.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def manufacturer_date(self):
        """
        Gets the manufacturer_date of this SupportCRU.
        VPD manufacture date.

        :return: The manufacturer_date of this SupportCRU.
        :rtype: int
        :required/optional: required
        """
        return self._manufacturer_date

    @manufacturer_date.setter
    def manufacturer_date(self, manufacturer_date):
        """
        Sets the manufacturer_date of this SupportCRU.
        VPD manufacture date.

        :param manufacturer_date: The manufacturer_date of this SupportCRU.
        :type: int
        """
        self._manufacturer_date = manufacturer_date

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this SupportCRU.
        VPD vendor name.

        :return: The vendor_name of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this SupportCRU.
        VPD vendor name.

        :param vendor_name: The vendor_name of this SupportCRU.
        :type: str
        """
        self._vendor_name = vendor_name

    @property
    def vendor_pn(self):
        """
        Gets the vendor_pn of this SupportCRU.
        VPD part number.

        :return: The vendor_pn of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_pn

    @vendor_pn.setter
    def vendor_pn(self, vendor_pn):
        """
        Sets the vendor_pn of this SupportCRU.
        VPD part number.

        :param vendor_pn: The vendor_pn of this SupportCRU.
        :type: str
        """
        self._vendor_pn = vendor_pn

    @property
    def vendor_sn(self):
        """
        Gets the vendor_sn of this SupportCRU.
        VPD serial number.

        :return: The vendor_sn of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_sn

    @vendor_sn.setter
    def vendor_sn(self, vendor_sn):
        """
        Sets the vendor_sn of this SupportCRU.
        VPD serial number.

        :param vendor_sn: The vendor_sn of this SupportCRU.
        :type: str
        """
        self._vendor_sn = vendor_sn

    @property
    def fru_type(self):
        """
        Gets the fru_type of this SupportCRU.
        VPD field replaceable unit type.

        :return: The fru_type of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._fru_type

    @fru_type.setter
    def fru_type(self, fru_type):
        """
        Sets the fru_type of this SupportCRU.
        VPD field replaceable unit type.

        :param fru_type: The fru_type of this SupportCRU.
        :type: str
        """
        self._fru_type = fru_type

    @property
    def ready_to_remove(self):
        """
        Gets the ready_to_remove of this SupportCRU.
        When set to True, the component is ready to remove (and the Ready to Remove indicator light is turned on). This field is deprecated. The rtrAttributes field should be used instead.

        :return: The ready_to_remove of this SupportCRU.
        :rtype: bool
        :required/optional: required
        """
        return self._ready_to_remove

    @ready_to_remove.setter
    def ready_to_remove(self, ready_to_remove):
        """
        Sets the ready_to_remove of this SupportCRU.
        When set to True, the component is ready to remove (and the Ready to Remove indicator light is turned on). This field is deprecated. The rtrAttributes field should be used instead.

        :param ready_to_remove: The ready_to_remove of this SupportCRU.
        :type: bool
        """
        self._ready_to_remove = ready_to_remove

    @property
    def rtr_attributes(self):
        """
        Gets the rtr_attributes of this SupportCRU.
        The CRU type of the support CRU plus its ready-to-remove attributes, which are based on the CRU type.

        :return: The rtr_attributes of this SupportCRU.
        :rtype: RTRAttributes
        :required/optional: required
        """
        return self._rtr_attributes

    @rtr_attributes.setter
    def rtr_attributes(self, rtr_attributes):
        """
        Sets the rtr_attributes of this SupportCRU.
        The CRU type of the support CRU plus its ready-to-remove attributes, which are based on the CRU type.

        :param rtr_attributes: The rtr_attributes of this SupportCRU.
        :type: RTRAttributes
        """
        self._rtr_attributes = rtr_attributes

    @property
    def configured_components(self):
        """
        Gets the configured_components of this SupportCRU.
        A variable-length list of the types of components that occupy the support CRU.

        :return: The configured_components of this SupportCRU.
        :rtype: list[str]
        :required/optional: required
        """
        return self._configured_components

    @configured_components.setter
    def configured_components(self, configured_components):
        """
        Sets the configured_components of this SupportCRU.
        A variable-length list of the types of components that occupy the support CRU.

        :param configured_components: The configured_components of this SupportCRU.
        :type: list[str]
        """
        self._configured_components = configured_components

    @property
    def type(self):
        """
        Gets the type of this SupportCRU.
        The type of this support CRU (e.g., \"power-fan\" or \"battery\")

        :return: The type of this SupportCRU.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SupportCRU.
        The type of this support CRU (e.g., \"power-fan\" or \"battery\")

        :param type: The type of this SupportCRU.
        :type: str
        """
        allowed_values = ["unknown", "powerFan", "battery", "fan", "powerSupply", "__UNDEFINED"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def repair_policy(self):
        """
        Gets the repair_policy of this SupportCRU.
        The repair policy for the support CRU component.

        :return: The repair_policy of this SupportCRU.
        :rtype: RepairPolicy
        :required/optional: required
        """
        return self._repair_policy

    @repair_policy.setter
    def repair_policy(self, repair_policy):
        """
        Sets the repair_policy of this SupportCRU.
        The repair policy for the support CRU component.

        :param repair_policy: The repair_policy of this SupportCRU.
        :type: RepairPolicy
        """
        self._repair_policy = repair_policy

    @property
    def id(self):
        """
        Gets the id of this SupportCRU.


        :return: The id of this SupportCRU.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SupportCRU.


        :param id: The id of this SupportCRU.
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

