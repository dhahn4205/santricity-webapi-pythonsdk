# coding: utf-8

"""
DiscoveryResponse.py

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


class DiscoveryResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DiscoveryResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_from_agent': 'bool',  # (required parameter)
            'agent_id': 'str',  # (required parameter)
            'controllers': 'list[AccessibleController]'
        }

        self.attribute_map = {
            'response_from_agent': 'responseFromAgent',  # (required parameter)
            'agent_id': 'agentId',  # (required parameter)
            'controllers': 'controllers'
        }

        self._response_from_agent = None
        self._agent_id = None
        self._controllers = None

    @property
    def response_from_agent(self):
        """
        Gets the response_from_agent of this DiscoveryResponse.
        A true value in this field indicates that the response was generated by a SYMbol agent; a false value indicates that the response is from a direct network-attached RAID controller.

        :return: The response_from_agent of this DiscoveryResponse.
        :rtype: bool
        :required/optional: required
        """
        return self._response_from_agent

    @response_from_agent.setter
    def response_from_agent(self, response_from_agent):
        """
        Sets the response_from_agent of this DiscoveryResponse.
        A true value in this field indicates that the response was generated by a SYMbol agent; a false value indicates that the response is from a direct network-attached RAID controller.

        :param response_from_agent: The response_from_agent of this DiscoveryResponse.
        :type: bool
        """
        self._response_from_agent = response_from_agent

    @property
    def agent_id(self):
        """
        Gets the agent_id of this DiscoveryResponse.
        A global identifier of the responding agent. Note that this value will not be set if the response is from a direct network-attached RAID controller instead of an agent.

        :return: The agent_id of this DiscoveryResponse.
        :rtype: str
        :required/optional: required
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this DiscoveryResponse.
        A global identifier of the responding agent. Note that this value will not be set if the response is from a direct network-attached RAID controller instead of an agent.

        :param agent_id: The agent_id of this DiscoveryResponse.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def controllers(self):
        """
        Gets the controllers of this DiscoveryResponse.
        This field contains a variable-length array of AccessibleController objects. There is one element for each controller that can be reached through the entity that is responding to the request.

        :return: The controllers of this DiscoveryResponse.
        :rtype: list[AccessibleController]
        :required/optional: required
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """
        Sets the controllers of this DiscoveryResponse.
        This field contains a variable-length array of AccessibleController objects. There is one element for each controller that can be reached through the entity that is responding to the request.

        :param controllers: The controllers of this DiscoveryResponse.
        :type: list[AccessibleController]
        """
        self._controllers = controllers

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

