from rest_framework import serializers
from.models import CustomerUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomerUser
        fields=["id","email","username","date_joined",'is_active',
                'last_login',"first_name","last_name"]
class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomerUser
        fields=['id',"email","username","password"]
        extra_kwargs={"password":{"write_only":True}}

    def create(self, validated_data):
        user=CustomerUser(email=validated_data["email"],
            username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user