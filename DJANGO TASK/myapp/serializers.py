from rest_marshmallow import  Schema, fields
from marshmallow import validate
from .models import Item
class ItemSchema(Schema):
    item = fields.String(validate=validate.OneOf(["book", "pen", "folder","bag"]))
    class Meta:
        model=Item
        fields=('id','item','status')
    
    def create(self,validated_data):
        return Item.objects.create(**validated_data)
   
