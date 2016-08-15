# coding: utf-8

"""
ExportDependencyTypeData.py

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


class ExportDependencyTypeData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ExportDependencyTypeData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',  # (required parameter)
            'metadata_ref': 'str',  
            'mirror_ref': 'str',  
            'snapshot_ref': 'str',  
            'volcopy_ref': 'str',  
            'amg_member': 'str',  
            'concat_vol': 'str',  
            'pit_group': 'str',  
            'pit_view': 'str'
        }

        self.attribute_map = {
            'type': 'type',  # (required parameter)
            'metadata_ref': 'metadataRef',  
            'mirror_ref': 'mirrorRef',  
            'snapshot_ref': 'snapshotRef',  
            'volcopy_ref': 'volcopyRef',  
            'amg_member': 'amgMember',  
            'concat_vol': 'concatVol',  
            'pit_group': 'pitGroup',  
            'pit_view': 'pitView'
        }

        self._type = None
        self._metadata_ref = None
        self._mirror_ref = None
        self._snapshot_ref = None
        self._volcopy_ref = None
        self._amg_member = None
        self._concat_vol = None
        self._pit_group = None
        self._pit_view = None

    @property
    def type(self):
        """
        Gets the type of this ExportDependencyTypeData.
        This enumeration specifies the types of dependencies that may be identified for a volume belonging to a group that is a candidate to be exported.

        :return: The type of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: required
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExportDependencyTypeData.
        This enumeration specifies the types of dependencies that may be identified for a volume belonging to a group that is a candidate to be exported.

        :param type: The type of this ExportDependencyTypeData.
        :type: str
        """
        allowed_values = ["snapshot", "volumeCopy", "metadata", "mirrorPair", "hostMapping", "persistentReservation", "raid6Support", "asyncMirrorGroupMember", "concatMember", "pitGroup", "pitView", "__UNDEFINED"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def metadata_ref(self):
        """
        Gets the metadata_ref of this ExportDependencyTypeData.
        The identification of a metadata volume that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_METADATA.

        :return: The metadata_ref of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._metadata_ref

    @metadata_ref.setter
    def metadata_ref(self, metadata_ref):
        """
        Sets the metadata_ref of this ExportDependencyTypeData.
        The identification of a metadata volume that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_METADATA.

        :param metadata_ref: The metadata_ref of this ExportDependencyTypeData.
        :type: str
        """
        self._metadata_ref = metadata_ref

    @property
    def mirror_ref(self):
        """
        Gets the mirror_ref of this ExportDependencyTypeData.
        The identification of the mirror pair that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_MIRROR_PAIR.

        :return: The mirror_ref of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._mirror_ref

    @mirror_ref.setter
    def mirror_ref(self, mirror_ref):
        """
        Sets the mirror_ref of this ExportDependencyTypeData.
        The identification of the mirror pair that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_MIRROR_PAIR.

        :param mirror_ref: The mirror_ref of this ExportDependencyTypeData.
        :type: str
        """
        self._mirror_ref = mirror_ref

    @property
    def snapshot_ref(self):
        """
        Gets the snapshot_ref of this ExportDependencyTypeData.
        The identification of a snapshot volume that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_SNAPSHOT.

        :return: The snapshot_ref of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._snapshot_ref

    @snapshot_ref.setter
    def snapshot_ref(self, snapshot_ref):
        """
        Sets the snapshot_ref of this ExportDependencyTypeData.
        The identification of a snapshot volume that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_SNAPSHOT.

        :param snapshot_ref: The snapshot_ref of this ExportDependencyTypeData.
        :type: str
        """
        self._snapshot_ref = snapshot_ref

    @property
    def volcopy_ref(self):
        """
        Gets the volcopy_ref of this ExportDependencyTypeData.
        The identification of a volume copy relationship that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_VOLUME_COPY.

        :return: The volcopy_ref of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._volcopy_ref

    @volcopy_ref.setter
    def volcopy_ref(self, volcopy_ref):
        """
        Sets the volcopy_ref of this ExportDependencyTypeData.
        The identification of a volume copy relationship that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_VOLUME_COPY.

        :param volcopy_ref: The volcopy_ref of this ExportDependencyTypeData.
        :type: str
        """
        self._volcopy_ref = volcopy_ref

    @property
    def amg_member(self):
        """
        Gets the amg_member of this ExportDependencyTypeData.
        The identification of an Async Mirror Group member that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_ASYNC_MIRROR_GROUP_MEMBER.

        :return: The amg_member of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._amg_member

    @amg_member.setter
    def amg_member(self, amg_member):
        """
        Sets the amg_member of this ExportDependencyTypeData.
        The identification of an Async Mirror Group member that is associated with the dependent volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_ASYNC_MIRROR_GROUP_MEMBER.

        :param amg_member: The amg_member of this ExportDependencyTypeData.
        :type: str
        """
        self._amg_member = amg_member

    @property
    def concat_vol(self):
        """
        Gets the concat_vol of this ExportDependencyTypeData.
        This field contains an identification of the Concat Volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_CONCAT_MEMBER.

        :return: The concat_vol of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._concat_vol

    @concat_vol.setter
    def concat_vol(self, concat_vol):
        """
        Sets the concat_vol of this ExportDependencyTypeData.
        This field contains an identification of the Concat Volume. This field is only present if the type field is set to EXPORT_DEPENDENCY_CONCAT_MEMBER.

        :param concat_vol: The concat_vol of this ExportDependencyTypeData.
        :type: str
        """
        self._concat_vol = concat_vol

    @property
    def pit_group(self):
        """
        Gets the pit_group of this ExportDependencyTypeData.
        This field contains an identification of the PiT Group. This field is only present if the type field is set to EXPORT_DEPENDENCY_PIT_GROUP.

        :return: The pit_group of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._pit_group

    @pit_group.setter
    def pit_group(self, pit_group):
        """
        Sets the pit_group of this ExportDependencyTypeData.
        This field contains an identification of the PiT Group. This field is only present if the type field is set to EXPORT_DEPENDENCY_PIT_GROUP.

        :param pit_group: The pit_group of this ExportDependencyTypeData.
        :type: str
        """
        self._pit_group = pit_group

    @property
    def pit_view(self):
        """
        Gets the pit_view of this ExportDependencyTypeData.
        This field contains an identification of the PiT View. This field is only present if the type field is set to EXPORT_DEPENDENCY_PIT_VIEW.

        :return: The pit_view of this ExportDependencyTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._pit_view

    @pit_view.setter
    def pit_view(self, pit_view):
        """
        Sets the pit_view of this ExportDependencyTypeData.
        This field contains an identification of the PiT View. This field is only present if the type field is set to EXPORT_DEPENDENCY_PIT_VIEW.

        :param pit_view: The pit_view of this ExportDependencyTypeData.
        :type: str
        """
        self._pit_view = pit_view

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
