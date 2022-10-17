def divis(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
divis(1,0)

def divis_2(lst):
    s=0
    for i in lst:
        try:
            s+=i
        except Exception:
            pass
    print(s)
divis_2([1,2,3,4,5,'str',6])

def divis_3(a):
    try:
        print(int(a))
    except Exception:
        print('не получилось')
divis_3('0')