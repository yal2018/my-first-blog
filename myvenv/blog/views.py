from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request,
                  'C:/Users/Luis/Python Dev/MotherSystem/djangogirls/myvenv/blog/templates/blog/post_list.html', {})
