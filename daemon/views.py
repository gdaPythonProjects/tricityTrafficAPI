from django.http import HttpResponse

from daemon.fetcher import Fetcher


def cron(request):
    try:
        fetcher = Fetcher()
        fetcher.fetch()
    except:
        return HttpResponse("Fetch failed.")
    else:
        return HttpResponse("Fetched successful.")

