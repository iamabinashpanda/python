# A weather forecasting organization wants to show whether it is day or night.
# Write a program to find whether is it dark outside or not based on the local system time.

import datetime
if int(datetime.datetime.today().strftime('%H')) in range(6,18):
    print("Light Outside")
else:
    print("Dark Outside")