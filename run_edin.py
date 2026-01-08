filename = 'ical_files/edin@ogtal.dk.ics'

# imports

from ical_network import Person, Meeting, load_single_ical, find_people
from ical_network import make_graph
from big_colorlist import colors

meetings = load_single_ical(filename)

people = find_people(meetings, colors, blocklist = ['droid', 'ninadamlind@gmail.com'])

g = make_graph(people, meetings)
print(g['edin@ogtal.dk']['ronnie@ogtal.dk']['info'])