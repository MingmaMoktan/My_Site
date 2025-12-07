from django.shortcuts import render

def post_list(request):
    return render(request, "blog/post_list.html")

def post_details(request, pk):
    return render(request, "blog/post_details.html")
