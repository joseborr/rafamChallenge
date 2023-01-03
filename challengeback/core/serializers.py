from core.models import Student,Friendship,Lesson
from rest_framework import serializers
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','username','created_at']

class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    friends = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Friendship
        fields = ['friends','created_at']

class FriendsForSpecificUserSerializer(serializers.HyperlinkedModelSerializer):
    friends = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field ='username'
    )
    class Meta:
        model = Student
        fields = ['id','username','created_at','friends']

class MyLessonsSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field ='name'
    )
    class Meta:
        model = Lesson
        fields = ['name','lessons','topic']