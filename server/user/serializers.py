from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password", "password2", "ethereum_wallet_address")
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def save(self):
        user = get_user_model()(
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            ethereum_wallet_address=self.validated_data["ethereum_wallet_address"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords do not match!"})

        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)


from .utils import get_eth_balance

class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "is_staff", "first_name", "last_name", "balance")
    
    def get_balance(self, obj):
        # Retrieve the Ethereum wallet address from the user's profile (adjust based on your model)
        wallet_address = obj.ethereum_wallet_address
        
        if wallet_address:
            try:
                # Get balance in Wei (smallest unit of ETH)
                balance = get_eth_balance(wallet_address)
                
                return str(balance)  # Return as string to avoid float issues in JSON
            except Exception as e:
                return f"Error fetching balance: {str(e)}"
        else:
            return "No wallet address"
