from django.urls import reverse_lazy
from django.shortcuts import (
    HttpResponse,
    render,
    redirect,
)


def not_found_exception(request, exception):
    return redirect("page-not-found-page")


def not_found_page_view(request, *args, **kwargs):
    context = {
        "request": request,
        "prevous_url": request.META,
        "msg": kwargs,
        "layout_path": "layout/base.html",
    }
    return render(request, "auth/pages/404.html", context)
