from django.shortcuts import render


def post_list(request):
    return render(request, 'Blog_V3/post_list.html', {})