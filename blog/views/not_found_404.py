from django.shortcuts import (
    HttpResponse,
)

def page_not_found_view(request, exception):
    return HttpResponse("page not found")