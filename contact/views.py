from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.core.mail import send_mail

@api_view(['POST'])
def contact_view(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():

        contact = serializer.save()

        send_mail(
            subject=f"Portfolio Contact from {contact.name}",
            message=f"""
Name: {contact.name}

Email: {contact.email}

Message:
{contact.message}
""",
            from_email='dharmalingamsure007@gmail.com',
            recipient_list=['dharmalingamsure007@gmail.com'],
        )

        return Response({"message": "Message sent successfully"})

    return Response(serializer.errors, status=400)