# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIndividualJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_param': 'PublishParam',
        'record_param': 'RecordParam'
    }

    attribute_map = {
        'publish_param': 'publish_param',
        'record_param': 'record_param'
    }

    def __init__(self, publish_param=None, record_param=None):
        """UpdateIndividualJobReq

        The model defined in huaweicloud sdk

        :param publish_param: 
        :type publish_param: :class:`huaweicloudsdkcloudrtc.v2.PublishParam`
        :param record_param: 
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        
        

        self._publish_param = None
        self._record_param = None
        self.discriminator = None

        if publish_param is not None:
            self.publish_param = publish_param
        if record_param is not None:
            self.record_param = record_param

    @property
    def publish_param(self):
        """Gets the publish_param of this UpdateIndividualJobReq.

        :return: The publish_param of this UpdateIndividualJobReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.PublishParam`
        """
        return self._publish_param

    @publish_param.setter
    def publish_param(self, publish_param):
        """Sets the publish_param of this UpdateIndividualJobReq.

        :param publish_param: The publish_param of this UpdateIndividualJobReq.
        :type publish_param: :class:`huaweicloudsdkcloudrtc.v2.PublishParam`
        """
        self._publish_param = publish_param

    @property
    def record_param(self):
        """Gets the record_param of this UpdateIndividualJobReq.

        :return: The record_param of this UpdateIndividualJobReq.
        :rtype: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        return self._record_param

    @record_param.setter
    def record_param(self, record_param):
        """Sets the record_param of this UpdateIndividualJobReq.

        :param record_param: The record_param of this UpdateIndividualJobReq.
        :type record_param: :class:`huaweicloudsdkcloudrtc.v2.RecordParam`
        """
        self._record_param = record_param

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
        if not isinstance(other, UpdateIndividualJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
