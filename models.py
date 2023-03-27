from marshmallow import Schema, fields, validate

VALIDATE_CMD_COMMAND = ("filter", "unique", "map", "limit", "sort", "regex")

class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(VALIDATE_CMD_COMMAND))
    value = fields.Str(required=True)

class BatchRequestSchema(Schema):
    queryes = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)