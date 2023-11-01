# southgate_reach_daily_schedule
Automates loading daily events onto Reach website

Every month the events for the next month need to be loaded
to a website called reach that scrolls these events on our 
local monitors. This program asks the month and year and what
each event is called for that month. The program reformats the 
to look like this 

-
Day, date
event
-

it then calculates the date that it will be shown on the monitors and
the date that it will stop displaying on the monitors. Using selenium 
a web browser driver it goes to the reach website navigates to the daily
schedular page, deletes old events and loads the new ones and then saves.