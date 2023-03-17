from django.urls import reverse_lazy
from django.shortcuts import (
    HttpResponse,
    render,
    redirect,
)

def error_view(request, exception):
    return redirect('error_page')

def not_found_page_view(request, *args, **kwargs):
    context = {
        'request': request,
        'prevous_url': request. META,
        'msg': kwargs,
        'layout_path': 'layout/base.html',
    }
    return render(request, 'auth/pages/404.html', context)