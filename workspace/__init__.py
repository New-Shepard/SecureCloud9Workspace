from aws_cdk import (
    core as cdk,
    aws_ec2 as ec2,
    aws_cloud9 as cloud9,
)


class WorkspaceStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cloud9_owner_arn = self.node.try_get_context("owner_arn")

        vpc = ec2.Vpc(self, 'vpc', 
            cidr="192.168.0.0/16",
            max_azs=1,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='private',
                    subnet_type=ec2.SubnetType.PRIVATE,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name='public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
        )

        cloud9.CfnEnvironmentEC2(self, 'workspace', 
            instance_type='t3.small',
            automatic_stop_time_minutes=60,
            connection_type='CONNECT_SSM',
            subnet_id=vpc.private_subnets[0].subnet_id,
            owner_arn=cloud9_owner_arn
        )