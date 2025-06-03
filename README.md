# Year-Progress-Calendar
Allows generating .ics file for events about percentage of year finished 

**Year Progress Calculator**

# For the year_progress.cpp file
   1. Change the var current_year to the current year
   2. If it is a leap year, change the number of days in February in the var months[12]
   3. If you want to change the calendar events, replace "% year gone" in all places with desired phrases
   4. Compile the cpp file using "g++ -o year_progress year_progress.cpp" and "year_progress"



# For the python file
   1. Copy the output at the end of the cpp file and paste it as input to vars date_list, time_list and progress_list
   2. Some **erroneous entries** will be there for example "31-04-2025" i.e. 31st April 2025 which is incorrect as April has inly 30 days. Change them to the correct date. Remember each percent of an year represents 3.65 days i.e. 3 days, 15 hrs and 36 mins. So, edit these erroenous entries accordingly before executing the python file.
   3. **Beware**: Change the var time_zone_offset according to your preferred time zone of living 
   4. You will need to import the ics library so it's better to copy paste the code in google colab and run it in a single cell. Run the python code.
   5. The printed output represents the calendar entries. 
   6. Import the calendar_invites.ics into your favourite calendar system
   7. Viola, have fun

Comment or raise a PR if there are any errors. 
