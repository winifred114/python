# "Hello World 출력하기"
# print("Hello World")

# number = 10
# double = 2*number
# print(double)
# number = 5
# print(double)
# double = 2*number
# print(double)

# num = 3.14
# print(num)
# num = 314e-2
# print(num)

# my_str = 'hello'
# print(my_str[4::-1])
# print(my_str[:4:-1])
# print(my_str[-4:-2:-2]) # -4부터-2면 진행방향이 오른쪽 근데 -2만큼 가라했으니까 안나옴
# print(my_str[-4:-2:2])

# my_str = 'hello'
# my_str[1] = 'a'  # 문자열은 변경 불가
# print(my_str)  # TypeError 발생

# my_list = [1,2,3]
# my_list[0] = 10  # 리스트는 변경 가능
# print(my_list)  # [10, 2, 3] 출력

# x, y = 10, 20  # 튜플 언패킹
# print(x, y)  # 10 20 출력

# x, y = y, x  # 튜플 언패킹을 이용한 값 교환
# print(x, y)  # 20 10 출력

# student = ('홍길동', 20, '서울')  # 튜플 생성
# name, age, city = student  # 튜플 언패킹
# print(name, age, city)  # 홍길동 20 서울 출력

# my_dict = {'name': '홍길동', 'age': 20, 'city': '서울'}  # 딕셔너리 생성
# print(my_dict['name'])  # 홍길동 출력
# my_dict['birth'] = '2000-01-01'  # 딕셔너리에 새로운 키-값 쌍 추가
# print(my_dict)  # {'name': '홍길동', 'age': 20, 'city': '서울', 'birth': '2000-01-01'} 출력
# my_dict['age'] = 21  # 딕셔너리의 값 변경
# print(my_dict)  # {'name': '홍길동', 'age': 21, 'city': '서울', 'birth': '2000-01-01'} 출력
# print(my_dict.keys())  # 딕셔너리의 키 출력
# print(my_dict.values())  # 딕셔너리의 값 출력
# print(my_dict.items())  # 딕셔너리의 키-값 쌍 출력
# print(my_dict['hello']) # KeyError 발생, 'hello' 키가 없음

# a = '123'
# b = '123'
# print(id(a))  # a의 주소값 출력
# print(id(b))  # b의 주소값 출력
# # a와 b는 같은 문자열을 참조하므로 주소값이 동일함
# # 리스트는 변경 가능
# c = [1, 2, 3]
# d = [1, 2, 3]
# print(id(c))  # c의 주소값 출력
# print(id(d))  # d의 주소값 출력
# print(c is d)  # False, c와 d는 다른 객체를 참조함
# print(c == d)  # True, c와 d는 같은 값을 가짐

# vowels = 'aeiou'

# print(('a' and 'b') in vowels)  # False, 'a'가 먼저 평가되어 b를 평가 b는 False니까 False
# print(('b' and 'a') in vowels)  # True, 'b'가 먼저 평가되어 마지막인 a, a는 True니까 True

# print(3 and 5)  # 5, 3이 True로 평가되므로 5가 출력됨
# print(3 and 0)  # 0, 3이 True로 평가되지만 0은 False로 평가되어 0이 출력됨
# print(0 and 3)  # 0, 0이 False로 평가되어 0이 출력됨
# print(0 and 0)  # 0, 둘 다 False로 평가되어 0이 출력됨

# print(5 or 3)  # 5, 5가 True로 평가되어 5가 출력됨
# print(3 or 5)  # 3, 3이 True로 평가되어 3이 출력됨
# print(3 or 0)  # 3, 3이 True로 평가되어 3이 출력됨
# print(0 or 3)  # 3, 0이 False로 평가되어 3이 출력됨
# print(0 or 0)  # 0, 둘 다 False로 평가되어 0이 출력됨
# print(f'{1}              {3}') # print안에서 띄어쓰기 하는법
# print(1, '           ', 3) # print안에서 띄어쓰기 하는법
# A = ['a', 'b', 'c', 'c', 'a'] # enumerate 사용 예
# B = [(i, v) for i, v in enumerate(A) if not i % 2]
# C = [(i, v) if v == 'a' else "불통" for i, v in enumerate(A)]
# D = [(i, v) for i, v in enumerate(A, start = 5)]
# print(A)
# print(B)
# print(C)
# print(D)