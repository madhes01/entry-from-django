from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import EntryForm
from myapp.functions.functions import handle_uploaded_file


def index(request):
    if request.method == "POST":
        entry = EntryForm(request.POST, request.FILES)
        if entry.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        entry = EntryForm()
    return render(request, "index.html", {'form':entry})