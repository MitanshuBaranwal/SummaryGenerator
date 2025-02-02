from .models import TextData
from .serializers import TextDataSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from openai import OpenAI
from openai import APIConnectionError, APIError
from django.conf import settings
from rest_framework.response import Response

client = OpenAI(api_key=settings.OPENAI_API_KEY)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_summary(request):
    try:
        text = request.data.get('text', '')

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ],
            max_tokens=100
        )

        # Extract the summary
        summary = response.choices[0].message.content.strip()

        # Save to database
        text_data = TextData.objects.create(original_text=text, summary=summary)

        # Serialize the response
        serializer = TextDataSerializer(text_data)
        return Response(serializer.data)

    except APIConnectionError as e:
        return Response({'error': 'Failed to connect to OpenAI API'}, status=500)
    except APIError as e:
        return Response({'error': 'OpenAI API error'}, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_bullet_points(request):
    try:
        text = request.data.get('text', '')

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates bullet points."},
                {"role": "user", "content": f"Generate bullet points for the following text:\n{text}"},
            ],
            max_tokens=100
        )

        # Extract the bullet points
        bullet_points = response.choices[0].message.content.strip()

        # Save to database
        text_data = TextData.objects.create(original_text=text, bullet_points=bullet_points)

        # Serialize the response
        serializer = TextDataSerializer(text_data)
        return Response(serializer.data)

    except Exception as e:
        return Response({'error': str(e)}, status=500)