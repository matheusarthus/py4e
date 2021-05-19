def add_time(start, duration, weekDay=False):
    weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    indexOfWeekDay = None
    message = ['', '', '', '', '']

    if weekDay:
        formatedWeekDay = weekDay.capitalize()
        indexOfWeekDay = weekDays.index(formatedWeekDay)
        
    startSplited = start.split()

    period = startSplited[1]
    startHour = int(startSplited[0].split(':')[0])
    startMin  = int(startSplited[0].split(':')[1])

    durationSplited = duration.split(':')

    durationHour = int(durationSplited[0])
    durationMin  = int(durationSplited[1])

    if period == 'AM' and startHour == 12:
        startHour = 0

    if period == 'PM' and startHour != 12:
        startHour = startHour + 12

    newHour = startHour + durationHour
    newMin = startMin + durationMin

    if newMin > 60:
        newMin = newMin - 60
        newHour = newHour + 1

    if newHour > 24 and newHour < 48:
        newHour = newHour - 24
        message[3] = " (next day)"

        if indexOfWeekDay != None:
            message[4] = ', ' + weekDays[indexOfWeekDay + 1]

    if newHour >= 48:
        days = newHour // 24
        newHour = newHour % 24

        message[3] = f' ({days} days later)'

        if indexOfWeekDay != None:
            if days < 7:
                message[4] = ', ' + weekDays[indexOfWeekDay + days]
            else:
                message[4] = ', ' + weekDays[(days + indexOfWeekDay) % 7]

    if indexOfWeekDay != None and message[4] == '':
        message[4] = ', ' + weekDays[indexOfWeekDay]

    if newHour < 12:
        message[2] = "AM"
    else:
        message[2] = "PM"

    if newHour > 12:
        newHour = newHour - 12

    if newHour == 0:
        newHour = 12

    message[1] = str(newMin)

    if newMin < 10:
        message[1] = '0' + message[1]

    message[0] = str(newHour)

    new_time = message[0] + ':' + message[1] + ' ' + message[2] + message[4] + message[3]

    return new_time