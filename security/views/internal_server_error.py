from django.urls import reverse_lazy
from django.shortcuts import (
    HttpResponse,
    render,
    redirect,
)

def internal_server_page_view(request, *args, **kwargs):
    context = {
        "request": request,
        "prevous_url": request.META,
        "msg": kwargs,
        "layout_path": "layout/base.html",
    }
    return render(request, "auth/pages/500.html", context)
