def dayOfYear(date: str):
    yr = int(date[0:4])
    mn = int(date[5:7])
    day = int(date[8:])
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(yr%400==0 or ((yr%4==0)and (yr%100!=0))):
        if(mn>2):
            return sum(days[:mn-1])+day+1
        else:
            return sum(days[:mn-1])+day
    else:
        return sum(days[:mn-1])+day

print(dayOfYear("2016-02-29"))