fun_list = []
for x in range(5):
    def internal_f(e):
        return e + 1
    fun_list.append(internal_f)

fun_list2 = []
for y in range(5):
    def fun2(e, iv=y):
        return e + iv
    fun_list2.append(fun2)

fun_list3 = [lambda e: e+i for i in range(5)]

fun_list4 = [lambda e,iv=i: e+iv for i in range(5)]

print(fun_list)
print(fun_list2)
print(fun_list3)
print(fun_list4)
print('-----------------------------------------------------')
print([f(10) for f in fun_list])
print([f(10) for f in fun_list2])
print([f(10) for f in fun_list3])
print([f(10) for f in fun_list4])
