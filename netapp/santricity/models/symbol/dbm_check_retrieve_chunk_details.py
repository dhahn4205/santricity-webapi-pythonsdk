# coding: utf-8

"""
DbmCheckRetrieveChunkDetails.py

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


class DbmCheckRetrieveChunkDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DbmCheckRetrieveChunkDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'validation_status': 'str',  # (required parameter)
            'block_data': 'str',  # (required parameter)
            'source_location': 'str'
        }

        self.attribute_map = {
            'validation_status': 'validationStatus',  # (required parameter)
            'block_data': 'blockData',  # (required parameter)
            'source_location': 'sourceLocation'
        }

        self._validation_status = None
        self._block_data = None
        self._source_location = None

    @property
    def validation_status(self):
        """
        Gets the validation_status of this DbmCheckRetrieveChunkDetails.
        If the consistency check is successful, this field will be set to DBM_VALIDATION_OK, otherwise it will contain a specific failure code. The returnCode field in RawDataRetrieveResult will always be set to RETCODE_OK.

        :return: The validation_status of this DbmCheckRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this DbmCheckRetrieveChunkDetails.
        If the consistency check is successful, this field will be set to DBM_VALIDATION_OK, otherwise it will contain a specific failure code. The returnCode field in RawDataRetrieveResult will always be set to RETCODE_OK.

        :param validation_status: The validation_status of this DbmCheckRetrieveChunkDetails.
        :type: str
        """
        allowed_values = ["ok", "noHeap", "ioError", "earlyExecution", "fatalFsInvalid", "fatalRootOutOfBounds", "fatalDupBlockPointers", "fatalDirOutOfBounds", "fatalCorruptMetadata", "fatalMissingMetadata", "fatalRecOutOfBounds", "fatalDupRecPointers", "fatalRecordUnallocated", "fatalOrphanBlock", "fatalFsOffline", "noDrives", "lockError", "fatalMirrorMismatch", "mirrorNotReady", "__UNDEFINED"]
        if validation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `validation_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._validation_status = validation_status

    @property
    def block_data(self):
        """
        Gets the block_data of this DbmCheckRetrieveChunkDetails.
        An array of opaque data fields will be returned.

        :return: The block_data of this DbmCheckRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._block_data

    @block_data.setter
    def block_data(self, block_data):
        """
        Sets the block_data of this DbmCheckRetrieveChunkDetails.
        An array of opaque data fields will be returned.

        :param block_data: The block_data of this DbmCheckRetrieveChunkDetails.
        :type: str
        """
        self._block_data = block_data

    @property
    def source_location(self):
        """
        Gets the source_location of this DbmCheckRetrieveChunkDetails.
        Specifies which storage device contains the image to be checked.

        :return: The source_location of this DbmCheckRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """
        Sets the source_location of this DbmCheckRetrieveChunkDetails.
        Specifies which storage device contains the image to be checked.

        :param source_location: The source_location of this DbmCheckRetrieveChunkDetails.
        :type: str
        """
        allowed_values = ["unknown", "dacstoreDisks", "onboardRpa", "hostImage", "__UNDEFINED"]
        if source_location not in allowed_values:
            raise ValueError(
                "Invalid value for `source_location`, must be one of {0}"
                .format(allowed_values)
            )
        self._source_location = source_location

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

