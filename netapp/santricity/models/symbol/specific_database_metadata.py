# coding: utf-8

"""
SpecificDatabaseMetadata.py

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


class SpecificDatabaseMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SpecificDatabaseMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller_ref': 'str',  # (required parameter)
            'db_location': 'str',  # (required parameter)
            'db_revision': 'str',  # (required parameter)
            'db_id': 'str',  # (required parameter)
            'db_gen_number': 'int',  # (required parameter)
            'disk_pool_id': 'str',  # (required parameter)
            'db_status': 'str',  # (required parameter)
            'db_access': 'str'
        }

        self.attribute_map = {
            'controller_ref': 'controllerRef',  # (required parameter)
            'db_location': 'dbLocation',  # (required parameter)
            'db_revision': 'dbRevision',  # (required parameter)
            'db_id': 'dbID',  # (required parameter)
            'db_gen_number': 'dbGenNumber',  # (required parameter)
            'disk_pool_id': 'diskPoolID',  # (required parameter)
            'db_status': 'dbStatus',  # (required parameter)
            'db_access': 'dbAccess'
        }

        self._controller_ref = None
        self._db_location = None
        self._db_revision = None
        self._db_id = None
        self._db_gen_number = None
        self._disk_pool_id = None
        self._db_status = None
        self._db_access = None

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this SpecificDatabaseMetadata.
        A reference to the controller. This is unused if the dbLocation field is DACSTORE_DISKS.

        :return: The controller_ref of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this SpecificDatabaseMetadata.
        A reference to the controller. This is unused if the dbLocation field is DACSTORE_DISKS.

        :param controller_ref: The controller_ref of this SpecificDatabaseMetadata.
        :type: str
        """
        self._controller_ref = controller_ref

    @property
    def db_location(self):
        """
        Gets the db_location of this SpecificDatabaseMetadata.
        The physical location of the database image.

        :return: The db_location of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._db_location

    @db_location.setter
    def db_location(self, db_location):
        """
        Sets the db_location of this SpecificDatabaseMetadata.
        The physical location of the database image.

        :param db_location: The db_location of this SpecificDatabaseMetadata.
        :type: str
        """
        allowed_values = ["unknown", "dacstoreDisks", "onboardRpa", "hostImage", "__UNDEFINED"]
        if db_location not in allowed_values:
            raise ValueError(
                "Invalid value for `db_location`, must be one of {0}"
                .format(allowed_values)
            )
        self._db_location = db_location

    @property
    def db_revision(self):
        """
        Gets the db_revision of this SpecificDatabaseMetadata.
        The database revision.

        :return: The db_revision of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._db_revision

    @db_revision.setter
    def db_revision(self, db_revision):
        """
        Sets the db_revision of this SpecificDatabaseMetadata.
        The database revision.

        :param db_revision: The db_revision of this SpecificDatabaseMetadata.
        :type: str
        """
        self._db_revision = db_revision

    @property
    def db_id(self):
        """
        Gets the db_id of this SpecificDatabaseMetadata.
        The database ID.

        :return: The db_id of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """
        Sets the db_id of this SpecificDatabaseMetadata.
        The database ID.

        :param db_id: The db_id of this SpecificDatabaseMetadata.
        :type: str
        """
        self._db_id = db_id

    @property
    def db_gen_number(self):
        """
        Gets the db_gen_number of this SpecificDatabaseMetadata.
        The database gen number.

        :return: The db_gen_number of this SpecificDatabaseMetadata.
        :rtype: int
        :required/optional: required
        """
        return self._db_gen_number

    @db_gen_number.setter
    def db_gen_number(self, db_gen_number):
        """
        Sets the db_gen_number of this SpecificDatabaseMetadata.
        The database gen number.

        :param db_gen_number: The db_gen_number of this SpecificDatabaseMetadata.
        :type: int
        """
        self._db_gen_number = db_gen_number

    @property
    def disk_pool_id(self):
        """
        Gets the disk_pool_id of this SpecificDatabaseMetadata.
        The disk pool ID (volume group WWN hash).

        :return: The disk_pool_id of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._disk_pool_id

    @disk_pool_id.setter
    def disk_pool_id(self, disk_pool_id):
        """
        Sets the disk_pool_id of this SpecificDatabaseMetadata.
        The disk pool ID (volume group WWN hash).

        :param disk_pool_id: The disk_pool_id of this SpecificDatabaseMetadata.
        :type: str
        """
        self._disk_pool_id = disk_pool_id

    @property
    def db_status(self):
        """
        Gets the db_status of this SpecificDatabaseMetadata.
        The database status.

        :return: The db_status of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._db_status

    @db_status.setter
    def db_status(self, db_status):
        """
        Sets the db_status of this SpecificDatabaseMetadata.
        The database status.

        :param db_status: The db_status of this SpecificDatabaseMetadata.
        :type: str
        """
        allowed_values = ["unknown", "optimal", "stale", "mismatch", "invalid", "frozen", "empty", "__UNDEFINED"]
        if db_status not in allowed_values:
            raise ValueError(
                "Invalid value for `db_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._db_status = db_status

    @property
    def db_access(self):
        """
        Gets the db_access of this SpecificDatabaseMetadata.
        The database accessibility mode.

        :return: The db_access of this SpecificDatabaseMetadata.
        :rtype: str
        :required/optional: required
        """
        return self._db_access

    @db_access.setter
    def db_access(self, db_access):
        """
        Sets the db_access of this SpecificDatabaseMetadata.
        The database accessibility mode.

        :param db_access: The db_access of this SpecificDatabaseMetadata.
        :type: str
        """
        allowed_values = ["unknown", "offline", "readOnly", "readWrite", "recoveryMode", "__UNDEFINED"]
        if db_access not in allowed_values:
            raise ValueError(
                "Invalid value for `db_access`, must be one of {0}"
                .format(allowed_values)
            )
        self._db_access = db_access

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

