# 문제 설명
# 정수 n과 정수 list인 numlist를 매개변수로 주고, numlist에서 n의 배수인 수만 포함한 list를 return하도록 함수를 완성하는 문제

# 저번 문제(배열의 유사도.py)와 비슷한 패턴이라 반복문과 조건문, 인덱스를 사용하여 코드 구성
# 통과한 최종 정답
def solution(n, numlist):
    answer = []
    for i in range(len(numlist)) :
        if numlist[i] % n == 0 : # 처음엔 첫 입출력 예시만 보고 3으로 했다가 수정(문제를 잘 읽자.)
            answer += [numlist[i]]
    return answer
# answer += [numlist[i]] 부분에서 처음엔 numlist[i]를 []로 감싸지 않아 TypeError가 났었음.
# 그니까 []에 그냥 int를 더하려고 했던 것..

# 다른 사람의 간단한 풀이
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
  
# filter 함수 : 조건에 맞는 요소만 걸러내는 함수
# filter(조건함수, 리스트) 
# 사용 예시
numbers = [1, 2, 3, 4, 5, 6]
# 짝수만 필터링
def is_even(x):
    return x % 2 == 0
result = filter(is_even, numbers)
list(result)  # [2, 4, 6]

# lambda 함수 : 이름 없는 함수
# lambda 매개변수 반환값(인데 수식이 포함된)
# 사용 예시 1
square = lambda x: x ** 2
square(5)  # 25
# 사용예시 2
add = lambda x, y: x + y
