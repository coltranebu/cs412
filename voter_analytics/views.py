# voter_analytics/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-01
# This file defines each view used in the website.

from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Voter

import plotly
import plotly.graph_objs as go

# Create your views here.

def get_party_list():
        """Get list of distinct parties in database"""
        parties = []
        for voter in Voter.objects.all():
            if voter.party not in parties:
                parties.append(voter.party)
        return parties

def get_dob_year_list():
        """Get list of distinct year of birth in database"""
        dob_years = []
        for voter in Voter.objects.all().order_by('dob'):
            if voter.dob.year not in dob_years:
                dob_years.append(voter.dob.year)
        return dob_years

class VotersListView(ListView):
    model = Voter
    template_name = "voter_analytics/voters.html"
    context_object_name = "voters"
    paginate_by = 100

    def get_queryset(self):
        """"""
        results = super().get_queryset()

        # Filter to party selected
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party:
                results = results.filter(party=party)
        
        # Filter to years above min selected
        if 'min_year' in self.request.GET:
            min_year = self.request.GET['min_year']
            if min_year:
                results = results.filter(dob__year__gte=min_year)

        # Filter to years below max selected
        if 'max_year' in self.request.GET:
            max_year = self.request.GET['max_year']
            if max_year:
                results = results.filter(dob__year__lte=max_year)

        # Filter to voter score selected
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                results = results.filter(voter_score=voter_score)

        # Filter to v20state voters if requested
        if 'v20state' in self.request.GET:
            v20state = self.request.GET['v20state']
            if v20state:
                results = results.filter(v20state="TRUE")

        # Filter to v21town voters if requested
        if 'v21town' in self.request.GET:
            v21town = self.request.GET['v21town']
            if v21town:
                results = results.filter(v21town="TRUE")

        # Filter to v21primary voters if requested
        if 'v21primary' in self.request.GET:
            v21primary = self.request.GET['v21primary']
            if v21primary:
                results = results.filter(v21primary="TRUE")

        # Filter to v22general voters if requested
        if 'v22general' in self.request.GET:
            v22general = self.request.GET['v22general']
            if v22general:
                results = results.filter(v22general="TRUE")

        # Filter to v23town voters if requested
        if 'v23town' in self.request.GET:
            v23town = self.request.GET['v23town']
            if v23town:
                results = results.filter(v23town="TRUE")

        return results

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data()
        context['party_list'] = get_party_list()
        context['dob_year_list'] = get_dob_year_list()
        return context

class VoterDetailView(DetailView):
    model = Voter
    context_object_name = "v"
    template_name = "voter_analytics/voter_detail.html"

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data()
        v = Voter.objects.get(pk=self.kwargs['pk'])
        context['google_maps'] = "https://www.google.com/maps/place/" + str(v.addr_num) + "+" + v.addr_st + ",+Newton,+MA+" + str(v.addr_zip)
        return context

