import random

# 리스트
menu = ["순남시레기","멀티캠퍼스 20층","양자강","강남목장", "시골집"]
# 딕셔너리
menu_detail = {"순남시레기":"시레기국, 보쌈","멀티캠퍼스 20층":"오늘의 메뉴",
               "양자강":"차돌짬뽕","강남목장":"뚝배기 불고기","시골집":"쌈밥정식"}

lunch = random.choice(menu)

# 문자열에 +는 문자열을 합친다는 의미
print(lunch + "에서는 " + menu_detail[lunch] + "이(가) 먹을만 합니다.")