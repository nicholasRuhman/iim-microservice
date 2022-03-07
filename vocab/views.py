from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vocab
from .serializers import VocabSerializer
from infinity_influencer_marketing_app import utils

# Create your views here.
@api_view(['GET', 'POST'])
def vocab(request):
    if request.method == 'GET':
        return Response(utils.format_vocab_json_response())

    elif request.method == 'POST':
        parsed_request_data = utils.parse_vocab_post_request(request.data, "vocab")
        if parsed_request_data:
            serializer = VocabSerializer(data=parsed_request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(utils.format_vocab_json_response(), status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Request requires JSON format {'vocab':[non-empty-strs]}.", status=status.HTTP_400_BAD_REQUEST)
