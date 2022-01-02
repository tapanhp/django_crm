from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(TemplateView):
    template_name = "leads/lead_list.html"
    extra_context = dict(leads=Lead.objects.all())


def lead_details(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {"current_lead": lead}
    return render(request, template_name="leads/lead_details.html", context=context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {"form": form}
    return render(request, template_name="leads/lead_create.html", context=context)


# The newest implementation supporting model forms
def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {"form": form, "lead": lead}
    return render(request, template_name="leads/lead_update.html", context=context)


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    # delete the model object directly without doing template action
    lead.delete()
    return redirect("/leads")
