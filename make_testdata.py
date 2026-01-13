# this produces a small ical file that is used to run the unittests (test_ical_network.py)

# if any changes are made here, we need to change test_answers = {} in the test suite 
# appropriately.


from icalendar import Calendar, Event, vCalAddress, vText
import datetime as dt
import uuid

# make some test calendars to test ical_network.py functionalities

uid_linked_1 = uuid.uuid4()
uid_linked_2 = uuid.uuid4()
uid_linked_3 = uuid.uuid4()

def make_testcal(testfile = 'test_files/test.ical'):

    # first test calendar. the three meetings with uid = uid_linked_1, (...) are shared
    # with the second test calendar.

    people = ['daniel@test.mail', 'sandra@test.mail', 'felix@evil.mail', 'johnella@evil.mail',
            'garfield@pets.com', 'unwanted@friend.net', '12345678@calendar.google.com']
            
    testcal = Calendar.example()

    testcal.description = 'test ical with a few meetings, in-house (test.mail) and external.'

    accepted = {'PARTSTAT':'ACCEPTED', 'CUTYPE':'INDIVIDUAL'}
    declined = {'PARTSTAT':'DECLINED', 'CUTYPE':'INDIVIDUAL'}
    resource = {'PARTSTAT':'ACCEPTED', 'CUTYPE':'RESOURCE'}

    # pre 2025 in house meeting
    event = Event()
    event_time = dt.datetime(2023, 3, 4, 9, 30)
    event.add('summary', 'pre-2025 in-house meeting')
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    testcal.add_component(event)

    # 2025 in house meeting
    event = Event()
    event_time = dt.datetime(2025, 9, 4, 9, 30)
    event.add('summary', '2025 in-house meeting 1')
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    testcal.add_component(event)

    # 2025 in house meeting
    event = Event()
    event_time = dt.datetime(2025, 10, 10, 9, 30)
    event.add('summary', '2025 in-house meeting 2')
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    testcal.add_component(event)

    # 2025 in house meeting with invite declined by second participant
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', '2025 in-house meeting 3')
    event.add('organizer', vCalAddress('mailto:'+ people[1]))
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = declined))
    testcal.add_component(event)

    # meeting with personal friend
    event = Event()
    event_time = dt.datetime(2025, 10, 17, 9, 30)
    event.add('summary', 'lets go for a nice walk')
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[5], params = accepted))
    testcal.add_component(event)

    # 2025 meeting with representative of evil company 
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'opportunities to take over the world')
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_1)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    testcal.add_component(event)

    # 2025 meeting with representative of evil company 
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'following up on: take over the world')
    event.add('organizer', vCalAddress('mailto:'+ people[3]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_2)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = declined))
    testcal.add_component(event)

    # 2025 meeting with evil and neutral companies
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'following up on: take over the world re. mondays')
    event.add('organizer', vCalAddress('mailto:'+ people[3]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_3)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[4], params = accepted))
    testcal.add_component(event)
    
    # post 2025 in house meeting
    event = Event()
    event_time = dt.datetime(2026, 1, 10, 9, 30)
    event.add('summary', 'post-2025 in-house meeting')
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    testcal.add_component(event)

    print('writing test calendar')         
    f = open(testfile, 'wb')
    f.write(testcal.to_ical())
    f.close()
    
def make_testcal_combine(testfile = 'test_files/test_combine.ical'):

    # this is a test calendar with three ADDITIONAL meetings
    # compared to the first test calendar. shared events are repeated.
    # (the idea is that it is from the point of view of felix@evil.mail)

    people = ['daniel@test.mail', 'sandra@test.mail', 'felix@evil.mail', 
                'johnella@evil.mail', 'garfield@pets.com','ted_danson@ofir.dk']
            
    testcal = Calendar.example()

    testcal.description = 'second test ical to be combined with the first one'

    accepted = {'PARTSTAT':'ACCEPTED', 'CUTYPE':'INDIVIDUAL'}
    declined = {'PARTSTAT':'DECLINED', 'CUTYPE':'INDIVIDUAL'}
    resource = {'PARTSTAT':'ACCEPTED', 'CUTYPE':'RESOURCE'}

    # 2025 meeting with representative of evil company 
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'opportunities to take over the world')
    event.add('organizer', vCalAddress('mailto:'+ people[0]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_1)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    testcal.add_component(event)

    # 2025 meeting with representative of evil company 
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'following up on: take over the world')
    event.add('organizer', vCalAddress('mailto:'+ people[3]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_2)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = declined))
    testcal.add_component(event)

    # 2025 meeting with evil and neutral companies
    event = Event()
    event_time = dt.datetime(2025, 10, 15, 9, 30)
    event.add('summary', 'following up on: take over the world re. mondays')
    event.add('organizer', vCalAddress('mailto:'+ people[3]))
    event.add('dtstart', event_time)
    event.add('uid', uid_linked_3)
    event.add('attendee', vCalAddress('mailto:'+ people[0], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[1], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[4], params = accepted))
    testcal.add_component(event)
    
    # in-house evil company meeting
    event = Event()
    event_time = dt.datetime(2025, 10, 16, 13, 30)
    event.add('summary', 'external offer to help us take over the world')
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('organizer', vCalAddress('mailto:'+ people[2]))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    testcal.add_component(event)
    
    # in-house evil company meeting
    event = Event()
    event_time = dt.datetime(2025, 10, 18, 13, 30)
    event.add('summary', 'do we really want to take over the world any more?')
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('organizer', vCalAddress('mailto:'+ people[2]))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[3], params = accepted))
    testcal.add_component(event)
    
    # contact between evil and neutral companies
    event = Event()
    event_time = dt.datetime(2025, 10, 18, 13, 30)
    event.add('summary', 'the grain we owe you')
    event.add('dtstart', event_time)
    event.add('uid', uuid.uuid4())
    event.add('organizer', vCalAddress('mailto:'+ people[2]))
    event.add('attendee', vCalAddress('mailto:'+ people[2], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[4], params = accepted))
    event.add('attendee', vCalAddress('mailto:'+ people[5], params = accepted))
    testcal.add_component(event)

    print('writing test calendar')         
    f = open(testfile, 'wb')
    f.write(testcal.to_ical())
    f.close()
    
if __name__ == '__main__':
    make_testcal()
    make_testcal_combine()