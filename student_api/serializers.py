from rest_framework import serializers
from .models import Path, Student
from django.utils.timezone import now

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     # id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         # instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # fields = ["id", 'first_name', "last_name", "number"]
        fields = '__all__'
        # exclude = ('id',)

    def validate_number(self, value):
        if value > 1000:
            raise serializers.ValidationError(
                "Student numberneed to be below 1000")
        return value

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days


class PathSerializer(serializers.ModelSerializer):

    # students = serializers.StringRelatedField(many=True)
 # students = StudentSerializer(many=True)
    students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Path
        fields = "__all__"
