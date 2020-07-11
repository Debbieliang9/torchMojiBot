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


class Build(object):
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
        'status': 'str',
        'build_id': 'str',
        'commit_sha': 'str',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'resource_type': 'str',
        'version_info': 'BuildVersionInfo'
    }

    attribute_map = {
        'status': 'status',
        'build_id': 'build_id',
        'commit_sha': 'commit_sha',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'resource_type': 'resource_type',
        'version_info': 'version_info'
    }

    def __init__(self, status=None, build_id=None, commit_sha=None, started_at=None, finished_at=None, resource_type=None, version_info=None):  # noqa: E501
        """Build - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._build_id = None
        self._commit_sha = None
        self._started_at = None
        self._finished_at = None
        self._resource_type = None
        self._version_info = None
        self.discriminator = None

        self.status = status
        self.build_id = build_id
        self.commit_sha = commit_sha
        self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if resource_type is not None:
            self.resource_type = resource_type
        if version_info is not None:
            self.version_info = version_info

    @property
    def status(self):
        """Gets the status of this Build.  # noqa: E501


        :return: The status of this Build.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Build.


        :param status: The status of this Build.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["in-progress", "succeeded", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def build_id(self):
        """Gets the build_id of this Build.  # noqa: E501


        :return: The build_id of this Build.  # noqa: E501
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this Build.


        :param build_id: The build_id of this Build.  # noqa: E501
        :type: str
        """
        if build_id is None:
            raise ValueError("Invalid value for `build_id`, must not be `None`")  # noqa: E501

        self._build_id = build_id

    @property
    def commit_sha(self):
        """Gets the commit_sha of this Build.  # noqa: E501


        :return: The commit_sha of this Build.  # noqa: E501
        :rtype: str
        """
        return self._commit_sha

    @commit_sha.setter
    def commit_sha(self, commit_sha):
        """Sets the commit_sha of this Build.


        :param commit_sha: The commit_sha of this Build.  # noqa: E501
        :type: str
        """
        if commit_sha is None:
            raise ValueError("Invalid value for `commit_sha`, must not be `None`")  # noqa: E501

        self._commit_sha = commit_sha

    @property
    def started_at(self):
        """Gets the started_at of this Build.  # noqa: E501


        :return: The started_at of this Build.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Build.


        :param started_at: The started_at of this Build.  # noqa: E501
        :type: datetime
        """
        if started_at is None:
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this Build.  # noqa: E501


        :return: The finished_at of this Build.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Build.


        :param finished_at: The finished_at of this Build.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def resource_type(self):
        """Gets the resource_type of this Build.  # noqa: E501


        :return: The resource_type of this Build.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Build.


        :param resource_type: The resource_type of this Build.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def version_info(self):
        """Gets the version_info of this Build.  # noqa: E501


        :return: The version_info of this Build.  # noqa: E501
        :rtype: BuildVersionInfo
        """
        return self._version_info

    @version_info.setter
    def version_info(self, version_info):
        """Sets the version_info of this Build.


        :param version_info: The version_info of this Build.  # noqa: E501
        :type: BuildVersionInfo
        """

        self._version_info = version_info

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
        if not isinstance(other, Build):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
