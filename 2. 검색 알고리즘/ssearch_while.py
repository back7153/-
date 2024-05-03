# while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int: # a는 Sequence형 데이터를, key는 어떤 데이터 타입이든 상관없이 파라미터로 입력받는다.
    '''
    시퀀스 a에서 key와 값이 같은 원소를 선형 검색
    '''

    i = 0 # 파라미터로 입력받은 a의 인덱스
    # a의 원소가 n개이면 len(a) = n
    # a의 인덱스는 0부터 n-1까지

    while True:
        if i == len(a): # a의 인덱스가 a의 길이가 되면(= 0부터 len(a)-1까지 검색했음에도 값을 못 찾은 경우)
            return -1 # 검색 실패
        if a[i] == key: # a[i]가 입력한 key값과 같은 경우
            return i # 해당 값의 인덱스를 반환
        i += 1 # 0부터 시작해서 while문을 반복하는 동안 +1

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 길이가 num인 리스트 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')