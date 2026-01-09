file1 = 'ical_files/edin@ogtal.dk.ics'
file2 = 'ical_files/ronnie@ogtal.dk.ics'

# imports

from ical_network import Person, Meeting, load_single_ical, find_people, combine_meetings
from ical_network import filter_meetings, categorize_meetings, make_graph
from big_colorlist import colors

ml1 = load_single_ical(file1)
ml2 = load_single_ical(file2)
meetings = combine_meetings([ml1, ml2])
categorize_meetings(meetings)
meetings = filter_meetings(meetings, dates = ['2025-01-01', '2025-12-31'], 
                            filter_in_group = True)

for m in meetings:
    print(m.summary, m.repeating, m.repeats, m.groups, m.in_group)

people = find_people(meetings, colors)

g = make_graph(people, meetings)
#print(g['edin@ogtal.dk']['ronnie@ogtal.dk']['summary'])