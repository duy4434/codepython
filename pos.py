print("โปรแกรมร้านขายของ")
a=(int(input("หมูสับ:")))
b=(int(input("ข้าวสาร:")))
c=(int(input("มาม่า:")))
d=(int(input("ซอสน้ำมันหอย:")))
e=(int(input("ปลากระป๋อง:")))
sum = a+b+c+d+e
print("ราคารวม:",sum)
print("กรุณาชำระเงิน")
change = (int(input("รับเงิน:")))
total = change -sum
print ("เงินทอน:",total)
