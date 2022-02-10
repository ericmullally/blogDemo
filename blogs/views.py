from django.http import Http404, HttpResponse
from django.shortcuts import render

databaseSim = {
    "blog_1": "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
    "blog_2": "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
    "blog_3": "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit"
}


def index(request):
    return HttpResponse("Blog Page")


def blog_post(request, name):
    try:
        # returns the blog if it is found in the databse.
        return render(request, "fullBlog.html", context={"blog": databaseSim[name]})
    except:
        return Http404("404 Page Not Found.")
