from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Secret, Score, GameStyle
import pystartgg
import json

# Create your views here.
def home(request):
    context = {}
    context['secret'] = request.POST.get("secret")
    return render(request, 'scores/home.html', context)

def view(request):
    secret = request.GET.get("s")
    return render(request, "scores/view.html", {'secret': secret})

def rawview(request):
    secret = request.GET.get("s")
    query = model_to_dict(Score.objects.get(secret=secret))
    try:
        query['style'] = model_to_dict(GameStyle.objects.get(game=query['game']))['style']
    except:
        query['style'] = -1
    score_json = json.dumps(query)
    return HttpResponse(score_json, content_type="application/json")

def getslug(request):
    slug = request.GET.get("s")
    query = Secret.objects.get(name="startgg")
    gg = pystartgg.StartGG(query.value)
    event_list = {}
    if slug != None:
        tourney_info = gg.tournament.get(slug)
        if tourney_info != None:
            tourney_id = tourney_info['id']
            events = gg.tournament.get_events(tourney_id)
            for event in events:
                event_list[event['name']] = {'id': event['id'], 'game': event['videogame']}
        return HttpResponse(json.dumps(event_list), content_type="application/json")

def getsets(request):
    event = request.GET.get("e")
    query = Secret.objects.get(name="startgg")
    gg = pystartgg.StartGG(query.value)
    sets = gg.event.get_scoreboard_all(event)
    if sets != None:
        set_list = {}
        for match in sets:
            if match['state'] not in [1,2] or match['p1name'] == None or match['p2name'] == None:
                continue
            print(match)
            set_list[match['p1name'] + " vs " + match['p2name']] = {
                    'p1Prefix': match['p1prefix'],
                    'p1Name': match['p1name'],
                    'p2Prefix': match['p2prefix'],
                    'p2Name': match['p2name'],
                    'roundText': match['fullRoundText'],
            }
        print(set_list)
        return HttpResponse(json.dumps(set_list), content_type="application/json")

def updatescores(request):
    response = HttpResponse()
    response.status_code = 200
    if request.method == 'POST':
        try:
            post_data = json.loads(request.body)
            valid_fields = []
            fields = Score._meta.get_fields()
            if 'secret' not in post_data.keys():
                return 500
            for field in fields:
                valid_fields.append(field.name)
            for key, value in post_data.items():
                if key not in valid_fields:
                    del post_data[key]
            try:
                Score.objects.create(**post_data)
            except:
                secret = post_data['secret']
                del post_data['secret']
                Score.objects.filter(secret=secret).update(**post_data)
        except:
            response.status_code = 500            
        return response
    else:
        return HttpResponse("Only accepts POST data")

