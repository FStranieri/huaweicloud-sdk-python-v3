# coding: utf-8

from __future__ import absolute_import

# import RmsClient
from huaweicloudsdkrms.v1.rms_client import RmsClient
from huaweicloudsdkrms.v1.rms_async_client import RmsAsyncClient
# import models into sdk package
from huaweicloudsdkrms.v1.model.account_aggregation_source import AccountAggregationSource
from huaweicloudsdkrms.v1.model.aggregate_compliance_detail_request import AggregateComplianceDetailRequest
from huaweicloudsdkrms.v1.model.aggregate_discovered_resource_counts_request import AggregateDiscoveredResourceCountsRequest
from huaweicloudsdkrms.v1.model.aggregate_discovered_resources_request import AggregateDiscoveredResourcesRequest
from huaweicloudsdkrms.v1.model.aggregate_policy_assignment_detail_request import AggregatePolicyAssignmentDetailRequest
from huaweicloudsdkrms.v1.model.aggregate_policy_assignments import AggregatePolicyAssignments
from huaweicloudsdkrms.v1.model.aggregate_policy_assignments_filters import AggregatePolicyAssignmentsFilters
from huaweicloudsdkrms.v1.model.aggregate_policy_assignments_request import AggregatePolicyAssignmentsRequest
from huaweicloudsdkrms.v1.model.aggregate_policy_compliance_summary_result import AggregatePolicyComplianceSummaryResult
from huaweicloudsdkrms.v1.model.aggregate_policy_states_request import AggregatePolicyStatesRequest
from huaweicloudsdkrms.v1.model.aggregate_resource_config_request import AggregateResourceConfigRequest
from huaweicloudsdkrms.v1.model.aggregated_source_status import AggregatedSourceStatus
from huaweicloudsdkrms.v1.model.aggregation_authorization_request import AggregationAuthorizationRequest
from huaweicloudsdkrms.v1.model.aggregation_authorization_resp import AggregationAuthorizationResp
from huaweicloudsdkrms.v1.model.channel_config_body import ChannelConfigBody
from huaweicloudsdkrms.v1.model.collect_all_resources_summary_request import CollectAllResourcesSummaryRequest
from huaweicloudsdkrms.v1.model.collect_all_resources_summary_response import CollectAllResourcesSummaryResponse
from huaweicloudsdkrms.v1.model.compliance import Compliance
from huaweicloudsdkrms.v1.model.configuration_aggregator_request import ConfigurationAggregatorRequest
from huaweicloudsdkrms.v1.model.configuration_aggregator_resp import ConfigurationAggregatorResp
from huaweicloudsdkrms.v1.model.count_all_resources_request import CountAllResourcesRequest
from huaweicloudsdkrms.v1.model.count_all_resources_response import CountAllResourcesResponse
from huaweicloudsdkrms.v1.model.create_aggregation_authorization_request import CreateAggregationAuthorizationRequest
from huaweicloudsdkrms.v1.model.create_aggregation_authorization_response import CreateAggregationAuthorizationResponse
from huaweicloudsdkrms.v1.model.create_configuration_aggregator_request import CreateConfigurationAggregatorRequest
from huaweicloudsdkrms.v1.model.create_configuration_aggregator_response import CreateConfigurationAggregatorResponse
from huaweicloudsdkrms.v1.model.create_organization_policy_assignment_request import CreateOrganizationPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.create_organization_policy_assignment_response import CreateOrganizationPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.create_policy_assignments_request import CreatePolicyAssignmentsRequest
from huaweicloudsdkrms.v1.model.create_policy_assignments_response import CreatePolicyAssignmentsResponse
from huaweicloudsdkrms.v1.model.create_stored_query_request import CreateStoredQueryRequest
from huaweicloudsdkrms.v1.model.create_stored_query_response import CreateStoredQueryResponse
from huaweicloudsdkrms.v1.model.create_tracker_config_request import CreateTrackerConfigRequest
from huaweicloudsdkrms.v1.model.create_tracker_config_response import CreateTrackerConfigResponse
from huaweicloudsdkrms.v1.model.custom_policy import CustomPolicy
from huaweicloudsdkrms.v1.model.delete_aggregation_authorization_request import DeleteAggregationAuthorizationRequest
from huaweicloudsdkrms.v1.model.delete_aggregation_authorization_response import DeleteAggregationAuthorizationResponse
from huaweicloudsdkrms.v1.model.delete_configuration_aggregator_request import DeleteConfigurationAggregatorRequest
from huaweicloudsdkrms.v1.model.delete_configuration_aggregator_response import DeleteConfigurationAggregatorResponse
from huaweicloudsdkrms.v1.model.delete_organization_policy_assignment_request import DeleteOrganizationPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.delete_organization_policy_assignment_response import DeleteOrganizationPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.delete_pending_aggregation_request_request import DeletePendingAggregationRequestRequest
from huaweicloudsdkrms.v1.model.delete_pending_aggregation_request_response import DeletePendingAggregationRequestResponse
from huaweicloudsdkrms.v1.model.delete_policy_assignment_request import DeletePolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.delete_policy_assignment_response import DeletePolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.delete_stored_query_request import DeleteStoredQueryRequest
from huaweicloudsdkrms.v1.model.delete_stored_query_response import DeleteStoredQueryResponse
from huaweicloudsdkrms.v1.model.delete_tracker_config_request import DeleteTrackerConfigRequest
from huaweicloudsdkrms.v1.model.delete_tracker_config_response import DeleteTrackerConfigResponse
from huaweicloudsdkrms.v1.model.disable_policy_assignment_request import DisablePolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.disable_policy_assignment_response import DisablePolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.enable_policy_assignment_request import EnablePolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.enable_policy_assignment_response import EnablePolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.grouped_resource_count import GroupedResourceCount
from huaweicloudsdkrms.v1.model.history_item import HistoryItem
from huaweicloudsdkrms.v1.model.list_aggregate_compliance_by_policy_assignment_request import ListAggregateComplianceByPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.list_aggregate_compliance_by_policy_assignment_response import ListAggregateComplianceByPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.list_aggregate_discovered_resources_request import ListAggregateDiscoveredResourcesRequest
from huaweicloudsdkrms.v1.model.list_aggregate_discovered_resources_response import ListAggregateDiscoveredResourcesResponse
from huaweicloudsdkrms.v1.model.list_aggregation_authorizations_request import ListAggregationAuthorizationsRequest
from huaweicloudsdkrms.v1.model.list_aggregation_authorizations_response import ListAggregationAuthorizationsResponse
from huaweicloudsdkrms.v1.model.list_all_resources_request import ListAllResourcesRequest
from huaweicloudsdkrms.v1.model.list_all_resources_response import ListAllResourcesResponse
from huaweicloudsdkrms.v1.model.list_all_tags_request import ListAllTagsRequest
from huaweicloudsdkrms.v1.model.list_all_tags_response import ListAllTagsResponse
from huaweicloudsdkrms.v1.model.list_built_in_policy_definitions_request import ListBuiltInPolicyDefinitionsRequest
from huaweicloudsdkrms.v1.model.list_built_in_policy_definitions_response import ListBuiltInPolicyDefinitionsResponse
from huaweicloudsdkrms.v1.model.list_configuration_aggregators_request import ListConfigurationAggregatorsRequest
from huaweicloudsdkrms.v1.model.list_configuration_aggregators_response import ListConfigurationAggregatorsResponse
from huaweicloudsdkrms.v1.model.list_organization_policy_assignments_request import ListOrganizationPolicyAssignmentsRequest
from huaweicloudsdkrms.v1.model.list_organization_policy_assignments_response import ListOrganizationPolicyAssignmentsResponse
from huaweicloudsdkrms.v1.model.list_pending_aggregation_requests_request import ListPendingAggregationRequestsRequest
from huaweicloudsdkrms.v1.model.list_pending_aggregation_requests_response import ListPendingAggregationRequestsResponse
from huaweicloudsdkrms.v1.model.list_policy_assignments_request import ListPolicyAssignmentsRequest
from huaweicloudsdkrms.v1.model.list_policy_assignments_response import ListPolicyAssignmentsResponse
from huaweicloudsdkrms.v1.model.list_policy_states_by_assignment_id_request import ListPolicyStatesByAssignmentIdRequest
from huaweicloudsdkrms.v1.model.list_policy_states_by_assignment_id_response import ListPolicyStatesByAssignmentIdResponse
from huaweicloudsdkrms.v1.model.list_policy_states_by_domain_id_request import ListPolicyStatesByDomainIdRequest
from huaweicloudsdkrms.v1.model.list_policy_states_by_domain_id_response import ListPolicyStatesByDomainIdResponse
from huaweicloudsdkrms.v1.model.list_policy_states_by_resource_id_request import ListPolicyStatesByResourceIdRequest
from huaweicloudsdkrms.v1.model.list_policy_states_by_resource_id_response import ListPolicyStatesByResourceIdResponse
from huaweicloudsdkrms.v1.model.list_providers_request import ListProvidersRequest
from huaweicloudsdkrms.v1.model.list_providers_response import ListProvidersResponse
from huaweicloudsdkrms.v1.model.list_regions_request import ListRegionsRequest
from huaweicloudsdkrms.v1.model.list_regions_response import ListRegionsResponse
from huaweicloudsdkrms.v1.model.list_resources_request import ListResourcesRequest
from huaweicloudsdkrms.v1.model.list_resources_response import ListResourcesResponse
from huaweicloudsdkrms.v1.model.list_schemas_request import ListSchemasRequest
from huaweicloudsdkrms.v1.model.list_schemas_response import ListSchemasResponse
from huaweicloudsdkrms.v1.model.list_stored_queries_request import ListStoredQueriesRequest
from huaweicloudsdkrms.v1.model.list_stored_queries_response import ListStoredQueriesResponse
from huaweicloudsdkrms.v1.model.managed_policy_assignment_metadata import ManagedPolicyAssignmentMetadata
from huaweicloudsdkrms.v1.model.organization_policy_assignment_detailed_status_response import OrganizationPolicyAssignmentDetailedStatusResponse
from huaweicloudsdkrms.v1.model.organization_policy_assignment_request import OrganizationPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.organization_policy_assignment_response import OrganizationPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.organization_policy_assignment_status_response import OrganizationPolicyAssignmentStatusResponse
from huaweicloudsdkrms.v1.model.page_info import PageInfo
from huaweicloudsdkrms.v1.model.pending_aggregation_request import PendingAggregationRequest
from huaweicloudsdkrms.v1.model.policy_assignment import PolicyAssignment
from huaweicloudsdkrms.v1.model.policy_assignment_request_body import PolicyAssignmentRequestBody
from huaweicloudsdkrms.v1.model.policy_compliance_summary_unit import PolicyComplianceSummaryUnit
from huaweicloudsdkrms.v1.model.policy_definition import PolicyDefinition
from huaweicloudsdkrms.v1.model.policy_filter_definition import PolicyFilterDefinition
from huaweicloudsdkrms.v1.model.policy_parameter_definition import PolicyParameterDefinition
from huaweicloudsdkrms.v1.model.policy_parameter_value import PolicyParameterValue
from huaweicloudsdkrms.v1.model.policy_resource import PolicyResource
from huaweicloudsdkrms.v1.model.policy_state import PolicyState
from huaweicloudsdkrms.v1.model.policy_state_request_body import PolicyStateRequestBody
from huaweicloudsdkrms.v1.model.query_info import QueryInfo
from huaweicloudsdkrms.v1.model.query_run_request_body import QueryRunRequestBody
from huaweicloudsdkrms.v1.model.region import Region
from huaweicloudsdkrms.v1.model.resource_counts_filters import ResourceCountsFilters
from huaweicloudsdkrms.v1.model.resource_entity import ResourceEntity
from huaweicloudsdkrms.v1.model.resource_identifier import ResourceIdentifier
from huaweicloudsdkrms.v1.model.resource_provider_response import ResourceProviderResponse
from huaweicloudsdkrms.v1.model.resource_relation import ResourceRelation
from huaweicloudsdkrms.v1.model.resource_schema_response import ResourceSchemaResponse
from huaweicloudsdkrms.v1.model.resource_summary_response_item import ResourceSummaryResponseItem
from huaweicloudsdkrms.v1.model.resource_summary_response_item_regions import ResourceSummaryResponseItemRegions
from huaweicloudsdkrms.v1.model.resource_summary_response_item_types import ResourceSummaryResponseItemTypes
from huaweicloudsdkrms.v1.model.resource_type_response import ResourceTypeResponse
from huaweicloudsdkrms.v1.model.resources_filters import ResourcesFilters
from huaweicloudsdkrms.v1.model.run_aggregate_resource_query_request import RunAggregateResourceQueryRequest
from huaweicloudsdkrms.v1.model.run_aggregate_resource_query_response import RunAggregateResourceQueryResponse
from huaweicloudsdkrms.v1.model.run_evaluation_by_policy_assignment_id_request import RunEvaluationByPolicyAssignmentIdRequest
from huaweicloudsdkrms.v1.model.run_evaluation_by_policy_assignment_id_response import RunEvaluationByPolicyAssignmentIdResponse
from huaweicloudsdkrms.v1.model.run_query_request import RunQueryRequest
from huaweicloudsdkrms.v1.model.run_query_response import RunQueryResponse
from huaweicloudsdkrms.v1.model.selector_config_body import SelectorConfigBody
from huaweicloudsdkrms.v1.model.show_aggregate_compliance_details_by_policy_assignment_request import ShowAggregateComplianceDetailsByPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.show_aggregate_compliance_details_by_policy_assignment_response import ShowAggregateComplianceDetailsByPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.show_aggregate_discovered_resource_counts_request import ShowAggregateDiscoveredResourceCountsRequest
from huaweicloudsdkrms.v1.model.show_aggregate_discovered_resource_counts_response import ShowAggregateDiscoveredResourceCountsResponse
from huaweicloudsdkrms.v1.model.show_aggregate_policy_assignment_detail_request import ShowAggregatePolicyAssignmentDetailRequest
from huaweicloudsdkrms.v1.model.show_aggregate_policy_assignment_detail_response import ShowAggregatePolicyAssignmentDetailResponse
from huaweicloudsdkrms.v1.model.show_aggregate_policy_state_compliance_summary_request import ShowAggregatePolicyStateComplianceSummaryRequest
from huaweicloudsdkrms.v1.model.show_aggregate_policy_state_compliance_summary_response import ShowAggregatePolicyStateComplianceSummaryResponse
from huaweicloudsdkrms.v1.model.show_aggregate_resource_config_request import ShowAggregateResourceConfigRequest
from huaweicloudsdkrms.v1.model.show_aggregate_resource_config_response import ShowAggregateResourceConfigResponse
from huaweicloudsdkrms.v1.model.show_built_in_policy_definition_request import ShowBuiltInPolicyDefinitionRequest
from huaweicloudsdkrms.v1.model.show_built_in_policy_definition_response import ShowBuiltInPolicyDefinitionResponse
from huaweicloudsdkrms.v1.model.show_configuration_aggregator_request import ShowConfigurationAggregatorRequest
from huaweicloudsdkrms.v1.model.show_configuration_aggregator_response import ShowConfigurationAggregatorResponse
from huaweicloudsdkrms.v1.model.show_configuration_aggregator_sources_status_request import ShowConfigurationAggregatorSourcesStatusRequest
from huaweicloudsdkrms.v1.model.show_configuration_aggregator_sources_status_response import ShowConfigurationAggregatorSourcesStatusResponse
from huaweicloudsdkrms.v1.model.show_evaluation_state_by_assignment_id_request import ShowEvaluationStateByAssignmentIdRequest
from huaweicloudsdkrms.v1.model.show_evaluation_state_by_assignment_id_response import ShowEvaluationStateByAssignmentIdResponse
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_detailed_status_request import ShowOrganizationPolicyAssignmentDetailedStatusRequest
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_detailed_status_response import ShowOrganizationPolicyAssignmentDetailedStatusResponse
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_request import ShowOrganizationPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_response import ShowOrganizationPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_statuses_request import ShowOrganizationPolicyAssignmentStatusesRequest
from huaweicloudsdkrms.v1.model.show_organization_policy_assignment_statuses_response import ShowOrganizationPolicyAssignmentStatusesResponse
from huaweicloudsdkrms.v1.model.show_policy_assignment_request import ShowPolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.show_policy_assignment_response import ShowPolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.show_resource_by_id_request import ShowResourceByIdRequest
from huaweicloudsdkrms.v1.model.show_resource_by_id_response import ShowResourceByIdResponse
from huaweicloudsdkrms.v1.model.show_resource_detail_request import ShowResourceDetailRequest
from huaweicloudsdkrms.v1.model.show_resource_detail_response import ShowResourceDetailResponse
from huaweicloudsdkrms.v1.model.show_resource_history_request import ShowResourceHistoryRequest
from huaweicloudsdkrms.v1.model.show_resource_history_response import ShowResourceHistoryResponse
from huaweicloudsdkrms.v1.model.show_resource_relations_detail_request import ShowResourceRelationsDetailRequest
from huaweicloudsdkrms.v1.model.show_resource_relations_detail_response import ShowResourceRelationsDetailResponse
from huaweicloudsdkrms.v1.model.show_resource_relations_request import ShowResourceRelationsRequest
from huaweicloudsdkrms.v1.model.show_resource_relations_response import ShowResourceRelationsResponse
from huaweicloudsdkrms.v1.model.show_stored_query_request import ShowStoredQueryRequest
from huaweicloudsdkrms.v1.model.show_stored_query_response import ShowStoredQueryResponse
from huaweicloudsdkrms.v1.model.show_tracker_config_request import ShowTrackerConfigRequest
from huaweicloudsdkrms.v1.model.show_tracker_config_response import ShowTrackerConfigResponse
from huaweicloudsdkrms.v1.model.stored_query import StoredQuery
from huaweicloudsdkrms.v1.model.stored_query_request_body import StoredQueryRequestBody
from huaweicloudsdkrms.v1.model.tag_detail import TagDetail
from huaweicloudsdkrms.v1.model.tracker_config_body import TrackerConfigBody
from huaweicloudsdkrms.v1.model.tracker_obs_channel_config_body import TrackerOBSChannelConfigBody
from huaweicloudsdkrms.v1.model.tracker_smn_channel_config_body import TrackerSMNChannelConfigBody
from huaweicloudsdkrms.v1.model.update_configuration_aggregator_request import UpdateConfigurationAggregatorRequest
from huaweicloudsdkrms.v1.model.update_configuration_aggregator_response import UpdateConfigurationAggregatorResponse
from huaweicloudsdkrms.v1.model.update_policy_assignment_request import UpdatePolicyAssignmentRequest
from huaweicloudsdkrms.v1.model.update_policy_assignment_response import UpdatePolicyAssignmentResponse
from huaweicloudsdkrms.v1.model.update_policy_state_request import UpdatePolicyStateRequest
from huaweicloudsdkrms.v1.model.update_policy_state_response import UpdatePolicyStateResponse
from huaweicloudsdkrms.v1.model.update_stored_query_request import UpdateStoredQueryRequest
from huaweicloudsdkrms.v1.model.update_stored_query_response import UpdateStoredQueryResponse

