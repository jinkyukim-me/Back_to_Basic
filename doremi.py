while True:
    try:
        fruit_name = input("입력하고 싶은 숫자가 뭐에요?")
        fruit_name = int(fruit_name)
        if fruit_name < 10:
            print("10보다 작은 숫자가 입력이 되었습니다")
        else:
            print("10보다 큰 숫자가 입력이 되었습니다.")
        break
    except:
        print("숫자를 입력해주세요 ㅠㅠ")
        continue

