# coding: utf-8

"""
PremiumFeature.py

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


class PremiumFeature(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PremiumFeature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capability': 'str',  # (required parameter)
            'is_enabled': 'bool',  # (required parameter)
            'is_compliant': 'bool',  # (required parameter)
            'is_within_limits': 'bool',  # (required parameter)
            'feature_id': 'str'
        }

        self.attribute_map = {
            'capability': 'capability',  # (required parameter)
            'is_enabled': 'isEnabled',  # (required parameter)
            'is_compliant': 'isCompliant',  # (required parameter)
            'is_within_limits': 'isWithinLimits',  # (required parameter)
            'feature_id': 'featureId'
        }

        self._capability = None
        self._is_enabled = None
        self._is_compliant = None
        self._is_within_limits = None
        self._feature_id = None

    @property
    def capability(self):
        """
        Gets the capability of this PremiumFeature.
        This field will contain the value of the premium feature being described.

        :return: The capability of this PremiumFeature.
        :rtype: str
        :required/optional: required
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """
        Sets the capability of this PremiumFeature.
        This field will contain the value of the premium feature being described.

        :param capability: The capability of this PremiumFeature.
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
    def is_enabled(self):
        """
        Gets the is_enabled of this PremiumFeature.
        A true value in this field indicates that the feature is enabled (regardless of compliance)

        :return: The is_enabled of this PremiumFeature.
        :rtype: bool
        :required/optional: required
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this PremiumFeature.
        A true value in this field indicates that the feature is enabled (regardless of compliance)

        :param is_enabled: The is_enabled of this PremiumFeature.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_compliant(self):
        """
        Gets the is_compliant of this PremiumFeature.
        A true value in this field indicates that the feature has been purchased (in compliance). A false value indicates that the feature has not been purchased. The user will receive warning messages indicating that they are not in compliance. The warning message will continue until the feature is purchased or the feature is disabled.

        :return: The is_compliant of this PremiumFeature.
        :rtype: bool
        :required/optional: required
        """
        return self._is_compliant

    @is_compliant.setter
    def is_compliant(self, is_compliant):
        """
        Sets the is_compliant of this PremiumFeature.
        A true value in this field indicates that the feature has been purchased (in compliance). A false value indicates that the feature has not been purchased. The user will receive warning messages indicating that they are not in compliance. The warning message will continue until the feature is purchased or the feature is disabled.

        :param is_compliant: The is_compliant of this PremiumFeature.
        :type: bool
        """
        self._is_compliant = is_compliant

    @property
    def is_within_limits(self):
        """
        Gets the is_within_limits of this PremiumFeature.
        A true value in this field indicates that the feature has been purchased and the subsystem configuration does not exceed the feature options specified at purchase. A false value in this field indicates that the feature has been purchased but new subsystem configuration has caused the user to exceed the feature options that were purchased. The user will receive warning messages indicating that they are no longer in compliance. The user can change the subsystem configuration so that it is in compliance with feature options or the user can purchase additional feature options so that the subsystem is again in compliance. The warning messages will continue until the feature is again in compliance or is disabled.

        :return: The is_within_limits of this PremiumFeature.
        :rtype: bool
        :required/optional: required
        """
        return self._is_within_limits

    @is_within_limits.setter
    def is_within_limits(self, is_within_limits):
        """
        Sets the is_within_limits of this PremiumFeature.
        A true value in this field indicates that the feature has been purchased and the subsystem configuration does not exceed the feature options specified at purchase. A false value in this field indicates that the feature has been purchased but new subsystem configuration has caused the user to exceed the feature options that were purchased. The user will receive warning messages indicating that they are no longer in compliance. The user can change the subsystem configuration so that it is in compliance with feature options or the user can purchase additional feature options so that the subsystem is again in compliance. The warning messages will continue until the feature is again in compliance or is disabled.

        :param is_within_limits: The is_within_limits of this PremiumFeature.
        :type: bool
        """
        self._is_within_limits = is_within_limits

    @property
    def feature_id(self):
        """
        Gets the feature_id of this PremiumFeature.
        This field contains the value of the feature ID associated with the feature.

        :return: The feature_id of this PremiumFeature.
        :rtype: str
        :required/optional: required
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """
        Sets the feature_id of this PremiumFeature.
        This field contains the value of the feature ID associated with the feature.

        :param feature_id: The feature_id of this PremiumFeature.
        :type: str
        """
        allowed_values = ["volumesPerPartition", "totalNumberOfVolumes", "storagePartitions", "snapshot", "volumeCopy", "remoteMirroring", "driveTrayExpansion", "mixedDriveTypes", "mgmtApplication", "supportedDrives", "supportedDriveTrays", "performanceTier", "totalNumberOfSnapshots", "totalNumberOfVolCopies", "goldKey", "snapshotsPerVolume", "totalNumberOfMirrors", "raid6", "stateCapture", "sataStrLen", "secureVolume", "protectionInformation", "solidStateDisk", "driveSlotLimit", "fdeProxyKeyManagement", "supportedInterposer", "vendorSupportedDrives", "flashReadCache", "totalNumberOfAsyncMirrorGroups", "totalNumberOfAsyncMirrorsPerGroup", "totalNumberOfArvmMirrorsPerArray", "totalNumberOfPitsPerArray", "pitGroupsPerVolume", "totalNumberOfPitGroups", "pitsPerPitGroup", "memberVolsPerPitConsistencyGroup", "totalNumberOfPitConsistencyGroups", "totalNumberOfPitViews", "totalNumberOfThinVolumesPerArray", "nativeSataDriveSupport", "solidStateDiskLimit", "totalNumberOfRemoteMirrorsPerArray", "asup", "ectSelector", "embeddedSnmpOid", "asupOnDemand", "dacstoreCompatId", "samoaHicProtocol", "targetPortLunMapping", "hildaBaseboardProtocol", "denali2Protocol", "__UNDEFINED"]
        if feature_id not in allowed_values:
            raise ValueError(
                "Invalid value for `feature_id`, must be one of {0}"
                .format(allowed_values)
            )
        self._feature_id = feature_id

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

