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


class ScmConnectionWithOauthUsername(object):
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
        'scm_type': 'ScmType',
        'label': 'str',
        'web_endpoint': 'str',
        'api_endpoint': 'str',
        'client_id': 'str',
        'owner_name': 'str',
        'oauth_username': 'str'
    }

    attribute_map = {
        'scm_type': 'scm_type',
        'label': 'label',
        'web_endpoint': 'web_endpoint',
        'api_endpoint': 'api_endpoint',
        'client_id': 'client_id',
        'owner_name': 'owner_name',
        'oauth_username': 'oauth_username'
    }

    def __init__(self, scm_type=None, label=None, web_endpoint=None, api_endpoint=None, client_id=None, owner_name=None, oauth_username=None):  # noqa: E501
        """ScmConnectionWithOauthUsername - a model defined in OpenAPI"""  # noqa: E501

        self._scm_type = None
        self._label = None
        self._web_endpoint = None
        self._api_endpoint = None
        self._client_id = None
        self._owner_name = None
        self._oauth_username = None
        self.discriminator = None

        if scm_type is not None:
            self.scm_type = scm_type
        if label is not None:
            self.label = label
        if web_endpoint is not None:
            self.web_endpoint = web_endpoint
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        if client_id is not None:
            self.client_id = client_id
        if owner_name is not None:
            self.owner_name = owner_name
        if oauth_username is not None:
            self.oauth_username = oauth_username

    @property
    def scm_type(self):
        """Gets the scm_type of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The scm_type of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: ScmType
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        """Sets the scm_type of this ScmConnectionWithOauthUsername.


        :param scm_type: The scm_type of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: ScmType
        """

        self._scm_type = scm_type

    @property
    def label(self):
        """Gets the label of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The label of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ScmConnectionWithOauthUsername.


        :param label: The label of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def web_endpoint(self):
        """Gets the web_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The web_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._web_endpoint

    @web_endpoint.setter
    def web_endpoint(self, web_endpoint):
        """Sets the web_endpoint of this ScmConnectionWithOauthUsername.


        :param web_endpoint: The web_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._web_endpoint = web_endpoint

    @property
    def api_endpoint(self):
        """Gets the api_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The api_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """Sets the api_endpoint of this ScmConnectionWithOauthUsername.


        :param api_endpoint: The api_endpoint of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._api_endpoint = api_endpoint

    @property
    def client_id(self):
        """Gets the client_id of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The client_id of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ScmConnectionWithOauthUsername.


        :param client_id: The client_id of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def owner_name(self):
        """Gets the owner_name of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The owner_name of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this ScmConnectionWithOauthUsername.


        :param owner_name: The owner_name of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def oauth_username(self):
        """Gets the oauth_username of this ScmConnectionWithOauthUsername.  # noqa: E501


        :return: The oauth_username of this ScmConnectionWithOauthUsername.  # noqa: E501
        :rtype: str
        """
        return self._oauth_username

    @oauth_username.setter
    def oauth_username(self, oauth_username):
        """Sets the oauth_username of this ScmConnectionWithOauthUsername.


        :param oauth_username: The oauth_username of this ScmConnectionWithOauthUsername.  # noqa: E501
        :type: str
        """

        self._oauth_username = oauth_username

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
        if not isinstance(other, ScmConnectionWithOauthUsername):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
