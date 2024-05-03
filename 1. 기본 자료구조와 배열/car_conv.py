def card_conv_verbose(x: int, r: int) -> str:
    '''
    정숫값 x를 r진수로 변환한 뒤 그 수를 문자열 타입으로 반환
    '''

    d = '' # 빈 문자열 생성
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 0 ~ 9 : 10개 + A ~ Z : 26 = 36개
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')

    while x > 0: # x가 0보다 큰 경우에는 계속 반복
        print('   +' + (n + 2) * '-')
        if x //r :
            print(f'{r:2} | {x // r:{n}d} ... {x % r}')
        else:
            print(f'     {x // r:{n}d} ... {x % r}')
        d += dchar[x % r] # x 나누기 r의 나머지를 인덱스로 해서 dchar의 문자열 중 하나의 문자열을 d 문자열에 추가
        x //= r # x 나누기 r의 몫을 x에 할당해서 다시 반복
    
    return d[::-1] # 반환은 역순으로

card_conv_verbose(29, 16)