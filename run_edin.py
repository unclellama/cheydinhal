filename = 'ical_files/edin@ogtal.dk.ics'

# imports

from ical_network import Person, Meeting, load_single_ical, find_people, filter_meetings
from ical_network import make_graph
from big_colorlist import colors

meetings = load_single_ical(filename)
print(len(meetings))
meetings = filter_meetings(meetings, dates = ['2025-01-01', '2025-12-31'])
print(len(meetings))

#people = find_people(meetings, colors, blocklist = ['droid', 'ninadamlind@gmail.com'])

#g = make_graph(people, meetings)
#print(g['edin@ogtal.dk']['ronnie@ogtal.dk']['info'])