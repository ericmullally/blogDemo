from django.http import Http404, HttpResponse
from django.shortcuts import render

blogs = [
    {
        "img": "/static/IMGS/daniel-jensen-NMk1Vggt2hg-unsplash.jpg",
        "title": "blog_1",
        "paragraph": [
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit"

        ]
    },
    {
        "img": "/static/IMGS/m-wrona-pCgxm-HDMNs-unsplash.jpg",
        "title": "blog_2",
        "paragraph": [
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit"

        ]
    },
    {
        "img": "/static/IMGS/gwendal-cottin-j85t8FTaCcE-unsplash.jpg",
        "title": "blog_3",
        "paragraph": [
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit",
            "Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit Et ipsum qui pariatur ullamco laboris.\
            Consequat quis et anim do eiusmod reprehenderit mollit elit. \
            Amet officia tempor esse consectetur qui. Reprehenderit proident culpa reprehenderit"

        ]

    }
]


def index(request):
    return HttpResponse("Blog Page")


def blog_post(request, name):

    blog = list(filter(lambda x: x["title"] == name, blogs))[0]
    try:
        # returns the blog if it is found in the databse.
        return render(request, "fullBlog.html", context=blog)
    except:
        return Http404("404 Page Not Found.")
