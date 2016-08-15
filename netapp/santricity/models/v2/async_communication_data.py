# coding: utf-8

"""
AsyncCommunicationData.py

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


class AsyncCommunicationData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsyncCommunicationData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timeout': 'int',  # (required parameter)
            'return_status': 'str',  # (required parameter)
            'successful': 'bool',  # (required parameter)
            'controller_ref': 'str',  # (required parameter)
            'amg_ref': 'str',  # (required parameter)
            'test_type': 'str',  # (required parameter)
            'bw_test_result': 'AsyncMirrorGroupLinkBandwidthTestResults',  # (required parameter)
            'lat_test_result': 'AsyncMirrorGroupLinkLatencyTestResults'
        }

        self.attribute_map = {
            'timeout': 'timeout',  # (required parameter)
            'return_status': 'returnStatus',  # (required parameter)
            'successful': 'successful',  # (required parameter)
            'controller_ref': 'controllerRef',  # (required parameter)
            'amg_ref': 'amgRef',  # (required parameter)
            'test_type': 'testType',  # (required parameter)
            'bw_test_result': 'bwTestResult',  # (required parameter)
            'lat_test_result': 'latTestResult'
        }

        self._timeout = None
        self._return_status = None
        self._successful = None
        self._controller_ref = None
        self._amg_ref = None
        self._test_type = None
        self._bw_test_result = None
        self._lat_test_result = None

    @property
    def timeout(self):
        """
        Gets the timeout of this AsyncCommunicationData.


        :return: The timeout of this AsyncCommunicationData.
        :rtype: int
        :required/optional: required
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this AsyncCommunicationData.


        :param timeout: The timeout of this AsyncCommunicationData.
        :type: int
        """
        self._timeout = timeout

    @property
    def return_status(self):
        """
        Gets the return_status of this AsyncCommunicationData.


        :return: The return_status of this AsyncCommunicationData.
        :rtype: str
        :required/optional: required
        """
        return self._return_status

    @return_status.setter
    def return_status(self, return_status):
        """
        Sets the return_status of this AsyncCommunicationData.


        :param return_status: The return_status of this AsyncCommunicationData.
        :type: str
        """
        allowed_values = ["uninitialized", "ok", "error", "busy", "illegalParam", "noHeap", "driveNotExist", "driveNotUnassigned", "noSparesAssigned", "someSparesAssigned", "volumeNotExist", "volumeReconfiguring", "notDualActive", "tryAlternate", "background", "notImplemented", "reservationConflict", "volumeDead", "internalError", "invalidRequest", "iconFailure", "volumeFormatting", "altRemoved", "cacheSyncFailure", "invalidFile", "reconfigSmallDacstore", "reconfigFailure", "nvramError", "flashError", "authFailParam", "authFailPassword", "memParityError", "invalidControllerref", "invalidVolumegroupref", "invalidVolumeref", "invalidDriveref", "invalidFreeextentref", "volumeOffline", "volumeNotOptimal", "modesenseError", "invalidSegmentsize", "invalidCacheblksize", "invalidFlushThreshold", "invalidFlushAmount", "invalidLabel", "invalidCacheModifier", "invalidReadahead", "invalidReconpriority", "invalidScanperiod", "invalidTrayposLength", "invalidRegionid", "invalidFibreid", "invalidEncryption", "invalidRaidlevel", "invalidExpansionList", "noSparesDeassigned", "someSparesDeassigned", "partDupId", "partLabelInvalid", "partNodeNonexistent", "partPortIdInvalid", "partVolumeNonexistent", "partLunCollision", "maxVolMappingExceeded", "partMappingNonexistent", "partNoHostports", "imageTransferred", "fileTooLarge", "invalidOffset", "overrun", "invalidChunksize", "invalidTotalsize", "downloadNotPermitted", "spawnError", "voltransferError", "invalidDlstate", "cacheconfigError", "downloadInProgress", "driveNotOptimal", "driveRemoved", "duplicateDrives", "numdrivesAdditional", "numdrivesGroup", "driveTooSmall", "capacityConstrained", "maxVolumesExceeded", "partIsUtmLun", "someSparesTooSmall", "sparesSmallUnassigned", "tooManyPartitions", "parityScanInProgress", "invalidSafeId", "invalidSafeKey", "invalidSafeCapability", "invalidSafeVersion", "partitionsDisabled", "driveDownloadFailed", "esmDownloadFailed", "esmPartialUpdate", "utmConflict", "noVolumes", "authFailReadpassword", "partCrteFailTblFull", "attemptToSetLocal", "invalidHostTypeIndex", "failVolumeVisible", "noDeleteUtmInUse", "invalidLun", "utmTooManyMaps", "diagReadFailure", "diagSrcLinkDown", "diagWriteFailure", "diagLoopbackError", "diagTimeout", "diagInProgress", "diagNoAlt", "diagIconSendErr", "diagInitErr", "diagModeErr", "diagInvalidTestId", "diagDriveErr", "diagLockErr", "diagConfigErr", "diagNoCacheMem", "diagNotQuiesced", "diagUtmNotEnabled", "invalidModeSwitch", "invalidPortname", "duplicateVolMapping", "maxSnapsPerBaseExceeded", "maxSnapsExceeded", "invalidBasevol", "snapNotAvailable", "notDisabled", "snapshotFeatureDisabled", "repositoryOffline", "repositoryReconfiguring", "rollbackInProgress", "numVolumesGroup", "ghostVolume", "repositoryMissing", "invalidRepositoryLabel", "invalidSnapLabel", "invalidRollbackPriority", "invalidWarnThreshold", "cannotMapVolume", "cannotFormatVolume", "dstNotFibre", "repositoryTooSmall", "repositoryFailed", "baseVolumeFailed", "baseVolumeOffline", "baseVolumeFormatting", "metadataVolNonexistent", "rvmFeatureDisabled", "mirrorsPresent", "rvmFeatureDeactivated", "maxMirrorsExceeded", "invalidMirrorCandidateVol", "invalidMirrorvol", "metadataAlreadyExists", "metadataMissing", "metadataOffline", "metadataReconfiguring", "localRoleChangeFailed", "remoteRoleChangeFailed", "localRoleChangeSuccessful", "onlyLocalMirrorDeleted", "noValidMirrorCandidate", "remoteMaxMirrorsExceeded", "remoteRvmFeatureDisabled", "remoteMetadataVolNonexistent", "notRegistered", "remoteInvalidCfgGen", "localRoleChangedNotForced", "remoteRoleChangedLocalFailed", "rvmSpmError", "remoteAuthFailPassword", "rvmVersionMismatch", "rvmRemoteArrayError", "rvmCommunicationError", "rvmFibreError", "mirrorVolNotPrimary", "secNotPromoteable", "priNotDemoteable", "metadataChildDeletion", "rmtvolOrphanDeletion", "rvmActivateDisallowed", "invalidTrayref", "partialDeletion", "defaultUtmCollision", "invalidCopyPriority", "invalidVolumecopyref", "copyChangeFailed", "copyActive", "copyInactive", "copyIncompatibleSource", "copyIncompatibleTarget", "copyGhostSource", "copyGhostTarget", "copyInvalidSourceRef", "copyInvalidTargetRef", "copyInvalidSourceState", "copyInvalidTargetState", "copySourceReconfig", "copyTargetReconfig", "copyTargetTooSmall", "copyTargetLimit", "maxVolumeCopysExceeded", "copySourceReservation", "copyTargetReservation", "copySourceFormat", "copyTargetFormat", "copyStartFailed", "copyStopFailed", "volcopyFeatureDisabled", "writeLock", "cannotReconfigure", "authFailContLockout", "prReservationConflict", "regDeleteFailed", "batteryNotInConfig", "batteryMissing", "noChannel", "rvmOperNotAllowedOnSec", "dataRedundancyRequired", "copySourceZeroCapacity", "invHostlunDefineMapping", "invHostlunMoveMapping", "invHostlunDefineHosttype", "invHostlunMoveHostport", "fwIncompatible", "mirrorAlreadySuspended", "insuffLocalMirRepResources", "insuffRemtMirRepResources", "ghostHasUnreadableSectors", "rvmCommStatRecoveredTimeout", "rvmCommStatRecoveredDelay", "rvmCommStatNotReady", "rvmCommStatTimeout", "rvmCommStatChannelFailure", "rvmCommStatNetworkFailure", "rvmCommStatDeviceMissing", "rvmCommStatLoginRejected", "rvmCommStatLoginFailure", "rvmCommStatInvNumSamplesReqd", "rvmQuiescenceInProgress", "rvmInvalidRemotevol", "sodInProgress", "invalidDrives", "invalidSetid", "invalidSetsize", "missingData", "quiescenceFailed", "validationError", "downloadHalted", "allFailed", "partialOk", "obsolete", "usmClearFailed", "controllerInServiceMode", "invalidDrive", "databaseError", "backgroundAutocfg", "autocfgInprogress", "unsupportedLhaSataEsm", "parityScanFailed", "parityRepairFailed", "mediaRepairFailed", "mirrorDegraded", "prohibitedByMdtRestrictions", "prohibitedByGoldKeyRestrictions", "safeControllerNotSubjectToGoldKey", "safeMdtNotPremiumFeature", "alarmNotPresent", "dltNotCompleted", "dependancyError", "cdmDatabaseFull", "requiredConditionNotPresent", "ddcUnavail", "ddcIllegalParam", "invalidDdcTag", "hosttypeConflict", "portConflict", "invalidHosttypeString", "invalidProtocol", "portRemoved", "disableNotPermitted", "prohibitedByDriveTrayLimit", "invalidEsmref", "invalidBundleMigration", "invalidBundleKey", "noSparesNeeded", "prohibitedByFeatureBundleViolation", "invalidAuthMethod", "invalidSecret", "secretAlreadyInUse", "manualConfigModeSet", "noIscsiSessions", "invalidInterfaceref", "initiatorConflict", "initiatorRemoved", "basevolSizeChanged", "volumeGroupNotExist", "volumeGroupNotOnline", "volumeGroupHasHotspare", "volumeGroupReconfiguring", "volumeGroupStateNotValid", "controllerNotOptimal", "insufficientCapacity", "volumeGroupExported", "volumeNotConfigurable", "volumeGroupNotConfigurable", "invalidDriveState", "volumeGroupReconstructing", "volumeGroupUndergoingCopyback", "volumeGroupNotComplete", "volumeGroupHasFailedDrives", "volumeGroupHasNonOptimalVols", "volumeGroupHasMirrorRelationship", "volumeGroupHasVolcopyRelationship", "volumeGroupHasMirroringMetadata", "volumeGroupHasMappedVols", "volumeGroupHasReservations", "volumeGroupHasIncompatibleDacstores", "volumeLimitExceeded", "volumeGroupHasUnknownRaidLevel", "volumeGroupHasUnsupportedRaidLevel", "volumeGroupHasCloneOpportunity", "volumeGroupHasInsufficientDrives", "volumeGroupHasFailedVols", "perfTierSafeUpgradeDisabled", "raid6FeatureUnsupported", "raid6FeatureDisabled", "safeControllerNotSubjectToRaid6", "volumeGroupNotContingent", "channelDiagsRunning", "channelDiagsResultsPartial", "volumeGroupHasSnapshotRelationship", "prohibitedBySafeViolation", "legacyVg", "vgNotForceable", "channelDiagsLockErr", "channelDiagsNotQuiesced", "channelDiagsAltCommFailed", "channelDiagsChanSetupFailed", "channelDiagsDeviceBypassFailed", "channelDiagsResultsNotAvailable", "driveSpinUpError", "driveTypeMismatch", "localRemoteArrayHasSameWwn", "volumeGroupHasIncompatibleDrive", "volumeGroupVolumeEncroachesOnDacstore", "volumeGroupImportInProgress", "drivesNeedToBeSpunUp", "noNativeSstor", "noSuchDebugChunk", "debugInfoConfigChanged", "lockdown", "drivesDacstoresOverlap", "volumeHasAsyncMirror", "reconfigLogSpaceError", "volumeGroupInaccessible", "volumeInitializing", "insufficientCache", "volumeInaccessible", "noDrivesAdopted", "someDrivesAdopted", "exportingDrivesDatabaseResynchronizing", "exportingDrivesDatabaseFailed", "exportingDrivesQuiesced", "learnActiveTryLater", "noLockedDrives", "driveSecurityEnabledFailed", "lockkeyFailed", "invalidSecurity", "noFdeDrives", "volumeGroupSecure", "invalidBlob", "unlockFailed", "noKeySet", "rekeyInProgress", "defaultHostGroupMappingNotAllowed", "ssdMediaScanNotAllowed", "premiumFeatureLimitExceedsMaximum", "disableEvaluationFeatureNotPermitted", "requestFailedDueToLun0Restrictions", "externalKmsEnabled", "externalKmsFailed", "externalKmsNotEnabled", "keyNotNeeded", "keyInvalidSequence", "diagNotRunning", "ctrlNotInServiceMode", "invalidFeatureref", "cacheBackupDevNotExist", "noMatchingLockKeyIdFound", "lockKeyValidationFailed", "lockKeyValidationDisabled", "externalKmsNotCompliant", "externalKmsTimeout", "cannotDisableNoKey", "previouslyEnabledForEval", "featureNotKeyable", "evalNotSupported", "rawdataTransferBadType", "rawdataTransferNotStarted", "rawdataTransferAlreadyStarted", "rawdataTransferPreparing", "rawdataTransferReadError", "rawdataTransferNoDrives", "rawdataTransferInvalidImage", "rawdataTransferCrcError", "dbmRestoreWriteError", "dbmRestoreNoDrives", "rawdataBadSeqNum", "invalidCapability", "externalKeyNotInMemory", "invalidLockKeyId", "invalidProtection", "volumeHasSnapshotRelationship", "volumeHasMirrorRelationship", "externalKmsDisabledNoKey", "dbmRestoreAltCtlNotOffline", "copyApptagMismatch", "invalidRequestForEnclosure", "dqRetrieveNothingToTransfer", "invalidIscsiConfiguration", "volumeHasVolcopyRelationship", "partPiIncapable", "requestFailedDueToPiRestrictions", "rawdataTransferUserCancelled", "duplicateIscsiIpAddress", "portSpeedConflict", "factoryDefaultDownloadFailed", "errorWritingToEeprom", "factoryDefaultPartialUpdate", "snapshotNotActive", "cannotRollback", "mirrorSyncNotPossible", "psuFirmwareDownloadFailed", "psuFirmwareUpdateMfgDeviceCodeMismatch", "psuFirmwareUpdateNotAllRedundant", "psuFirmwareUpdateNotAllOptimal", "insufficientRepositoryCapacity", "rollbackStartFailure", "csbReserveFailed", "csbReleaseFailedNoLock", "csbReleaseFailedInvalidKey", "flashcacheAlreadyExists", "flashcacheFeatureDisabled", "flashcacheAlreadySuspended", "flashcacheNotSuspended", "flashcacheInvalidConfigType", "invalidPitGroupLabel", "invalidPitConsistencyGroupLabel", "invalidPitAutoDeleteLimit", "invalidPitRepositoryFullPolicy", "invalidConcatVolMemberLabel", "concatVolMemberTooSmall", "invalidPitGroupRef", "invalidPitRef", "dveNotAllowed", "dssNotAllowed", "dplCoreDumpInvalidTag", "invalidPitViewLabel", "invalidPitViewRef", "invalidConcatVolRef", "notFlashcacheVol", "flashcacheDeleted", "flashcacheEnabled", "flashcacheNotEnabled", "noRepDeletion", "maxPitsPerGroupExceeded", "maxPitsExceeded", "maxPitGroupsPerBaseExceeded", "maxPitGroupsExceeded", "maxViewsPerPitExceeded", "maxViewsExceeded", "maxConsistencyGroupsExceeded", "maxConsistencyGroupMembersExceeded", "maxMappableVolumesExceeded", "notOldestPit", "viewStopped", "concatMemberLimitExceeded", "invalidMemberVol", "memberVolMapped", "invalidMemberVolState", "invalidTrimCount", "pitGroupInConsistencyGroup", "pitInConsistencyGroup", "pitViewInConsistencyGroup", "incompatibleMemberVol", "volumeInUse", "rvmOverIscsiNotSupported", "arvmGroupUserLabelExists", "arvmGroupDoesNotExist", "arvmGroupNotEmpty", "concatVolumeFailed", "invalidPitConsistencyGroupRef", "invalidPitConsistencyGroupViewRef", "invalidPitConsistencyGroupViewLabel", "alternateRequiredForOperation", "invalidPitForView", "consistencyGroupArvmBindingConflict", "attributeFixedByArvm", "operationFailedVolumeCopyClone", "pitCreatePending", "dbmDbSourceUnavailable", "dbmRestoreSourceMismatch", "invalidCriticalThreshold", "volumeGroupHasArvmRelationship", "arvmRecoveryPointDeletionRequired", "volumeGroupHasPitgroupRelationship", "volumeGroupHasPitviewRelationship", "volumeGroupHasConcatRelationship", "flashcacheSuspended", "flashcacheAlreadyEnabled", "dbmDbImageCorrupt", "illegalVolume", "invalidRepositoryCapacity", "invalidProvisionedCapacityQuota", "invalidExpansionPolicy", "invalidVirtualCapacity", "cannotExpandConcatMember", "thresholdBelowUsedCapacity", "invalidExpansionOperation", "repositoryFull", "insufficientExpansionSpace", "invalidExpansionSize", "invalidReinitAction", "invalidReinitCapacity", "invalidIncompleteMemberRef", "arvmGroupNotPrimary", "arvmGroupNotSecondary", "arvmMemberFailed", "arvmGroupNotSuspended", "arvmInvalidMirrorState", "arvmVolumeAlreadyInMirrorRelationship", "arvmMemberLimitExceeded", "arvmSuspendFailure", "arvmResumeFailure", "arvmSynchronizeFailure", "remoteTargetNotFound", "arvmMirrorMemberDoesNotExist", "snapConversionTooManySnaps", "snapConversionMissingLabel", "arvmFeatureDeactivated", "incompatibleRepositorySecurity", "incompatibleSecondarySecurity", "mirrorProtocolMismatch", "arvmAsyncMirrorGroupPresent", "cacheParametersNotChangeable", "flashcacheMaxCapacityExceeded", "flashcacheFailed", "dplCoreDumpRestoreInProgress", "arvmGroupHasIncompleteMember", "arvmConnectivityTestAlreadyInProgress", "arvmConnectivityTestNetworkError", "arvmConnectivityTestRemoteTimeout", "arvmConnectivityTestLoginFailure", "arvmConnectivityTestNameServiceError", "arvmConnectivityTestTurError", "arvmConnectivityTestMissingRemoteAmg", "arvmConnectivityTestAmgMemberMismatch", "invalidSyncPriority", "invalidRecoveryPointAlertThreshold", "invalidSyncAlertThreshold", "mustSpecifyExistingVolumes", "arvmConnectivityTestTimeoutExceeded", "flashcacheMaxLimitExceeded", "volsInVgUsingNonSecureCapableFlashcache", "volsInVgUsingSecureDisabledFlashcache", "invalidSubmodelId", "premiumFeatureLimitMismatch", "volumeGroupNotImportable", "primaryCacheSizeMismatch", "flashcacheUserLabelExists", "maxThinVolumesExceeded", "arvmInvalidSecondaryCapacity", "arvmOnlyPrimaryMemberRemoved", "arvmOnlySecondaryMemberRemoved", "arvmInvalidAmgRequestWhileSuspended", "arvmManualSyncAlreadyInProgress", "arvmManualSyncRetryTooSoon", "diskPoolNotEmpty", "flashCacheInvalidBaseVol", "flashCacheFdeEnablementDisallowed", "remoteArvmFeatureDeactivated", "remoteArvmFeatureDisabled", "arvmOrphanGroup", "arvmOrphanMember", "volumeNotAvailable", "volumeHasUnreadableSectors", "thinProvisioningFeatureDisabled", "pitGroupsFeatureDisabled", "exceedDiskPoolLimit", "flashcacheDegradedState", "flashcacheNonDaCapableDriveDisallowed", "arvmMaxAsyncMirrorGroupsExceeded", "arvmMaxMirrorsPerArrayExceeded", "maxTotalMirrorsPerArrayExceeded", "exceedDiskPoolCapacity", "exceedMaxVolumeCapacity", "arvmRemoteMaxAsyncMirrorGroupsExceeded", "arvmRemoteMaxMirrorsPerArrayExceeded", "remoteMaxTotalMirrorsPerArrayExceeded", "arvmInvalidSyncInterval", "remoteNoHeap", "remoteInternalError", "remoteRvmSpmError", "arvmRemoteMirrorMemberDoesNotExist", "arvmRemoteGroupUserLabelExists", "arvmRemoteGroupNotSecondary", "arvmRemoteGroupDoesNotExist", "remoteInvalidProtection", "remoteDatabaseError", "arvmRemoteGroupNotEmpty", "arvmRemoteSuspendFailure", "arvmRemoteResumeFailure", "arvmRemoteSynchronizeFailure", "flashcacheInvalidAnalyticsState", "arvmExpansionSynchronizationInProgress", "arvmRemoteExpansionSynchronizationInProgress", "faultConditionStillExists", "remoteTryAlternate", "arvmOnlyLocalAmgDeleted", "arvmRoleChangePending", "arvmRoleChangeInProgress", "arvmMemberStopped", "reconstructionInProgress", "copybackInProgress", "adminPasswordNotSet", "keyDoesNotExist", "takeRecoveryActionsFirst", "coredumpBackupInProgress", "legacyRvmAsyncModeUnsupported", "arvmIncorrectVolumeType", "thinVolumeParametersCannotBeModified", "arvmRemoteThinNotSupported", "snmpInvalidCommunityName", "snmpInvalidCommunityPermission", "snmpInvalidCommunityRef", "snmpInvalidTrapDestinationRef", "invalidIpAddress", "snmpMaxCommunitiesExceeded", "snmpMaxTrapDestinationsExceeded", "snmpCommunityNameInUse", "snmpTrapDestinationAddressInUse", "snmpUnknownSystemVariable", "snmpInvalidSystemVariableValue", "snmpIncompatibleFirmware", "snmpAgentDisabled", "snmpAgentInitFailed", "arvmThinVolInitError", "arvmRemoteThinVolInitError", "snmpIncompatibleIpv4Address", "snmpIncompatibleIpv6Address", "drivesNotAvailableForRemoval", "snmpCannotDisableIpv4", "snmpCannotDisableIpv6", "snmpIpv4ConfigError", "iocDumpInProgress", "iocRestoreInProgress", "iocDumpInvalidTag", "unsupportedEsmRequest", "isnsDhcpNotSupported", "dpcVolumeGroupNotRedundant", "dpcVolumeNotInitialized", "dpcExclusiveOperationActive", "dpcUnableToPowerUpDrive", "dpcFormatActive", "dpcUnreadableSectorsPresent", "dpcPowerCycleAlreadyInProgress", "dpcEnclosureHardwareUnsupported", "dpcEnclosureFwDownlevel", "evacInProgress", "noEvacFound", "noHotspareAvailable", "driveServiceInProgress", "hdd4kbSegmentsizeNotAllowed", "diskPoolNoSpareDrives", "diskPoolExceedSpareCapacity", "autoLoadBalanceUserDisabled", "autoLoadBalanceInsufficientStatistics", "invalidLoadBalanceAction", "invalidLoadBalanceDelay", "reservedAddress", "volumeCreationInProgress", "keyValueTagInvalidRef", "keyValueTagInvalidDuplicate", "keyValueTagInUse", "workloadInvalidRef", "invalidKeyValueTagObjectReference", "mappingInvalidDuplicate", "downloadCompleteNoReboot", "downloadCompleteMswOnlyReboot", "workloadInvalidDuplicate", "mappingInvalidRef", "workloadInUse", "__UNDEFINED"]
        if return_status not in allowed_values:
            raise ValueError(
                "Invalid value for `return_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._return_status = return_status

    @property
    def successful(self):
        """
        Gets the successful of this AsyncCommunicationData.


        :return: The successful of this AsyncCommunicationData.
        :rtype: bool
        :required/optional: required
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this AsyncCommunicationData.


        :param successful: The successful of this AsyncCommunicationData.
        :type: bool
        """
        self._successful = successful

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this AsyncCommunicationData.


        :return: The controller_ref of this AsyncCommunicationData.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this AsyncCommunicationData.


        :param controller_ref: The controller_ref of this AsyncCommunicationData.
        :type: str
        """
        self._controller_ref = controller_ref

    @property
    def amg_ref(self):
        """
        Gets the amg_ref of this AsyncCommunicationData.


        :return: The amg_ref of this AsyncCommunicationData.
        :rtype: str
        :required/optional: required
        """
        return self._amg_ref

    @amg_ref.setter
    def amg_ref(self, amg_ref):
        """
        Sets the amg_ref of this AsyncCommunicationData.


        :param amg_ref: The amg_ref of this AsyncCommunicationData.
        :type: str
        """
        self._amg_ref = amg_ref

    @property
    def test_type(self):
        """
        Gets the test_type of this AsyncCommunicationData.


        :return: The test_type of this AsyncCommunicationData.
        :rtype: str
        :required/optional: required
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """
        Sets the test_type of this AsyncCommunicationData.


        :param test_type: The test_type of this AsyncCommunicationData.
        :type: str
        """
        allowed_values = ["connectivityTestUnknown", "basicConnectivityTest", "linkLatencyTest", "linkBandwidthTest", "__UNDEFINED"]
        if test_type not in allowed_values:
            raise ValueError(
                "Invalid value for `test_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._test_type = test_type

    @property
    def bw_test_result(self):
        """
        Gets the bw_test_result of this AsyncCommunicationData.


        :return: The bw_test_result of this AsyncCommunicationData.
        :rtype: AsyncMirrorGroupLinkBandwidthTestResults
        :required/optional: required
        """
        return self._bw_test_result

    @bw_test_result.setter
    def bw_test_result(self, bw_test_result):
        """
        Sets the bw_test_result of this AsyncCommunicationData.


        :param bw_test_result: The bw_test_result of this AsyncCommunicationData.
        :type: AsyncMirrorGroupLinkBandwidthTestResults
        """
        self._bw_test_result = bw_test_result

    @property
    def lat_test_result(self):
        """
        Gets the lat_test_result of this AsyncCommunicationData.


        :return: The lat_test_result of this AsyncCommunicationData.
        :rtype: AsyncMirrorGroupLinkLatencyTestResults
        :required/optional: required
        """
        return self._lat_test_result

    @lat_test_result.setter
    def lat_test_result(self, lat_test_result):
        """
        Sets the lat_test_result of this AsyncCommunicationData.


        :param lat_test_result: The lat_test_result of this AsyncCommunicationData.
        :type: AsyncMirrorGroupLinkLatencyTestResults
        """
        self._lat_test_result = lat_test_result

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

