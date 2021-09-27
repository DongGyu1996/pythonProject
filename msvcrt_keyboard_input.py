import msvcrt
import os


def msvcrt_getch():
    return msvcrt.getch()


def view_msvcrt_getch():
    special_key = []
    print("입력하세요")
    while True:
        a = msvcrt_getch()
        if a == b'\xe0' or a == b'K' or a == b'M' or a == b'H' or a == b'P':
            special_key.append(a)
            if special_key[0] != b'\xe0':
                print(special_key[0])
                special_key.clear()
            # 리스트 길이가 2면 현재 값을 저장해라.
            if len(special_key) == 2:
                if special_key[0] == b'\xe0' and special_key[1] == b'K':
                    print('press key left...')
                    special_key.clear()
                elif special_key[0] == b'\xe0' and special_key[1] == b'M':
                    print('press key right...')
                    special_key.clear()
                elif special_key[0] == b'\xe0' and special_key[1] == b'H':
                    print('press key up...')
                    special_key.clear()
                elif special_key[0] == b'\xe0' and special_key[1] == b'P':
                    print('press key down...')
                    special_key.clear()
        else:
            print(a)
        if a == b'c' or a == b'C':
            print("종료합니다.")
            os.system('pause')
            return 0


view_msvcrt_getch()

'''
    방향키 왼쪽 b'K' 오른쪽 b'M' 위 b'H' 아래 b'P' 
    특수키 b'\xe0'
'''
