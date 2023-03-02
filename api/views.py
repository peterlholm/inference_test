import json
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .forms import ApiForm, ApiTestForm

# Create your views here.

RETURN_FILE = Path(__file__).parent / 'testimage' / 'dias.jpg'

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
    "standard infer request"
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
        return render(request, 'infer.html', context={'form': form})
    else:
        res = HttpResponse("Method not allow" )
        res.status_code=405
        return res

@csrf_exempt
def vinfer(request):
    "standard infer request without picture"
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

@csrf_exempt
def tinfer(request):
    "standard infer request"
    print("Tinfer")
    if request.method == 'POST':
        form = ApiTestForm(request.POST)
        if form.is_valid():
            print(request.FILES)
            for k, v in request.FILES:
                print(k,v)

            returnval= {"error": 0, 'error_text':"alt er i orden"}
            print(returnval)
            content = json.dumps(returnval)
            #content = json.dumps(returnval, content_type="application/json")
            print(content)
            return render(request, 'infer.html', context={'form': form, 'redirect':'http://localhost:8000/peter'})
        return HttpResponseBadRequest("bad response")

    form = ApiTestForm()
    #rendered_form = form.render("infer.html")
    context = {'form': form, 'redirect':'http://localhost:8000/peter'}
    return render(request, 'infer.html', context)

def finfer(request):
    "standard infer request"
    print("Tinfer")
    if request.method == 'POST':
        form = ApiTestForm(request.POST)
        if form.is_valid():
            print(request.FILES)
            for k, v in request.FILES:
                print(k,v)

            returnval= {"error": 0, 'error_text':"alt er i orden"}
            print(returnval)
            content = json.dumps(returnval)
            #content = json.dumps(returnval, content_type="application/json")
            print(content)
            return render(request, 'infer.html', context={'form': form, 'redirect':'http://localhost:8000/peter'})
        return HttpResponseBadRequest("bad response")

    form = ApiTestForm()
    #rendered_form = form.render("infer.html")
    context = {'form': form, 'redirect':'http://localhost:8000/peter'}
    return render(request, 'infer.html', context)
