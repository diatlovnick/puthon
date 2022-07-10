#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for i in range(2):
    x = i
    for j in range(2):
        y = j
        for k in range(2):
            z = k
            f1 = not(x or y or z)#можно задать любое утверждение
            f2 = not(x) and not(y) and not(z)# и сравнить со вторым
if f1 == f2:
    print('утверждение истинное')
else:
    print('утверждение ложное')
