provider "aws" {
    region = var.aws_region
    profile = var.user_aws_profile
}


# Crear un rol IAM para Elastic Beanstalk
resource "aws_iam_role" "beanstalk_role" {
    name = "beanstalk-role"

    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Action = "sts:AssumeRole"
            Effect = "Allow"
            Principal = {
            Service = "ec2.amazonaws.com"
            }
        },
        ]
    })
}

# Adjuntar una política gestionada de AWS al rol
resource "aws_iam_role_policy_attachment" "beanstalk_policy" {
    role       = aws_iam_role.beanstalk_role.name
    policy_arn = "arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier"
}

# Crear un perfil de instancia
resource "aws_iam_instance_profile" "beanstalk_profile" {
    name = "beanstalk-instance-profile"
    role = aws_iam_role.beanstalk_role.name
}

# Referenciar el rol de servicio existente
data "aws_iam_role" "beanstalk_service_role" {
    name = "aws-elasticbeanstalk-service-role"
}



resource "aws_elastic_beanstalk_application" "app" {
    name        = var.app_name
    description = "Elastic Beanstalk application for ${var.app_name}"
}


resource "aws_elastic_beanstalk_environment" "qa" {
    name                = "${var.app_name}-qa"
    application         = aws_elastic_beanstalk_application.app.name
    solution_stack_name = "64bit Amazon Linux 2023 v4.3.4 running Docker"
    depends_on = [ aws_elastic_beanstalk_application.app ]



    setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "InstanceType"
        value     = "t2.micro"
    }

    setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "IamInstanceProfile"
        value     = aws_iam_instance_profile.beanstalk_profile.name
    }


    setting {
        namespace = "aws:autoscaling:launchconfiguration"
        name      = "InstanceType"
        value     = "t2.micro"
    }

    setting {
        namespace = "aws:elasticbeanstalk:environment:proxy"
        name      = "ProxyServer"
        value     = "nginx"
    }

    setting {
        namespace = "aws:elasticbeanstalk:environment"
        name      = "ServiceRole"
        value     = data.aws_iam_role.beanstalk_service_role.arn
    }


}