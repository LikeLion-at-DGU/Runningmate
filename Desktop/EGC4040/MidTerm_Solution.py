#1-1
hours = 24
minutes = hours * 60
seconds = minutes * 60
print('하루는 %d시간, %d분, %d초입니다.' %(hours, minutes, seconds))

#1-2
name = 'Peter'
day = 'Monday'
temperature = 17
weather = 'Rainy'
##프린트문 필요

#1-3
side_a = 105.51
side_b = 624

side_c = (side_a**2 + side_b**2)**(0.5)

print(f'피타고라스의 정리: 변A의 길이가 {side_a:6.2f}, 변B의 길이가 {side_b:6.2f}일 때 가장 긴 변 C의 길이는 {side_c:6.2f}입니다.')

#2
a= int(input('첫번째 숫자를 입력하세요 (0보다 큰 정수): '))
b= int(input('두번째 숫자를 입력하세요 (0보다 큰 정수): '))

check = (a>= (10**(b-1))) and (a < 10**b)
print(f'{a}는 {b}자리 숫자입니다: {check}')

#3
my_lst = [1, 2, ['a', ['b', 'c', 'd'], 'd', 'e'] 5, 6, 7]
sub_lst = [3, 4, 5]

my_lst[2][1].insert(2, sub_lst)
del my_lst[2][2]
del my_lst [3]
print(my_lst)


#4
my_dict = {'이름':'Emma', '전공': 'AI convergence', '정보':{'나이':20, '생년월일':2003.03.14}, '성별':'female'}
my_str = my_dict['정보']['생년월일']
##b_month = int(my_str[5:7])
b_month = int(my_str.split('.')[1])

if 3<=b_month<=5:
    seaseon = '봄'
elif 6<=b_month<=8:
    season = '여름'
elif 9<=b_month<=11:
    season = '가을'
else:
    season = '겨울'

print(f"{my_dict['이름']}는 {my_dict['전공']} 소속이며, 태어난 계절은 {season}입니다.")


#5


