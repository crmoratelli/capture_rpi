from globals import marshmallow
from marshmallow import fields, post_load

class RecordSchema(marshmallow.Schema):
    class Meta:
        fields = ("status", "msg")

record_schema = RecordSchema()

