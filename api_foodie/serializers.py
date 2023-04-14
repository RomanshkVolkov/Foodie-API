from rest_framework import serializers


class MySerializer(serializers.Serializer):
    search = serializers.CharField(required=True)
    training_mode = serializers.BooleanField(required=False, default=False)

    def validate_search(self, value):
        """
        Validar el valor del parámetro de búsqueda.
        """
        if not isinstance(value, str):
            raise serializers.ValidationError(
                'El parámetro de búsqueda debe ser una cadena.')
        if len(value) < 3:
            raise serializers.ValidationError(
                'La longitud del parámetro de búsqueda debe ser de al menos 3 caracteres.')
        return value
    
    def validate_training_mode(self, value):
        """
        Validar el valor del parámetro de training_mode.
        """
        if not isinstance(value, bool):
            raise serializers.ValidationError(
                'El parámetro training_mode debe ser un booleano.')
        return value

    def to_representation(self, instance):
        """
        Devuelve un diccionario con el parámetro de búsqueda.
        """
        search = self.validated_data['search']
        training_mode = self.validated_data.get('training_mode', False)
        return {'search': search, 'training_mode': training_mode}
