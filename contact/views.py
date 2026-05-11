from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


@api_view(['POST'])
def contact_view(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({
            "message": "Message Sent Successfully"
        })

    return Response(serializer.errors, status=400)