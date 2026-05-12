import os
import resend

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


resend.api_key = os.environ.get("RESEND_API_KEY")


@api_view(['POST'])
def contact_view(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():

        contact = serializer.save()

        try:

            resend.Emails.send({

                "from": "onboarding@resend.dev",

                "to": "dharmalingamsure007@gmail.com",

                "subject": f"Portfolio Contact from {contact.name}",

                "html": f"""
                <h2>New Portfolio Contact</h2>

                <p><strong>Name:</strong> {contact.name}</p>

                <p><strong>Email:</strong> {contact.email}</p>

                <p><strong>Message:</strong></p>

                <p>{contact.message}</p>
                """
            })

        except Exception as e:
            print(e)

        return Response({
            "message": "Message Sent Successfully"
        })

    return Response(serializer.errors, status=400)