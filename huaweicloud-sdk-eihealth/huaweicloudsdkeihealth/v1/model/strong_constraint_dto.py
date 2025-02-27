# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StrongConstraintDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'StrongConstraintType',
        'bool': 'bool',
        'range': 'list[float]',
        'struct': 'StructureConstraintParamsDto',
        'quantiles': 'list[float]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'bool': 'bool',
        'range': 'range',
        'struct': 'struct',
        'quantiles': 'quantiles'
    }

    def __init__(self, name=None, type=None, bool=None, range=None, struct=None, quantiles=None):
        """StrongConstraintDto

        The model defined in huaweicloud sdk

        :param name: 属性名称
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkeihealth.v1.StrongConstraintType`
        :param bool: 属性约束类型bool的参数
        :type bool: bool
        :param range: 属性约束类型range的参数
        :type range: list[float]
        :param struct: 
        :type struct: :class:`huaweicloudsdkeihealth.v1.StructureConstraintParamsDto`
        :param quantiles: 属性约束类型minimize和maximize的参数
        :type quantiles: list[float]
        """
        
        

        self._name = None
        self._type = None
        self._bool = None
        self._range = None
        self._struct = None
        self._quantiles = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.type = type
        if bool is not None:
            self.bool = bool
        if range is not None:
            self.range = range
        if struct is not None:
            self.struct = struct
        if quantiles is not None:
            self.quantiles = quantiles

    @property
    def name(self):
        """Gets the name of this StrongConstraintDto.

        属性名称

        :return: The name of this StrongConstraintDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StrongConstraintDto.

        属性名称

        :param name: The name of this StrongConstraintDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this StrongConstraintDto.

        :return: The type of this StrongConstraintDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.StrongConstraintType`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StrongConstraintDto.

        :param type: The type of this StrongConstraintDto.
        :type type: :class:`huaweicloudsdkeihealth.v1.StrongConstraintType`
        """
        self._type = type

    @property
    def bool(self):
        """Gets the bool of this StrongConstraintDto.

        属性约束类型bool的参数

        :return: The bool of this StrongConstraintDto.
        :rtype: bool
        """
        return self._bool

    @bool.setter
    def bool(self, bool):
        """Sets the bool of this StrongConstraintDto.

        属性约束类型bool的参数

        :param bool: The bool of this StrongConstraintDto.
        :type bool: bool
        """
        self._bool = bool

    @property
    def range(self):
        """Gets the range of this StrongConstraintDto.

        属性约束类型range的参数

        :return: The range of this StrongConstraintDto.
        :rtype: list[float]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this StrongConstraintDto.

        属性约束类型range的参数

        :param range: The range of this StrongConstraintDto.
        :type range: list[float]
        """
        self._range = range

    @property
    def struct(self):
        """Gets the struct of this StrongConstraintDto.

        :return: The struct of this StrongConstraintDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.StructureConstraintParamsDto`
        """
        return self._struct

    @struct.setter
    def struct(self, struct):
        """Sets the struct of this StrongConstraintDto.

        :param struct: The struct of this StrongConstraintDto.
        :type struct: :class:`huaweicloudsdkeihealth.v1.StructureConstraintParamsDto`
        """
        self._struct = struct

    @property
    def quantiles(self):
        """Gets the quantiles of this StrongConstraintDto.

        属性约束类型minimize和maximize的参数

        :return: The quantiles of this StrongConstraintDto.
        :rtype: list[float]
        """
        return self._quantiles

    @quantiles.setter
    def quantiles(self, quantiles):
        """Sets the quantiles of this StrongConstraintDto.

        属性约束类型minimize和maximize的参数

        :param quantiles: The quantiles of this StrongConstraintDto.
        :type quantiles: list[float]
        """
        self._quantiles = quantiles

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
        if not isinstance(other, StrongConstraintDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
