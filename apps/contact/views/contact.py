from rest_framework.views import APIView
from rest_framework.response import Response
from apps.contact.models import Contact
from apps.contact.serializers import ContactSerializer
from rest_framework import status
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from dotenv import load_dotenv
import os


# Create your views here.
class ContactView(APIView):

    def post(self, request):
        contact_serializer = ContactSerializer(data=request.data)
        print(request.data)

        if contact_serializer.is_valid():
            # Load .env file
            load_dotenv()

            # Save register in Database
            contact_serializer.save()

            # Send email configuration
            subject = 'Thanks for contact with us'
            contact_email = contact_serializer.data['email']
            contact_name = contact_serializer.data['name']

            # Create body for email
            body = render_to_string(
                'contact/email-notification.html', {
                    'name': contact_name,
                    'email': contact_email
                }
            )

            # Send email
            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=os.getenv('EMAIL_HOST_USER'),
                to=[contact_email]
            )

            email_message.content_subtype = 'html'
            email_message.send()

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)