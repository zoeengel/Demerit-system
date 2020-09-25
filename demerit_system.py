speed= int(input("Enter your speed in km/h: "))
allowed_speed= int(input("Enter the average speed: "))
demerits= (speed-allowed_speed)//5
if (speed<=allowed_speed):
    print("OK")
elif speed>allowed_speed:
    print("you got", demerits, "demerit points")
    if demerits>12:
        print("Go to Jail")

else:
    print("wrong input")

