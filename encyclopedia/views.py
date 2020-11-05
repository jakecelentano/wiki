from django.shortcuts import render
from django import forms

from . import util

import markdown2
import random

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Markdown content")

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Markdown content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry = util.get_entry(name)
    if entry is None:
        entrybody = "Page not found" # not found page
    else:
        entrybody = markdown2.markdown(entry)

    return render(request, "encyclopedia/entry.html", {
        "entrybody": entrybody,
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

    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = markdown2.markdown(form.cleaned_data["content"])
            util.save_entry(title, content)



    return render(request, "encyclopedia/new.html", {
        "form": NewPageForm()

    })


def randomPage(request):
    all_entries = util.list_entries()
    random_page = random.choice(all_entries)
    entry = util.get_entry(random_page)
    return render(request, "encyclopedia/entry.html", {
        "entrybody": markdown2.markdown(entry),
        "name": entry.capitalize(),

    })


def edit(request):

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = markdown2.markdown(form.cleaned_data["content"])
            util.save_entry(name, content)



    return render(request, "encyclopedia/edit.html", {
        "form": EditPageForm()

    })







