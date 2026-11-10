from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):

    timetable = [
        {
            'day': 'Monday',
            'subject': 'Maths',
        },
        {
            'day': 'Monday',
            'subject': 'Computer Art',
        },
        {
            'day': 'Tuesday',
            'subject': 'Fundamentals of Web',
        },
        {
            'day': 'Tuesday',
            'subject': 'Python Programming',
        },
        {
            'day': 'Tuesday',
            'subject': 'Digital Electronics',
        },
        {
            'day': 'Wednesday',
            'subject': 'Fundamentals of Web',
        },
        {
            'day': 'Wednesday',
            'subject': 'Computer Art',
        },
        {
            'day': 'Thursday',
            'subject': 'Fundamentals of Web App',
        },
        {
            'day': 'Thursday',
            'subject': 'Python Programming',
        },
        {
            'day': 'Thursday',
            'subject': 'Japanese',
        },
        {
            'day': 'Friday',
            'subject': 'Statistics and Numerical Methods',
        },
        {
            'day': 'Friday',
            'subject': 'Japanese',
        },
        {
            'day': 'Saturday',
            'subject': 'Python Programming',
        },
        {
            'day': 'Saturday',
            'subject': 'Statistics and Numerical Methods',
        },
        {
            'day': 'Saturday',
            'subject': 'Digital Electronics',
        },
    ]

    return render(request, 'timetable.html', {
        'timetable': timetable
    })