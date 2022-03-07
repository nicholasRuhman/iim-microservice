from rest_framework.decorators import api_view
from rest_framework.response import Response
from infinity_influencer_marketing_app import utils

# Create your views here.
@api_view(['POST'])
def prediction(request):
    vocab_set = utils.get_vocab_set()
    post_text_words = utils.get_valid_words(request, "post_text")
    for word in post_text_words:
        if word in vocab_set:
            return Response({"prediction": "sponsored"})
    return Response({"prediction": "non-sponsored"})
