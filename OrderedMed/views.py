from django.shortcuts import render
from A05Blo.models import Post


def home(request):
    first = Post.objects.filter(published=True).first()
    currentpage = 1
    return render(request, 'home.html', locals())
