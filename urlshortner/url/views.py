from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UrlData
from .forms import Url
import random,string

# Create your views here.

def index(request):
    return HttpResponse("Hello , Welcome to url shortner Project...!!!")


def urlshort(request):
    # form = Url(request.POST)
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                               for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            return render(request, 'slug.html', {'form' : form, 'slug' : slug})



            # request.user.urlshort.add(new_url)
            # return redirect('/')
    else:
        form = Url()
        # slug = "INVALID URL"
        return render(request, 'index.html',{'form' : form})    


        # slug = "INVALID URL"

    # data = UrlData.objects.all()
    # context = {
    #     'form': form,
    #     'data': data
    # }
    # return render(request, 'index.html', context)
    # return render(request, 'index.html', {'form' : form, 'slug' : slug})



# urlRedirect() — This Function tracks the slug to Original URL and redirects it to Original URL.
def urlRedirect(request, slugs):
    print(slugs)
    data = UrlData.objects.get(slug=slugs)

    return redirect(data.url)
