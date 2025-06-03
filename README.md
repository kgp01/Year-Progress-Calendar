# Year-Progress-Calendar
Allows generating .ics file for events about percentage of year finished 

**Year Progress Calculator**


Adivce: Before following the workflow below, try it by setting the var end_percent = 6 {percentage of year finished} to understand the whole workflow and import the entires into your calendar. The reason is if you make a mistake and import incorrect entries, they will have to be deleted manually one by one which is very cumbersome for 100 entries. 

# For the year_progress.cpp file
   1. Change the var current_year to the current year
   2. If it is a leap year, change the number of days in February in the var months[12]
   3. If you want to change the name of the calendar events, replace "% year gone" in all places with desired phrase
   4. Compile the cpp file using "g++ -o year_progress year_progress.cpp" and "year_progress"



# For the python file
   1. Copy the output at the end of the cpp file and paste it as input to vars date_list, time_list and progress_list
   2. Some **erroneous date entries** will be there {5-6 date entries} for example "31-04-2025" i.e. 31st April 2025 which is incorrect as April has only 30 days. Change them to the correct         date. Remember each percent of an year represents 3.65 days i.e. 3 days, 15 hrs and 36 mins. So, edit these erroenous entries accordingly before executing the python file.
   4. **Beware**: Change the var time_zone_offset according to your preferred time zone of living 
   5. You will need to import the ics library so it's better to copy paste the code in google colab and run it in a single cell. Run the python code.
   6. The printed output represents the expected calendar entries. 
   7. Import the calendar_invites.ics into your favourite calendar system
   8. Viola, have fun

Comment or raise a PR if there are any errors. 
