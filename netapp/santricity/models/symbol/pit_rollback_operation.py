# coding: utf-8

"""
PITRollbackOperation.py

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


class PITRollbackOperation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PITRollbackOperation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pit_group_ref': 'str',  # (required parameter)
            'pit_ref': 'str',  # (required parameter)
            'pending': 'bool',  # (required parameter)
            'percent_complete': 'int',  # (required parameter)
            'time_to_completion': 'int'
        }

        self.attribute_map = {
            'pit_group_ref': 'pitGroupRef',  # (required parameter)
            'pit_ref': 'pitRef',  # (required parameter)
            'pending': 'pending',  # (required parameter)
            'percent_complete': 'percentComplete',  # (required parameter)
            'time_to_completion': 'timeToCompletion'
        }

        self._pit_group_ref = None
        self._pit_ref = None
        self._pending = None
        self._percent_complete = None
        self._time_to_completion = None

    @property
    def pit_group_ref(self):
        """
        Gets the pit_group_ref of this PITRollbackOperation.
        A reference to the PiT Group.

        :return: The pit_group_ref of this PITRollbackOperation.
        :rtype: str
        :required/optional: required
        """
        return self._pit_group_ref

    @pit_group_ref.setter
    def pit_group_ref(self, pit_group_ref):
        """
        Sets the pit_group_ref of this PITRollbackOperation.
        A reference to the PiT Group.

        :param pit_group_ref: The pit_group_ref of this PITRollbackOperation.
        :type: str
        """
        self._pit_group_ref = pit_group_ref

    @property
    def pit_ref(self):
        """
        Gets the pit_ref of this PITRollbackOperation.
        A reference to the specific PiT being rolled back.

        :return: The pit_ref of this PITRollbackOperation.
        :rtype: str
        :required/optional: required
        """
        return self._pit_ref

    @pit_ref.setter
    def pit_ref(self, pit_ref):
        """
        Sets the pit_ref of this PITRollbackOperation.
        A reference to the specific PiT being rolled back.

        :param pit_ref: The pit_ref of this PITRollbackOperation.
        :type: str
        """
        self._pit_ref = pit_ref

    @property
    def pending(self):
        """
        Gets the pending of this PITRollbackOperation.
        If true, the operation has not started.

        :return: The pending of this PITRollbackOperation.
        :rtype: bool
        :required/optional: required
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """
        Sets the pending of this PITRollbackOperation.
        If true, the operation has not started.

        :param pending: The pending of this PITRollbackOperation.
        :type: bool
        """
        self._pending = pending

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this PITRollbackOperation.
        The completion percentage for the operation. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :return: The percent_complete of this PITRollbackOperation.
        :rtype: int
        :required/optional: required
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this PITRollbackOperation.
        The completion percentage for the operation. If the operation is not currently running this value will be equal to PERCENT_COMPLETE_OP_NOT_RUNNING.

        :param percent_complete: The percent_complete of this PITRollbackOperation.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def time_to_completion(self):
        """
        Gets the time_to_completion of this PITRollbackOperation.
        The estimated time to completion in minutes. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :return: The time_to_completion of this PITRollbackOperation.
        :rtype: int
        :required/optional: required
        """
        return self._time_to_completion

    @time_to_completion.setter
    def time_to_completion(self, time_to_completion):
        """
        Sets the time_to_completion of this PITRollbackOperation.
        The estimated time to completion in minutes. If the time is not known this value will be equal to TIME_TO_COMPLETION_UNKNOWN.

        :param time_to_completion: The time_to_completion of this PITRollbackOperation.
        :type: int
        """
        self._time_to_completion = time_to_completion

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

