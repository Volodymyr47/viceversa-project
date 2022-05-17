from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    words_count = len(user_text.split())
    isplural = ''
    if words_count > 1:
        isplural = 'words'
    elif (user_text == '') & (words_count == 1):
        isplural = 'now words'
        words_count = ''
    else:
        isplural = 'word'
    print(user_text, words_count)
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text,
                                            'wordscount':words_count, 'isplural': isplural})