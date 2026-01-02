# 문제 설명
# 두 문자열 list인 s1, s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수 완성하기

# 풀이 과정
# n과 m을 각각 s1, s2의 인덱스로 사용하기 위해 정의하고, 값이 같으면 answer에 1을 더하면 된다고 생각해서 처음에는 아래와 같이 작성함.
def solution(s1, s2):
    answer = 0
    n >= 0
    m >= 0
    if s1[n] = s2[m] :
        answer =+ 1
    return answer # 다 틀림..

# (1) n과 m을 할당하는 방식(비교 연산)도 틀렸고, 단순히 할당만 해서는 문자열 list 내의 모든 원소들을 비교할 수 없음.
# list 내의 모든 원소들을 비교하려면 반복문을 사용해야 함! (특히 이 문제에서는 n, m 중첩 반복문)

# (2) answer =+ 1 아니고 answer += 1 # 심각..

# 최종 통과된 정답
def solution(s1, s2):
    answer = 0
    for n in range(len(s1)):
        for m in range(len(s2)):
            if s1[n] == s2[m] :
                answer += 1
    return answer

# 다른 사람의 간단한 풀이 - set과 & 연산자 사용
def solution(s1, s2):
    return len(set(s1)&set(s2)) # 충격적..

# set : 중복을 허용하지 않고, 순서가 없는 데이터 묶음
# 연산자 & 를 사용하면 교집합 연산이 자동으로 공통된 것만 찾아준다.
