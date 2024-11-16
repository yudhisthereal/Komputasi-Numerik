Es = 0.00000001
xn = 1

while True:
    xn_1 = (1 - xn**5) / 2
    E = abs(xn_1 - xn)
    print(xn, xn_1, E)
    if E < Es:
        break
    xn = xn_1

print(f'xn = {xn}')
print(f'xn_1 = {xn_1}')
print(f'E = {E}')
