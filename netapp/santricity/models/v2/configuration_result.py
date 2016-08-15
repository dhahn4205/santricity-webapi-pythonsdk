# coding: utf-8

"""
ConfigurationResult.py

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


class ConfigurationResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConfigurationResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date': 'datetime',  
            'end_date': 'datetime',  
            'current_results': 'list[ConfigurationResultItem]',  
            'total_systems': 'int',  
            'number_done': 'int',  
            'operation_done': 'bool'
        }

        self.attribute_map = {
            'start_date': 'startDate',  
            'end_date': 'endDate',  
            'current_results': 'currentResults',  
            'total_systems': 'totalSystems',  
            'number_done': 'numberDone',  
            'operation_done': 'operationDone'
        }

        self._start_date = None
        self._end_date = None
        self._current_results = None
        self._total_systems = None
        self._number_done = None
        self._operation_done = None

    @property
    def start_date(self):
        """
        Gets the start_date of this ConfigurationResult.
        The time the configuration operation started

        :return: The start_date of this ConfigurationResult.
        :rtype: datetime
        :required/optional: optional
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ConfigurationResult.
        The time the configuration operation started

        :param start_date: The start_date of this ConfigurationResult.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this ConfigurationResult.
        The time the operation finished.  Null if an operation is in progress

        :return: The end_date of this ConfigurationResult.
        :rtype: datetime
        :required/optional: optional
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ConfigurationResult.
        The time the operation finished.  Null if an operation is in progress

        :param end_date: The end_date of this ConfigurationResult.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def current_results(self):
        """
        Gets the current_results of this ConfigurationResult.
        The list of results for each system being configured.  The size of this list will be < total until the operation is finished

        :return: The current_results of this ConfigurationResult.
        :rtype: list[ConfigurationResultItem]
        :required/optional: optional
        """
        return self._current_results

    @current_results.setter
    def current_results(self, current_results):
        """
        Sets the current_results of this ConfigurationResult.
        The list of results for each system being configured.  The size of this list will be < total until the operation is finished

        :param current_results: The current_results of this ConfigurationResult.
        :type: list[ConfigurationResultItem]
        """
        self._current_results = current_results

    @property
    def total_systems(self):
        """
        Gets the total_systems of this ConfigurationResult.
        the total number of systems requested to be configured

        :return: The total_systems of this ConfigurationResult.
        :rtype: int
        :required/optional: optional
        """
        return self._total_systems

    @total_systems.setter
    def total_systems(self, total_systems):
        """
        Sets the total_systems of this ConfigurationResult.
        the total number of systems requested to be configured

        :param total_systems: The total_systems of this ConfigurationResult.
        :type: int
        """
        self._total_systems = total_systems

    @property
    def number_done(self):
        """
        Gets the number_done of this ConfigurationResult.
        the number of system currently attempted

        :return: The number_done of this ConfigurationResult.
        :rtype: int
        :required/optional: optional
        """
        return self._number_done

    @number_done.setter
    def number_done(self, number_done):
        """
        Sets the number_done of this ConfigurationResult.
        the number of system currently attempted

        :param number_done: The number_done of this ConfigurationResult.
        :type: int
        """
        self._number_done = number_done

    @property
    def operation_done(self):
        """
        Gets the operation_done of this ConfigurationResult.
        true when the configuration operation is finished

        :return: The operation_done of this ConfigurationResult.
        :rtype: bool
        :required/optional: optional
        """
        return self._operation_done

    @operation_done.setter
    def operation_done(self, operation_done):
        """
        Sets the operation_done of this ConfigurationResult.
        true when the configuration operation is finished

        :param operation_done: The operation_done of this ConfigurationResult.
        :type: bool
        """
        self._operation_done = operation_done

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

