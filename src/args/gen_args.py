from webargs import fields, validate


argsTest = {

    "name": fields.Str(
        required=True, validate=validate.Length(max=6)
    ),

    "version": fields.Int(
        required=False
    ),

    "msg": fields.Str(
        required=False, validate=validate.Length(min=6)
    )

}