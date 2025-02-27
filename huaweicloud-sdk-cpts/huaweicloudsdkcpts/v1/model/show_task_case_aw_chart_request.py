# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskCaseAwChartRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_id': 'int',
        'case_run_id': 'int',
        'detail_id': 'str'
    }

    attribute_map = {
        'task_run_id': 'task_run_id',
        'case_run_id': 'case_run_id',
        'detail_id': 'detail_id'
    }

    def __init__(self, task_run_id=None, case_run_id=None, detail_id=None):
        """ShowTaskCaseAwChartRequest

        The model defined in huaweicloud sdk

        :param task_run_id: 任务运行id（报告id）
        :type task_run_id: int
        :param case_run_id: 用例运行id
        :type case_run_id: int
        :param detail_id: 详情id
        :type detail_id: str
        """
        
        

        self._task_run_id = None
        self._case_run_id = None
        self._detail_id = None
        self.discriminator = None

        self.task_run_id = task_run_id
        self.case_run_id = case_run_id
        self.detail_id = detail_id

    @property
    def task_run_id(self):
        """Gets the task_run_id of this ShowTaskCaseAwChartRequest.

        任务运行id（报告id）

        :return: The task_run_id of this ShowTaskCaseAwChartRequest.
        :rtype: int
        """
        return self._task_run_id

    @task_run_id.setter
    def task_run_id(self, task_run_id):
        """Sets the task_run_id of this ShowTaskCaseAwChartRequest.

        任务运行id（报告id）

        :param task_run_id: The task_run_id of this ShowTaskCaseAwChartRequest.
        :type task_run_id: int
        """
        self._task_run_id = task_run_id

    @property
    def case_run_id(self):
        """Gets the case_run_id of this ShowTaskCaseAwChartRequest.

        用例运行id

        :return: The case_run_id of this ShowTaskCaseAwChartRequest.
        :rtype: int
        """
        return self._case_run_id

    @case_run_id.setter
    def case_run_id(self, case_run_id):
        """Sets the case_run_id of this ShowTaskCaseAwChartRequest.

        用例运行id

        :param case_run_id: The case_run_id of this ShowTaskCaseAwChartRequest.
        :type case_run_id: int
        """
        self._case_run_id = case_run_id

    @property
    def detail_id(self):
        """Gets the detail_id of this ShowTaskCaseAwChartRequest.

        详情id

        :return: The detail_id of this ShowTaskCaseAwChartRequest.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this ShowTaskCaseAwChartRequest.

        详情id

        :param detail_id: The detail_id of this ShowTaskCaseAwChartRequest.
        :type detail_id: str
        """
        self._detail_id = detail_id

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
        if not isinstance(other, ShowTaskCaseAwChartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
