output "application_name" {
    description = "The name of the Elastic Beanstalk application"
    value       = aws_elastic_beanstalk_application.app.name
}

output "application_url" {
    description = "url del servicio"
    value = aws_elastic_beanstalk_environment.qa.endpoint_url
}
