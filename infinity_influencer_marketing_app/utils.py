import string

from vocab.models import Vocab
from vocab.serializers import VocabSerializer


def parse_vocab_post_request(request, strkey):
    result = request.get(strkey, [])
    if len(result) != 1:
        return None
    if not isinstance(result[0], str):
        return None
    if not result[0] or result[0] == " ":
        return None
    return {strkey: result[0]}


def format_vocab_json_response():
    query_set = Vocab.objects.all()
    serializer = VocabSerializer(query_set, many=True)
    return {"vocab": [elem['vocab'] for elem in serializer.data]}


def get_vocab_set():
    vocab_query_set = Vocab.objects.all()
    serializer = VocabSerializer(vocab_query_set, many=True)
    if serializer.data:
        return {elem['vocab'] for elem in serializer.data}
    return None


def get_valid_words(request, strkey):
    post_text = request.data.get(strkey, "")
    if not post_text:
        return []
    if not isinstance(post_text, str):
        return []
    ignored_punctuation = str.maketrans(dict.fromkeys(string.punctuation))
    ignored_punctuation.pop(ord("#"), None)
    return post_text.translate(ignored_punctuation).split()
