from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'wordcount/home.html')

def about(req):
    return render(req, 'wordcount/about.html')

def count(req):
    full_text = req.GET['fulltext']
    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
            word_dictionary[word] =1
    return render(req, 'wordcount/count.html', {'fulltext':full_text, 'total': len(word_list), 'dictionary':word_dictionary.items()})
