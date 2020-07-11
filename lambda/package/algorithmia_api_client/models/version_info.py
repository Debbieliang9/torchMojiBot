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


class VersionInfo(object):
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
        'semantic_version': 'str',
        'git_hash': 'str',
        'release_notes': 'str',
        'sample_input': 'str',
        'sample_output': 'str'
    }

    attribute_map = {
        'semantic_version': 'semantic_version',
        'git_hash': 'git_hash',
        'release_notes': 'release_notes',
        'sample_input': 'sample_input',
        'sample_output': 'sample_output'
    }

    def __init__(self, semantic_version=None, git_hash=None, release_notes=None, sample_input=None, sample_output=None):  # noqa: E501
        """VersionInfo - a model defined in OpenAPI"""  # noqa: E501

        self._semantic_version = None
        self._git_hash = None
        self._release_notes = None
        self._sample_input = None
        self._sample_output = None
        self.discriminator = None

        if semantic_version is not None:
            self.semantic_version = semantic_version
        if git_hash is not None:
            self.git_hash = git_hash
        if release_notes is not None:
            self.release_notes = release_notes
        if sample_input is not None:
            self.sample_input = sample_input
        if sample_output is not None:
            self.sample_output = sample_output

    @property
    def semantic_version(self):
        """Gets the semantic_version of this VersionInfo.  # noqa: E501


        :return: The semantic_version of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._semantic_version

    @semantic_version.setter
    def semantic_version(self, semantic_version):
        """Sets the semantic_version of this VersionInfo.


        :param semantic_version: The semantic_version of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._semantic_version = semantic_version

    @property
    def git_hash(self):
        """Gets the git_hash of this VersionInfo.  # noqa: E501


        :return: The git_hash of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._git_hash

    @git_hash.setter
    def git_hash(self, git_hash):
        """Sets the git_hash of this VersionInfo.


        :param git_hash: The git_hash of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._git_hash = git_hash

    @property
    def release_notes(self):
        """Gets the release_notes of this VersionInfo.  # noqa: E501


        :return: The release_notes of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this VersionInfo.


        :param release_notes: The release_notes of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def sample_input(self):
        """Gets the sample_input of this VersionInfo.  # noqa: E501


        :return: The sample_input of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._sample_input

    @sample_input.setter
    def sample_input(self, sample_input):
        """Sets the sample_input of this VersionInfo.


        :param sample_input: The sample_input of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._sample_input = sample_input

    @property
    def sample_output(self):
        """Gets the sample_output of this VersionInfo.  # noqa: E501


        :return: The sample_output of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._sample_output

    @sample_output.setter
    def sample_output(self, sample_output):
        """Sets the sample_output of this VersionInfo.


        :param sample_output: The sample_output of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._sample_output = sample_output

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
        if not isinstance(other, VersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
