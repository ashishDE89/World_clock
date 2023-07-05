from django.shortcuts import render
from datetime import datetime
import pytz

def world_clock(request):
    timezones = {
        'New York': 'America/New_York',
        'London': 'Europe/London',
        'India': 'Asia/Kolkata',
    }
    clocks = []
    for city, timezone in timezones.items():
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        clocks.append({'city': city, 'time': current_time})

    return render(request, 'clock/world_clock.html', {'clocks': clocks})
