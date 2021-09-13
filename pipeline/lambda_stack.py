from aws_cdk import core, aws_lambda as _lambda, aws_ecr as _ecr
import datetime

class LambdaStack(core.Stack):

    def __init__(self, app: core.App, id: str, tag, **kwargs):
        super().__init__(app, id, **kwargs)

        ecr_repo_name = core.Fn.import_value("ecr-repo-name") 

        func = _lambda.DockerImageFunction(
            self, "LambdaContainerFunction",
            code=_lambda.DockerImageCode.from_ecr(
                _ecr.Repository.from_repository_name(self, 'lambda_container_pipeline', 
                repository_name=ecr_repo_name), tag=tag),
            memory_size=1024,
            description="Function generated on {}".format(datetime.datetime.now()),
            timeout=core.Duration.seconds(30),
            )



