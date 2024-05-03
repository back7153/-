from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    '''
    이진 검색을 수행하는 과정을 출력
    '''
    pl = 0
    pr = len(a) - 1

    print(' |', end = '')
    for i in range(len(a)):
        print(f'{i : 4}', end = '')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2

        print(' |', end = '')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end = '')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end = '')
        if pc != pr:
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end = '')
        for i in range(len(a)):
            print(f'{a[i]:4}', end = '')
        print('\n   |')

        pc = (pl + pr) // 2 # 중앙 인덱스
        if a[pc] == key: # a[pc]가 찾는 값이면
            return pc # 인덱스 pc를 반환
        elif a[pc] < key: # 찾는 값이 a[pc]보다 크면
            pl = pc + 1 # 검색 범위의 앞부분을 a[pc+1]로 업데이트
        else:
            pr = pc - 1 # 아니라면(=찾는 값이 a[pc]보다 작으면) # 검색 범위의 뒷부분을 a[pc-1]로 업데이트
        if pl > pr: # pl이 pr보다 커지면(=검색 범위를 좁히다가 검색 범위가 더 이상 없는 경우)
            break # while문 탈출
    return -1 # 그리고 -1을 반환(검색 실패)

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')