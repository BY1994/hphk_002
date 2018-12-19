"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
# 1. iu_score라고 하는 dic 변수에서 value값만 뽑아내보자.
total_score = 0
count = 0
# 2. 뽑아낸 값들의 총합을 구한다.
for score in iu_score:
    total_score = total_score + iu_score[score]
    count = count + 1
# 3. 총합을 개수로 나눈다.
print(total_score/count)

scores = list(iu_score.values())
# python get values of dict
print(sum(scores)/len(scores))
# python get length of list
# pytho get sum of list




# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}


# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")

# 1. 각 반을 순회하는 반복문을 작성한다.
for cl in score:
# 2. 한 번 순회를 할 때 1번에서 작성한 코드를 활용한다.
    tmp = list(score[cl].values())
# 3. 출력한다.
    print("{}: {}".format(cl, sum(tmp)/len(tmp)))



# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
# 1. 각 도시를 순회하는 반복문을 작성한다.
for ct in city:
    temp = city[ct]
# 2. 1번의 코드를 활용하여 순회할 때마다 평균 값을 출력한다.
    print("{}의 평균기온: {}".format(ct, round(sum(temp)/len(temp),1)))
    # 반올림 대신 다른 방법
    print("{}의 평균기온: {:0.1f}".format(ct, sum(temp)/len(temp)))
    # python get round value


# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

# 1. 최저 기온, 최고 기온을 저장할 수 있는 변수를 선언한다.
minimum = ["도시명", 1000]
maximum = ["도시명", -1000]
# 2. 각 도시를 순회하는 반복문을 만든다.
for ct in city:
# 3. 각 도시의 기온 정보를 순회하는 반복문을 만든다.
    for temp in city[ct]:
# 4. 순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은값이,
#   최고 기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
#   현재 저장되어 있는 값을 바꾼다.
        # 최고기온에 해당하는 조건문
        if (maximum[1] < temp):
            maximum[0] = ct
            maximum[1] = temp
        # 최저기온에 해당하는 조건문
        if (minimum[1] > temp):
            minimum[0] = ct
            minimum[1] = temp
print("최고 기온은 {}의 {}도이며, 최저 기온은 {}의 {}도 입니다.".format(maximum[0],maximum[1],minimum[0],minimum[1]))


hot_temp = {"name":"default","temp":0}
cold_temp= {"name":"default","temp":0}
for city_name in city:
    for temp in city[city_name]:
        if temp > hot_temp["temp"]:
            hot_temp["name"] = city_name
            hot_temp["temp"] = temp
        if temp < cold_temp["temp"]:
            cold_temp["name"] = city_name
            cold_temp["temp"] = temp
print("Q3-1")
print("가장 추웠던 곳 : " + cold_temp["name"])
print("가장 더웠던 곳 : " + hot_temp["name"])



# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
# 1. city 변수에서 서울 부분만 추출해서 seoul 변수에 저장한다.
# 1-1. flag라고 하는 변수에 flase 저장한다.
# 2. seoul 변수(list)를 순회하며 요소가 2와 같았던 적이 있는지 확인한다.
# 3. 2도 같았던 적이 있다면 flag 변수를 true로 바꿔준다.
# 4. flag 변수에 따라 출력문을 작성한다.

print("Q4")
check = 0
for temp in city["서울"]:
    if temp == 2:
        check = 1
        
if check == 1:
    print("True")
else:
    print("False")
