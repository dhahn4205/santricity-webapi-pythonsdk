# coding: utf-8

"""
ConcatVolume.py

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


class ConcatVolume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConcatVolume - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'concat_vol_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'member_count': 'int',  # (required parameter)
            'aggregate_capacity': 'int',  # (required parameter)
            'media_scan_params': 'VolumeMediaScanParams',  # (required parameter)
            'volume_handle': 'int',  # (required parameter)
            'allowed_operations': 'VolumePerms',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'concat_vol_ref': 'concatVolRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'member_count': 'memberCount',  # (required parameter)
            'aggregate_capacity': 'aggregateCapacity',  # (required parameter)
            'media_scan_params': 'mediaScanParams',  # (required parameter)
            'volume_handle': 'volumeHandle',  # (required parameter)
            'allowed_operations': 'allowedOperations',  # (required parameter)
            'id': 'id'
        }

        self._concat_vol_ref = None
        self._status = None
        self._member_count = None
        self._aggregate_capacity = None
        self._media_scan_params = None
        self._volume_handle = None
        self._allowed_operations = None
        self._id = None

    @property
    def concat_vol_ref(self):
        """
        Gets the concat_vol_ref of this ConcatVolume.
        A reference (key) for ConcatVolume.

        :return: The concat_vol_ref of this ConcatVolume.
        :rtype: str
        :required/optional: required
        """
        return self._concat_vol_ref

    @concat_vol_ref.setter
    def concat_vol_ref(self, concat_vol_ref):
        """
        Sets the concat_vol_ref of this ConcatVolume.
        A reference (key) for ConcatVolume.

        :param concat_vol_ref: The concat_vol_ref of this ConcatVolume.
        :type: str
        """
        self._concat_vol_ref = concat_vol_ref

    @property
    def status(self):
        """
        Gets the status of this ConcatVolume.
        The status/state of the concatenated volume. This will be the worst status among the member volumes.

        :return: The status of this ConcatVolume.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConcatVolume.
        The status/state of the concatenated volume. This will be the worst status among the member volumes.

        :param status: The status of this ConcatVolume.
        :type: str
        """
        allowed_values = ["unknown", "optimal", "degraded", "failed", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def member_count(self):
        """
        Gets the member_count of this ConcatVolume.
        The number of actual storage volumes comprising this volume. Note that this is just for convenience, this information can be derived from member objects.

        :return: The member_count of this ConcatVolume.
        :rtype: int
        :required/optional: required
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """
        Sets the member_count of this ConcatVolume.
        The number of actual storage volumes comprising this volume. Note that this is just for convenience, this information can be derived from member objects.

        :param member_count: The member_count of this ConcatVolume.
        :type: int
        """
        self._member_count = member_count

    @property
    def aggregate_capacity(self):
        """
        Gets the aggregate_capacity of this ConcatVolume.
        The aggregate capacity in bytes of all member volumes.

        :return: The aggregate_capacity of this ConcatVolume.
        :rtype: int
        :required/optional: required
        """
        return self._aggregate_capacity

    @aggregate_capacity.setter
    def aggregate_capacity(self, aggregate_capacity):
        """
        Sets the aggregate_capacity of this ConcatVolume.
        The aggregate capacity in bytes of all member volumes.

        :param aggregate_capacity: The aggregate_capacity of this ConcatVolume.
        :type: int
        """
        self._aggregate_capacity = aggregate_capacity

    @property
    def media_scan_params(self):
        """
        Gets the media_scan_params of this ConcatVolume.
        Media scan parameters.

        :return: The media_scan_params of this ConcatVolume.
        :rtype: VolumeMediaScanParams
        :required/optional: required
        """
        return self._media_scan_params

    @media_scan_params.setter
    def media_scan_params(self, media_scan_params):
        """
        Sets the media_scan_params of this ConcatVolume.
        Media scan parameters.

        :param media_scan_params: The media_scan_params of this ConcatVolume.
        :type: VolumeMediaScanParams
        """
        self._media_scan_params = media_scan_params

    @property
    def volume_handle(self):
        """
        Gets the volume_handle of this ConcatVolume.
        The volume ssid. This is provided primarily for debug purposes.

        :return: The volume_handle of this ConcatVolume.
        :rtype: int
        :required/optional: required
        """
        return self._volume_handle

    @volume_handle.setter
    def volume_handle(self, volume_handle):
        """
        Sets the volume_handle of this ConcatVolume.
        The volume ssid. This is provided primarily for debug purposes.

        :param volume_handle: The volume_handle of this ConcatVolume.
        :type: int
        """
        self._volume_handle = volume_handle

    @property
    def allowed_operations(self):
        """
        Gets the allowed_operations of this ConcatVolume.
        Operations allowed on the ConcatVolume. This can be used if ConcatVolume is ever exposed as a host-addressable volume to specify whether the volume is host-mappable or not (repository volumes would never be mappable).

        :return: The allowed_operations of this ConcatVolume.
        :rtype: VolumePerms
        :required/optional: required
        """
        return self._allowed_operations

    @allowed_operations.setter
    def allowed_operations(self, allowed_operations):
        """
        Sets the allowed_operations of this ConcatVolume.
        Operations allowed on the ConcatVolume. This can be used if ConcatVolume is ever exposed as a host-addressable volume to specify whether the volume is host-mappable or not (repository volumes would never be mappable).

        :param allowed_operations: The allowed_operations of this ConcatVolume.
        :type: VolumePerms
        """
        self._allowed_operations = allowed_operations

    @property
    def id(self):
        """
        Gets the id of this ConcatVolume.


        :return: The id of this ConcatVolume.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConcatVolume.


        :param id: The id of this ConcatVolume.
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

