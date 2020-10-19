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

def search(request):
    query = request.GET['q']
    entry = util.get_entry(query.lower())
    name = query

    if entry is None:
        all_entries = util.list_entries()
        matching_entries = []
        print(all_entries)

        for search_entry in all_entries:
            print("is " + query.lower() + " in " + search_entry.lower() + "?")
            if query.lower() in search_entry.lower():
                matching_entries.append(search_entry)
            else:
                continue

        print(matching_entries)
        return render(request, "encyclopedia/searchresults.html", {
        "name": name,
        "entries": matching_entries
    }) 

    return render(request, "encyclopedia/entry.html", {
        "entrybody": markdown2.markdown(entry),
        "name": name.capitalize(),

    })





