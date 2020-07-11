# coding: utf-8

"""
    Algorithmia Management APIs

    APIs for managing actions on the Algorithmia platform  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: support@algorithmia.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SettingsMandatory(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source_control_management_system': 'SourceControlManagementSystem',
        'source_visibility': 'SourceVisibility',
        'language': 'Language',
        'environment': 'Environment',
        'package_set': 'str',
        'license': 'License',
        'royalty_microcredits': 'int',
        'network_access': 'NetworkAccess',
        'pipeline_enabled': 'bool'
    }

    attribute_map = {
        'source_control_management_system': 'source_control_management_system',
        'source_visibility': 'source_visibility',
        'language': 'language',
        'environment': 'environment',
        'package_set': 'package_set',
        'license': 'license',
        'royalty_microcredits': 'royalty_microcredits',
        'network_access': 'network_access',
        'pipeline_enabled': 'pipeline_enabled'
    }

    def __init__(self, source_control_management_system=None, source_visibility=None, language=None, environment=None, package_set=None, license=None, royalty_microcredits=None, network_access=None, pipeline_enabled=None):  # noqa: E501
        """SettingsMandatory - a model defined in OpenAPI"""  # noqa: E501

        self._source_control_management_system = None
        self._source_visibility = None
        self._language = None
        self._environment = None
        self._package_set = None
        self._license = None
        self._royalty_microcredits = None
        self._network_access = None
        self._pipeline_enabled = None
        self.discriminator = None

        if source_control_management_system is not None:
            self.source_control_management_system = source_control_management_system
        self.source_visibility = source_visibility
        if language is not None:
            self.language = language
        if environment is not None:
            self.environment = environment
        if package_set is not None:
            self.package_set = package_set
        self.license = license
        if royalty_microcredits is not None:
            self.royalty_microcredits = royalty_microcredits
        self.network_access = network_access
        self.pipeline_enabled = pipeline_enabled

    @property
    def source_control_management_system(self):
        """Gets the source_control_management_system of this SettingsMandatory.  # noqa: E501


        :return: The source_control_management_system of this SettingsMandatory.  # noqa: E501
        :rtype: SourceControlManagementSystem
        """
        return self._source_control_management_system

    @source_control_management_system.setter
    def source_control_management_system(self, source_control_management_system):
        """Sets the source_control_management_system of this SettingsMandatory.


        :param source_control_management_system: The source_control_management_system of this SettingsMandatory.  # noqa: E501
        :type: SourceControlManagementSystem
        """

        self._source_control_management_system = source_control_management_system

    @property
    def source_visibility(self):
        """Gets the source_visibility of this SettingsMandatory.  # noqa: E501


        :return: The source_visibility of this SettingsMandatory.  # noqa: E501
        :rtype: SourceVisibility
        """
        return self._source_visibility

    @source_visibility.setter
    def source_visibility(self, source_visibility):
        """Sets the source_visibility of this SettingsMandatory.


        :param source_visibility: The source_visibility of this SettingsMandatory.  # noqa: E501
        :type: SourceVisibility
        """
        if source_visibility is None:
            raise ValueError("Invalid value for `source_visibility`, must not be `None`")  # noqa: E501

        self._source_visibility = source_visibility

    @property
    def language(self):
        """Gets the language of this SettingsMandatory.  # noqa: E501


        :return: The language of this SettingsMandatory.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SettingsMandatory.


        :param language: The language of this SettingsMandatory.  # noqa: E501
        :type: Language
        """

        self._language = language

    @property
    def environment(self):
        """Gets the environment of this SettingsMandatory.  # noqa: E501


        :return: The environment of this SettingsMandatory.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this SettingsMandatory.


        :param environment: The environment of this SettingsMandatory.  # noqa: E501
        :type: Environment
        """

        self._environment = environment

    @property
    def package_set(self):
        """Gets the package_set of this SettingsMandatory.  # noqa: E501


        :return: The package_set of this SettingsMandatory.  # noqa: E501
        :rtype: str
        """
        return self._package_set

    @package_set.setter
    def package_set(self, package_set):
        """Sets the package_set of this SettingsMandatory.


        :param package_set: The package_set of this SettingsMandatory.  # noqa: E501
        :type: str
        """

        self._package_set = package_set

    @property
    def license(self):
        """Gets the license of this SettingsMandatory.  # noqa: E501


        :return: The license of this SettingsMandatory.  # noqa: E501
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this SettingsMandatory.


        :param license: The license of this SettingsMandatory.  # noqa: E501
        :type: License
        """
        if license is None:
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def royalty_microcredits(self):
        """Gets the royalty_microcredits of this SettingsMandatory.  # noqa: E501


        :return: The royalty_microcredits of this SettingsMandatory.  # noqa: E501
        :rtype: int
        """
        return self._royalty_microcredits

    @royalty_microcredits.setter
    def royalty_microcredits(self, royalty_microcredits):
        """Sets the royalty_microcredits of this SettingsMandatory.


        :param royalty_microcredits: The royalty_microcredits of this SettingsMandatory.  # noqa: E501
        :type: int
        """
        if royalty_microcredits is not None and royalty_microcredits < 0:  # noqa: E501
            raise ValueError("Invalid value for `royalty_microcredits`, must be a value greater than or equal to `0`")  # noqa: E501

        self._royalty_microcredits = royalty_microcredits

    @property
    def network_access(self):
        """Gets the network_access of this SettingsMandatory.  # noqa: E501


        :return: The network_access of this SettingsMandatory.  # noqa: E501
        :rtype: NetworkAccess
        """
        return self._network_access

    @network_access.setter
    def network_access(self, network_access):
        """Sets the network_access of this SettingsMandatory.


        :param network_access: The network_access of this SettingsMandatory.  # noqa: E501
        :type: NetworkAccess
        """
        if network_access is None:
            raise ValueError("Invalid value for `network_access`, must not be `None`")  # noqa: E501

        self._network_access = network_access

    @property
    def pipeline_enabled(self):
        """Gets the pipeline_enabled of this SettingsMandatory.  # noqa: E501


        :return: The pipeline_enabled of this SettingsMandatory.  # noqa: E501
        :rtype: bool
        """
        return self._pipeline_enabled

    @pipeline_enabled.setter
    def pipeline_enabled(self, pipeline_enabled):
        """Sets the pipeline_enabled of this SettingsMandatory.


        :param pipeline_enabled: The pipeline_enabled of this SettingsMandatory.  # noqa: E501
        :type: bool
        """
        if pipeline_enabled is None:
            raise ValueError("Invalid value for `pipeline_enabled`, must not be `None`")  # noqa: E501

        self._pipeline_enabled = pipeline_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsMandatory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
