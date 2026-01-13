file1 = 'ical_files/edin@ogtal.dk.ics'
file2 = 'ical_files/ronnie@ogtal.dk.ics'

# imports

from ical_network import Person, Meeting, load_single_ical, find_people, combine_meetings
from ical_network import filter_meetings, categorize_meetings, make_graph
from thoravej29_dicts import tv29_colors, tv29_blocklist

ml1 = load_single_ical(file1)
ml2 = load_single_ical(file2)
meetings = combine_meetings([ml1, ml2])
categorize_meetings(meetings)
meetings = filter_meetings(meetings, dates = ['2025-01-01', '2025-12-31'])

#for m in meetings:
#    print(m.summary, m.repeating, m.repeats, m.groups)

people = find_people(meetings, colors = tv29_colors, blocklist = tv29_blocklist)

# all connections
g = make_graph(people, meetings)

# remove connections that only occurred one time ('intro meetings')
g2 = make_graph(people, meetings, filename = "outputs/con_trimmed.gexf", 
                    min_connections = 2)
                    
navne = list(g2.nodes)
for navn in navne:
    print(navn)