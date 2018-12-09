from apps.cliente.models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

        
        #read_only_fields = ['id', 'correo']

    # def create(self, validated_data):
    #     user = Cliente(
    #         email=validated_data['correo'],
    #         username=validated_data['nombre_compelto']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user