# coding: utf-8

"""
FeatureKey.py

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


class FeatureKey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FeatureKey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key_version': 'int',  # (required parameter)
            'capability': 'str',  # (required parameter)
            'sa_id': 'SAIdentifier',  # (required parameter)
            'digest': 'str',  # (required parameter)
            'limit': 'int',  # (required parameter)
            'duration': 'int',  # (required parameter)
            'key_id': 'str',  # (required parameter)
            'supported_feature_bundle_id': 'int'
        }

        self.attribute_map = {
            'key_version': 'keyVersion',  # (required parameter)
            'capability': 'capability',  # (required parameter)
            'sa_id': 'saId',  # (required parameter)
            'digest': 'digest',  # (required parameter)
            'limit': 'limit',  # (required parameter)
            'duration': 'duration',  # (required parameter)
            'key_id': 'keyId',  # (required parameter)
            'supported_feature_bundle_id': 'supportedFeatureBundleId'
        }

        self._key_version = None
        self._capability = None
        self._sa_id = None
        self._digest = None
        self._limit = None
        self._duration = None
        self._key_id = None
        self._supported_feature_bundle_id = None

    @property
    def key_version(self):
        """
        Gets the key_version of this FeatureKey.
        An internal indication of the version of the feature key.

        :return: The key_version of this FeatureKey.
        :rtype: int
        :required/optional: required
        """
        return self._key_version

    @key_version.setter
    def key_version(self, key_version):
        """
        Sets the key_version of this FeatureKey.
        An internal indication of the version of the feature key.

        :param key_version: The key_version of this FeatureKey.
        :type: int
        """
        self._key_version = key_version

    @property
    def capability(self):
        """
        Gets the capability of this FeatureKey.
        The capability code for the feature that is to be enabled by this key.

        :return: The capability of this FeatureKey.
        :rtype: str
        :required/optional: required
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """
        Sets the capability of this FeatureKey.
        The capability code for the feature that is to be enabled by this key.

        :param capability: The capability of this FeatureKey.
        :type: str
        """
        allowed_values = ["none", "sharedVolume", "storagePoolsTo4", "mixedRaidlevel", "autoCodeSync", "autoLunTransfer", "subLunsAllowed", "storagePoolsTo8", "storagePoolsTo2", "storagePoolsToMax", "storagePoolsTo64", "storagePoolsTo16", "snapshots", "remoteMirroring", "volumeCopy", "stagedDownload", "mixedDriveTypes", "goldKey", "driveTrayExpansion", "bundleMigration", "storagePoolsTo128", "storagePoolsTo256", "raid6", "performanceTier", "storagePoolsTo32", "storagePoolsTo96", "storagePoolsTo192", "storagePoolsTo512", "remoteMirrorsTo16", "remoteMirrorsTo32", "remoteMirrorsTo64", "remoteMirrorsTo128", "snapshotsPerVolTo4", "snapshotsPerVolTo8", "snapshotsPerVolTo16", "snapshotsPerVolTo2", "secureVolume", "protectionInformation", "ssdSupport", "driveSlotLimitTo112", "driveSlotLimitTo120", "driveSlotLimitTo256", "driveSlotLimitTo448", "driveSlotLimitTo480", "driveSlotLimitToMax", "driveSlotLimit", "driveSlotLimitTo12", "driveSlotLimitTo16", "driveSlotLimitTo24", "driveSlotLimitTo32", "driveSlotLimitTo48", "driveSlotLimitTo60", "driveSlotLimitTo64", "driveSlotLimitTo72", "driveSlotLimitTo96", "driveSlotLimitTo128", "driveSlotLimitTo136", "driveSlotLimitTo144", "driveSlotLimitTo180", "driveSlotLimitTo192", "driveSlotLimitTo272", "fdeProxyKeyManagement", "remoteMirrorsTo8", "driveSlotLimitTo384", "driveSlotLimitTo300", "driveSlotLimitTo360", "flashReadCache", "storagePoolsType2", "remoteMirroringType2", "totalNumberOfArvmMirrorsPerArray", "totalNumberOfPitsPerArray", "totalNumberOfThinVolumesPerArray", "driveSlotLimitTo240", "snapshotsType2", "targetPortLunMapping", "__UNDEFINED"]
        if capability not in allowed_values:
            raise ValueError(
                "Invalid value for `capability`, must be one of {0}"
                .format(allowed_values)
            )
        self._capability = capability

    @property
    def sa_id(self):
        """
        Gets the sa_id of this FeatureKey.
        This field contains a unique identifier maintained by SAFE for use by storage management software. Storage management software uses this data to enable SAFE features and perform Feature Bundle migration.

        :return: The sa_id of this FeatureKey.
        :rtype: SAIdentifier
        :required/optional: required
        """
        return self._sa_id

    @sa_id.setter
    def sa_id(self, sa_id):
        """
        Sets the sa_id of this FeatureKey.
        This field contains a unique identifier maintained by SAFE for use by storage management software. Storage management software uses this data to enable SAFE features and perform Feature Bundle migration.

        :param sa_id: The sa_id of this FeatureKey.
        :type: SAIdentifier
        """
        self._sa_id = sa_id

    @property
    def digest(self):
        """
        Gets the digest of this FeatureKey.
        A computed message digest that verifies the authenticity of this feature key.

        :return: The digest of this FeatureKey.
        :rtype: str
        :required/optional: required
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this FeatureKey.
        A computed message digest that verifies the authenticity of this feature key.

        :param digest: The digest of this FeatureKey.
        :type: str
        """
        self._digest = digest

    @property
    def limit(self):
        """
        Gets the limit of this FeatureKey.
        The numeric limit for this specific feature. A zero value for a limit indicates a feature that is fully enabled and does not support tiers such as RAID 6.

        :return: The limit of this FeatureKey.
        :rtype: int
        :required/optional: required
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this FeatureKey.
        The numeric limit for this specific feature. A zero value for a limit indicates a feature that is fully enabled and does not support tiers such as RAID 6.

        :param limit: The limit of this FeatureKey.
        :type: int
        """
        self._limit = limit

    @property
    def duration(self):
        """
        Gets the duration of this FeatureKey.
        The duration before this feature is expired. An evaluation period is specified in days. A zero value for an evaluation period indicates a permanent license that has been purchased.

        :return: The duration of this FeatureKey.
        :rtype: int
        :required/optional: required
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this FeatureKey.
        The duration before this feature is expired. An evaluation period is specified in days. A zero value for an evaluation period indicates a permanent license that has been purchased.

        :param duration: The duration of this FeatureKey.
        :type: int
        """
        self._duration = duration

    @property
    def key_id(self):
        """
        Gets the key_id of this FeatureKey.
        For an additive license this will be the Key ID.

        :return: The key_id of this FeatureKey.
        :rtype: str
        :required/optional: required
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this FeatureKey.
        For an additive license this will be the Key ID.

        :param key_id: The key_id of this FeatureKey.
        :type: str
        """
        self._key_id = key_id

    @property
    def supported_feature_bundle_id(self):
        """
        Gets the supported_feature_bundle_id of this FeatureKey.
        The supported Feature Bundle ID. When not in use this value will be zero.

        :return: The supported_feature_bundle_id of this FeatureKey.
        :rtype: int
        :required/optional: required
        """
        return self._supported_feature_bundle_id

    @supported_feature_bundle_id.setter
    def supported_feature_bundle_id(self, supported_feature_bundle_id):
        """
        Sets the supported_feature_bundle_id of this FeatureKey.
        The supported Feature Bundle ID. When not in use this value will be zero.

        :param supported_feature_bundle_id: The supported_feature_bundle_id of this FeatureKey.
        :type: int
        """
        self._supported_feature_bundle_id = supported_feature_bundle_id

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
