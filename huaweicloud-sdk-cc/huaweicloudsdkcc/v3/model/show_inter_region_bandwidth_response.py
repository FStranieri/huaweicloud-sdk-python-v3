# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInterRegionBandwidthResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inter_region_bandwidth': 'InterRegionBandwidth',
        'request_id': 'str'
    }

    attribute_map = {
        'inter_region_bandwidth': 'inter_region_bandwidth',
        'request_id': 'request_id'
    }

    def __init__(self, inter_region_bandwidth=None, request_id=None):
        """ShowInterRegionBandwidthResponse

        The model defined in huaweicloud sdk

        :param inter_region_bandwidth: 
        :type inter_region_bandwidth: :class:`huaweicloudsdkcc.v3.InterRegionBandwidth`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ShowInterRegionBandwidthResponse, self).__init__()

        self._inter_region_bandwidth = None
        self._request_id = None
        self.discriminator = None

        if inter_region_bandwidth is not None:
            self.inter_region_bandwidth = inter_region_bandwidth
        if request_id is not None:
            self.request_id = request_id

    @property
    def inter_region_bandwidth(self):
        """Gets the inter_region_bandwidth of this ShowInterRegionBandwidthResponse.

        :return: The inter_region_bandwidth of this ShowInterRegionBandwidthResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.InterRegionBandwidth`
        """
        return self._inter_region_bandwidth

    @inter_region_bandwidth.setter
    def inter_region_bandwidth(self, inter_region_bandwidth):
        """Sets the inter_region_bandwidth of this ShowInterRegionBandwidthResponse.

        :param inter_region_bandwidth: The inter_region_bandwidth of this ShowInterRegionBandwidthResponse.
        :type inter_region_bandwidth: :class:`huaweicloudsdkcc.v3.InterRegionBandwidth`
        """
        self._inter_region_bandwidth = inter_region_bandwidth

    @property
    def request_id(self):
        """Gets the request_id of this ShowInterRegionBandwidthResponse.

        请求ID。

        :return: The request_id of this ShowInterRegionBandwidthResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowInterRegionBandwidthResponse.

        请求ID。

        :param request_id: The request_id of this ShowInterRegionBandwidthResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowInterRegionBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
