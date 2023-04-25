def add_time(start, duration, *args):

    def hourtoformat24(hour, ampm): #convert hour to 24h format
        h = hour
        f = ampm 
        if h == 12 and f == "AM":
            h -= 12
        elif 1 <= h <= 11 and f == "PM":
            h += 12
        return h
    
    def hourtoformat12(hour):   #convert hour to 12h format
        h = hour
        if h == 0:
            h += 12
            f = "AM"
        elif 1 <= h <= 11:
            f = "AM"
        elif h == 12:
            f = "PM"
        elif 13 <= h <= 23:
            h -= 12
            f = "PM"
        return h, f
    
    days = ["", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    try:
        startlist = start.split()
        hour = startlist[0]
        ampm = startlist[1]
        s = [int(x) for x in hour.split(":")]
        s.append(ampm)
        sh = s[0]   #start hour
        sm = s[1]   #start minute
        sf = s[2]   #start 12h format
    except:
        return "'start' parameter format must be like the following: '00:00 AM'"

    if not(0 <= sh <= 12):
        return "Hours of 'start' parameter must be between 0 and 12"
    
    if not(0 <= sm <= 59):
        return "Minutes of 'start' parameter must be between 0 and 59"
    
    if not(sf == "AM" or sf == "PM"):
        return "12h format of 'start' parameter requires 'AM' or 'PM' expression"
    
    try:
        d = [int(x) for x in duration.split(":")]
        dh = d[0]   #duration hour
        dm = d[1]   #duration minute
    except:
        return "'duration' parameter format must be like the following: '00:00'"

    if not(0 <= sm <= 59):
        return "Minutes of 'duration' parameter must be between 0 and 59"

    sh = hourtoformat24(sh, sf)

    numd = 0    #days number initialization
    acth = sh   #actual hour
    for i in range(dh):
        acth += 1
        if acth > 23:
            acth = 0
            numd += 1
    
    actm = sm   #actual minute
    for i in range(dm):
        actm += 1
        if actm > 59:
            actm = 0
            acth += 1
        if acth > 23:
            acth = 0
            numd += 1

    newh, newf = hourtoformat12(acth) # new hour and new format assignment
    newm = actm #new minute assignment

    if args:
        day = args[0].lower()   #extract day of the week from args tuple and convert to lowercase
        if day in days:
            actd = days.index(day)  #actual day
        else:
            return "The optional parameter does not contain a day of the week"
        for i in range(numd):
            actd += 1
            if actd > 7:
                actd = 1
    else:
        actd = 0    #with no arguments inserted actd is ""

    if actd == 0:
        newd = ""
    else:
        newd = days[actd]   #new day assignment
        newd = ", " + newd[:1].upper() + newd[1:]  #convert to uppercase only first character and add comma

    if numd == 0:
        numdtext = ""
    elif numd == 1:
        numdtext = " (next day)"
    elif numd > 1:
        numdtext = " (" + str(numd) + " days later)"

    new_time = str(newh) + ":" + str(newm).zfill(2) + " " + str(newf) + newd + numdtext

    return new_time

print(add_time("11:43 PM", "24:20", "tueSday"))