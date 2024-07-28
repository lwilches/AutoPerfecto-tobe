provider "aws" {
    region = var.aws_region
    profile = var.user_aws_profile
}

# Crear el repositorio ECR api de autenticacion 
resource "aws_ecr_repository" "auth_api" {
    name = "autoperfecto-auth-api"
}

# Crear el repositorio ECR api de negocio
resource "aws_ecr_repository" "business_api" {
    name = "autoperfecto-business-api"
}

# Usar un rol IAM para Elastic Beanstalk
data "aws_iam_role" "beanstalk_role" {
    name = "beanstalk_role"
}

# Referenciar el rol de servicio existente
data "aws_iam_role" "beanstalk_service_role" {
    name = "aws-elasticbeanstalk-service-role"
}



# Crear un perfil de instancia
resource "aws_iam_instance_profile" "beanstalk_profile" {
    name = "beanstalk-instance-profile"
    role = data.aws_iam_role.beanstalk_role.name
}

# Crear app beanstalk para auth_api 
resource "aws_elastic_beanstalk_application" "app_auth_api" {
    name        = var.app_name_auth_api
    description = "Elastic Beanstalk application for ${var.app_name_auth_api}"
}
# Crear enviroment beanstalk para auth_api 
resource "aws_elastic_beanstalk_environment" "qa_auth_api" {
    name                = "${var.app_name_auth_api}-qa"
    application         = aws_elastic_beanstalk_application.app_auth_api.name
    solution_stack_name = "64bit Amazon Linux 2023 v4.3.4 running Docker"
    depends_on = [ aws_elastic_beanstalk_application.app_auth_api ]

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


# Crear app beanstalk para business api 
resource "aws_elastic_beanstalk_application" "app_business_api" {
    name        = var.app_name_business_api
    description = "Elastic Beanstalk application for ${var.app_name_business_api}"
}
# Crear enviroment beanstalk para auth_api 
resource "aws_elastic_beanstalk_environment" "qa_business_api" {
    name                = "${var.app_name_business_api}-qa"
    application         = aws_elastic_beanstalk_application.app_business_api.name
    solution_stack_name = "64bit Amazon Linux 2023 v4.3.4 running Docker"
    depends_on = [ aws_elastic_beanstalk_application.app_business_api ]

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