from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dict = {}
    for wd in words:
        if wd in word_dict:
            word_dict[wd]+=1
        else:
            word_dict[wd]=1
    return render(request, 'result.html', {'fulltext' : text, 'length' : len(words), 'dict' : word_dict.items()})
