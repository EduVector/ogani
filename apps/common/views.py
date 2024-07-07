from django.shortcuts import render
from apps.common.models import SubEmail


def subemail(request):
    if request.method == "POST":
        email = request.POST.get("subemail")

        SubEmail.objects.create(
            email=email,
        )
