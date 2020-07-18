from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .forms import DataForm
from .models import Friend


def indexView(request):
    form = DataForm ()
    friends = Friend.objects.all ()
    return render (request, "index.html", {"form": form, "friends": friends})


def appendData(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = DataForm (request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid ():
            instance = form.save ()
            # serialize in new friend object in json
            ser_instance = serializers.serialize ('json', [instance, ])
            # send to client side.
            return JsonResponse ({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse ({"error": form.errors}, status=400)

    return JsonResponse ({"error": ""}, status=400)


def saveData(request):
    form = DataForm ()
    friends = Friend.objects.all ()

    if request.is_ajax ():
        form = DataForm (request.POST)
        print (request.POST)
        if form.is_valid ():
            form.save ()
            return JsonResponse ({
                'message': 'success'
            })

    return render (request, "index.html", {"form": form, "friends": friends})


# def checkFormId(request):
#     # request should be ajax and method should be GET.
#     if request.is_ajax and request.method == "GET":
#         # get the nick name from the client side.
#         form_id = request.GET.get ("form_id", None)
#         # check for the nick name in the database.
#         if Friend.objects.filter (form_id=form_id).exists ():
#             # if nick_name found return not valid new friend
#             return JsonResponse ({"valid": False}, status=200)
#         else:
#             # if nick_name not found, then user can create a new friend.
#             return JsonResponse ({"valid": True}, status=200)
#
#     return JsonResponse ({}, status=400)
