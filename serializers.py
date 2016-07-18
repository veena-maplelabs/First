from rest_framework import serializers

class MemberSerializer(serializers.Serializer):
	name = serializers.CharField()
	mobile = serializers.CharField()



class MemberPutSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField()
	mobile = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	login_id = serializers.IntegerField(read_only=True)
	college = serializers.CharField()
	spec = serializers.CharField()

