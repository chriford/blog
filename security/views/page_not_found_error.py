from django.shortcuts import (
    render,
)

def not_found_page_view(request, *args, **kwargs):
    context = {
        "request": request,
        "prevous_url": request.META,
        "msg": kwargs,
        "layout_path": "layout/base.html",
    }
    return render(request, "auth/pages/404.html", context)
