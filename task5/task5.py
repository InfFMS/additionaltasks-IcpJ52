s = input()
dct = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
n = ''
for el in s:
    if el in '0987654321':
        n += el
    else:
        dct[el] += int(n)
        n = ''
ans = ''
if dct['N'] > dct['S']:
    ans += str(dct['N'] - dct['S']) + 'N'
elif dct['S'] > dct['N']:
    ans += str(dct['S'] - dct['N']) + 'S'
if dct['W'] > dct['E']:
    ans += str(dct['W'] - dct['E']) + 'W'
elif dct['E'] > dct['W']:
    ans += str(dct['E'] - dct['W']) + 'E'
print(ans)
