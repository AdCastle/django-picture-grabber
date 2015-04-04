from django.shortcuts import render

from instagram.client import InstagramAPI


def _instagram(tag):
    access_token = "{Enter you OAuth ID}"
    api = InstagramAPI(access_token=access_token)
    tag_search, next_tag = api.tag_search(q=tag)
    if tag_search:
        tag_recent_media, next = api.tag_recent_media(
            tag_name=tag_search[0].name)
        return tag_recent_media
    return []


def index(request):
    media = {'tag': "",
             'pics': [],
             'count': "",
             'ajax': False}

    tag = request.GET.get('tag')
    ajax = request.GET.get('ajax')
    count = request.GET.get('count')
    media['ajax'] = ajax
    if tag:
        media['tag'] = tag
        media['pics'] = _instagram(tag)
        if count:
            media['pics'] = media['pics'][:int(count)]
    return render(request, 'index.html', media)