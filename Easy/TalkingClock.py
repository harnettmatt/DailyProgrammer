# [2017-06-27] Challenge #321 [Easy] Talking Clock

# Description
#
# No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.
#
# Input Description
#
# An hour (0-23) followed by a colon followed by the minute (0-59).
#
# Output Description
#
# The time in words, using 12-hour format followed by am or pm.
#
# Sample Input data
#
# 00:00
# 01:30
# 12:05
# 14:01
# 20:29
# 21:00
# Sample Output data
#
# It's twelve am
# It's one thirty am
# It's twelve oh five pm
# It's two oh one pm
# It's eight twenty nine pm
# It's nine pm

zero_to_nineteen = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty"]

abrv = "am"
time = input("Enter a valid military time: ")
time = time.split(":")
hours = int(time[0])
mins = int(time[1])

# check if it is the afternoon and covert out of military time
if hours >= 12:
    abrv = "pm"
    hours = hours % 12

# convert 00:xx to 12:xx
if hours == 0:
    hours = 12

hours_str = zero_to_nineteen[hours]

if 0 < mins < 10:
    mins_str = "oh " + zero_to_nineteen[mins]
elif mins < 20:
    mins_str = zero_to_nineteen[mins]
else:
    mins_arr = [int(d) for d in str(mins)]
    mins_str = tens[mins_arr[0]] + " " + zero_to_nineteen[mins_arr[1]]

print("It's " + hours_str + " " + mins_str + " " + abrv)
