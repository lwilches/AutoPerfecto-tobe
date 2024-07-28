variable "aws_region" {
    description = "The AWS region to deploy in"
    type        = string
    default     = "us-east-1"
}

variable "user_aws_profile"{
    description = "profile de usario de conexion a aws "
    type = string
    default = "profile user-iac-beanstalk-resources"
}

variable "app_name" {
    description = "The name of the Elastic Beanstalk application"
    type        = string
    default     = "auto-perfecto-auth-api"
}


variable "plataform_name" {
    description = "The name of the Elastic Beanstalk "
    type        = string
    default     = "auto-perfecto-apps"
}

variable "env_name" {
    description = "The name of the Elastic Beanstalk environment"
    type        = string
    default     =  "auto-perfecto-auth-api-qa"
}