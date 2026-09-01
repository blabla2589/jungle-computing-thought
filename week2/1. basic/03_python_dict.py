"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""

def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수
    
    Args:
        students: 학생 정보 딕셔너리 리스트
    
    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """
    # TODO: 모든 학생의 점수를 리스트로 추출하세요
    pass

    # 컴프리헨션(Comprehension)은 파이썬(Python)을 포함한 일부 프로그래밍 언어에서 반복문과 조건문을 사용하여
    # 리스트, 딕셔너리, 세트 등의 자료구조를 간결하고 직관적으로 생성하는 문법
    # students: 우리가 가진 전체 학생 리스트
    # student: 거기서 하나씩 쏙쏙 뽑아낼 때 쓸 임시 이름(변수)
    # student['score']: 그 학생 데이터에서 점수만 꺼내겠다는 표현식

    # 여기서 student 대신 x를 써도 똑같이 작동합니다 ([x['score'] for x in students]).

    # for i in range(total) :
    #     sum += i

    total = [s['score'] for s in students]
     
   
    #for student in students : students 리스트에서 학생 데이터를 하나씩 꺼내어 student라는 변수에 담는다.
    #student['score'] : 그 꺼낸 학생 데이터(student)에서 score(점수) 키에 해당하는 값만 쏙 뽑아낸다.
    #[ ... ] : 그렇게 뽑아낸 값들을 모아서 새로운 리스트(scores)로 완성한다.
    # TODO: 평균 점수를 계산하세요
    pass

    avg = sum(total) / len(students)
    
    # TODO: 평균 이상인 학생들의 이름을 리스트로 추출하세요
    pass

    name_score = [s['name'] for s in students if avg <= s['score']]
    return avg, name_score


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95}
    ]
    
    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()
    
    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90}
    ]
    
    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")


# total = [student['score'] for student in students]

#     total = [s['score'] for s in students]
#     avg = sum(total)/len(students)
#     students = [s['name'] for s  in students if avg < s['score']]
#     return avg, students


