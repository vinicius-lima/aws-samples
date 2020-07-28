# AWS Fargate CI/CD sample

This sample uses a pre-built AWS CodePipeline pipeline to create a Docker image, push it to Amazon ECR and perform a blue/green deployment to Fargate.

Notice that all resources must be previously create, for example, AWS Application Load Balancer, AWS Fargate cluster, AWS ECS task definitions, etc.

A complete infrastructure could be automatic created using an [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/?id=docs_gateway) template.
