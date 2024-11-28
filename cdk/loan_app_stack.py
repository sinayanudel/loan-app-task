from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_rds as rds,
    aws_iam as iam,
)
from constructs import Construct


class LoanAppStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "LoanAppVPC", max_azs=2)

        # ECS Cluster
        cluster = ecs.Cluster(self, "LoanAppCluster", vpc=vpc)

        # ECR Repository
        repository = ecr.Repository(self, "LoanAppRepository")

        # RDS Database
        db_instance = rds.DatabaseInstance(
            self, "LoanAppDB",
            engine=rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_13_3),
            vpc=vpc,
            credentials=rds.Credentials.from_generated_secret("postgres"),
            multi_az=False,
            allocated_storage=20,
            max_allocated_storage=100,
            publicly_accessible=False,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
        )

        # Task Definition and Container
        task_definition = ecs.FargateTaskDefinition(self, "TaskDef")
        container = task_definition.add_container(
            "LoanAppContainer",
            image=ecs.ContainerImage.from_ecr_repository(repository),
            logging=ecs.LogDrivers.aws_logs(stream_prefix="LoanApp"),
            environment={
                "DATABASE_URL": db_instance.instance_endpoint.socket_address
            }
        )
        container.add_port_mappings(ecs.PortMapping(container_port=80))

        # Fargate Service
        service = ecs.FargateService(
            self, "LoanAppService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=1,
            assign_public_ip=False,
            security_groups=[ec2.SecurityGroup.from_security_group_id(self, "SG", vpc.vpc_default_security_group)]
        )

        # Permissions
        db_instance.connections.allow_from(service.connections, ec2.Port.tcp(5432))
