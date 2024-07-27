while True:
    a=eval(input("Enter the serial number:"))
    if(a>0 and a<=5):
        print("Your from batch A")
    elif(a>5 and a<=10):
        print("Your from batch B")
    elif(a>10 and a<=15):
        print("Your from batch C")
    elif(a>15 and a<=20):
        print("Your from batch D")
    elif(a>20 and a<=25):
        print("Your from batch E")
    elif(a>25 and a<=30):
        print("Your from batch F")
    elif(a>30 and a<=35):
        print("Your from batch G")
    elif(a>35 and a<=40):
        print("Your from batch H")
    else:
        print("Your not from this class")
        break
