from django.shortcuts import render
from django.db.models import Count, Sum, F

from .models import Bandmate, Groupname, Vote


def election(request):
    if request.method == 'POST' and request.POST['mate'] in ['drums', 'bass', 'keys', 'guitar']:
        context = {
            'bandmates': Bandmate.objects.all(),
            'groupnames': Groupname.objects.all(),
            'votes': Vote.objects.all(),
            'mate': request.POST['mate']
        }

        if 'value' in request.POST:
            try:
                vote = Vote.objects.get(groupname=Groupname.objects.get(name=request.POST['groupname']), bandmate=Bandmate.objects.get(name=request.POST['mate']))
                vote.value = request.POST['value']
                vote.save()
            except Vote.DoesNotExist:
                vote = Vote(groupname=Groupname.objects.get(name=request.POST['groupname']), bandmate=Bandmate.objects.get(name=request.POST['mate']), value=request.POST['value'])
                vote.save()
            return render(request, 'election2020.html', context)

        if 'newgroupname' in request.POST:
            groupname = Groupname(name=request.POST['newgroupname'])
            groupname.save()
        return render(request, 'election2020.html', context)

    return render(request, 'enter.html')


def results (request):
    context = {
        'results': Groupname.objects.annotate(overall=Sum('votes__value')).order_by('-overall'),
    }

    return render(request, 'results.html', context)
