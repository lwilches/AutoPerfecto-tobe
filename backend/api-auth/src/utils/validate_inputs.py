from jsonschema import Draft202012Validator , ValidationError  , validate ,FormatChecker

non_empty_pattern = "^(?!\s*$).+"

# Define el esquema JSON
schema_input_create_input_user  = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "user_name": {
      "type": "string",
      "pattern": non_empty_pattern
    },
    "pwd": {
      "type": "string",
      "pattern": non_empty_pattern
    },
    "tipo_doc": {
            "type": "string",
            "enum": ["CC", "CE", "PS", "TI"]
        },
    "nro_doc": {
        "type": "string",
        "pattern": "^[0-9]{3,}$" 
    },
    "nombres": {
      "type": "string",
      "pattern": non_empty_pattern
    },
    "apellidos": {
        "type": "string",
        "pattern": non_empty_pattern
    }
  },
  "required": ["user_name", "pwd", "tipo_doc" , "nro_doc", "nombres" , "apellidos" ],
  "additionalProperties": False
}




## clase para validar jsons
class ValidateInputs():
    def validate_json_add_user(self ,data ):
        try:
            validator = Draft202012Validator(schema_input_create_input_user , format_checker=FormatChecker())
            errors = list(validator.iter_errors(data))
            if not errors:
                return ValidationResult(success=True)
            else:
                error_messages =    [ f"Field:{ error.json_path} Error: {error.message} "  for error in errors]
                combined_error_message = "\n".join(error_messages)
                return ValidationResult(success=False,  error=combined_error_message)
            
        except ValidationError as e:
                return ValidationResult(success=False, error= f"Field:* Error: {e.message} ")

## clase para gerstionar resultado
class ValidationResult:
    def __init__(self, success, error=None):
        self.success = success
        self.error = error
        
        print( f"Valido: {self.success} - Error: {self.error} ")

validator = ValidateInputs()


