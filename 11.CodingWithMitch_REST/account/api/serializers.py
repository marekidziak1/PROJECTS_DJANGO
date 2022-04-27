from rest_framework import serializers
from account.models import Account
class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'email', 'username','password']
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)    #1 opcja nadawania ograniczeń
    class Meta:
        model=Account
        fields = ['pk','email','username','password','password2']
        extra_kwargs ={                                                                     #2 opcja nadawania ograniczeń
            'password': {'write_only': True}
        }
    def update(self, instance, validated_data):
        email=self.validated_data['email']                                                 #3 validated_data --> traktujesz jak cleaned_Data we forms.ModelForm
        username = self.validated_data['username']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        instance.email=email
        instance.username=username
        instance.set_password(password)
        instance.save()
        return instance
    def create(self, validated_data):
        account = Account(
            email=self.validated_data['email'],                                             #3 validated_data --> traktujesz jak cleaned_Data we forms.ModelForm
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
    

