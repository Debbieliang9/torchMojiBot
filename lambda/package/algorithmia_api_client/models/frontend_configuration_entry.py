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


class FrontendConfigurationEntry(object):
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
        'keyname': 'str',
        'value': 'str',
        'created_at': 'float',
        'updated_at': 'float',
        'resource_type': 'str'
    }

    attribute_map = {
        'keyname': 'keyname',
        'value': 'value',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'resource_type': 'resource_type'
    }

    def __init__(self, keyname=None, value=None, created_at=None, updated_at=None, resource_type=None):  # noqa: E501
        """FrontendConfigurationEntry - a model defined in OpenAPI"""  # noqa: E501

        self._keyname = None
        self._value = None
        self._created_at = None
        self._updated_at = None
        self._resource_type = None
        self.discriminator = None

        self.keyname = keyname
        self.value = value
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.resource_type = resource_type

    @property
    def keyname(self):
        """Gets the keyname of this FrontendConfigurationEntry.  # noqa: E501


        :return: The keyname of this FrontendConfigurationEntry.  # noqa: E501
        :rtype: str
        """
        return self._keyname

    @keyname.setter
    def keyname(self, keyname):
        """Sets the keyname of this FrontendConfigurationEntry.


        :param keyname: The keyname of this FrontendConfigurationEntry.  # noqa: E501
        :type: str
        """
        if keyname is None:
            raise ValueError("Invalid value for `keyname`, must not be `None`")  # noqa: E501

        self._keyname = keyname

    @property
    def value(self):
        """Gets the value of this FrontendConfigurationEntry.  # noqa: E501


        :return: The value of this FrontendConfigurationEntry.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FrontendConfigurationEntry.


        :param value: The value of this FrontendConfigurationEntry.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def created_at(self):
        """Gets the created_at of this FrontendConfigurationEntry.  # noqa: E501


        :return: The created_at of this FrontendConfigurationEntry.  # noqa: E501
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FrontendConfigurationEntry.


        :param created_at: The created_at of this FrontendConfigurationEntry.  # noqa: E501
        :type: float
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FrontendConfigurationEntry.  # noqa: E501


        :return: The updated_at of this FrontendConfigurationEntry.  # noqa: E501
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FrontendConfigurationEntry.


        :param updated_at: The updated_at of this FrontendConfigurationEntry.  # noqa: E501
        :type: float
        """

        self._updated_at = updated_at

    @property
    def resource_type(self):
        """Gets the resource_type of this FrontendConfigurationEntry.  # noqa: E501


        :return: The resource_type of this FrontendConfigurationEntry.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FrontendConfigurationEntry.


        :param resource_type: The resource_type of this FrontendConfigurationEntry.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

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
        if not isinstance(other, FrontendConfigurationEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
