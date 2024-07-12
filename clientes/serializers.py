from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não incluir numeros neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O rg deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"o celular deve ser padrão (98 91234-1234)"})
        return data