## Create schema
1. From dictionaries
2. From class (use this)
  ```python
  from marshmallow import Schema, fields
  class UserSchema(Schema):
      name = fields.Str()
      email = fields.Email()
      created_at = fields.DateTime()
  ```
  
 ## Add validations
1. Using `validates` decorator (use this)
```python
from marshmallow import fields, Schema, validates, ValidationError
class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30.")
```

## Validate
1. With deserialisation
```python
try:
    UserSchema().load(json_data)
except ValidationError as err:
    err_dict = err.messages
```
2. Without deserialisation
```python
  err_dict = UserSchema().validate(data)
```

## Partial validation
Say a schema has 10 fields and we want to patch only one field. We can validate that one specific field by setting `partial` to `True`
