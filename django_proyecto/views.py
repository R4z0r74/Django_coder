from django.shortcuts import render

def inicio(request):
    context = {}
    http_response = render(
        request=request,
        template_name="inicio.html",
        context=context,
    )
    return http_response



