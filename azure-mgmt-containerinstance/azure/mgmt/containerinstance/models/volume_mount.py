# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VolumeMount(Model):
    """The properties of the volume mount.

    :param name: The name of the volume mount.
    :type name: str
    :param mount_path: The path within the container where the volume should
     be mounted. Must not contain colon (:).
    :type mount_path: str
    :param read_only: The flag indicating whether the volume mount is
     read-only.
    :type read_only: bool
    """

    _validation = {
        'name': {'required': True},
        'mount_path': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'mount_path': {'key': 'mountPath', 'type': 'str'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
    }

    def __init__(self, name, mount_path, read_only=None):
        super(VolumeMount, self).__init__()
        self.name = name
        self.mount_path = mount_path
        self.read_only = read_only
