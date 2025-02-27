# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceModelAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_type': 'str',
        'sex': 'str',
        'language': 'str'
    }

    attribute_map = {
        'model_type': 'model_type',
        'sex': 'sex',
        'language': 'language'
    }

    def __init__(self, model_type=None, sex=None, language=None):
        """VoiceModelAssetMeta

        The model defined in huaweicloud sdk

        :param model_type: 音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型
        :type model_type: str
        :param sex: 音色性别。默认UNKNOW。 * UNKNOW： 中性音色 * MALE： 男性音色 * FEMALE： 女性音色
        :type sex: str
        :param language: 音色语言。默认UNKNOW。 * UNKNOW： 未知 * CN： 中文 * EN： 英文
        :type language: str
        """
        
        

        self._model_type = None
        self._sex = None
        self._language = None
        self.discriminator = None

        if model_type is not None:
            self.model_type = model_type
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language

    @property
    def model_type(self):
        """Gets the model_type of this VoiceModelAssetMeta.

        音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型

        :return: The model_type of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this VoiceModelAssetMeta.

        音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型

        :param model_type: The model_type of this VoiceModelAssetMeta.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def sex(self):
        """Gets the sex of this VoiceModelAssetMeta.

        音色性别。默认UNKNOW。 * UNKNOW： 中性音色 * MALE： 男性音色 * FEMALE： 女性音色

        :return: The sex of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this VoiceModelAssetMeta.

        音色性别。默认UNKNOW。 * UNKNOW： 中性音色 * MALE： 男性音色 * FEMALE： 女性音色

        :param sex: The sex of this VoiceModelAssetMeta.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        """Gets the language of this VoiceModelAssetMeta.

        音色语言。默认UNKNOW。 * UNKNOW： 未知 * CN： 中文 * EN： 英文

        :return: The language of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VoiceModelAssetMeta.

        音色语言。默认UNKNOW。 * UNKNOW： 未知 * CN： 中文 * EN： 英文

        :param language: The language of this VoiceModelAssetMeta.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, VoiceModelAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
