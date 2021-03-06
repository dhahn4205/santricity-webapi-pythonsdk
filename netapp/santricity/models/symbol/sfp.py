# coding: utf-8

"""
Sfp.py

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


class Sfp(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Sfp - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sfp_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'sfp_type': 'SFPType',  # (required parameter)
            'sfp_port': 'str',  # (required parameter)
            'parent_data': 'SFPParentTypeData',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str',  
            'sfp_port_ref': 'str',  # (required parameter)
            'repair_policy': 'RepairPolicy',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'sfp_ref': 'sfpRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'sfp_type': 'sfpType',  # (required parameter)
            'sfp_port': 'sfpPort',  # (required parameter)
            'parent_data': 'parentData',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2',  
            'sfp_port_ref': 'sfpPortRef',  # (required parameter)
            'repair_policy': 'repairPolicy',  # (required parameter)
            'id': 'id'
        }

        self._sfp_ref = None
        self._status = None
        self._physical_location = None
        self._sfp_type = None
        self._sfp_port = None
        self._parent_data = None
        self._reserved1 = None
        self._reserved2 = None
        self._sfp_port_ref = None
        self._repair_policy = None
        self._id = None

    @property
    def sfp_ref(self):
        """
        Gets the sfp_ref of this Sfp.
        The reference for this physical SFP.

        :return: The sfp_ref of this Sfp.
        :rtype: str
        :required/optional: required
        """
        return self._sfp_ref

    @sfp_ref.setter
    def sfp_ref(self, sfp_ref):
        """
        Sets the sfp_ref of this Sfp.
        The reference for this physical SFP.

        :param sfp_ref: The sfp_ref of this Sfp.
        :type: str
        """
        self._sfp_ref = sfp_ref

    @property
    def status(self):
        """
        Gets the status of this Sfp.
        The operational status of the SFP.

        :return: The status of this Sfp.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Sfp.
        The operational status of the SFP.

        :param status: The status of this Sfp.
        :type: str
        """
        allowed_values = ["optimal", "failed", "removed", "unknown", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def physical_location(self):
        """
        Gets the physical_location of this Sfp.
        The physical location of the SFP.

        :return: The physical_location of this Sfp.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this Sfp.
        The physical location of the SFP.

        :param physical_location: The physical_location of this Sfp.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def sfp_type(self):
        """
        Gets the sfp_type of this Sfp.
        The type of the SFP.

        :return: The sfp_type of this Sfp.
        :rtype: SFPType
        :required/optional: required
        """
        return self._sfp_type

    @sfp_type.setter
    def sfp_type(self, sfp_type):
        """
        Sets the sfp_type of this Sfp.
        The type of the SFP.

        :param sfp_type: The sfp_type of this Sfp.
        :type: SFPType
        """
        self._sfp_type = sfp_type

    @property
    def sfp_port(self):
        """
        Gets the sfp_port of this Sfp.
        The port that the SFP is associated with.

        :return: The sfp_port of this Sfp.
        :rtype: str
        :required/optional: required
        """
        return self._sfp_port

    @sfp_port.setter
    def sfp_port(self, sfp_port):
        """
        Sets the sfp_port of this Sfp.
        The port that the SFP is associated with.

        :param sfp_port: The sfp_port of this Sfp.
        :type: str
        """
        allowed_values = ["portUnknown", "port1", "port2", "port3", "port4", "__UNDEFINED"]
        if sfp_port not in allowed_values:
            raise ValueError(
                "Invalid value for `sfp_port`, must be one of {0}"
                .format(allowed_values)
            )
        self._sfp_port = sfp_port

    @property
    def parent_data(self):
        """
        Gets the parent_data of this Sfp.
        Data specific to SFP parent type.

        :return: The parent_data of this Sfp.
        :rtype: SFPParentTypeData
        :required/optional: required
        """
        return self._parent_data

    @parent_data.setter
    def parent_data(self, parent_data):
        """
        Sets the parent_data of this Sfp.
        Data specific to SFP parent type.

        :param parent_data: The parent_data of this Sfp.
        :type: SFPParentTypeData
        """
        self._parent_data = parent_data

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this Sfp.


        :return: The reserved1 of this Sfp.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this Sfp.


        :param reserved1: The reserved1 of this Sfp.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this Sfp.


        :return: The reserved2 of this Sfp.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this Sfp.


        :param reserved2: The reserved2 of this Sfp.
        :type: str
        """
        self._reserved2 = reserved2

    @property
    def sfp_port_ref(self):
        """
        Gets the sfp_port_ref of this Sfp.
        A reference identifying the channel port that the SFP is plugged into.

        :return: The sfp_port_ref of this Sfp.
        :rtype: str
        :required/optional: required
        """
        return self._sfp_port_ref

    @sfp_port_ref.setter
    def sfp_port_ref(self, sfp_port_ref):
        """
        Sets the sfp_port_ref of this Sfp.
        A reference identifying the channel port that the SFP is plugged into.

        :param sfp_port_ref: The sfp_port_ref of this Sfp.
        :type: str
        """
        self._sfp_port_ref = sfp_port_ref

    @property
    def repair_policy(self):
        """
        Gets the repair_policy of this Sfp.
        The repair policy for the SFP component.

        :return: The repair_policy of this Sfp.
        :rtype: RepairPolicy
        :required/optional: required
        """
        return self._repair_policy

    @repair_policy.setter
    def repair_policy(self, repair_policy):
        """
        Sets the repair_policy of this Sfp.
        The repair policy for the SFP component.

        :param repair_policy: The repair_policy of this Sfp.
        :type: RepairPolicy
        """
        self._repair_policy = repair_policy

    @property
    def id(self):
        """
        Gets the id of this Sfp.


        :return: The id of this Sfp.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sfp.


        :param id: The id of this Sfp.
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

