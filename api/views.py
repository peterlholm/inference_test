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
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def infer(request):
    "standard infer request"
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if request.POST.get('api_key') != "123":
            return HttpResponseForbidden("No authorization")
        
        if form.is_valid():
            print(request.FILES)    
            for k, v in request.FILES:
                print(k,v)
            returnval= {"error": 0, 'error_text':"alt er i orden"}
            content = json.dumps(returnval)
            img = open(RETURN_FILE, 'rb')
            response = FileResponse(img)
            return response
            #return HttpResponse(content, content_type="application/json")
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
def tinfer(request):
    "standard infer request"
    print("Tinfer")
    if request.method == 'POST':
        form = ApiTestForm(request.POST)
        if form.is_valid():
            returnval= {"error": 0, 'error_text':"alt er i orden"}
            print(returnval)
            content = json.dumps(returnval)
            #content = json.dumps(returnval, content_type="application/json")
            print(content)
            return render(request, 'infer.html', context={'form': form})
            return HttpResponse(content)



        return HttpResponseBadRequest("bad response")

    
    
    form = ApiTestForm()
    #rendered_form = form.render("infer.html")
    context = {'form': form}
    return render(request, 'infer.html', context)
