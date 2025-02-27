# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApiRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'api_id': 'str',
        'body': 'Api'
    }

    attribute_map = {
        'workspace': 'workspace',
        'api_id': 'api_id',
        'body': 'body'
    }

    def __init__(self, workspace=None, api_id=None, body=None):
        """UpdateApiRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param api_id: API ID
        :type api_id: str
        :param body: Body of the UpdateApiRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.Api`
        """
        
        

        self._workspace = None
        self._api_id = None
        self._body = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.api_id = api_id
        if body is not None:
            self.body = body

    @property
    def workspace(self):
        """Gets the workspace of this UpdateApiRequest.

        工作空间id

        :return: The workspace of this UpdateApiRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this UpdateApiRequest.

        工作空间id

        :param workspace: The workspace of this UpdateApiRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def api_id(self):
        """Gets the api_id of this UpdateApiRequest.

        API ID

        :return: The api_id of this UpdateApiRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this UpdateApiRequest.

        API ID

        :param api_id: The api_id of this UpdateApiRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def body(self):
        """Gets the body of this UpdateApiRequest.

        :return: The body of this UpdateApiRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Api`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateApiRequest.

        :param body: The body of this UpdateApiRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.Api`
        """
        self._body = body

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
