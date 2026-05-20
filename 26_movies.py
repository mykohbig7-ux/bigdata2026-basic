def book_movie(title, seat):
    print(f"🎬{title}{seat}번 좌석 예매가 완료되었습니다!")


# ↓ 여기서부터 작성하세요

def check_age(age):
    if age >= 15:
        print('[나이확인] 관람 가능합니다')
        return True
    else:
        print('[나이확인] 15세 미만은 관람 불가합니다')
        return False


def check_seat(seat):
    if seat <= 100:
        print('[좌석확인] 유효한 좌석입니다')
        return True
    else:
        print('[좌석확인] 좌석번호는 1번에서 100번 사이여야 합니다')
        return False



if __name__ == "__main__":
    age = int(input('나이를 입력하세요: '))
    if check_age(age):
        seat = int(input('좌석 번호를 입력하세요: '))
        
