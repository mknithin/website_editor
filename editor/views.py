from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


def load_editor(request):
    return render(request, 'editor/editor.html', {})


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['file']:
        image = request.FILES['file']
        fs = FileSystemStorage()
        image_name = fs.save(image.name, image)
        uploaded_image_url = fs.url(image_name)
    else:
        print("oops! this is a GET")

    return JsonResponse({'uploaded_path': uploaded_image_url})



