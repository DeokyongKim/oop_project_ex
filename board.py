import random

flag = 0 #박스를 하나도 이동시킬 수 없는 명령이 있었는지 판단(0일때 못움직임)

class box:#박스 객체 선언

    def __init__(self, num, locate, color):
        self.num = num
        self.locate = locate
        self.color = color
        self.y = (locate-1)//s
        self.x = (locate-1)%s
        board[self.y][self.x] = self.num

    def move_up(self):#위로 이동
        global flag
        while True:#이동 못할 때 까지 반복
            if board[self.y-1][self.x]==board[self.y][self.x] and self.y>0:#위에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y-1][self.x] = 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate-s:
                        boxes.remove(l)
                        break
                self.y = self.y - 1
                self.locate = self.locate - s
                self.num = 2 * self.num
                flag = 1
                break
            elif board[self.y-1][self.x]==0 and self.y>0: #위에 칸이 있고 비어있으면 위로 이동
                board[self.y][self.x]=0
                board[self.y-1][self.x]=self.num
                self.y = self.y - 1
                self.locate = self.locate - s
                flag = 1
            else:#못 움직이면 끝내기
                break

        while True:#합친후에 더 움직일 수 있으면 움직이기
            if board[self.y-1][self.x]==0 and self.y>0: #위에 칸이 있고 비어있으면 위로 이동
                board[self.y][self.x]=0
                board[self.y-1][self.x]=self.num
                self.y = self.y - 1
                self.locate = self.locate - s
            else:#못 움직이면 끝내기
                break

    def move_down(self):#아래로 이동
        global flag
        while True:#이동 못할 때 까지 반복
            if self.y < s-1 and board[self.y+1][self.x]==board[self.y][self.x]:#위에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y+1][self.x] = 2 * self.num
                for l in boxes:
                    if l.locate == self.locate+s:#기존의 박스 제거
                        boxes.remove(l)
                        break
                self.y = self.y + 1
                self.locate = self.locate + s
                self.num = 2 * self.num
                flag = 1
                break

            elif self.y < s-1 and board[self.y+1][self.x]==0:#아래에 칸이 있고 비어있으면 아래로 이동
                board[self.y][self.x]=0
                board[self.y+1][self.x]=self.num
                self.y = self.y + 1
                self.locate = self.locate + s
                flag = 1
            else:
                break

        while True:#합친후에 더 움직일 수 있으면 움직이기
            if self.y < s-1 and board[self.y+1][self.x]==0:#아래에 칸이 있고 비어있으면 아래로 이동
                board[self.y][self.x]=0
                board[self.y+1][self.x]=self.num
                self.y = self.y + 1
                self.locate = self.locate + s
            else:
                break

    def move_right(self):#오른쪽으로 이동
        global flag
        while True:#이동 못할 때 까지 반복
            if self.x < s-1 and board[self.y][self.x+1]==board[self.y][self.x]:#오른쪽에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y][self.x+1] = 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate+1:
                        boxes.remove(l)
                        break
                self.x = self.x + 1
                self.locate = self.locate + 1
                self.num = 2 * self.num
                flag = 1
                break

            elif self.x < s-1 and board[self.y][self.x+1]==0:#오른쪽에 칸이 있고 비어있으면 오른쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x+1]=self.num
                self.x = self.x + 1
                self.locate = self.locate + 1
                flag = 1
            else:
                break

            while True: #합친후에 더 움직일 수 있으면 움직이기
                if self.x < s - 1 and board[self.y][self.x + 1] == 0:  # 오른쪽에 칸이 있고 비어있으면 오른쪽으로 이동
                    board[self.y][self.x] = 0
                    board[self.y][self.x + 1] = self.num
                    self.x = self.x + 1
                    self.locate = self.locate + 1
                else:
                    break

    def move_left(self):#왼쪽으로 이동
        global flag
        while True:#이동 못할 때 까지 반복
            if board[self.y][self.x-1]==board[self.y][self.x] and self.x > 0:#왼쪽에 칸이 있고 비어있으면 왼쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x-1]= 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate-1:
                        boxes.remove(l)
                        break
                self.x = self.x - 1
                self.locate = self.locate - 1
                self.num = 2 * self.num
                flag = 1
                break

            elif board[self.y][self.x-1]==0 and self.x > 0:#왼쪽에 칸이 있고 비어있으면 왼쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x-1]=self.num
                self.x = self.x - 1
                self.locate = self.locate - 1
                flag = 1
            else:
                break

        while True:#합친후에 더 움직일 수 있으면 움직이기
            if board[self.y][self.x-1]==0 and self.x > 0:#왼쪽에 칸이 있고 비어있으면 왼쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x-1]=self.num
                self.x = self.x - 1
                self.locate = self.locate - 1
            else:
                break

def is_range_in(player_s):#변의 길이가 2~8까지의 숫자인지를 판별
    for i in ['2', '3', '4', '5', '6', '7', '8']:
        if player_s == i:
            return True
    return False

def gen_box_locate(): #비어있는 곳을 찾고 그 곳중 랜덤한 위치 선정함
    location = []
    for i in range(s):
        for j in range(s):
            if board[i][j]==0:
                location.append(s*i+j+1)
    return location

def player_move():#플레이어의 상자 움직이기
    global flag
    flag = 0
    while True:#플레이어의 상자 움직이는 방향 입력받음
        player_move = input('direction?')

        if player_move == 'up':#위로 움직이는 경우
            for i in range(s):
                for j in range(s):
                    if board[i][j] is not 0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_up()#박스를 위로 이동

        if player_move == 'down':#아래로 움직이는 경우
            for i in range(s-1, -1, -1):
                for j in range(s):
                    if board[i][j] is not 0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_down()#박스를 아래로 이동

        if player_move == 'right':#오른쪽으로 움직이는 경우
            for i in range(s):
                for j in range(s-1, -1, -1):
                    if board[i][j]!=0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_right()#박스를 오른쪽으로 이동

        if player_move == 'left':#왼쪽으로 움직이는 경우
            for i in range(s):
                for j in range(s):
                    if board[i][j]!=0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_left()#박스를 왼쪽으로 이동

        if player_move in ['up', 'down', 'right', 'left'] and flag==1:#방향을 틀리게 입력하면 재입력
            break

def is_game_over():
    """
    보드가 다 찼을 때 더 움직일 수 있는지 판단하는 함수
    True면 게임이 끝남
    :return: bool
    """
    for i in range(0, s-1):#양 옆, 위아래으로 합칠 수 있는지 판단
        for j in range(0, s-1):
            if board[i][j]!=0 and (board[i][j]==board[i][j+1] or board[i][j]==board[i+1][j]):
                return False
    return True

def is_board_full():
    """
    보드가 다 찼는지 판단하는 함수
    True면 보드가 다 참
    :return: bool
    """
    for i in range(s):#각각의 칸이 0인지 판단
        for j in range(s):
            if board[i][j]==0:
                return False
    return True

while True:
    while True:#변 길이 입력받기
        s = input("한 변의 크기를 입력해 주세요 (2~8):")
        if is_range_in(s): #s가 2~8까지의 문자인지 판별
            s = int(s) #정수로 변환
            break #정수가 아니면 재입력

    board = []

    for _ in range(s):#게임보드 형성
        board.append([0] * s) #board의 모든 수 0으로 선언(0이 비고 1이 참)

    boxes=[]

    boxes.append(box(random.choice([2, 4]), random.choice(gen_box_locate()), 'White'))# 상자 랜덤한 위치에 생성

    while True:#상자 생성 - 상자 움직이기 실행
        for i in range(s):
            for j in range(s):
                print("%d " %board[i][j],end='')
            print()
        if is_board_full():
            if is_game_over():
                print("게임 종료")
                break
        player_move()#방향 입력 받아 움직이기
        boxes.append(box(random.choice([2, 4]), random.choice(gen_box_locate()), 'White'))  # 상자 랜덤한 위치에 생성

