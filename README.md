# pythonProject
# msvcrt keyboard input

msvcrt 라이브러리로 키보드 입력 시 특수키를 먼저 입력받아서 b'\xe0' 값이 먼저 입력 받고, 그 다음 b'K', b'M', b'H', b'P' 값을 받음.

방향키 왼쪽   b'\xe0', b'K' 
방향키 오른쪽 b'\xe0', b'M'
방향키 위     b'\xe0', b'H'
방향키 아래   b'\xe0', b'P' 

이렇게 받으므로 입력값에 따라 다르게 출력 될 수 있도록 작성
