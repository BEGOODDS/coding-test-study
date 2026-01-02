# 문제 설명
# 리스트 numbers가 매개변수로 주어졌을 때, numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성하는 문제

# 제출하여 통과한 정답
def solution(numbers):
answer = 0
numbers.sort()
numbers.reverse()
answer =  numbers[0] * numbers[1]
return answer

# 오답 해결 과정
# 1. 매개변수 numbers의 타입이 정의되어 있지 않아 함수 내에서 한 번 정의해줘야 한다고 잘못 생각하여 numbers = [] 실행
# numbers = []는 정의해주는 코드가 아니라 입력된 numbers를 빈 list로 바꾸기만 하는 코드였음.
# 2. 문제의 조건이 두 개를 곱해 만들 수 있는 가장 큰 수를 구하는 것이므로 정렬하여 인덱스를 활용하여 풀려 했고,
# numbers.sort() 후 numbers.reverse() 하고자 우선적으로 numbers = numbers.sort()를 실행했는데
# numbers.sort() 는 numbers가 오름차순 정렬되는 함수는 맞지만 정렬된 list를 값으로 가지고 있는 게 아니라 그냥 정렬만 하기 때문에 값으로는 None을 반환함.
# 따라서 numbers = numbers.sort() 를 하면 numbers = None 이 되는 거임. 절망.
# 결론 - list를 정렬하고 싶으면 그냥 .sort()(or .reverse())만 붙이면 된다.

# 충격적으로 간단한 다른 사람의 풀이
def solution(numbers):
numbers.sort()
return numbers[-2] * numbers[-1]

# 정렬 후 인덱스를 거꾸로 사용하면 훨씬 간단함.
