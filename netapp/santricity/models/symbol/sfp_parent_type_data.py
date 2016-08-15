# coding: utf-8

"""
SFPParentTypeData.py

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


class SFPParentTypeData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SFPParentTypeData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sfp_parent_type': 'str',  # (required parameter)
            'controller_sfp': 'ControllerSFP',  
            'parent_esm': 'str',  
            'parent_minihub': 'str'
        }

        self.attribute_map = {
            'sfp_parent_type': 'sfpParentType',  # (required parameter)
            'controller_sfp': 'controllerSFP',  
            'parent_esm': 'parentEsm',  
            'parent_minihub': 'parentMinihub'
        }

        self._sfp_parent_type = None
        self._controller_sfp = None
        self._parent_esm = None
        self._parent_minihub = None

    @property
    def sfp_parent_type(self):
        """
        Gets the sfp_parent_type of this SFPParentTypeData.
        This enumeration object is used to describe the parent type of a SFP.

        :return: The sfp_parent_type of this SFPParentTypeData.
        :rtype: str
        :required/optional: required
        """
        return self._sfp_parent_type

    @sfp_parent_type.setter
    def sfp_parent_type(self, sfp_parent_type):
        """
        Sets the sfp_parent_type of this SFPParentTypeData.
        This enumeration object is used to describe the parent type of a SFP.

        :param sfp_parent_type: The sfp_parent_type of this SFPParentTypeData.
        :type: str
        """
        allowed_values = ["unknown", "esm", "minihub", "controller", "__UNDEFINED"]
        if sfp_parent_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sfp_parent_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._sfp_parent_type = sfp_parent_type

    @property
    def controller_sfp(self):
        """
        Gets the controller_sfp of this SFPParentTypeData.
        This field is present only if the sfpParentType is equal to SFP_PARENT_TYPE_CONTROLLER. It contains the parent type of a SFP.

        :return: The controller_sfp of this SFPParentTypeData.
        :rtype: ControllerSFP
        :required/optional: optional
        """
        return self._controller_sfp

    @controller_sfp.setter
    def controller_sfp(self, controller_sfp):
        """
        Sets the controller_sfp of this SFPParentTypeData.
        This field is present only if the sfpParentType is equal to SFP_PARENT_TYPE_CONTROLLER. It contains the parent type of a SFP.

        :param controller_sfp: The controller_sfp of this SFPParentTypeData.
        :type: ControllerSFP
        """
        self._controller_sfp = controller_sfp

    @property
    def parent_esm(self):
        """
        Gets the parent_esm of this SFPParentTypeData.
        No information is returned

        :return: The parent_esm of this SFPParentTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._parent_esm

    @parent_esm.setter
    def parent_esm(self, parent_esm):
        """
        Sets the parent_esm of this SFPParentTypeData.
        No information is returned

        :param parent_esm: The parent_esm of this SFPParentTypeData.
        :type: str
        """
        self._parent_esm = parent_esm

    @property
    def parent_minihub(self):
        """
        Gets the parent_minihub of this SFPParentTypeData.
        This field is present only if the sfpParentType is equal to SFP_PARENT_TYPE_MINIHUB. It contains the parent type of a SFP.

        :return: The parent_minihub of this SFPParentTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._parent_minihub

    @parent_minihub.setter
    def parent_minihub(self, parent_minihub):
        """
        Sets the parent_minihub of this SFPParentTypeData.
        This field is present only if the sfpParentType is equal to SFP_PARENT_TYPE_MINIHUB. It contains the parent type of a SFP.

        :param parent_minihub: The parent_minihub of this SFPParentTypeData.
        :type: str
        """
        self._parent_minihub = parent_minihub

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

