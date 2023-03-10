import json
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .forms import ApiForm, ApiTestForm

# Create your views here.

RETURN_FILE = Path(__file__).parent / 'testimage' / 'file1.ply'
RETURN_FILE = Path(__file__).parent / 'testimage/org' / 'pointcloud.ply'

def index(request):
    "test"
    return HttpResponse("Hello, world.")


def save_uploaded_file(f, savefile):
    "check filetype and save file"
    # check filetypes
    if f.content_type != "image/png":
        print("Wrong image type")
        return False
    with open(str(savefile), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return True

@csrf_exempt
def infer(request):
    "standard infer request med ply pointcloud retur"
    if request.method == 'POST':
        form = ApiForm(request.POST, request.FILES)
        if request.POST.get('api_key') != "123":
            return HttpResponseForbidden("No authorization")
        if form.is_valid():
            img = open(RETURN_FILE, 'rb')
            response = FileResponse(img)
            return response
        # form is not valide
        print(form.errors)
        returnval= {"error": 1, 'error_text':"Parameter error"}
        return HttpResponse(json.dumps(returnval), content_type="application/json")
    if request.method == "GET":
        form = ApiForm()
        resp = render(request, 'infer.html', context={'form': form})
        resp.status_code=400
        return resp
    else:
        res = HttpResponse("Method not allow" )
        res.status_code=405
        return res
    return HttpResponseBadRequest()

@csrf_exempt
def finfer(request):
    "standard infer request med ply pointcloud retur"
    if request.method == 'POST':
        form = ApiForm(request.POST, request.FILES)
        if request.POST.get('api_key') != "123":
            return HttpResponseForbidden("No authorization")
        if form.is_valid():
            img = open(RETURN_FILE, 'rb')
            response = FileResponse(img)
            return response
        # form is not valide
        print(form.errors)
        returnval= {"error": 1, 'error_text':"Parameter error"}
        return HttpResponse(json.dumps(returnval), content_type="application/json")
    if request.method == "GET":
        form = ApiForm()
        resp = render(request, 'finfer.html', context={'form': form})
        resp.status_code=400
        return resp
    else:
        res = HttpResponse("Method not allow" )
        res.status_code=405
        return res
    return HttpResponseBadRequest()

@csrf_exempt
def pinfer(request):
    "standard infer request med png picture retur"
    if request.method == 'POST':
        form = ApiForm(request.POST, request.FILES)
        if request.POST.get('api_key') != "123":
            return HttpResponseForbidden("No authorization")
        if form.is_valid():
            img = open(Path(__file__).parent / 'testimage' / 'dias.png', 'rb')
            response = FileResponse(img)
            return response
        # form is not valide
        print(form.errors)
        returnval= {"error": 1, 'error_text':"Parameter error"}
        return HttpResponse(json.dumps(returnval), content_type="application/json")
    if request.method == "GET":
        form = ApiForm()
        return render(request, 'infer.html', context={'form': form})
    else:
        res = HttpResponse("Method not allow" )
        res.status_code=405
        return res

@csrf_exempt
def vinfer(request):
    "standard infer request without picture and with form retur"
    if request.method == 'POST':
        form = ApiForm(request.POST, request.FILES)
        if request.POST.get('api_key') != "123":
            return HttpResponseForbidden("No authorization")
        if form.is_valid():
            print("Valid", request.FILES)
            print(request.FILES['color'], request.FILES['color'].name ,request.FILES['color'].content_type)
            for file in ['color', 'fringe']:
                if not save_uploaded_file(request.FILES[file],"/tmp/" + file + ".png"):
                    return HttpResponse(f"{file} NOT OK" )
            return HttpResponse("OK" )
        # form is not valide
        print(form.errors)
        return render(request, 'infer.html', context={'form': form})
    if request.method == "GET":
        form = ApiForm()
        return render(request, 'infer.html', context={'form': form})
    else:
        res = HttpResponse("Method not allow" )
        res.status_code=405
        return res
