from django.shortcuts import render, redirect

from .models import CorruptionForm, Act
from .forms import CommentForm, IncidentForm

def home(request):
    objs = CorruptionForm.objects.all()
    return render(request, "home.html",  {"formsc": objs})

# def act_detail(request, corruption_id):
#     # Fetch item data based on item_id
#     item = {'id': corruption_id, 'name': f'Item {corruption_id}'}
#     return render(request, 'corruption_detail.html', {'item': item})

def register_like(request, act_id, corruption_id):
    print(act_id, corruption_id)
    if act_id and corruption_id:
        act = Act.objects.get(id=act_id)
        act.likes += 1
        act.save()
        return redirect('act_detail', corruption_id=corruption_id)


def act_detail(request, corruption_id, *args, **kwargs):
    c_form = CorruptionForm.objects.get(id=corruption_id)
    factors = c_form.factors.all()
    acts = c_form.acts.all()
    context = {'c_form': c_form, "factors": factors, "acts": acts, "form": CommentForm()}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('act_detail', corruption_id=corruption_id)
    return render(request, 'corruption_detail.html', context)

def report_incident(request):
    context = {"form": IncidentForm()}
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report-incident')
    return render(request, 'report.html', context)
