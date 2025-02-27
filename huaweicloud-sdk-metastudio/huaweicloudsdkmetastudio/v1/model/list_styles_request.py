# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStylesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'state': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'create_until': 'str',
        'create_since': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'create_until': 'create_until',
        'create_since': 'create_since'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, state=None, sort_key=None, sort_dir=None, create_until=None, create_since=None):
        """ListStylesRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param state: 任务状态，默认所有状态，可多个状态查询，使用英文逗号分隔。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED: 部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消
        :type state: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 升序还是降序，默认升序。 * asc：升序 * desc：降序
        :type sort_dir: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;&#39;&#39;。
        :type create_until: str
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。格式遵循：RFC 3339 如\&quot;2021-01-10T10:43:17Z\&quot;&#39;&#39;。
        :type create_since: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._state = None
        self._sort_key = None
        self._sort_dir = None
        self._create_until = None
        self._create_since = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if create_until is not None:
            self.create_until = create_until
        if create_since is not None:
            self.create_since = create_since

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ListStylesRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this ListStylesRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ListStylesRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this ListStylesRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        """Gets the offset of this ListStylesRequest.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListStylesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListStylesRequest.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListStylesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListStylesRequest.

        每页显示的条目数量

        :return: The limit of this ListStylesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStylesRequest.

        每页显示的条目数量

        :param limit: The limit of this ListStylesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        """Gets the state of this ListStylesRequest.

        任务状态，默认所有状态，可多个状态查询，使用英文逗号分隔。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED: 部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :return: The state of this ListStylesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListStylesRequest.

        任务状态，默认所有状态，可多个状态查询，使用英文逗号分隔。 * WAITING：等待任务调度 * PROCESSING：正在处理 * PARTIAL_SUCCEED: 部分成功（模型生成，截图失败） * SUCCEED：成功 * FAILED：失败 * CANCELED：取消

        :param state: The state of this ListStylesRequest.
        :type state: str
        """
        self._state = state

    @property
    def sort_key(self):
        """Gets the sort_key of this ListStylesRequest.

        排序字段。

        :return: The sort_key of this ListStylesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListStylesRequest.

        排序字段。

        :param sort_key: The sort_key of this ListStylesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListStylesRequest.

        升序还是降序，默认升序。 * asc：升序 * desc：降序

        :return: The sort_dir of this ListStylesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListStylesRequest.

        升序还是降序，默认升序。 * asc：升序 * desc：降序

        :param sort_dir: The sort_dir of this ListStylesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def create_until(self):
        """Gets the create_until of this ListStylesRequest.

        过滤创建时间<=输入时间的记录。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"''。

        :return: The create_until of this ListStylesRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        """Sets the create_until of this ListStylesRequest.

        过滤创建时间<=输入时间的记录。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"''。

        :param create_until: The create_until of this ListStylesRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def create_since(self):
        """Gets the create_since of this ListStylesRequest.

        过滤创建时间>=输入时间的记录。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"''。

        :return: The create_since of this ListStylesRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        """Sets the create_since of this ListStylesRequest.

        过滤创建时间>=输入时间的记录。格式遵循：RFC 3339 如\"2021-01-10T10:43:17Z\"''。

        :param create_since: The create_since of this ListStylesRequest.
        :type create_since: str
        """
        self._create_since = create_since

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
        if not isinstance(other, ListStylesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
