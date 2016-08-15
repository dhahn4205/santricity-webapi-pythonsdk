# coding: utf-8

"""
CacheBackupDeviceLocation.py

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


class CacheBackupDeviceLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CacheBackupDeviceLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller_tray': 'int',  # (required parameter)
            'controller_slot': 'int',  # (required parameter)
            'cache_backup_device_slot': 'int'
        }

        self.attribute_map = {
            'controller_tray': 'controllerTray',  # (required parameter)
            'controller_slot': 'controllerSlot',  # (required parameter)
            'cache_backup_device_slot': 'cacheBackupDeviceSlot'
        }

        self._controller_tray = None
        self._controller_slot = None
        self._cache_backup_device_slot = None

    @property
    def controller_tray(self):
        """
        Gets the controller_tray of this CacheBackupDeviceLocation.
        The tray ID of the controller that houses the cache backup device.

        :return: The controller_tray of this CacheBackupDeviceLocation.
        :rtype: int
        :required/optional: required
        """
        return self._controller_tray

    @controller_tray.setter
    def controller_tray(self, controller_tray):
        """
        Sets the controller_tray of this CacheBackupDeviceLocation.
        The tray ID of the controller that houses the cache backup device.

        :param controller_tray: The controller_tray of this CacheBackupDeviceLocation.
        :type: int
        """
        self._controller_tray = controller_tray

    @property
    def controller_slot(self):
        """
        Gets the controller_slot of this CacheBackupDeviceLocation.
        The slot number of the controller that houses the cache backup device.

        :return: The controller_slot of this CacheBackupDeviceLocation.
        :rtype: int
        :required/optional: required
        """
        return self._controller_slot

    @controller_slot.setter
    def controller_slot(self, controller_slot):
        """
        Sets the controller_slot of this CacheBackupDeviceLocation.
        The slot number of the controller that houses the cache backup device.

        :param controller_slot: The controller_slot of this CacheBackupDeviceLocation.
        :type: int
        """
        self._controller_slot = controller_slot

    @property
    def cache_backup_device_slot(self):
        """
        Gets the cache_backup_device_slot of this CacheBackupDeviceLocation.
        The number of the slot on the controller in which the cache backup device resides.

        :return: The cache_backup_device_slot of this CacheBackupDeviceLocation.
        :rtype: int
        :required/optional: required
        """
        return self._cache_backup_device_slot

    @cache_backup_device_slot.setter
    def cache_backup_device_slot(self, cache_backup_device_slot):
        """
        Sets the cache_backup_device_slot of this CacheBackupDeviceLocation.
        The number of the slot on the controller in which the cache backup device resides.

        :param cache_backup_device_slot: The cache_backup_device_slot of this CacheBackupDeviceLocation.
        :type: int
        """
        self._cache_backup_device_slot = cache_backup_device_slot

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

