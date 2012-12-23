from django.http import HttpResponse

from models import Sponsor
import json

def getSponsor(request):
    sponsor = Sponsor.objects.order_by('?')[0]
    data = { 'url' : sponsor.url, 'logo' : sponsor.logo.url, 'navn' : sponsor.navn }
    return HttpResponse(json.dumps(data), mimetype="application/json")

def getAllSponsors(request):
    sponsors = Sponsor.objects.all()
    data = { 'sponsors': sponsors }
    res = []
    for sponsor in sponsors:
        res.append( { 'url' : sponsor.url, 'logo' : sponsor.logo.url, 'navn' : sponsor.navn } )
    return HttpResponse(json.dumps(res), mimetype="application/json")
