from django.shortcuts import render
from rest_framework.views import APIView
from email_app.serializers import SubscriberSerializer, UnsubscriberSerializer
from rest_framework.response import Response
from rest_framework import status
from email_app.models import Subscriber
from email_app.task import send_email

# Create your views here.
class AddSubscriberView(APIView):
    def post(self, request, format=None):
        try:
            print(request.data)
            serializer = SubscriberSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({'error': 'Bad request', 'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST)  
            serializer.save()
            return Response({'msg': 'Subscriber created successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
    

class UnsubscribeView(APIView):
    def post(self, request, format=None):
        serializer = UnsubscriberSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'Bad request', 'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST) 
        subscriber = Subscriber.objects.get(email_id=serializer.validated_data.get('email_id'))
        subscriber.is_active = False
        subscriber.save()
        return Response({'msg': 'Unsubscribe successfully'}, status=status.HTTP_200_OK)
    

# class SendDailyCampaignView(APIView):
#     def post(self, request, format=None):
#         try:
#             serializer = CampaignSerializer(data=request.data)
#             print(request.data)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'error': 'Bad request', 'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST) 
#             data = serializer.validated_data
#             subscribers = Subscriber.objects.filter(is_active=True)
#             for subscriber in subscribers:
#                 send_email(
#                     subscriber.email_id,
#                     data
#                 )
#         except Exception as e:
#             print(e)
        
    