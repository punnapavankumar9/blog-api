from rest_framework import serializers
from django.contrib.auth.models import User

class Registrationserializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'password', 'password1']
        extra_kwargs = {
            'password': {'write_only' : True}
        }
    def save(self):
        account = User(
                        username=self.validated_data['username'],
                        email = self.validated_data['email']
                    )
        password = self.validated_data['password']
        password1 = self.validated_data['password1']
        if password1 != password:
            raise serializers.ValidationError({'error':"password fields doesn't matched"})
        account.set_password(password)
        account.save()
        return account