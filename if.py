salary = int(input())
if salary >= 15000:
    if salary < 70000:
         print("silver")
    elif salary < 100000:
         print("Golden")
    elif salary < 1000000:
         print ("Platinum")
else:
    print ("กรุณาตรวจสอบเงื่อนไข")
            
