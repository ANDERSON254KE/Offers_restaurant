from rest_framework import serializers
from .models import Message, ChatRoom
from accounts.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'room',
            'content',
            'created_at'
        ]

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = [
            'id',
            'participants',
            'messages',
            'created_at'
        ] 