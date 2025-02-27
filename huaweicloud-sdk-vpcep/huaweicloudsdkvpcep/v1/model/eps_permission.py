# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EpsPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'permission': 'str',
        'description': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'description': 'description',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, permission=None, description=None, created_at=None):
        """EpsPermission

        The model defined in huaweicloud sdk

        :param id: 白名单表主键ID
        :type id: str
        :param permission: 权限格式为：iam:domain::domain_id其中， ● “iam:domain::”为固定格式。 ● “domain_id”为可连接用户的帐号ID。 支持输入1~64个字符，包括“a~z”、“A~Z”、“0~9”或者“”。 “”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd
        :type permission: str
        :param description: 终端节点服务白名单描述
        :type description: str
        :param created_at: 白名单创建时间
        :type created_at: str
        """
        
        

        self._id = None
        self._permission = None
        self._description = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this EpsPermission.

        白名单表主键ID

        :return: The id of this EpsPermission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EpsPermission.

        白名单表主键ID

        :param id: The id of this EpsPermission.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        """Gets the permission of this EpsPermission.

        权限格式为：iam:domain::domain_id其中， ● “iam:domain::”为固定格式。 ● “domain_id”为可连接用户的帐号ID。 支持输入1~64个字符，包括“a~z”、“A~Z”、“0~9”或者“”。 “”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd

        :return: The permission of this EpsPermission.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this EpsPermission.

        权限格式为：iam:domain::domain_id其中， ● “iam:domain::”为固定格式。 ● “domain_id”为可连接用户的帐号ID。 支持输入1~64个字符，包括“a~z”、“A~Z”、“0~9”或者“”。 “”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd

        :param permission: The permission of this EpsPermission.
        :type permission: str
        """
        self._permission = permission

    @property
    def description(self):
        """Gets the description of this EpsPermission.

        终端节点服务白名单描述

        :return: The description of this EpsPermission.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EpsPermission.

        终端节点服务白名单描述

        :param description: The description of this EpsPermission.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this EpsPermission.

        白名单创建时间

        :return: The created_at of this EpsPermission.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EpsPermission.

        白名单创建时间

        :param created_at: The created_at of this EpsPermission.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, EpsPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
