# voter_analytics/models.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-01
# This file defines the Voter model used in Voter Analytics.

from django.db import models

# Create your models here.

class Voter(models.Model):
    """Store the data from one voter, containing the following information:
    * Last Name
    * First Name
    * Residential Address - Street Number
    * Residential Address - Street Name
    * Residential Address - Apartment Number
    * Residential Address - Zip Code
    * Date of Birth
    * Date of Registration
    * Party Affiliation (**note, this is a 2-character wide field**)
    * Precinct Number

    The following fields indicate whether of not the voter participated in
    several recent elections:
    * v20state
    * v21town
    * v21primary
    * v22general
    * v23town

    The following field indicates how many of the past 5 elections the voter
    participated in:
    * voter_score

    """

    last_name = models.TextField()
    first_name = models.TextField()
    addr_num = models.IntegerField()
    addr_st = models.TextField()
    addr_apt = models.TextField()
    addr_zip = models.IntegerField()
    dob = models.DateField()
    dor = models.DateField()
    party = models.CharField(max_length=2)
    precinct = models.TextField()

    v20state = models.TextField()
    v21primary = models.TextField()
    v21town = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()

    voter_score = models.IntegerField()

    def get_party_list(self):
        """Get list of distinct parties in database"""
        parties = []
        for voter in Voter.objects.all():
            if voter.party not in parties:
                parties.append(voter.party)
        return parties

def load_data():
    """Create Voters from a hard-defined CSV."""
    # Define filename
    filename = '/Users/coltrane/Documents/newton_voters.csv'
    # Open file
    f = open(filename, 'r')
    # Discard headers
    f.readline()
    # Read each row:

    for line in f:
        try:
            # Split on commas
            fields = line.strip().split(',')
            # Define voter with voter fields
            voter = Voter(last_name = fields[1],
                            first_name = fields[2],
                            addr_num = fields[3],
                            addr_st = fields[4],
                            addr_apt = fields[5],
                            addr_zip = fields[6],
                            dob = fields[7],
                            dor = fields[8],
                            party = fields[9],
                            precinct = fields[10],

                            v20state = fields[11],
                            v21primary = fields[12],
                            v21town = fields[13],
                            v22general = fields[14],
                            v23town = fields[15],

                            voter_score = fields[16]
                        )
            voter.save()
        except:
            # Error message
            print("Something went wrong!")
            print(f"line={line}")
    # Print num of Voters
    print(f"Created {len(Voter.objects.all())} Voters")
