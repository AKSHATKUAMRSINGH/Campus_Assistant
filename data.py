# data.py

# A simple python dictionary to store timetable
# You can edit this dictionary later to update the timetable
TIMETABLE = {
    "Day 1": {
        "Consumer Behaviour": {"time": "11:35 AM - 12:25 PM", "room": "LH: 1105"},
        "Lab": {"time": "12:30 PM - 04:00 PM", "room": "Lab Slots"}
    },
    "Day 2": {
        "Lab": {"time": "08:00 AM - 12:25 PM", "room": "Lab Slots"},
        "Social Network Analysis": {"time": "12:30 PM - 02:15 PM", "room": "B503"},
        "Consumer Behaviour": {"time": "02:20 PM - 04:00 PM", "room": "LH: 1105"}
    },
    "Day 3": {
        "Speech Recognition": {"time": "08:00 AM - 09:40 AM", "room": "CLS: 1320"},
        "Advanced Mobile Communications": {"time": "10:40 AM - 11:30 AM", "room": "LH: 1215"},
        "Social Network Analysis": {"time": "11:35 AM - 12:25 PM (Optional)", "room": "B503"},
        "Lab": {"time": "12:30 PM - 04:50 PM", "room": "Lab Slots"}
    },
    "Day 4": {
        "Lab": {"time": "08:00 AM - 12:25 PM", "room": "Lab Slots"},
        "Advanced Mobile Communications": {"time": "12:30 PM - 02:15 PM", "room": "LH: 1215"},
        "Social Network Analysis": {"time": "02:20 PM - 03:10 PM", "room": "B503"},
        "Speech Recognition": {"time": "04:00 PM - 04:50 PM", "room": "CLS: 1320"}
    },
    "Day 5": {
        "Speech Recognition": {"time": "09:45 AM - 10:35 AM (Optional)", "room": "CLS: 1320"},
        "Advanced Mobile Communications": {"time": "11:35 AM - 12:25 PM (Optional)", "room": "LH: 1215"},
        "Lab": {"time": "12:30 PM - 04:50 PM", "room": "Lab Slots"}
    }
}

# 10 predefined academic FAQs
FAQS = {
    "library timing": "The library is open from 8:00 AM to 8:00 PM on weekdays, and 9:00 AM to 1:00 PM on Saturdays.",
    "office timing": "The administrative office is open from 9:00 AM to 5:00 PM from Monday to Friday.",
    "semester duration": "Each academic semester lasts for exactly 15 weeks.",
    "attendance requirement": "A minimum of 75% attendance is required to appear for final examinations.",
    "exam form": "Exam forms are usually released one month before the mid-term or final exams.",
    "lab timing": "Computer and Science labs are open from 9:00 AM to 4:00 PM.",
    "faculty room": "Faculty rooms are located on the second floor of the main administrative building.",
    "break timing": "The standard lunch break is from 1:00 PM to 2:00 PM every day.",
    "holiday query": "The upcoming holiday list is available on the university notice board and student portal.",
    "department location": "The Computer Science department is situated in Block C."
}

# Automatically extract available subjects from the timetable
# Added AI, ML, Cloud so the system recognizes these queries and gracefully states they aren't on the schedule
SUBJECTS = ["AI", "ML", "Cloud"]
for day_sch in TIMETABLE.values():
    for sub in day_sch.keys():
        if sub not in SUBJECTS:
            SUBJECTS.append(sub)

# Available days
DAYS = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
