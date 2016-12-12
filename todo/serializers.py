from rest_framework import serializers

from models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('label', 'text', 'done')

    def validate_label(self, value):
        return self.check_str(value);

    def validate_text(self, value):
        return self.check_str(value);

    def check_str(self, value):
        if 'javascript' in str(value):
            raise serializers.ValidationError('Malicious content is blocked')
        elif '>' in str(value) or '<' in str(value):
            raise serializers.ValidationError('HTML is not allowed')
        return value