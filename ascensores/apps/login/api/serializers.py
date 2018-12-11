from apps.login.models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        #read_only_fields = ['id', 'correo']

    def createUsuario(self, validated_data):
        user = Usuario(
            correo=validated_data['correo'],
            nombre_completo=validated_data['nombre_compelto']
        )
        user.set_password(validated_data['contraseña'])
        user.save()
        return user