# coding: utf-8

"""
DbmBlkRetrieveStartDetails.py

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


class DbmBlkRetrieveStartDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DbmBlkRetrieveStartDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'omit_unallocated_blocks': 'bool',  # (required parameter)
            'skip_block_coherency_check': 'bool',  # (required parameter)
            'skip_structure_integrity_check': 'bool',  # (required parameter)
            'source_location': 'str'
        }

        self.attribute_map = {
            'omit_unallocated_blocks': 'omitUnallocatedBlocks',  # (required parameter)
            'skip_block_coherency_check': 'skipBlockCoherencyCheck',  # (required parameter)
            'skip_structure_integrity_check': 'skipStructureIntegrityCheck',  # (required parameter)
            'source_location': 'sourceLocation'
        }

        self._omit_unallocated_blocks = None
        self._skip_block_coherency_check = None
        self._skip_structure_integrity_check = None
        self._source_location = None

    @property
    def omit_unallocated_blocks(self):
        """
        Gets the omit_unallocated_blocks of this DbmBlkRetrieveStartDetails.
        When true, unallocated blocks are omitted from the retrieved data.

        :return: The omit_unallocated_blocks of this DbmBlkRetrieveStartDetails.
        :rtype: bool
        :required/optional: required
        """
        return self._omit_unallocated_blocks

    @omit_unallocated_blocks.setter
    def omit_unallocated_blocks(self, omit_unallocated_blocks):
        """
        Sets the omit_unallocated_blocks of this DbmBlkRetrieveStartDetails.
        When true, unallocated blocks are omitted from the retrieved data.

        :param omit_unallocated_blocks: The omit_unallocated_blocks of this DbmBlkRetrieveStartDetails.
        :type: bool
        """
        self._omit_unallocated_blocks = omit_unallocated_blocks

    @property
    def skip_block_coherency_check(self):
        """
        Gets the skip_block_coherency_check of this DbmBlkRetrieveStartDetails.
        When true, the block coherency check is not performed during the preparation phase of the data transfer.

        :return: The skip_block_coherency_check of this DbmBlkRetrieveStartDetails.
        :rtype: bool
        :required/optional: required
        """
        return self._skip_block_coherency_check

    @skip_block_coherency_check.setter
    def skip_block_coherency_check(self, skip_block_coherency_check):
        """
        Sets the skip_block_coherency_check of this DbmBlkRetrieveStartDetails.
        When true, the block coherency check is not performed during the preparation phase of the data transfer.

        :param skip_block_coherency_check: The skip_block_coherency_check of this DbmBlkRetrieveStartDetails.
        :type: bool
        """
        self._skip_block_coherency_check = skip_block_coherency_check

    @property
    def skip_structure_integrity_check(self):
        """
        Gets the skip_structure_integrity_check of this DbmBlkRetrieveStartDetails.
        When true, the structure integrity check is not performed during the preparation phase of the data transfer.

        :return: The skip_structure_integrity_check of this DbmBlkRetrieveStartDetails.
        :rtype: bool
        :required/optional: required
        """
        return self._skip_structure_integrity_check

    @skip_structure_integrity_check.setter
    def skip_structure_integrity_check(self, skip_structure_integrity_check):
        """
        Sets the skip_structure_integrity_check of this DbmBlkRetrieveStartDetails.
        When true, the structure integrity check is not performed during the preparation phase of the data transfer.

        :param skip_structure_integrity_check: The skip_structure_integrity_check of this DbmBlkRetrieveStartDetails.
        :type: bool
        """
        self._skip_structure_integrity_check = skip_structure_integrity_check

    @property
    def source_location(self):
        """
        Gets the source_location of this DbmBlkRetrieveStartDetails.
        Defines which storage device to read the image from.

        :return: The source_location of this DbmBlkRetrieveStartDetails.
        :rtype: str
        :required/optional: required
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """
        Sets the source_location of this DbmBlkRetrieveStartDetails.
        Defines which storage device to read the image from.

        :param source_location: The source_location of this DbmBlkRetrieveStartDetails.
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

