# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class SFSTurboRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("SFSTURBO")

    CN_EAST_2 = Region("cn-east-2",
                        "https://sfs-turbo.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://sfs-turbo.cn-east-3.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://sfs-turbo.cn-north-1.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://sfs-turbo.cn-north-2.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://sfs-turbo.cn-north-4.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://sfs-turbo.cn-north-9.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://sfs-turbo.cn-south-1.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://sfs-turbo.cn-south-2.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://sfs-turbo.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://sfs-turbo.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://sfs-turbo.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://sfs-turbo.ap-southeast-3.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://sfs-turbo.sa-brazil-1.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://sfs-turbo.la-south-2.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://sfs-turbo.la-north-2.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://sfs-turbo.af-south-1.myhuaweicloud.com")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://sfs-turbo.na-mexico-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://sfs-turbo.tr-west-1.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://sfs-turbo.ap-southeast-4.myhuaweicloud.com")
    EU_WEST_0 = Region("eu-west-0",
                        "https://sfs.eu-west-0.myhuaweicloud.com")
    EU_WEST_101 = Region("eu-west-101",
                        "https://sfs-turbo.eu-west-101.myhuaweicloud.com")

    static_fields = {
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-north-1": CN_NORTH_1,
        "cn-north-2": CN_NORTH_2,
        "cn-north-4": CN_NORTH_4,
        "cn-north-9": CN_NORTH_9,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-south-2": LA_SOUTH_2,
        "la-north-2": LA_NORTH_2,
        "af-south-1": AF_SOUTH_1,
        "na-mexico-1": NA_MEXICO_1,
        "tr-west-1": TR_WEST_1,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "eu-west-0": EU_WEST_0,
        "eu-west-101": EU_WEST_101,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


