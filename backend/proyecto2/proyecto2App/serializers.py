from rest_framework import serializers 
from proyecto2App.models import Login, Registro, Documento
 
 
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('usuario',
                  'clave')

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('nombres',
                  'apellidos',
                  'usuario',
                  'clave')

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('codigo',
                  'hash')                  