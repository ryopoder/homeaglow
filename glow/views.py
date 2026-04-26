from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from glow.models import User, Room
from rest_framework.decorators import action
from glow.serializers import UserSerializer, RoomSerializer
from glow.twilio_client import TwilioClient


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # TODO add permission here
    @action(methods=['post'], detail=False, url_path='create-room', url_name='create_room')
    def create_room(self, request):
        # print('we got here')
        # return response.Response("got it!")

        room_name = request.data.get('name')
        numbers_raw = request.data.get('phone_numbers', '')

        phone_list = [n.strip() for n in numbers_raw.split(',') if n.strip()]

        if not room_name:
            return Response({"error": "Room name required"}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Create the Room
        room = Room.objects.create(name=room_name, phone_numbers=numbers_raw)

        # 4. Handle Users
        for number in phone_list:
            # Create user if they don't exist; use number as username for now
            if not User.objects.filter(phone_number=number).exists():
                user = User.objects.create(phone_number=number, username=number, name='Guest User')
                room.participants.add(user)
            # try:
            #     user, created = User.objects.get_or_create(
            #         phone_number=number,
            #         defaults={'name': 'Guest User'}
            #     )
            # except Exception as e:
            #     print(e)

        # 5. Redirect to Home (or a success page)
        # TODO maybe here we fire off all the celery tasks to do this
        twilio_client = TwilioClient()
        user_phone = request.user.phone_number
        phone_list.append(user_phone)
        for num in phone_list:
            twilio_client.send_text(from_phone=request.user.phone_number, to_phone=num, message='Welcome blah blah')
        return redirect('home')

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room_info(request):
    return render(request, 'room-info.html')