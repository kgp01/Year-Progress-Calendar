# pip install ics

date_list = ["1-01-2025","4-01-2025","8-01-2025","11-01-2025","15-01-2025"]
time_list = ["0:0","15:36","7:12","22:48","14:24"]
progress_list = ["0% year gone","1% year gone","2% year gone","3% year gone","4% year gone"]


# Full list for 2025

# date_list = ["1-01-2025","4-01-2025","8-01-2025","11-01-2025","15-01-2025","19-01-2025","22-01-2025","26-01-2025","30-01-2025","2-02-2025","6-02-2025","10-02-2025","13-02-2025","17-02-2025","21-02-2025","24-02-2025","28-02-2025","4-03-2025",
#              "7-03-2025","11-03-2025","15-03-2025","18-03-2025","22-03-2025","25-03-2025","29-03-2025","2-04-2025",
#              "5-04-2025","9-04-2025","13-04-2025","16-04-2025","20-04-2025","24-04-2025","27-04-2025","30-04-2025",
#              "5-05-2025","8-05-2025","12-05-2025","16-05-2025","19-05-2025","23-05-2025","27-05-2025","30-05-2025",
#              "3-06-2025","6-06-2025","10-06-2025","14-06-2025","17-06-2025","21-06-2025","25-06-2025","28-06-2025",
#              "2-07-2025","6-07-2025","9-07-2025","13-07-2025","17-07-2025","20-07-2025","24-07-2025","28-07-2025",
#              "31-07-2025","4-08-2025","8-08-2025","11-08-2025","15-08-2025","18-08-2025","22-08-2025","26-08-2025",
#              "29-08-2025","2-09-2025","6-09-2025","9-09-2025","13-09-2025","17-09-2025","20-09-2025","24-09-2025",
#              "28-09-2025","30-09-2025","5-10-2025","9-10-2025","12-10-2025","16-10-2025","20-10-2025","23-10-2025","27-10-2025","30-10-2025","3-11-2025","7-11-2025","10-11-2025","14-11-2025","18-11-2025","21-11-2025","25-11-2025","29-11-2025","2-12-2025","6-12-2025","10-12-2025","13-12-2025","17-12-2025","21-12-2025","24-12-2025","28-12-2025","31-12-2025"]
# time_list = ["0:0","15:35","7:11","22:47","14:23","6:0","21:35","13:12","4:47","20:24","12:0","3:35","19:11","10:48","2:24","18:0","9:35","1:11","16:48","8:23","0:0","15:36","7:11","22:48","14:23","6:0","21:36","13:11","4:48","20:23","12:0","3:36","19:11","10:48","2:23","18:0","9:36","1:12","16:47","8:23","0:0","15:36","7:12","22:47","14:23","6:0","21:36","13:12","4:47","20:23","12:0","3:36","19:12","10:47","2:23","18:0","9:36","1:12","16:47","8:23","0:0","15:36","7:12","22:47","14:23","6:0","21:36","13:12","4:47","20:23","12:0","3:35","19:12","10:47","2:24","18:0","9:35","1:12","16:47","8:24","0:0","15:35","7:12","22:47","14:24","6:0","21:35","13:12","4:47","20:24","12:0","3:35","19:12","10:47","2:24","18:0","9:35","1:12","16:47","8:24","23:45"]
# progress_list = ["0% year gone","1% year gone","2% year gone","3% year gone","4% year gone","5% year gone","6% year gone","7% year gone","8% year gone","9% year gone","10% year gone","11% year gone","12% year gone","13% year gone","14% year gone","15% year gone","16% year gone","17% year gone","18% year gone","19% year gone","20% year gone","21% year gone","22% year gone","23% year gone","24% year gone","25% year gone","26% year gone","27% year gone","28% year gone","29% year gone","30% year gone","31% year gone","32% year gone","33% year gone","34% year gone","35% year gone","36% year gone","37% year gone","38% year gone","39% year gone","40% year gone","41% year gone","42% year gone","43% year gone","44% year gone","45% year gone","46% year gone","47% year gone","48% year gone","49% year gone","50% year gone","51% year gone","52% year gone","53% year gone","54% year gone","55% year gone","56% year gone","57% year gone","58% year gone","59% year gone","60% year gone","61% year gone","62% year gone","63% year gone","64% year gone","65% year gone","66% year gone","67% year gone","68% year gone","69% year gone","70% year gone","71% year gone","72% year gone","73% year gone","74% year gone","75% year gone","76% year gone","77% year gone","78% year gone","79% year gone","80% year gone","81% year gone","82% year gone","83% year gone","84% year gone","85% year gone","86% year gone","87% year gone","88% year gone","89% year gone","90% year gone","91% year gone","92% year gone","93% year gone","94% year gone","95% year gone","96% year gone","97% year gone","98% year gone","99% year gone","100% year gone"]


import calendar
from datetime import datetime, timedelta
from ics import Calendar, Event  # You may need to install the 'ics' library using pip

def create_calendar_invites(events):
    cal = Calendar()

    for event_details in events:
        start_date, start_time, duration_hours, event_title, event_description = event_details

        # Combine date and time
        start_datetime_str = f"{start_date} {start_time}"
        start_datetime = datetime.strptime(start_datetime_str, "%d-%m-%Y %H:%M")
        time_zone_offset = timedelta(hours=5, minutes=30)
        start_datetime_gmt530 = start_datetime - time_zone_offset
        end_datetime_gmt530 = start_datetime_gmt530 + timedelta(hours=duration_hours)

        # Create event
        event = Event()
        event.name = event_title
        event.begin = start_datetime_gmt530
        event.end = end_datetime_gmt530    
        event.description = event_description

        # Add event to calendar
        cal.events.add(event)
        
    # Save to .ics file
    with open('calendar_invites.ics', 'w') as f:
        f.writelines(cal)


if __name__ == "__main__":
    
    events = [
        # Add more events as needed
    ]

    for i in range(0, len(date_list)):
      events.append((date_list[i], time_list[i], 0.25, progress_list[i], ""))
      
      try:
        create_calendar_invites(events)
      except:
        print(date_list[i], time_list[i], 0.25, progress_list[i], "")


    print(events)

    # # Create and save calendar invite
    create_calendar_invites(events)