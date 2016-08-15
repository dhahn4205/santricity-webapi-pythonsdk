# coding: utf-8

"""
ThermalSensor.py

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


class ThermalSensor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ThermalSensor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'thermal_sensor_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str',  
            'rtr_attributes': 'RTRAttributes',  # (required parameter)
            'repair_policy': 'RepairPolicy',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'thermal_sensor_ref': 'thermalSensorRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2',  
            'rtr_attributes': 'rtrAttributes',  # (required parameter)
            'repair_policy': 'repairPolicy',  # (required parameter)
            'id': 'id'
        }

        self._thermal_sensor_ref = None
        self._status = None
        self._physical_location = None
        self._reserved1 = None
        self._reserved2 = None
        self._rtr_attributes = None
        self._repair_policy = None
        self._id = None

    @property
    def thermal_sensor_ref(self):
        """
        Gets the thermal_sensor_ref of this ThermalSensor.
        The reference for this physical thermal sensor.

        :return: The thermal_sensor_ref of this ThermalSensor.
        :rtype: str
        :required/optional: required
        """
        return self._thermal_sensor_ref

    @thermal_sensor_ref.setter
    def thermal_sensor_ref(self, thermal_sensor_ref):
        """
        Sets the thermal_sensor_ref of this ThermalSensor.
        The reference for this physical thermal sensor.

        :param thermal_sensor_ref: The thermal_sensor_ref of this ThermalSensor.
        :type: str
        """
        self._thermal_sensor_ref = thermal_sensor_ref

    @property
    def status(self):
        """
        Gets the status of this ThermalSensor.
        The operational status of the thermal sensor.

        :return: The status of this ThermalSensor.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ThermalSensor.
        The operational status of the thermal sensor.

        :param status: The status of this ThermalSensor.
        :type: str
        """
        allowed_values = ["optimal", "nominalTempExceed", "maxTempExceed", "removed", "unknown", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def physical_location(self):
        """
        Gets the physical_location of this ThermalSensor.
        The physical location of the thermal sensor. The parent reference in Location identifies the CRU that physically houses the thermal sensor, and the position field is the parent-relative/like-component relative number of the thermal sensor, starting at one.

        :return: The physical_location of this ThermalSensor.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this ThermalSensor.
        The physical location of the thermal sensor. The parent reference in Location identifies the CRU that physically houses the thermal sensor, and the position field is the parent-relative/like-component relative number of the thermal sensor, starting at one.

        :param physical_location: The physical_location of this ThermalSensor.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this ThermalSensor.


        :return: The reserved1 of this ThermalSensor.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this ThermalSensor.


        :param reserved1: The reserved1 of this ThermalSensor.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this ThermalSensor.


        :return: The reserved2 of this ThermalSensor.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this ThermalSensor.


        :param reserved2: The reserved2 of this ThermalSensor.
        :type: str
        """
        self._reserved2 = reserved2

    @property
    def rtr_attributes(self):
        """
        Gets the rtr_attributes of this ThermalSensor.
        The CRU type of the thermal sensor plus its ready-to-remove attributes, which are based on the CRU type

        :return: The rtr_attributes of this ThermalSensor.
        :rtype: RTRAttributes
        :required/optional: required
        """
        return self._rtr_attributes

    @rtr_attributes.setter
    def rtr_attributes(self, rtr_attributes):
        """
        Sets the rtr_attributes of this ThermalSensor.
        The CRU type of the thermal sensor plus its ready-to-remove attributes, which are based on the CRU type

        :param rtr_attributes: The rtr_attributes of this ThermalSensor.
        :type: RTRAttributes
        """
        self._rtr_attributes = rtr_attributes

    @property
    def repair_policy(self):
        """
        Gets the repair_policy of this ThermalSensor.
        The repair policy for the thermal sensor component.

        :return: The repair_policy of this ThermalSensor.
        :rtype: RepairPolicy
        :required/optional: required
        """
        return self._repair_policy

    @repair_policy.setter
    def repair_policy(self, repair_policy):
        """
        Sets the repair_policy of this ThermalSensor.
        The repair policy for the thermal sensor component.

        :param repair_policy: The repair_policy of this ThermalSensor.
        :type: RepairPolicy
        """
        self._repair_policy = repair_policy

    @property
    def id(self):
        """
        Gets the id of this ThermalSensor.


        :return: The id of this ThermalSensor.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ThermalSensor.


        :param id: The id of this ThermalSensor.
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

