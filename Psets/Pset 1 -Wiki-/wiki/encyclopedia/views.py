from django.http import HttpResponseRedirect
from django.shortcuts import render
import random
from django import forms
from django.urls import reverse
from . import util
from markdown2 import Markdown

markdowner = Markdown()

def Search(request):
    value = request.GET.get('q','')

    return HttpResponseRedirect(reverse("entry", kwargs={'entry':value})) if util.get_entry(value) is not None else SubString(value, request)

def SubString(value,req):
    Strings = []
    for entry in util.list_entries():
        if value.upper() is entry.upper():
            Strings.append(entry)
    return render(req, "encyclopedia/index.html"), {"entries":Strings, "search":True, "value":value}


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(req, entry):
    markdowner = Markdown()
    entries = util.get_entry(entry)
    if entries is not None:
        context = {"entry":markdowner.convert(entries), "entryTyle": entry}
        return render(req, "encyclopedia/entry.html", context)
    else:
        return render(req,'encyclopedia/error404.html')

