Es = 10e-6
xn = 1.0
n = 0
Er = 100

print('n. xn    xn_1    Er')
while Er > Es:
    xn_1 = (1.0 - xn**5) / 2.0
    n += 1
    Er = abs((xn_1 - xn) / xn_1) * 100
    print(f'{n}. {xn}   {xn_1}  {Er}')
    xn = xn_1
