from django.shortcuts import render


def uploader(request):
    return render(request, 'editor.html', {})
