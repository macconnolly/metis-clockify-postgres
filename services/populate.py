import sys

sys.path.append("../")
from models import Client, Member, Project, TimeEntry, IndicatorConsolidation

if __name__ == "__main__":
    Member.save_from_clockify()
    Client.save_from_clockify()
    Project.save_from_clockify(archived="")
    TimeEntry.save_from_clockify(start="2020-06-01T00:00:01Z")
    IndicatorConsolidation.populate_prep(start="2020-06-01T00:00:01")