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


class DscCompilationJobCreateParameters(Model):
    """The parameters supplied to the create compilation job operation.

    :param configuration: Gets or sets the configuration.
    :type configuration:
     ~azure.mgmt.automation.models.DscConfigurationAssociationProperty
    :param parameters: Gets or sets the parameters of the job.
    :type parameters: dict[str, str]
    :param new_node_configuration_build_version_required: If a new build
     version of NodeConfiguration is required.
    :type new_node_configuration_build_version_required: bool
    :param name: Gets or sets name of the resource.
    :type name: str
    :param location: Gets or sets the location of the resource.
    :type location: str
    :param tags: Gets or sets the tags attached to the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'configuration': {'required': True},
    }

    _attribute_map = {
        'configuration': {'key': 'properties.configuration', 'type': 'DscConfigurationAssociationProperty'},
        'parameters': {'key': 'properties.parameters', 'type': '{str}'},
        'new_node_configuration_build_version_required': {'key': 'properties.newNodeConfigurationBuildVersionRequired', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, configuration, parameters=None, new_node_configuration_build_version_required=None, name=None, location=None, tags=None):
        super(DscCompilationJobCreateParameters, self).__init__()
        self.configuration = configuration
        self.parameters = parameters
        self.new_node_configuration_build_version_required = new_node_configuration_build_version_required
        self.name = name
        self.location = location
        self.tags = tags
