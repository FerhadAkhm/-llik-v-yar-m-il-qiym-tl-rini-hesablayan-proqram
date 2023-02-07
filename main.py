a = int(input("1-ci KSQ qiymetini daxil et: "))
b = int(input("2-ci KSQ qiymetini daxil et: "))
c = int(input("3-ci KSQ qiymetini daxil et: "))
d = int(input("4-ci KSQ qiymetini daxil et: "))
e = int(input("5-ci KSQ qiymetini daxil et: "))
f = int(input("6-ci KSQ qiymetini daxil et: "))
q1 = int(input("1-ci BSQ qiymetini daxil et: "))
q2 = int(input("2-ci BSQ qiymetini daxil et: "))
y_illiy_qiymet = (((a+b+c)/3) *40 / 100) + q1 * 60 / 100
illiy_qiymet = (((a+b+c+d+e+f)/6) *40 / 100) + ((q1 + q2)/2) *60 /100
print("Yarim il qiymeti: ",y_illiy_qiymet)
print("Illiy qiymet: ",illiy_qiymet)