file1 = 'ical_files/edin@ogtal.dk.ics'
file2 = 'ical_files/ronnie@ogtal.dk.ics'

# imports

from ical_network import Person, Meeting, load_single_ical, find_people, combine_meetings
from ical_network import filter_meetings, make_graph
from big_colorlist import colors

ml1 = load_single_ical(file1)
ml2 = load_single_ical(file2)
meetings = combine_meetings([ml1, ml2])
meetings = filter_meetings(meetings, dates = ['2025-01-01', '2025-12-31'])

people = find_people(meetings, colors)

g = make_graph(people, meetings)
print(g['edin@ogtal.dk']['ronnie@ogtal.dk']['info'])