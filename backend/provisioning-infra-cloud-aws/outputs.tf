output "application_name_auth_api" {
    description = "The name of the Elastic Beanstalk application"
    value       = aws_elastic_beanstalk_application.app_auth_api.name
}

output "application_url_auth_api" {
    description = "url del servicio"
    value = aws_elastic_beanstalk_environment.qa_auth_api.endpoint_url
}
