import json
from marshmallow import Schema, fields, validates, ValidationError


class PlayerSchema(Schema):
    name = fields.Str(required=True)
    number = fields.Int(required=True)
    height = fields.Int(strict=False)
    team = fields.Str()
    comparisons = fields.List(fields.Str())
    awards = fields.Dict(keys=fields.Str(), values=fields.List(fields.Int()))

    # Use this way to add custom validation
    @validates("team")
    def validate_team(self, value):
        if value not in ["Golden State Warriors", "LA Lakers"]:
            raise ValidationError("Must be a valid NBA team")


player_json = json.dumps(
    {
        "name": "Stephen Curry",
        "number": 30,
        "height": "191",  # OK because strict=False
        "team": "Golden State Warriors",
        "comparisons": ["Reggie Miller", "Trae Young"],
        "awards": {"MVP": [2016, 2017], "FMVP": [2022]},
    }
)


if __name__ == "__main__":

    #####################################
    # ==== Deserialise and validate ====#
    #####################################

    # Will raise ValidationError if validation fails

    try:
        result = PlayerSchema().loads(player_json)
    except ValidationError as err:
        print(err.messages)

    ##########################
    # ==== Just validate ====#
    ##########################

    # Will not raise ValidationError if validation fails
    # Returns errors as dict
    player_obj = json.loads(player_json)
    errors = PlayerSchema().validate(player_obj)
