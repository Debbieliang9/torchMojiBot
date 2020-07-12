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


class Settings(object):
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
        'algorithm_callability': 'AlgorithmCallability',
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
        'algorithm_callability': 'algorithm_callability',
        'source_visibility': 'source_visibility',
        'language': 'language',
        'environment': 'environment',
        'package_set': 'package_set',
        'license': 'license',
        'royalty_microcredits': 'royalty_microcredits',
        'network_access': 'network_access',
        'pipeline_enabled': 'pipeline_enabled'
    }

    def __init__(self, algorithm_callability=None, source_visibility=None, language=None, environment=None, package_set=None, license=None, royalty_microcredits=None, network_access=None, pipeline_enabled=None):  # noqa: E501
        """Settings - a model defined in OpenAPI"""  # noqa: E501

        self._algorithm_callability = None
        self._source_visibility = None
        self._language = None
        self._environment = None
        self._package_set = None
        self._license = None
        self._royalty_microcredits = None
        self._network_access = None
        self._pipeline_enabled = None
        self.discriminator = None

        if algorithm_callability is not None:
            self.algorithm_callability = algorithm_callability
        if source_visibility is not None:
            self.source_visibility = source_visibility
        if language is not None:
            self.language = language
        if environment is not None:
            self.environment = environment
        if package_set is not None:
            self.package_set = package_set
        if license is not None:
            self.license = license
        if royalty_microcredits is not None:
            self.royalty_microcredits = royalty_microcredits
        if network_access is not None:
            self.network_access = network_access
        if pipeline_enabled is not None:
            self.pipeline_enabled = pipeline_enabled

    @property
    def algorithm_callability(self):
        """Gets the algorithm_callability of this Settings.  # noqa: E501


        :return: The algorithm_callability of this Settings.  # noqa: E501
        :rtype: AlgorithmCallability
        """
        return self._algorithm_callability

    @algorithm_callability.setter
    def algorithm_callability(self, algorithm_callability):
        """Sets the algorithm_callability of this Settings.


        :param algorithm_callability: The algorithm_callability of this Settings.  # noqa: E501
        :type: AlgorithmCallability
        """

        self._algorithm_callability = algorithm_callability

    @property
    def source_visibility(self):
        """Gets the source_visibility of this Settings.  # noqa: E501


        :return: The source_visibility of this Settings.  # noqa: E501
        :rtype: SourceVisibility
        """
        return self._source_visibility

    @source_visibility.setter
    def source_visibility(self, source_visibility):
        """Sets the source_visibility of this Settings.


        :param source_visibility: The source_visibility of this Settings.  # noqa: E501
        :type: SourceVisibility
        """

        self._source_visibility = source_visibility

    @property
    def language(self):
        """Gets the language of this Settings.  # noqa: E501


        :return: The language of this Settings.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Settings.


        :param language: The language of this Settings.  # noqa: E501
        :type: Language
        """

        self._language = language

    @property
    def environment(self):
        """Gets the environment of this Settings.  # noqa: E501


        :return: The environment of this Settings.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Settings.


        :param environment: The environment of this Settings.  # noqa: E501
        :type: Environment
        """

        self._environment = environment

    @property
    def package_set(self):
        """Gets the package_set of this Settings.  # noqa: E501


        :return: The package_set of this Settings.  # noqa: E501
        :rtype: str
        """
        return self._package_set

    @package_set.setter
    def package_set(self, package_set):
        """Sets the package_set of this Settings.


        :param package_set: The package_set of this Settings.  # noqa: E501
        :type: str
        """

        self._package_set = package_set

    @property
    def license(self):
        """Gets the license of this Settings.  # noqa: E501


        :return: The license of this Settings.  # noqa: E501
        :rtype: License
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Settings.


        :param license: The license of this Settings.  # noqa: E501
        :type: License
        """

        self._license = license

    @property
    def royalty_microcredits(self):
        """Gets the royalty_microcredits of this Settings.  # noqa: E501


        :return: The royalty_microcredits of this Settings.  # noqa: E501
        :rtype: int
        """
        return self._royalty_microcredits

    @royalty_microcredits.setter
    def royalty_microcredits(self, royalty_microcredits):
        """Sets the royalty_microcredits of this Settings.


        :param royalty_microcredits: The royalty_microcredits of this Settings.  # noqa: E501
        :type: int
        """
        if royalty_microcredits is not None and royalty_microcredits < 0:  # noqa: E501
            raise ValueError("Invalid value for `royalty_microcredits`, must be a value greater than or equal to `0`")  # noqa: E501

        self._royalty_microcredits = royalty_microcredits

    @property
    def network_access(self):
        """Gets the network_access of this Settings.  # noqa: E501


        :return: The network_access of this Settings.  # noqa: E501
        :rtype: NetworkAccess
        """
        return self._network_access

    @network_access.setter
    def network_access(self, network_access):
        """Sets the network_access of this Settings.


        :param network_access: The network_access of this Settings.  # noqa: E501
        :type: NetworkAccess
        """

        self._network_access = network_access

    @property
    def pipeline_enabled(self):
        """Gets the pipeline_enabled of this Settings.  # noqa: E501


        :return: The pipeline_enabled of this Settings.  # noqa: E501
        :rtype: bool
        """
        return self._pipeline_enabled

    @pipeline_enabled.setter
    def pipeline_enabled(self, pipeline_enabled):
        """Sets the pipeline_enabled of this Settings.


        :param pipeline_enabled: The pipeline_enabled of this Settings.  # noqa: E501
        :type: bool
        """

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
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other