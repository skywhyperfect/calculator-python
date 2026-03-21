a=float(input("Первое число: "))
b=float(input("Второе число: "))
op=input("Операция (+ - * /): ")
if op=="+":
    print(f"{int(a)}+{int(b)}={int(a+b)}")
if op=="-":
    print(f"{int(a)}-{int(b)}={int(a-b)}")
if op=="*":
    print(f"{int(a)}*{int(b)}={int(a*b)}")
if op=="/":
    print(f"{int(a)}/{int(b)}={int(a/b)}")