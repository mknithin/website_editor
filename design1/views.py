from django.shortcuts import render


def load_design_1(request):
    return render(request, 'design1/index.html', {})
