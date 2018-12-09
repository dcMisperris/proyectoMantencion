from apps.login.models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        #read_only_fields = ['id', 'correo']

    def create(self, validated_data):
        user = Usuario(
            email=validated_data['correo'],
            username=validated_data['nombre_compelto']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user