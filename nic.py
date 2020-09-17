print("  Birthday Found Using As NIC  "+'\n')
print("     Created by Oshan Malith   "+'\n')
nic=input("Enter Nic = ")
year="19"+nic[0]+nic[1];
day=int(nic[2]+nic[3]+nic[4])

if day>500:
    gender="female"
    day=day-500
else :
    gender ="male"

if int(year) :
    if day<=31:
        month="january"
        date=day
    elif day<=60:
        month="February"
        date=day-31
    elif day<=91:
        month="march"
        date=day-60
    elif day<=121:
        month="April"
        date=day-91
    elif day<=152:
        month="May"
        date=day-121
    elif day<=182:
        month="June"
        date=day-152
    elif day<=213:
        month="July"
        date=day-182
    elif day<=244:
        month="August"
        date=day-213
    elif day<=274:
        month="September"
        date=day-244
    elif day<=305:
        month="october"
        date=day-274
    elif day<=335:
        month="november"
        date=day-305
    elif day<=366:
        month="desember"
        date=day-335

    print ('\n'+  "Gender = "+gender)
    print ("Year = "+year)
    print("Month = "+month)
    print("Day = "+str(date))
    x =input('\n'+"want to exit press enter"+'\n')

    '''Oshan Malith'''