# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdknat.v2.model.associated_transit_ip import AssociatedTransitIp
from huaweicloudsdknat.v2.model.batch_create_delete_private_nat_tags_request import BatchCreateDeletePrivateNatTagsRequest
from huaweicloudsdknat.v2.model.batch_create_delete_private_nat_tags_response import BatchCreateDeletePrivateNatTagsResponse
from huaweicloudsdknat.v2.model.batch_create_delete_transit_ip_tags_request import BatchCreateDeleteTransitIpTagsRequest
from huaweicloudsdknat.v2.model.batch_create_delete_transit_ip_tags_response import BatchCreateDeleteTransitIpTagsResponse
from huaweicloudsdknat.v2.model.batch_create_nat_gateway_dnat_rules_request import BatchCreateNatGatewayDnatRulesRequest
from huaweicloudsdknat.v2.model.batch_create_nat_gateway_dnat_rules_request_body import BatchCreateNatGatewayDnatRulesRequestBody
from huaweicloudsdknat.v2.model.batch_create_nat_gateway_dnat_rules_response import BatchCreateNatGatewayDnatRulesResponse
from huaweicloudsdknat.v2.model.batch_operate_resource_tags_request_body import BatchOperateResourceTagsRequestBody
from huaweicloudsdknat.v2.model.creat_transit_ip_option import CreatTransitIpOption
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_option import CreateNatGatewayDnatOption
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_option import CreateNatGatewayDnatRuleOption
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_request import CreateNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_dnat_rule_response import CreateNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_option import CreateNatGatewayOption
from huaweicloudsdknat.v2.model.create_nat_gateway_request import CreateNatGatewayRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_request_body import CreateNatGatewayRequestBody
from huaweicloudsdknat.v2.model.create_nat_gateway_response import CreateNatGatewayResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_option import CreateNatGatewaySnatRuleOption
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_request import CreateNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_request_option import CreateNatGatewaySnatRuleRequestOption
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_response import CreateNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.create_nat_gateway_snat_rule_response_body import CreateNatGatewaySnatRuleResponseBody
from huaweicloudsdknat.v2.model.create_private_dnat_option import CreatePrivateDnatOption
from huaweicloudsdknat.v2.model.create_private_dnat_option_body import CreatePrivateDnatOptionBody
from huaweicloudsdknat.v2.model.create_private_dnat_request import CreatePrivateDnatRequest
from huaweicloudsdknat.v2.model.create_private_dnat_response import CreatePrivateDnatResponse
from huaweicloudsdknat.v2.model.create_private_nat_option import CreatePrivateNatOption
from huaweicloudsdknat.v2.model.create_private_nat_request import CreatePrivateNatRequest
from huaweicloudsdknat.v2.model.create_private_nat_request_body import CreatePrivateNatRequestBody
from huaweicloudsdknat.v2.model.create_private_nat_response import CreatePrivateNatResponse
from huaweicloudsdknat.v2.model.create_private_nat_tag_request import CreatePrivateNatTagRequest
from huaweicloudsdknat.v2.model.create_private_nat_tag_response import CreatePrivateNatTagResponse
from huaweicloudsdknat.v2.model.create_private_snat_option import CreatePrivateSnatOption
from huaweicloudsdknat.v2.model.create_private_snat_option_body import CreatePrivateSnatOptionBody
from huaweicloudsdknat.v2.model.create_private_snat_request import CreatePrivateSnatRequest
from huaweicloudsdknat.v2.model.create_private_snat_response import CreatePrivateSnatResponse
from huaweicloudsdknat.v2.model.create_resource_tag_request_body import CreateResourceTagRequestBody
from huaweicloudsdknat.v2.model.create_transit_ip_request import CreateTransitIpRequest
from huaweicloudsdknat.v2.model.create_transit_ip_request_body import CreateTransitIpRequestBody
from huaweicloudsdknat.v2.model.create_transit_ip_response import CreateTransitIpResponse
from huaweicloudsdknat.v2.model.create_transit_ip_tag_request import CreateTransitIpTagRequest
from huaweicloudsdknat.v2.model.create_transit_ip_tag_response import CreateTransitIpTagResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_dnat_rule_request import DeleteNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_dnat_rule_response import DeleteNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_request import DeleteNatGatewayRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_response import DeleteNatGatewayResponse
from huaweicloudsdknat.v2.model.delete_nat_gateway_snat_rule_request import DeleteNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.delete_nat_gateway_snat_rule_response import DeleteNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.delete_private_dnat_request import DeletePrivateDnatRequest
from huaweicloudsdknat.v2.model.delete_private_dnat_response import DeletePrivateDnatResponse
from huaweicloudsdknat.v2.model.delete_private_nat_request import DeletePrivateNatRequest
from huaweicloudsdknat.v2.model.delete_private_nat_response import DeletePrivateNatResponse
from huaweicloudsdknat.v2.model.delete_private_nat_tag_request import DeletePrivateNatTagRequest
from huaweicloudsdknat.v2.model.delete_private_nat_tag_response import DeletePrivateNatTagResponse
from huaweicloudsdknat.v2.model.delete_private_snat_request import DeletePrivateSnatRequest
from huaweicloudsdknat.v2.model.delete_private_snat_response import DeletePrivateSnatResponse
from huaweicloudsdknat.v2.model.delete_transit_ip_request import DeleteTransitIpRequest
from huaweicloudsdknat.v2.model.delete_transit_ip_response import DeleteTransitIpResponse
from huaweicloudsdknat.v2.model.delete_transit_ip_tag_request import DeleteTransitIpTagRequest
from huaweicloudsdknat.v2.model.delete_transit_ip_tag_response import DeleteTransitIpTagResponse
from huaweicloudsdknat.v2.model.downlink_vpc import DownlinkVpc
from huaweicloudsdknat.v2.model.downlink_vpc_option import DownlinkVpcOption
from huaweicloudsdknat.v2.model.list_nat_gateway_dnat_rules_request import ListNatGatewayDnatRulesRequest
from huaweicloudsdknat.v2.model.list_nat_gateway_dnat_rules_response import ListNatGatewayDnatRulesResponse
from huaweicloudsdknat.v2.model.list_nat_gateway_snat_rules_request import ListNatGatewaySnatRulesRequest
from huaweicloudsdknat.v2.model.list_nat_gateway_snat_rules_response import ListNatGatewaySnatRulesResponse
from huaweicloudsdknat.v2.model.list_nat_gateways_request import ListNatGatewaysRequest
from huaweicloudsdknat.v2.model.list_nat_gateways_response import ListNatGatewaysResponse
from huaweicloudsdknat.v2.model.list_private_dnats_request import ListPrivateDnatsRequest
from huaweicloudsdknat.v2.model.list_private_dnats_response import ListPrivateDnatsResponse
from huaweicloudsdknat.v2.model.list_private_nat_tags_request import ListPrivateNatTagsRequest
from huaweicloudsdknat.v2.model.list_private_nat_tags_response import ListPrivateNatTagsResponse
from huaweicloudsdknat.v2.model.list_private_nats_by_tags_request import ListPrivateNatsByTagsRequest
from huaweicloudsdknat.v2.model.list_private_nats_by_tags_response import ListPrivateNatsByTagsResponse
from huaweicloudsdknat.v2.model.list_private_nats_request import ListPrivateNatsRequest
from huaweicloudsdknat.v2.model.list_private_nats_response import ListPrivateNatsResponse
from huaweicloudsdknat.v2.model.list_private_snats_request import ListPrivateSnatsRequest
from huaweicloudsdknat.v2.model.list_private_snats_response import ListPrivateSnatsResponse
from huaweicloudsdknat.v2.model.list_tag_resource_instances_request_body import ListTagResourceInstancesRequestBody
from huaweicloudsdknat.v2.model.list_transit_ip_tags_request import ListTransitIpTagsRequest
from huaweicloudsdknat.v2.model.list_transit_ip_tags_response import ListTransitIpTagsResponse
from huaweicloudsdknat.v2.model.list_transit_ips_by_tags_request import ListTransitIpsByTagsRequest
from huaweicloudsdknat.v2.model.list_transit_ips_by_tags_response import ListTransitIpsByTagsResponse
from huaweicloudsdknat.v2.model.list_transit_ips_request import ListTransitIpsRequest
from huaweicloudsdknat.v2.model.list_transit_ips_response import ListTransitIpsResponse
from huaweicloudsdknat.v2.model.match import Match
from huaweicloudsdknat.v2.model.nat_gateway_dnat_rule_response_body import NatGatewayDnatRuleResponseBody
from huaweicloudsdknat.v2.model.nat_gateway_response_body import NatGatewayResponseBody
from huaweicloudsdknat.v2.model.nat_gateway_snat_rule_response_body import NatGatewaySnatRuleResponseBody
from huaweicloudsdknat.v2.model.nat_gateway_update_snat_rule_response_body import NatGatewayUpdateSnatRuleResponseBody
from huaweicloudsdknat.v2.model.page_info import PageInfo
from huaweicloudsdknat.v2.model.private_dnat import PrivateDnat
from huaweicloudsdknat.v2.model.private_nat import PrivateNat
from huaweicloudsdknat.v2.model.private_snat import PrivateSnat
from huaweicloudsdknat.v2.model.private_tag import PrivateTag
from huaweicloudsdknat.v2.model.resource import Resource
from huaweicloudsdknat.v2.model.resource_tag import ResourceTag
from huaweicloudsdknat.v2.model.show_nat_gateway_dnat_rule_request import ShowNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_dnat_rule_response import ShowNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.show_nat_gateway_request import ShowNatGatewayRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_response import ShowNatGatewayResponse
from huaweicloudsdknat.v2.model.show_nat_gateway_snat_rule_request import ShowNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.show_nat_gateway_snat_rule_response import ShowNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.show_private_dnat_request import ShowPrivateDnatRequest
from huaweicloudsdknat.v2.model.show_private_dnat_response import ShowPrivateDnatResponse
from huaweicloudsdknat.v2.model.show_private_nat_request import ShowPrivateNatRequest
from huaweicloudsdknat.v2.model.show_private_nat_response import ShowPrivateNatResponse
from huaweicloudsdknat.v2.model.show_private_nat_tags_request import ShowPrivateNatTagsRequest
from huaweicloudsdknat.v2.model.show_private_nat_tags_response import ShowPrivateNatTagsResponse
from huaweicloudsdknat.v2.model.show_private_snat_request import ShowPrivateSnatRequest
from huaweicloudsdknat.v2.model.show_private_snat_response import ShowPrivateSnatResponse
from huaweicloudsdknat.v2.model.show_transit_ip_request import ShowTransitIpRequest
from huaweicloudsdknat.v2.model.show_transit_ip_response import ShowTransitIpResponse
from huaweicloudsdknat.v2.model.show_transit_ip_tags_request import ShowTransitIpTagsRequest
from huaweicloudsdknat.v2.model.show_transit_ip_tags_response import ShowTransitIpTagsResponse
from huaweicloudsdknat.v2.model.tag import Tag
from huaweicloudsdknat.v2.model.tags import Tags
from huaweicloudsdknat.v2.model.transit_ip import TransitIp
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_option import UpdateNatGatewayDnatRuleOption
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_request import UpdateNatGatewayDnatRuleRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_request_body import UpdateNatGatewayDnatRuleRequestBody
from huaweicloudsdknat.v2.model.update_nat_gateway_dnat_rule_response import UpdateNatGatewayDnatRuleResponse
from huaweicloudsdknat.v2.model.update_nat_gateway_option import UpdateNatGatewayOption
from huaweicloudsdknat.v2.model.update_nat_gateway_request import UpdateNatGatewayRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_request_body import UpdateNatGatewayRequestBody
from huaweicloudsdknat.v2.model.update_nat_gateway_response import UpdateNatGatewayResponse
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_option import UpdateNatGatewaySnatRuleOption
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_request import UpdateNatGatewaySnatRuleRequest
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_request_option import UpdateNatGatewaySnatRuleRequestOption
from huaweicloudsdknat.v2.model.update_nat_gateway_snat_rule_response import UpdateNatGatewaySnatRuleResponse
from huaweicloudsdknat.v2.model.update_private_dnat_option import UpdatePrivateDnatOption
from huaweicloudsdknat.v2.model.update_private_dnat_request import UpdatePrivateDnatRequest
from huaweicloudsdknat.v2.model.update_private_dnat_request_body import UpdatePrivateDnatRequestBody
from huaweicloudsdknat.v2.model.update_private_dnat_response import UpdatePrivateDnatResponse
from huaweicloudsdknat.v2.model.update_private_nat_option import UpdatePrivateNatOption
from huaweicloudsdknat.v2.model.update_private_nat_request import UpdatePrivateNatRequest
from huaweicloudsdknat.v2.model.update_private_nat_request_body import UpdatePrivateNatRequestBody
from huaweicloudsdknat.v2.model.update_private_nat_response import UpdatePrivateNatResponse
from huaweicloudsdknat.v2.model.update_private_snat_option import UpdatePrivateSnatOption
from huaweicloudsdknat.v2.model.update_private_snat_option_body import UpdatePrivateSnatOptionBody
from huaweicloudsdknat.v2.model.update_private_snat_request import UpdatePrivateSnatRequest
from huaweicloudsdknat.v2.model.update_private_snat_response import UpdatePrivateSnatResponse
