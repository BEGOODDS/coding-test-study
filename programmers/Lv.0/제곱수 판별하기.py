# 문제 설명
# 정수 n을 매개변수로 주는 함수인데, 이 n이 제곱수면 1, 아니면 2를 반환하도록 함수를 완성하는 문제

# 1. 첫 번째 풀이
def solution(n):
    for i in range(100):
        if (n % i) % i == 0 : # %을 두 번 사용하면 된다고 생각(..)
            answer = 1
        else :
            answer = 2
    return answer
# (1) 반복문 범위에 0이 포함되어
# ZeroDivisionError: integer division or modulo by zero 발생
# 0으로 나누려 할 때 발생하는 에러
# (2) 제곱수의 판별 조건이 틀림
# 어떤 수 i로 나눴을 때 나머지가 0이 되면 안되고, i로 나눴을 때 i가 되어야 함.

# 2. 두 번째 풀이
def solution(n):
    for i in range(1, 100): # 범위 앞단에 1 추가
        if n % i == 0 and n // i == i: # 제곱수 판별 조건 수정
            answer = 1
        else :
            answer = 2
    return answer
# 두 가지 수정 후 실행해 본 결과 맞는 예시도 있지만 틀린 예시도 발생
# 당연함. 반복문 내에 answer를 넣었으니 값이 갱신되는 것
# 제대로 나오게 하려면 2는 반복문 밖에서 내야 함
# 근데 이제 그냥 answer = 2를 반복문 밖으로 빼면 그냥 모든 예시의 결과가 2로 갱신됨. 때문에 반복문 내에서 return을 한 번 해주고, 아예 밖에서 return을 써줘야 두 가지 각각의 경우에 따라 올바른 값을 반환함

# 3. 최종 통과 정답
def solution(n):
    for i in range(1, 10000): # 범위 수정(틀리는 예시들이 존재)
        if n % i == 0 and n // i == i: 
            return 1
    return 2
# range를 (1, 100)로 설정하여 이보다 큰 예시들에서는 여전히 오답 발생하여 range(1, 10000)로 수정
# 더 정확한 범위는 range(1, int(n**0.5) + 1)임. n의 제곱근까지만!
# 0.5승을 생각하지 못함,,

# 충격적으로 간단한 정답
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
# is_integer()는 (n).is_integer() 형태로 쓰이면서 n이 정수면 True, 아니면 False를 반환하는 함수
# 제곱근이 정수면 제곱수니까,, + 0.5승
# if문을 한 줄에 쓰는 간결함
  
# 추가적인 기초
# // 연산자는 소수점 이하는 버리는 몫 나눗셈!(/ 는 float 나눗셈..)
# 반복문 범위 (시작: 포함, 끝: 미포함, 간격(생략 시 1))
