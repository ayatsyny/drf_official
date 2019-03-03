from rest_framework import serializers
from apps.snippets.models import LANGUAGE_CHOICES, Snippet


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#
#     def create(self, validated_data):
#         """
#         Create and return a new Snippet instance, given the validate data.
#         :param validated_data:
#         :return:
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validate_data):
#         """
#
#         :param instance:
#         :param validate_data:
#         :return:
#         """
#         instance.title = validate_data.get('title', instance.title)
#         instance.code = validate_data.get('code', instance.code)
#         instance.linenos = validate_data.get('linenos', instance.linenos)
#         instance.language = validate_data.get('language', instance.language)
#         # instance.style = validate_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language')

