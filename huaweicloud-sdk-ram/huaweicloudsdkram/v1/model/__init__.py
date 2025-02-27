# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkram.v1.model.accept_resource_share_invitation_request import AcceptResourceShareInvitationRequest
from huaweicloudsdkram.v1.model.accept_resource_share_invitation_response import AcceptResourceShareInvitationResponse
from huaweicloudsdkram.v1.model.associate_permission_req_body import AssociatePermissionReqBody
from huaweicloudsdkram.v1.model.associate_resource_share_permission_request import AssociateResourceSharePermissionRequest
from huaweicloudsdkram.v1.model.associate_resource_share_permission_response import AssociateResourceSharePermissionResponse
from huaweicloudsdkram.v1.model.associate_resource_share_request import AssociateResourceShareRequest
from huaweicloudsdkram.v1.model.associate_resource_share_response import AssociateResourceShareResponse
from huaweicloudsdkram.v1.model.associated_permission import AssociatedPermission
from huaweicloudsdkram.v1.model.batch_create_resource_share_tags_request import BatchCreateResourceShareTagsRequest
from huaweicloudsdkram.v1.model.batch_create_resource_share_tags_response import BatchCreateResourceShareTagsResponse
from huaweicloudsdkram.v1.model.batch_delete_resource_share_tags_request import BatchDeleteResourceShareTagsRequest
from huaweicloudsdkram.v1.model.batch_delete_resource_share_tags_response import BatchDeleteResourceShareTagsResponse
from huaweicloudsdkram.v1.model.create_resource_share_req_body import CreateResourceShareReqBody
from huaweicloudsdkram.v1.model.create_resource_share_request import CreateResourceShareRequest
from huaweicloudsdkram.v1.model.create_resource_share_response import CreateResourceShareResponse
from huaweicloudsdkram.v1.model.delete_resource_share_request import DeleteResourceShareRequest
from huaweicloudsdkram.v1.model.delete_resource_share_response import DeleteResourceShareResponse
from huaweicloudsdkram.v1.model.disable_organization_share_request import DisableOrganizationShareRequest
from huaweicloudsdkram.v1.model.disable_organization_share_response import DisableOrganizationShareResponse
from huaweicloudsdkram.v1.model.disassociate_permission_req_body import DisassociatePermissionReqBody
from huaweicloudsdkram.v1.model.disassociate_resource_share_permission_request import DisassociateResourceSharePermissionRequest
from huaweicloudsdkram.v1.model.disassociate_resource_share_permission_response import DisassociateResourceSharePermissionResponse
from huaweicloudsdkram.v1.model.disassociate_resource_share_request import DisassociateResourceShareRequest
from huaweicloudsdkram.v1.model.disassociate_resource_share_response import DisassociateResourceShareResponse
from huaweicloudsdkram.v1.model.distinct_shared_principal import DistinctSharedPrincipal
from huaweicloudsdkram.v1.model.distinct_shared_resource import DistinctSharedResource
from huaweicloudsdkram.v1.model.enable_organization_share_request import EnableOrganizationShareRequest
from huaweicloudsdkram.v1.model.enable_organization_share_response import EnableOrganizationShareResponse
from huaweicloudsdkram.v1.model.list_permissions_request import ListPermissionsRequest
from huaweicloudsdkram.v1.model.list_permissions_response import ListPermissionsResponse
from huaweicloudsdkram.v1.model.list_quota_request import ListQuotaRequest
from huaweicloudsdkram.v1.model.list_quota_response import ListQuotaResponse
from huaweicloudsdkram.v1.model.list_resource_share_permissions_request import ListResourceSharePermissionsRequest
from huaweicloudsdkram.v1.model.list_resource_share_permissions_response import ListResourceSharePermissionsResponse
from huaweicloudsdkram.v1.model.list_resource_share_tags_request import ListResourceShareTagsRequest
from huaweicloudsdkram.v1.model.list_resource_share_tags_response import ListResourceShareTagsResponse
from huaweicloudsdkram.v1.model.list_resource_shares_by_tags_request import ListResourceSharesByTagsRequest
from huaweicloudsdkram.v1.model.list_resource_shares_by_tags_response import ListResourceSharesByTagsResponse
from huaweicloudsdkram.v1.model.match import Match
from huaweicloudsdkram.v1.model.page_info import PageInfo
from huaweicloudsdkram.v1.model.page_info_marker_by_key import PageInfoMarkerByKey
from huaweicloudsdkram.v1.model.permission import Permission
from huaweicloudsdkram.v1.model.permission_summary import PermissionSummary
from huaweicloudsdkram.v1.model.quota_resources_dto import QuotaResourcesDto
from huaweicloudsdkram.v1.model.quotas import Quotas
from huaweicloudsdkram.v1.model.reject_resource_share_invitation_request import RejectResourceShareInvitationRequest
from huaweicloudsdkram.v1.model.reject_resource_share_invitation_response import RejectResourceShareInvitationResponse
from huaweicloudsdkram.v1.model.resource_dto import ResourceDTO
from huaweicloudsdkram.v1.model.resource_share import ResourceShare
from huaweicloudsdkram.v1.model.resource_share_association import ResourceShareAssociation
from huaweicloudsdkram.v1.model.resource_share_association_req_body import ResourceShareAssociationReqBody
from huaweicloudsdkram.v1.model.resource_share_invitation import ResourceShareInvitation
from huaweicloudsdkram.v1.model.resource_shares_by_tags_req_body import ResourceSharesByTagsReqBody
from huaweicloudsdkram.v1.model.search_distinct_principals_request import SearchDistinctPrincipalsRequest
from huaweicloudsdkram.v1.model.search_distinct_principals_response import SearchDistinctPrincipalsResponse
from huaweicloudsdkram.v1.model.search_distinct_shared_principals_req_body import SearchDistinctSharedPrincipalsReqBody
from huaweicloudsdkram.v1.model.search_distinct_shared_resources_req_body import SearchDistinctSharedResourcesReqBody
from huaweicloudsdkram.v1.model.search_distinct_shared_resources_request import SearchDistinctSharedResourcesRequest
from huaweicloudsdkram.v1.model.search_distinct_shared_resources_response import SearchDistinctSharedResourcesResponse
from huaweicloudsdkram.v1.model.search_resource_share_associations_req_body import SearchResourceShareAssociationsReqBody
from huaweicloudsdkram.v1.model.search_resource_share_associations_request import SearchResourceShareAssociationsRequest
from huaweicloudsdkram.v1.model.search_resource_share_associations_response import SearchResourceShareAssociationsResponse
from huaweicloudsdkram.v1.model.search_resource_share_count_by_tags_request import SearchResourceShareCountByTagsRequest
from huaweicloudsdkram.v1.model.search_resource_share_count_by_tags_response import SearchResourceShareCountByTagsResponse
from huaweicloudsdkram.v1.model.search_resource_share_invitation_req_body import SearchResourceShareInvitationReqBody
from huaweicloudsdkram.v1.model.search_resource_share_invitation_request import SearchResourceShareInvitationRequest
from huaweicloudsdkram.v1.model.search_resource_share_invitation_response import SearchResourceShareInvitationResponse
from huaweicloudsdkram.v1.model.search_resource_shares_req_body import SearchResourceSharesReqBody
from huaweicloudsdkram.v1.model.search_resource_shares_request import SearchResourceSharesRequest
from huaweicloudsdkram.v1.model.search_resource_shares_response import SearchResourceSharesResponse
from huaweicloudsdkram.v1.model.search_shared_principals_req_body import SearchSharedPrincipalsReqBody
from huaweicloudsdkram.v1.model.search_shared_principals_request import SearchSharedPrincipalsRequest
from huaweicloudsdkram.v1.model.search_shared_principals_response import SearchSharedPrincipalsResponse
from huaweicloudsdkram.v1.model.search_shared_resources_req_body import SearchSharedResourcesReqBody
from huaweicloudsdkram.v1.model.search_shared_resources_request import SearchSharedResourcesRequest
from huaweicloudsdkram.v1.model.search_shared_resources_response import SearchSharedResourcesResponse
from huaweicloudsdkram.v1.model.shared_principal import SharedPrincipal
from huaweicloudsdkram.v1.model.shared_resource import SharedResource
from huaweicloudsdkram.v1.model.show_organization_share_request import ShowOrganizationShareRequest
from huaweicloudsdkram.v1.model.show_organization_share_response import ShowOrganizationShareResponse
from huaweicloudsdkram.v1.model.show_permission_request import ShowPermissionRequest
from huaweicloudsdkram.v1.model.show_permission_response import ShowPermissionResponse
from huaweicloudsdkram.v1.model.tag import Tag
from huaweicloudsdkram.v1.model.tag_dto import TagDTO
from huaweicloudsdkram.v1.model.tag_filter import TagFilter
from huaweicloudsdkram.v1.model.tag_resource_req_body import TagResourceReqBody
from huaweicloudsdkram.v1.model.untag import Untag
from huaweicloudsdkram.v1.model.untag_resource_req_body import UntagResourceReqBody
from huaweicloudsdkram.v1.model.update_resource_share_req_body import UpdateResourceShareReqBody
from huaweicloudsdkram.v1.model.update_resource_share_request import UpdateResourceShareRequest
from huaweicloudsdkram.v1.model.update_resource_share_response import UpdateResourceShareResponse
