from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    entry = util.get_entry(name)
    if entry is None:
        return index(request) # not found page

    return render(request, "encyclopedia/entry.html", {
        "entrybody": markdown2.markdown(entry),
        "name": name.capitalize(),

    })

def search(request, query):
    result = util.get_entry(query)

    if result is None:
        return index(request) # list of results

    return render(request, "encyclopedia/entry.html", {
        "entries": util.list_entries()
    })




