# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelationFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'bucket_id': 'str',
        'assets_name': 'str',
        'risk_start': 'int',
        'risk_end': 'int',
        'offset': 'int',
        'size': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'bucket_id': 'bucket_id',
        'assets_name': 'assets_name',
        'risk_start': 'risk_start',
        'risk_end': 'risk_end',
        'offset': 'offset',
        'size': 'size',
        'limit': 'limit'
    }

    def __init__(self, job_id=None, bucket_id=None, assets_name=None, risk_start=None, risk_end=None, offset=None, size=None, limit=None):
        """ListRelationFileRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param bucket_id: 桶ID
        :type bucket_id: str
        :param assets_name: 资产名称
        :type assets_name: str
        :param risk_start: 起始风险等级
        :type risk_start: int
        :param risk_end: 终止风险等级
        :type risk_end: int
        :param offset: 偏移量
        :type offset: int
        :param size: 页面大小
        :type size: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._job_id = None
        self._bucket_id = None
        self._assets_name = None
        self._risk_start = None
        self._risk_end = None
        self._offset = None
        self._size = None
        self._limit = None
        self.discriminator = None

        self.job_id = job_id
        self.bucket_id = bucket_id
        if assets_name is not None:
            self.assets_name = assets_name
        self.risk_start = risk_start
        self.risk_end = risk_end
        self.offset = offset
        self.size = size
        if limit is not None:
            self.limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ListRelationFileRequest.

        任务ID

        :return: The job_id of this ListRelationFileRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListRelationFileRequest.

        任务ID

        :param job_id: The job_id of this ListRelationFileRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def bucket_id(self):
        """Gets the bucket_id of this ListRelationFileRequest.

        桶ID

        :return: The bucket_id of this ListRelationFileRequest.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this ListRelationFileRequest.

        桶ID

        :param bucket_id: The bucket_id of this ListRelationFileRequest.
        :type bucket_id: str
        """
        self._bucket_id = bucket_id

    @property
    def assets_name(self):
        """Gets the assets_name of this ListRelationFileRequest.

        资产名称

        :return: The assets_name of this ListRelationFileRequest.
        :rtype: str
        """
        return self._assets_name

    @assets_name.setter
    def assets_name(self, assets_name):
        """Sets the assets_name of this ListRelationFileRequest.

        资产名称

        :param assets_name: The assets_name of this ListRelationFileRequest.
        :type assets_name: str
        """
        self._assets_name = assets_name

    @property
    def risk_start(self):
        """Gets the risk_start of this ListRelationFileRequest.

        起始风险等级

        :return: The risk_start of this ListRelationFileRequest.
        :rtype: int
        """
        return self._risk_start

    @risk_start.setter
    def risk_start(self, risk_start):
        """Sets the risk_start of this ListRelationFileRequest.

        起始风险等级

        :param risk_start: The risk_start of this ListRelationFileRequest.
        :type risk_start: int
        """
        self._risk_start = risk_start

    @property
    def risk_end(self):
        """Gets the risk_end of this ListRelationFileRequest.

        终止风险等级

        :return: The risk_end of this ListRelationFileRequest.
        :rtype: int
        """
        return self._risk_end

    @risk_end.setter
    def risk_end(self, risk_end):
        """Sets the risk_end of this ListRelationFileRequest.

        终止风险等级

        :param risk_end: The risk_end of this ListRelationFileRequest.
        :type risk_end: int
        """
        self._risk_end = risk_end

    @property
    def offset(self):
        """Gets the offset of this ListRelationFileRequest.

        偏移量

        :return: The offset of this ListRelationFileRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRelationFileRequest.

        偏移量

        :param offset: The offset of this ListRelationFileRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def size(self):
        """Gets the size of this ListRelationFileRequest.

        页面大小

        :return: The size of this ListRelationFileRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListRelationFileRequest.

        页面大小

        :param size: The size of this ListRelationFileRequest.
        :type size: int
        """
        self._size = size

    @property
    def limit(self):
        """Gets the limit of this ListRelationFileRequest.

        分页大小

        :return: The limit of this ListRelationFileRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRelationFileRequest.

        分页大小

        :param limit: The limit of this ListRelationFileRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRelationFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
