from django.http.response import HttpResponse, JsonResponse

# function-based view
def h(request):
    return HttpResponse("Hello, World!")
    
# function-based view
def h2(request):
    return JsonResponse({"message":"Hello, World!"})