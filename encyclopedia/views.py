from django.shortcuts import render
from django import forms

from . import util

import markdown2

class NewPageForm(forms.Form):
    name = forms.CharField(label="Title")
    markdown = forms.CharField(widget=forms.Textarea, label="Markdown")



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

        for search_entry in all_entries:
            if query.lower() in search_entry.lower():
                matching_entries.append(search_entry)
            else:
                continue

        return render(request, "encyclopedia/searchresults.html", {
        "name": name,
        "entries": matching_entries
    }) 

    return render(request, "encyclopedia/entry.html", {
        "entrybody": markdown2.markdown(entry),
        "name": name.capitalize(),

    })


def new(request):

    return render(request, "encyclopedia/new.html", {
        "form": NewPageForm()

    })





