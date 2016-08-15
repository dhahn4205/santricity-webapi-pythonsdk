# coding: utf-8

"""
ScheduleCreateRequest.py

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


class ScheduleCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScheduleCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',  # (required parameter)
            'target_object': 'str',  
            'schedule_method': 'str',  # (required parameter)
            'daily_schedule': 'DailySchedule',  # (required parameter)
            'days_of_week': 'list[str]',  
            'months_of_year': 'list[str]',  
            'days_of_month': 'list[str]',  
            'start_date': 'int',  # (required parameter)
            'end_date': 'int',  # (required parameter)
            'timezone': 'TimeZoneDescription'
        }

        self.attribute_map = {
            'action': 'action',  # (required parameter)
            'target_object': 'targetObject',  
            'schedule_method': 'scheduleMethod',  # (required parameter)
            'daily_schedule': 'dailySchedule',  # (required parameter)
            'days_of_week': 'daysOfWeek',  
            'months_of_year': 'monthsOfYear',  
            'days_of_month': 'daysOfMonth',  
            'start_date': 'startDate',  # (required parameter)
            'end_date': 'endDate',  # (required parameter)
            'timezone': 'timezone'
        }

        self._action = None
        self._target_object = None
        self._schedule_method = None
        self._daily_schedule = None
        self._days_of_week = None
        self._months_of_year = None
        self._days_of_month = None
        self._start_date = None
        self._end_date = None
        self._timezone = None

    @property
    def action(self):
        """
        Gets the action of this ScheduleCreateRequest.
        The schedule action type.

        :return: The action of this ScheduleCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ScheduleCreateRequest.
        The schedule action type.

        :param action: The action of this ScheduleCreateRequest.
        :type: str
        """
        allowed_values = ["unknown", "resnap", "newpit", "newcgpit", "__UNDEFINED"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action`, must be one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def target_object(self):
        """
        Gets the target_object of this ScheduleCreateRequest.
        The SYMbol reference of the target object.

        :return: The target_object of this ScheduleCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._target_object

    @target_object.setter
    def target_object(self, target_object):
        """
        Sets the target_object of this ScheduleCreateRequest.
        The SYMbol reference of the target object.

        :param target_object: The target_object of this ScheduleCreateRequest.
        :type: str
        """
        self._target_object = target_object

    @property
    def schedule_method(self):
        """
        Gets the schedule_method of this ScheduleCreateRequest.
        The schedule calendar type.

        :return: The schedule_method of this ScheduleCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._schedule_method

    @schedule_method.setter
    def schedule_method(self, schedule_method):
        """
        Sets the schedule_method of this ScheduleCreateRequest.
        The schedule calendar type.

        :param schedule_method: The schedule_method of this ScheduleCreateRequest.
        :type: str
        """
        allowed_values = ["unknown", "daily", "weekly", "monthlyDate", "monthlyDay", "__UNDEFINED"]
        if schedule_method not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._schedule_method = schedule_method

    @property
    def daily_schedule(self):
        """
        Gets the daily_schedule of this ScheduleCreateRequest.
        The daily schedule times for all schedule methods.

        :return: The daily_schedule of this ScheduleCreateRequest.
        :rtype: DailySchedule
        :required/optional: required
        """
        return self._daily_schedule

    @daily_schedule.setter
    def daily_schedule(self, daily_schedule):
        """
        Sets the daily_schedule of this ScheduleCreateRequest.
        The daily schedule times for all schedule methods.

        :param daily_schedule: The daily_schedule of this ScheduleCreateRequest.
        :type: DailySchedule
        """
        self._daily_schedule = daily_schedule

    @property
    def days_of_week(self):
        """
        Gets the days_of_week of this ScheduleCreateRequest.
        The days of the week for the weekly schedule method.

        :return: The days_of_week of this ScheduleCreateRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """
        Sets the days_of_week of this ScheduleCreateRequest.
        The days of the week for the weekly schedule method.

        :param days_of_week: The days_of_week of this ScheduleCreateRequest.
        :type: list[str]
        """
        self._days_of_week = days_of_week

    @property
    def months_of_year(self):
        """
        Gets the months_of_year of this ScheduleCreateRequest.
        The months of the year for the monthly by date schedule method.

        :return: The months_of_year of this ScheduleCreateRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._months_of_year

    @months_of_year.setter
    def months_of_year(self, months_of_year):
        """
        Sets the months_of_year of this ScheduleCreateRequest.
        The months of the year for the monthly by date schedule method.

        :param months_of_year: The months_of_year of this ScheduleCreateRequest.
        :type: list[str]
        """
        self._months_of_year = months_of_year

    @property
    def days_of_month(self):
        """
        Gets the days_of_month of this ScheduleCreateRequest.
        The days of the month for the monthly by date schedule method.

        :return: The days_of_month of this ScheduleCreateRequest.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, days_of_month):
        """
        Sets the days_of_month of this ScheduleCreateRequest.
        The days of the month for the monthly by date schedule method.

        :param days_of_month: The days_of_month of this ScheduleCreateRequest.
        :type: list[str]
        """
        self._days_of_month = days_of_month

    @property
    def start_date(self):
        """
        Gets the start_date of this ScheduleCreateRequest.
        The start date for the schedule.

        :return: The start_date of this ScheduleCreateRequest.
        :rtype: int
        :required/optional: required
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ScheduleCreateRequest.
        The start date for the schedule.

        :param start_date: The start_date of this ScheduleCreateRequest.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this ScheduleCreateRequest.
        The end date for the schedule, 0 for no end date.

        :return: The end_date of this ScheduleCreateRequest.
        :rtype: int
        :required/optional: required
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ScheduleCreateRequest.
        The end date for the schedule, 0 for no end date.

        :param end_date: The end_date of this ScheduleCreateRequest.
        :type: int
        """
        self._end_date = end_date

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduleCreateRequest.
        The schedule time zone information.

        :return: The timezone of this ScheduleCreateRequest.
        :rtype: TimeZoneDescription
        :required/optional: required
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduleCreateRequest.
        The schedule time zone information.

        :param timezone: The timezone of this ScheduleCreateRequest.
        :type: TimeZoneDescription
        """
        self._timezone = timezone

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

