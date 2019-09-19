def parking(hour, day):
    if hour>=19 and hour<21:
        return "both"
    if day%2==0:
        if hour>=21 and hour<24:
            return "left"
        else:
            return "right"    
    else:
        if hour>=21 and hour<24:
            return "right"
        else:
            return "left"
day=int(input("day: "))
hour=int(input("hour: "))
print(parking(hour, day))
    
