## aws_cdk.aws_ec2이 모듈을 다 가져와서 ec2라고 부르겠다 예를들면 ec2.*
import aws_cdk.aws_ec2 as ec2

from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

base_name = "haedalwang"
route53_domain_name ="seungdobae.com"

class CdkEksSampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ## vpc라는 변수에 ec2.Vpc을 만들겠다 
        vpc = ec2.Vpc(self, "VPC",
            vpc_name =f"{base_name}-VPC",
            ip_addresses = ec2.IpAddresses.cidr("10.200.0.0/16"),
            availability_zones = ["ap-northeast-2a","ap-northeast-2b","ap-northeast-2c","ap-northeast-2d"],
            enable_dns_support = True,
            nat_gateways = 1,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    name=f"{base_name}-Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24  # 퍼블릭 서브넷 CIDR 블록
                ),
                ec2.SubnetConfiguration(
                    name=f"{base_name}-Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24  # 프라이빗 서브넷 CIDR 블록
                ),
            ]
        )