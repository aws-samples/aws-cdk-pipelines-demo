buildspec = {
    "version":"0.2",

    "phases": {
        "install" : {
            "runtime-versions": {
                    "python": 3.8,
                    "docker": 19
            },
        },

        "pre_build" : {
            "commands": [
                    'echo Logging in to Amazon ECR...',
                    'echo $AWS_DEFAULT_REGION',
                    'echo $AWS_ACCOUNT_ID',
                    'aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com'
                    ],

        },

        "build" : {
            "commands": [
                    'echo Building image...',
                    'echo $IMAGE_REPO_NAME',
                    'echo $IMAGE_TAG',
                    'docker build --no-cache -t $IMAGE_REPO_NAME:$IMAGE_TAG .',
                    'docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $IMAGE_REPO_NAME:$IMAGE_TAG',
            ],
        },

        "post_build" : {
            "commands": [
                    'echo Pushing the Docker images...',
                    'docker push $IMAGE_REPO_NAME:$IMAGE_TAG',
                    'echo Build completed',
            ],
        },
    },
}