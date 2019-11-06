# Solution 1
while True:
    score_input = input("학생점수입력: ")
    try:
        score = float(score_input)
    except:
        print("점수를 입력해주세요~!")
        continue
    if score > 100 or score < 0:
        print("범위를 벗어났습니다.")
        continue
    elif score >= 88:
        print("A+")
        break
    elif score >= 77:
        print("A0")
        break
    elif score == 0:
        print("F")
        break
    else:
        print("B+")
        break

# solution2
try:
    score_input = input("학생점수입력: ")
    score = int(score_input)
    try:
        if score > 100 or score < 0:
            raise Exception
        elif score >= 88:
            print("A+")
        elif score >= 77:
            print("A0")
        elif score == 0:
            print("F")
        else:
            print("B+")
    except:
        print("범위를 벗어났습니다.")
except:
    print("숫자를 입력해주세요.")