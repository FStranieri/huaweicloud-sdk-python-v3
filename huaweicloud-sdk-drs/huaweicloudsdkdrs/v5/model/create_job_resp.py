# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobResp:

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
        'name': 'str',
        'status': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None):
        """CreateJobResp

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间。
        :type create_time: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this CreateJobResp.

        任务ID。

        :return: The id of this CreateJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateJobResp.

        任务ID。

        :param id: The id of this CreateJobResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateJobResp.

        任务名称。

        :return: The name of this CreateJobResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateJobResp.

        任务名称。

        :param name: The name of this CreateJobResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CreateJobResp.

        任务状态。

        :return: The status of this CreateJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateJobResp.

        任务状态。

        :param status: The status of this CreateJobResp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this CreateJobResp.

        任务创建时间。

        :return: The create_time of this CreateJobResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateJobResp.

        任务创建时间。

        :param create_time: The create_time of this CreateJobResp.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, CreateJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
