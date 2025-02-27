# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerListOrDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[str]',
        'total': 'int',
        'brokers': 'list[Brokers]'
    }

    attribute_map = {
        'topics': 'topics',
        'total': 'total',
        'brokers': 'brokers'
    }

    def __init__(self, topics=None, total=None, brokers=None):
        """ShowConsumerListOrDetailsResponse

        The model defined in huaweicloud sdk

        :param topics: Topic列表（当查询topic消费“列表”时才显示此参数）。
        :type topics: list[str]
        :param total: Topic总数（当查询topic消费“列表”时才显示此参数）。
        :type total: int
        :param brokers: Topic关联代理（当查询topic消费“详情”才显示此参数）。
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        
        super(ShowConsumerListOrDetailsResponse, self).__init__()

        self._topics = None
        self._total = None
        self._brokers = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics
        if total is not None:
            self.total = total
        if brokers is not None:
            self.brokers = brokers

    @property
    def topics(self):
        """Gets the topics of this ShowConsumerListOrDetailsResponse.

        Topic列表（当查询topic消费“列表”时才显示此参数）。

        :return: The topics of this ShowConsumerListOrDetailsResponse.
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ShowConsumerListOrDetailsResponse.

        Topic列表（当查询topic消费“列表”时才显示此参数）。

        :param topics: The topics of this ShowConsumerListOrDetailsResponse.
        :type topics: list[str]
        """
        self._topics = topics

    @property
    def total(self):
        """Gets the total of this ShowConsumerListOrDetailsResponse.

        Topic总数（当查询topic消费“列表”时才显示此参数）。

        :return: The total of this ShowConsumerListOrDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowConsumerListOrDetailsResponse.

        Topic总数（当查询topic消费“列表”时才显示此参数）。

        :param total: The total of this ShowConsumerListOrDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def brokers(self):
        """Gets the brokers of this ShowConsumerListOrDetailsResponse.

        Topic关联代理（当查询topic消费“详情”才显示此参数）。

        :return: The brokers of this ShowConsumerListOrDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this ShowConsumerListOrDetailsResponse.

        Topic关联代理（当查询topic消费“详情”才显示此参数）。

        :param brokers: The brokers of this ShowConsumerListOrDetailsResponse.
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        self._brokers = brokers

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
        if not isinstance(other, ShowConsumerListOrDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
