from max import max_of

number = 0
x = []

while True:
    s = input()
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'{number}개 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')