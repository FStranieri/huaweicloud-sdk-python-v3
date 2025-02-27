# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiCatalogListRequest:

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
        'catalog_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'catalog_id': 'catalog_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, catalog_id=None, offset=None, limit=None):
        """ListApiCatalogListRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param catalog_id: 目录编号
        :type catalog_id: str
        :param offset: 查询起始坐标, 即跳过前X条数据
        :type offset: int
        :param limit: 查询条数, 即查询Y条数据
        :type limit: int
        """
        
        

        self._workspace = None
        self._catalog_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        self.catalog_id = catalog_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        """Gets the workspace of this ListApiCatalogListRequest.

        工作空间id

        :return: The workspace of this ListApiCatalogListRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListApiCatalogListRequest.

        工作空间id

        :param workspace: The workspace of this ListApiCatalogListRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def catalog_id(self):
        """Gets the catalog_id of this ListApiCatalogListRequest.

        目录编号

        :return: The catalog_id of this ListApiCatalogListRequest.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this ListApiCatalogListRequest.

        目录编号

        :param catalog_id: The catalog_id of this ListApiCatalogListRequest.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def offset(self):
        """Gets the offset of this ListApiCatalogListRequest.

        查询起始坐标, 即跳过前X条数据

        :return: The offset of this ListApiCatalogListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApiCatalogListRequest.

        查询起始坐标, 即跳过前X条数据

        :param offset: The offset of this ListApiCatalogListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApiCatalogListRequest.

        查询条数, 即查询Y条数据

        :return: The limit of this ListApiCatalogListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApiCatalogListRequest.

        查询条数, 即查询Y条数据

        :param limit: The limit of this ListApiCatalogListRequest.
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
        if not isinstance(other, ListApiCatalogListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
