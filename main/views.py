from django.shortcuts import render, HttpResponse

# Create your views here.
def indexvalues():
    values = {
        "orgName" : "Ecomweb",
        "pagetitle" : "Home Page",
        "happyClients": 2,
        "projects":2,
        "hoursOfSupport": 28
        }
    return values

def main_view(request):
    return render(request, "index.html", context = indexvalues())
