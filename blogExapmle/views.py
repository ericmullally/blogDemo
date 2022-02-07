from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    blogContient = [
        {
            "img": "static/IMGS/daniel-jensen-NMk1Vggt2hg-unsplash.jpg",
            "title": "title 1",
            "paragraph": "Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.",
            "url": "/title 1"
        },
        {
            "img": "static/IMGS/m-wrona-pCgxm-HDMNs-unsplash.jpg",
            "title": "title 2",
            "paragraph": "Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.",
            "url": "/title 1"
        },

        {
            "img": "static/IMGS/gwendal-cottin-j85t8FTaCcE-unsplash.jpg",
            "title": "title 3",
            "paragraph": "Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.\
                    Minim in minim ad duis proident qui cillum cillum laborum dolore.",
            "url": "/title 1"

        }
    ]
    content = {"blogContient": blogContient}

    return render(request, "index.html", context=content)
