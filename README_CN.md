[English](./README.md) | 简体中文

# 华为云开发者 Python 软件开发工具包 （Python SDK）

欢迎使用华为云 Python SDK。

华为云 Python SDK让您无需关心请求细节即可快速使用云服务器、虚拟私有云等多个华为云服务。

这里将向您介绍如何获取并使用华为云 Python SDK。

## 在线示例

[API Explorer](https://apiexplorer.developer.huaweicloud.com/apiexplorer/overview) 提供API检索及平台调试，支持全量快速检索、可视化调试、帮助文档查看、在线咨询。

## 现在开始

- 要使用华为云 Python SDK，您需要拥有云账号以及该账号对应的Access Key（AK）和Secret Access Key（SK）。 请在华为云控制台“我的凭证-访问密钥”页面上创建和查看您的AKSK。更多信息请查看[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html)。

- 华为云 Python SDK 支持 python3 及以上版本。

## SDK 获取和安装

华为云 Python SDK 支持 python3 及以上版本。执行 ``python --version`` 检查当前python的版本信息。

无论您要使用哪个产品/服务的开发工具包，都必须安装 `huaweicloudsdkcore` 。以使用虚拟私有云 VPC SDK 为例，您需要安装 `huaweicloudsdkcore` 和 `huaweicloudsdkvpc` ：

- 使用 pip 安装

    执行如下命令安装华为云 Python SDK核心库以及相关服务库:
    
    ```bash
    # 安装核心库
    pip install huaweicloudsdkcore
    
    # 安装VPC服务库
    pip install huaweicloudsdkvpc
    ```

- 使用源码安装

    执行如下命令安装华为云 Python SDK核心库以及相关服务库:
    
    ```bash
    # 安装核心库
    cd huaweicloudsdkcore-${version}
    python setup.py install
    
    # 安装VPC服务库
    cd huaweicloudsdkvpc-${version}
    python setup.py install
    ```

## 开始使用

1. 导入依赖模块:

    ``` python
    from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
    from huaweicloudsdkcore.exceptions import exceptions
    from huaweicloudsdkcore.http.http_config import HttpConfig
    # 导入指定云服务的库 huaweicloudsdk{service}
    from huaweicloudsdkvpc.v2 import *
    # 导入指定云服务的region文件 {Service}Region
    from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
    ```

2. 配置客户端属性

    2.1 默认配置

    ``` python
    # 使用默认配置
    config = HttpConfig.get_default_config()
    ```

    2.2 代理配置(可选)

    ``` python
    # 使用代理服务器（可选）
    config.proxy_protocol = 'http'
    config.proxy_host = 'proxy.huaweicloud.com'
    config.proxy_port = 80
    config.proxy_user = 'username'
    config.proxy_password = 'password'
    ```

    2.3 连接配置(可选)

    ``` python
    # 配置连接超时（可选），支持统一指定超时时长timeout=timeout，或分别指定超时时长timeout=(connect timeout, read timeout)
    config.timeout = 3
    ```

    2.4 SSL配置(可选)

    ``` python
    # 配置跳过服务端证书验证（可选）
    config.ignore_ssl_verification = True
    # 配置服务器端CA证书，用于SDK验证服务端证书合法性
    config.ssl_ca_cert = ssl_ca_cert
    ```

3. 初始化认证信息

    **说明**：
    华为云服务存在两种部署方式，Region级服务和Global级服务。Global级服务当前仅支持BSS, DevStar, EPS, IAM, RMS, TMS。
    
    Region级服务仅需要提供 projectId。Global级服务需要提供domainId。

    使用Region创建客户端场景时，projectId、domainId支持自动获取，无需再次配置。

    - `ak` 华为云账号 Access Key 。
    - `sk` 华为云账号 Secret Access Key 。
    - `project_id` 云服务所在项目 ID ，根据你想操作的项目所属区域选择对应的项目 ID 。
    - `domain_id` 华为云账号ID 。
    - `security_token` 采用临时AK/SK认证场景下的安全票据。

    3.1 使用永久AK/SK
    
    ``` python
    # Region级服务
    credentials = BasicCredentials(ak, sk, project_id)
   
    # Global级服务
    credentials = GlobalCredentials(ak, sk, domain_id)
    ```
    
    3.2 使用临时AK/SK
    
    首选需要获得临时AK、SK和SecurityToken，获取可以从永久AK/SK获得，或者通过委托授权首选获得。
    
    通过永久AK/SK获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0002.html, 对应IAM SDK 中的createTemporaryAccessKeyByToken方法。
    
    通过委托授权获得可以参考文档：https://support.huaweicloud.com/api-iam/iam_04_0101.html, 对应IAM SDK 中的createTemporaryAccessKeyByAgency方法。
    
    ``` python
    # Region级服务
    credentials = BasicCredentials(ak, sk, project_id).with_security_token(security_token)
   
    # Global级服务
    credentials = GlobalCredentials(ak, sk, domain_id).with_security_token(security_token)
    ```

4. 初始化客户端（两种方式）
    
    4.1  指定云服务Endpoint方式

    ``` python
    # 初始化指定云服务的客户端 {Service}Client ，以初始化 VpcClient 为例
    client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \  # 日志打印至文件
        .with_stream_log(log_level=logging.INFO) \                 # 日志打印至控制台
        .build()
    ```

    **说明:**

    - `endpoint` 华为云各服务应用区域和各服务的终端节点，详情请查看[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
    - `with_file_log` 支持如下配置：
        - `path`: 日志文件路径。
        - `log_level`: 日志级别，默认INFO。
        - `max_bytes`: 单个日志文件大小，默认为10485760 bytes。
        - `backup_count`: 日志文件个数，默认为5个。
    - `with_stream_log` 支持如下配置：
        - `stream`: 流对象，默认sys.stdout。
        - `log_level`: 日志级别，默认INFO。

    打开日志开关后，每次请求将打印访问日志，格式如下：'%(asctime)s %(thread)d %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s'

    ```shell script
    2020-06-16 10:44:02,019 4568 HuaweiCloud-SDK http_handler.py 28 INFO "GET https://vpc.cn-north-1.myhuaweicloud.com/v1/0904f9e1f100d2932f94c01f9aa1cfd7/vpcs" 200 11 0:00:00.543430 b5c927ffdab8401e772e70aa49972037
    ```

    4.2  指定Region方式（推荐）

    ``` python
    # 初始化指定云服务的客户端 {Service}Client ，以初始化 IamClient 为例
    client = IamClient.new_builder(IamClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(IamRegion.CN_NORTH_4) \
        .with_file_log(path="test.log", log_level=logging.INFO) \  # 日志打印至文件
        .with_stream_log(log_level=logging.INFO) \                 # 日志打印至控制台
        .build()
    ```

    **说明:**

    - 指定Region方式创建客户端场景，支持自动获取用户的regionId以及domainId，认证Credential中无需再次指定。
    - 不适用于`多ProjectId`场景。

5. 发送请求并查看响应.

    ``` python
    # 初始化请求，以调用接口 ListVpcs 为例
    request = ListVpcsRequest()
    response = client.list_vpcs(request)
    print(respones)
    ```

6. 异常处理

    | 一级分类 | 一级分类说明 | 二级分类 | 二级分类说明 |
    | :---- | :---- | :---- | :---- |
    | ConnectionException | 连接类异常 | HostUnreachableException | 网络不可达、被拒绝 |
    | | | SslHandShakeException | SSL认证异常 |
    | RequestTimeoutException | 响应超时异常 | CallTimeoutException | 单次请求，服务器处理超时未返回 |
    | | | RetryOutageException | 在重试策略消耗完成已后，仍无有效的响应 |
    | ServiceResponseException | 服务器响应异常 | ServerResponseException | 服务端内部错误，Http响应码：[500,] |
    | | | ClientRequestException | 请求参数不合法，Http响应码：[400， 500) |

    ``` python
    # 异常处理
    try:
        request = ListVpcsRequest()
        response = client.list_vpcs(request)
    except exception.ServiceResponseException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
    ```

7. 异步场景

    ``` python
    # 初始化异步客户端，以初始化 VpcAsyncClient 为例
    vpc_client = VpcAsyncClient.new_builder(VpcAsyncClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    # 发送异步请求
    request = ListVpcsRequest()
    response = client.list_vpcs_async(request)

    # 获取异步请求结果
    print(response.result())
    ```

8. 问题定位

    在某些场景下可能对业务发出的Http请求进行Debug，需要看到原始的Http请求和返回信息，SDK提供侦听器功能来获取原始的为加密的Http请求和返回信息。

    **注意：** 原始信息打印仅在debug阶段使用，请不要在生产系统中将原始的Http头和Body信息打印到日志，这些信息并未加密且其中包含敏感数据，例如所创建虚拟机的密码，IAM用户的密码等;
    当Body体为二进制内容,即Content-Type标识为二进制时 body为"***",详细内容不输出。

    ``` python
    def response_handler(**kwargs):
        logger = kwargs.get("logger")
        response = kwargs.get("response")
        request = response.request

        base = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
        if len(request.headers) != 0:
            base = base + "> Headers:" + "\n"
            for each in request.headers:
                base = base + "    %s : %s" % (each, request.headers[each]) + "\n"
        base = base + "> Body: %s" % request.body + "\n\n"

        base = base + "< Response HTTP/1.1 %s " % response.status_code + "\n"
        if len(response.headers) != 0:
            base = base + "< Headers:" + "\n"
            for each in response.headers:
                base = base + "    %s : %s" % (each, response.headers[each],) + "\n"
        base = base + "< Body: %s" % response.content
        logger.debug(base)
    
    client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .with_file_log(path="test.log", log_level=logging.INFO) \
        .with_stream_log(log_level=logging.INFO) \
        .with_http_handler(HttpHandler().add_response_handler(response_handler)) \
        .build()
    ```

       **说明:**

    HttpHandler支持如下方法add_request_handler、add_response_handler。

## 代码实例

- 使用如下代码同步查询特定 Region 下的 VPC 清单，实际使用中请将 `VpcClient` 替换为您使用的产品/服务相应的 `{Service}Client`。
- 调用前请根据实际情况替换如下变量：`{your ak string}`、 `{your sk string}`、 `{your endpoint}` 以及 `{your project id}`。

``` python
# coding: utf-8


from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkvpc.v2 import *


def list_vpc(client):
    try:
        request = ListVpcsRequest()
        response = client.list_vpcs(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == "__main__":
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    vpc_client = VpcClient.new_builder(VpcClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    list_vpc(vpc_client)
```
