# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class KooMessageClient(Client):
    def __init__(self):
        super(KooMessageClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkoomessage.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "KooMessageClient":
            raise TypeError("client type error, support client type is KooMessageClient")

        return ClientBuilder(clazz)

    def add_call_back(self, request):
        """注册智能信息回执URL

        用户根据要求创建回执接口后，可以调用此接口进行注册，注意：此接口仅允许te_admin角色用户调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddCallBack
        :type request: :class:`huaweicloudsdkkoomessage.v1.AddCallBackRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AddCallBackResponse`
        """
        return self._add_call_back_with_http_info(request)

    def _add_call_back_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/callbacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddCallBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_callbacks(self, request):
        """查询用户已注册回执接口

        用户注册回执接口之后，可以根据此接口查询所有已注册回执接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimCallbacks
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimCallbacksRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimCallbacksResponse`
        """
        return self._list_aim_callbacks_with_http_info(request)

    def _list_aim_callbacks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/callbacks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimCallbacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_mobile_capability(self, request):
        """查询手机号智能信息解析能力

        用户在下发智能信息前，通过此接口批量查询对应手机的智能信息解析能力。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckMobileCapability
        :type request: :class:`huaweicloudsdkkoomessage.v1.CheckMobileCapabilityRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CheckMobileCapabilityResponse`
        """
        return self._check_mobile_capability_with_http_info(request)

    def _check_mobile_capability_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/mobile-capabilities/check',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckMobileCapabilityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resolve_task(self, request):
        """生成解析任务

        生成解析的短链。一次最多生成100个解析的短链。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResolveTask
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskResponse`
        """
        return self._create_resolve_task_with_http_info(request)

    def _create_resolve_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/resolve-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResolveTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_resolve_details(self, request):
        """查询解析明细

        根据用户提供的过滤条件查询个性化解析明细，包括：发送任务ID、发送手机号码等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimResolveDetails
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimResolveDetailsRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimResolveDetailsResponse`
        """
        return self._list_aim_resolve_details_with_http_info(request)

    def _list_aim_resolve_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'cust_flag' in local_var_params:
            query_params.append(('cust_flag', local_var_params['cust_flag']))
        if 'sms_sign' in local_var_params:
            query_params.append(('sms_sign', local_var_params['sms_sign']))
        if 'aim_url' in local_var_params:
            query_params.append(('aim_url', local_var_params['aim_url']))
        if 'resolved_status' in local_var_params:
            query_params.append(('resolved_status', local_var_params['resolved_status']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/resolve-details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimResolveDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resolve_tasks(self, request):
        """查询解析任务

        创建解析任务后，客户可以查询解析任务状态信息。
        
        通过模板ID等过滤条件，查询解析任务列表。
        
        如需查询明细，建议使用查询解析明细接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResolveTasks
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListResolveTasksRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListResolveTasksResponse`
        """
        return self._list_resolve_tasks_with_http_info(request)

    def _list_resolve_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'cust_flag' in local_var_params:
            query_params.append(('cust_flag', local_var_params['cust_flag']))
        if 'aim_url' in local_var_params:
            query_params.append(('aim_url', local_var_params['aim_url']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/resolve-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResolveTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_aim_send_task(self, request):
        """发送智能信息

        根据客户的参数发送任务名称、智能信息模板ID等进行智能信息发送。一次最多发送100个智能信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAimSendTask
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreateAimSendTaskRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreateAimSendTaskResponse`
        """
        return self._create_aim_send_task_with_http_info(request)

    def _create_aim_send_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/send-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAimSendTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_send_details(self, request):
        """查询智能信息发送明细

        根据用户提供的过滤条件查询发送明细列表，包括：发送任务ID、发送手机号码等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimSendDetails
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimSendDetailsRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimSendDetailsResponse`
        """
        return self._list_aim_send_details_with_http_info(request)

    def _list_aim_send_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'sms_sign' in local_var_params:
            query_params.append(('sms_sign', local_var_params['sms_sign']))
        if 'cust_flag' in local_var_params:
            query_params.append(('cust_flag', local_var_params['cust_flag']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/send-details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimSendDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_send_reports(self, request):
        """查询智能信息发送报表

        查询智能信息发送报表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimSendReports
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimSendReportsRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimSendReportsResponse`
        """
        return self._list_aim_send_reports_with_http_info(request)

    def _list_aim_send_reports_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/send-reports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimSendReportsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_send_tasks(self, request):
        """查询智能信息发送任务

        
        根据用户提供的过滤条件查询智能信息发送任务列表，包括：发送任务名称、智能信息模板ID等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimSendTasks
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimSendTasksRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimSendTasksResponse`
        """
        return self._list_aim_send_tasks_with_http_info(request)

    def _list_aim_send_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/send-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimSendTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_aim_personal_template(self, request):
        """创建个人模板

        用于用户创建个人模板。
        
        &gt; 请求中所有字符串不允许携带“&lt;”、“&gt;”或多个空格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAimPersonalTemplate
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreateAimPersonalTemplateRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreateAimPersonalTemplateResponse`
        """
        return self._create_aim_personal_template_with_http_info(request)

    def _create_aim_personal_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAimPersonalTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_aim_personal_template(self, request):
        """删除模板实例

        根据客户提供的模板ID，删除智能信息个人模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAimPersonalTemplate
        :type request: :class:`huaweicloudsdkkoomessage.v1.DeleteAimPersonalTemplateRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.DeleteAimPersonalTemplateResponse`
        """
        return self._delete_aim_personal_template_with_http_info(request)

    def _delete_aim_personal_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/template/{tpl_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAimPersonalTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template_material(self, request):
        """删除模板素材

        根据客户提供的模板ID，删除模板素材。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateMaterial
        :type request: :class:`huaweicloudsdkkoomessage.v1.DeleteTemplateMaterialRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.DeleteTemplateMaterialResponse`
        """
        return self._delete_template_material_with_http_info(request)

    def _delete_template_material_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/template-materials/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_template_materials(self, request):
        """查询智能消息模板素材列表

        根据客户提供的过滤条件，查询模板素材列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimTemplateMaterials
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateMaterialsRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateMaterialsResponse`
        """
        return self._list_aim_template_materials_with_http_info(request)

    def _list_aim_template_materials_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'material_id' in local_var_params:
            query_params.append(('material_id', local_var_params['material_id']))
        if 'aim_resource_id' in local_var_params:
            query_params.append(('aim_resource_id', local_var_params['aim_resource_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/template-materials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimTemplateMaterialsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_template_reports(self, request):
        """查询模板报表

        根据用户指定过滤条件查询指定智能信息模板的解析次数。当日数据需要次日16:00之后才能查询到。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimTemplateReports
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateReportsRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplateReportsResponse`
        """
        return self._list_aim_template_reports_with_http_info(request)

    def _list_aim_template_reports_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/tempalte-reports/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimTemplateReportsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_aim_templates(self, request):
        """查询模板

        
        根据客户提供的过滤条件查询智能信息模板列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAimTemplates
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplatesRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListAimTemplatesResponse`
        """
        return self._list_aim_templates_with_http_info(request)

    def _list_aim_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'tpl_type' in local_var_params:
            query_params.append(('tpl_type', local_var_params['tpl_type']))
        if 'factory_type' in local_var_params:
            query_params.append(('factory_type', local_var_params['factory_type']))
            collection_formats['factory_type'] = 'csv'
        if 'has_param' in local_var_params:
            query_params.append(('has_param', local_var_params['has_param']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'is_only_status' in local_var_params:
            query_params.append(('is_only_status', local_var_params['is_only_status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAimTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_personal_template_state(self, request):
        """启用或禁用模板实例

        根据客户提供的模板ID，启用或禁用智能信息个人模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePersonalTemplateState
        :type request: :class:`huaweicloudsdkkoomessage.v1.UpdatePersonalTemplateStateRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UpdatePersonalTemplateStateResponse`
        """
        return self._update_personal_template_state_with_http_info(request)

    def _update_personal_template_state_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tpl_id' in local_var_params:
            path_params['tpl_id'] = local_var_params['tpl_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/template-state/{tpl_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePersonalTemplateStateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_aim_template_material(self, request):
        """上传智能信息模板素材

        支持用户上传模板使用的图片或者视频。
        
        &gt; 单个租户资源空间为10GB，包括回收站内容，请及时清理无用资源，防止资源浪费。
        &gt; 请求中所有字符串不允许携带“&lt;”、“&gt;”或多个空格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAimTemplateMaterial
        :type request: :class:`huaweicloudsdkkoomessage.v1.UploadAimTemplateMaterialRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UploadAimTemplateMaterialResponse`
        """
        return self._upload_aim_template_material_with_http_info(request)

    def _upload_aim_template_material_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim/template-materials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadAimTemplateMaterialResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_menus(self, request):
        """查询智能信息服务号菜单

        根据用户提供的过滤条件查询服务号菜单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMenus
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListMenusRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListMenusResponse`
        """
        return self._list_menus_with_http_info(request)

    def _list_menus_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'menu_id' in local_var_params:
            query_params.append(('menu_id', local_var_params['menu_id']))
        if 'pub_id' in local_var_params:
            query_params.append(('pub_id', local_var_params['pub_id']))
        if 'pub_name' in local_var_params:
            query_params.append(('pub_name', local_var_params['pub_name']))
        if 'online_begin_time' in local_var_params:
            query_params.append(('online_begin_time', local_var_params['online_begin_time']))
        if 'online_end_time' in local_var_params:
            query_params.append(('online_end_time', local_var_params['online_end_time']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'menu_name' in local_var_params:
            query_params.append(('menu_name', local_var_params['menu_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/menus',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMenusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_menu(self, request):
        """修改智能信息服务号菜单

        
        支持用户修改所属企业的指定菜单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMenu
        :type request: :class:`huaweicloudsdkkoomessage.v1.UpdateMenuRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UpdateMenuResponse`
        """
        return self._update_menu_with_http_info(request)

    def _update_menu_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'menu_id' in local_var_params:
            path_params['menu_id'] = local_var_params['menu_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/menus/{menu_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMenuResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_port_info(self, request):
        """删除通道号

        删除通道号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePortInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.DeletePortInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.DeletePortInfoResponse`
        """
        return self._delete_port_info_with_http_info(request)

    def _delete_port_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/ports/{port_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePortInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_port_infos(self, request):
        """查询通道号列表

        支持查询通道号列表和通道号绑定信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPortInfos
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListPortInfosRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListPortInfosResponse`
        """
        return self._list_port_infos_with_http_info(request)

    def _list_port_infos_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'port_type' in local_var_params:
            query_params.append(('port_type', local_var_params['port_type']))
        if 'sign_search' in local_var_params:
            query_params.append(('sign_search', local_var_params['sign_search']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'pub_name' in local_var_params:
            query_params.append(('pub_name', local_var_params['pub_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def lock_port(self, request):
        """通道号绑定服务号

        通道号绑定服务号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LockPort
        :type request: :class:`huaweicloudsdkkoomessage.v1.LockPortRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.LockPortResponse`
        """
        return self._lock_port_with_http_info(request)

    def _lock_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/ports/associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='LockPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_port(self, request):
        """注册通道号

        注册通道号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterPort
        :type request: :class:`huaweicloudsdkkoomessage.v1.RegisterPortRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.RegisterPortResponse`
        """
        return self._register_port_with_http_info(request)

    def _register_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/ports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unlock_port(self, request):
        """通道号解绑服务号

        通道号解绑服务号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnlockPort
        :type request: :class:`huaweicloudsdkkoomessage.v1.UnlockPortRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UnlockPortResponse`
        """
        return self._unlock_port_with_http_info(request)

    def _unlock_port_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/ports/disassociate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnlockPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_portal_infos(self, request):
        """查询主页列表

        
        根据用户提供的过滤条件查找用户管理的主页列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPortalInfos
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListPortalInfosRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListPortalInfosResponse`
        """
        return self._list_portal_infos_with_http_info(request)

    def _list_portal_infos_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pub_name' in local_var_params:
            query_params.append(('pub_name', local_var_params['pub_name']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/portals',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPortalInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_portal_info(self, request):
        """修改主页信息

        
        用户对已创建的主页进行信息的修改。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePortalInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.UpdatePortalInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UpdatePortalInfoResponse`
        """
        return self._update_portal_info_with_http_info(request)

    def _update_portal_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'portal_id' in local_var_params:
            path_params['portal_id'] = local_var_params['portal_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/portals/{portal_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePortalInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def freeze_pub(self, request):
        """冻结服务号

        支持用户通过此接口冻结服务号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for FreezePub
        :type request: :class:`huaweicloudsdkkoomessage.v1.FreezePubRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.FreezePubResponse`
        """
        return self._freeze_pub_with_http_info(request)

    def _freeze_pub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pub_id' in local_var_params:
            path_params['pub_id'] = local_var_params['pub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/pubs/{pub_id}/freeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='FreezePubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pub_infos(self, request):
        """查询服务号列表

        
        支持根据用户提供的过滤条件查询服务号列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPubInfos
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListPubInfosRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListPubInfosResponse`
        """
        return self._list_pub_infos_with_http_info(request)

    def _list_pub_infos_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pub_name' in local_var_params:
            query_params.append(('pub_name', local_var_params['pub_name']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'industry' in local_var_params:
            query_params.append(('industry', local_var_params['industry']))
        if 'approve_state' in local_var_params:
            query_params.append(('approve_state', local_var_params['approve_state']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/pubs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPubInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def unfreeze_pub(self, request):
        """解冻服务号

        服务号解结，冻结服务号。需审核，审核通过生效。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnfreezePub
        :type request: :class:`huaweicloudsdkkoomessage.v1.UnfreezePubRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UnfreezePubResponse`
        """
        return self._unfreeze_pub_with_http_info(request)

    def _unfreeze_pub_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pub_id' in local_var_params:
            path_params['pub_id'] = local_var_params['pub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/pubs/{pub_id}/unfreeze',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UnfreezePubResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_pub_info(self, request):
        """更新服务号信息

        支持用户更新服务号信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePubInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.UpdatePubInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UpdatePubInfoResponse`
        """
        return self._update_pub_info_with_http_info(request)

    def _update_pub_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pub_id' in local_var_params:
            path_params['pub_id'] = local_var_params['pub_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/pubs/{pub_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePubInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pub_info(self, request):
        """一站式服务号创建

        一站式服务号创建。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePubInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreatePubInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreatePubInfoResponse`
        """
        return self._create_pub_info_with_http_info(request)

    def _create_pub_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/unify/pubs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePubInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_menu_info(self, request):
        """催审菜单

        支持用户通过此接口根据菜单ID催审。菜单需要在与其关联的服务号审核通过之后才能催审。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushMenuInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.PushMenuInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PushMenuInfoResponse`
        """
        return self._push_menu_info_with_http_info(request)

    def _push_menu_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'menu_id' in local_var_params:
            path_params['menu_id'] = local_var_params['menu_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/menus/{menu_id}/push',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushMenuInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_portal_info(self, request):
        """催审主页

        支持用户通过此接口根据主页ID催审。主页需要在与其关联的服务号审核通过之后才能催审。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushPortalInfo
        :type request: :class:`huaweicloudsdkkoomessage.v1.PushPortalInfoRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.PushPortalInfoResponse`
        """
        return self._push_portal_info_with_http_info(request)

    def _push_portal_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'portal_id' in local_var_params:
            path_params['portal_id'] = local_var_params['portal_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-sa/portals/{portal_id}/push',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushPortalInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_media(self, request):
        """上传智能信息服务号图片资源

        支持用户上传图片资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadMedia
        :type request: :class:`huaweicloudsdkkoomessage.v1.UploadMediaRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UploadMediaResponse`
        """
        return self._upload_media_with_http_info(request)

    def _upload_media_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'file_type' in local_var_params:
            form_params['file_type'] = local_var_params['file_type']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim-sa/media/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadMediaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_vms_call_back(self, request):
        """注册智能信息基础版回执URL

        用户根据要求创建智能信息基础版回执接口后，可以调用此接口进行注册。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddVmsCallBack
        :type request: :class:`huaweicloudsdkkoomessage.v1.AddVmsCallBackRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.AddVmsCallBackResponse`
        """
        return self._add_vms_call_back_with_http_info(request)

    def _add_vms_call_back_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-basic/callbacks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddVmsCallBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vms_send_task(self, request):
        """发送智能信息基础版任务

        支持用户通过此接口进行智能信息基础版任务发送。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVmsSendTask
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreateVmsSendTaskRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreateVmsSendTaskResponse`
        """
        return self._create_vms_send_task_with_http_info(request)

    def _create_vms_send_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-basic/send-tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVmsSendTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vms_callbacks(self, request):
        """查询用户已注册智能信息基础版回执接口

        查询所有已注册的智能信息基础版回执接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVmsCallbacks
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListVmsCallbacksRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListVmsCallbacksResponse`
        """
        return self._list_vms_callbacks_with_http_info(request)

    def _list_vms_callbacks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-basic/callbacks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVmsCallbacksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vms_send_tasks(self, request):
        """查询智能信息基础版发送任务

        支持用户根据过滤条件查询智能信息基础版任务列表。包括：发送任务名称、智能信息基础版模板ID等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVmsSendTasks
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListVmsSendTasksRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListVmsSendTasksResponse`
        """
        return self._list_vms_send_tasks_with_http_info(request)

    def _list_vms_send_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'send_begin_time' in local_var_params:
            query_params.append(('send_begin_time', local_var_params['send_begin_time']))
        if 'send_end_time' in local_var_params:
            query_params.append(('send_end_time', local_var_params['send_end_time']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'task_status' in local_var_params:
            query_params.append(('task_status', local_var_params['task_status']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/aim-basic/send-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVmsSendTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vms_template(self, request):
        """新建智能信息基础版模板

        支持用户通过此接口创建智能信息基础版模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVmsTemplate
        :type request: :class:`huaweicloudsdkkoomessage.v1.CreateVmsTemplateRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.CreateVmsTemplateResponse`
        """
        return self._create_vms_template_with_http_info(request)

    def _create_vms_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim-basic/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVmsTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vms_template_status(self, request):
        """查询智能信息基础版模板状态

        根据用户提供的过滤条件查询智能信息基础版模板状态列表。
        包括：模板ID、模板名称等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVmsTemplateStatus
        :type request: :class:`huaweicloudsdkkoomessage.v1.ListVmsTemplateStatusRequest`
        :rtype: :class:`huaweicloudsdkkoomessage.v1.ListVmsTemplateStatusResponse`
        """
        return self._list_vms_template_status_with_http_info(request)

    def _list_vms_template_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tpl_id' in local_var_params:
            query_params.append(('tpl_id', local_var_params['tpl_id']))
        if 'tpl_name' in local_var_params:
            query_params.append(('tpl_name', local_var_params['tpl_name']))
        if 'tpl_type' in local_var_params:
            query_params.append(('tpl_type', local_var_params['tpl_type']))
        if 'has_param' in local_var_params:
            query_params.append(('has_param', local_var_params['has_param']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/aim-basic/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVmsTemplateStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
