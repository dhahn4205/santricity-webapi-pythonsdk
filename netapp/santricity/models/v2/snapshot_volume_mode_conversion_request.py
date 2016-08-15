# coding: utf-8

"""
SnapshotVolumeModeConversionRequest.py

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


class SnapshotVolumeModeConversionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SnapshotVolumeModeConversionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'repository_percentage': 'float',  
            'repository_candidate': 'ConcatVolumeCandidate',  
            'full_threshold': 'int'
        }

        self.attribute_map = {
            'repository_percentage': 'repositoryPercentage',  
            'repository_candidate': 'repositoryCandidate',  
            'full_threshold': 'fullThreshold'
        }

        self._repository_percentage = None
        self._repository_candidate = None
        self._full_threshold = None

    @property
    def repository_percentage(self):
        """
        Gets the repository_percentage of this SnapshotVolumeModeConversionRequest.
        Percentage of the base capacity to make the repository.

        :return: The repository_percentage of this SnapshotVolumeModeConversionRequest.
        :rtype: float
        :required/optional: optional
        """
        return self._repository_percentage

    @repository_percentage.setter
    def repository_percentage(self, repository_percentage):
        """
        Sets the repository_percentage of this SnapshotVolumeModeConversionRequest.
        Percentage of the base capacity to make the repository.

        :param repository_percentage: The repository_percentage of this SnapshotVolumeModeConversionRequest.
        :type: float
        """
        self._repository_percentage = repository_percentage

    @property
    def repository_candidate(self):
        """
        Gets the repository_candidate of this SnapshotVolumeModeConversionRequest.
        Allows a repository candidate to be manually specified for use in the conversion. By default, the best candidate will be selected.

        :return: The repository_candidate of this SnapshotVolumeModeConversionRequest.
        :rtype: ConcatVolumeCandidate
        :required/optional: optional
        """
        return self._repository_candidate

    @repository_candidate.setter
    def repository_candidate(self, repository_candidate):
        """
        Sets the repository_candidate of this SnapshotVolumeModeConversionRequest.
        Allows a repository candidate to be manually specified for use in the conversion. By default, the best candidate will be selected.

        :param repository_candidate: The repository_candidate of this SnapshotVolumeModeConversionRequest.
        :type: ConcatVolumeCandidate
        """
        self._repository_candidate = repository_candidate

    @property
    def full_threshold(self):
        """
        Gets the full_threshold of this SnapshotVolumeModeConversionRequest.
        The repository utilization warning threshold percentage.

        :return: The full_threshold of this SnapshotVolumeModeConversionRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._full_threshold

    @full_threshold.setter
    def full_threshold(self, full_threshold):
        """
        Sets the full_threshold of this SnapshotVolumeModeConversionRequest.
        The repository utilization warning threshold percentage.

        :param full_threshold: The full_threshold of this SnapshotVolumeModeConversionRequest.
        :type: int
        """
        self._full_threshold = full_threshold

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

