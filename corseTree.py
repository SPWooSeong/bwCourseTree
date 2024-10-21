import pandas as pd
# Modify the Subject class and conversion logic accordingly
file_path = 'corseTree.xlsx'
df = pd.read_excel(file_path)

class Subject:
    def __init__(self, ID, name, code, prerequisite, course_type, major_category, mandatory, minor, credit, semester, note):
        self.ID = ID
        self.name = name  # 과목명
        self.code = code  # 과목 코드
        # Split prerequisite string into list if multiple codes are present
        self.prerequisite = prerequisite.split(',') if isinstance(prerequisite, str) else []  
        self.course_type = course_type  # 이수구분
        self.major_category = major_category  # 전공분류
        # Convert mandatory and minor fields to bool
        self.mandatory = bool(mandatory)  # 전공필수여부
        self.minor = bool(minor)  # 부전공여부
        self.credit = credit  # 학점
        self.semester = semester  # 개설 학기
        self.note = note  # 특이사항

    def __repr__(self):
        return f"Subject({self.name}, {self.code}, {self.credit}학점, 선수과목: {self.prerequisite})"

class User:
    def __init__(self, name, student_id, major):
        self.name = name  # 유저의 이름
        self.student_id = student_id  # 유저의 학번
        self.major = major  # 유저의 전공
        # 각 학기별로 과목을 저장할 수 있는 my_corse_tree 딕셔너리
        self.my_corse_tree = {
            "1학년 1학기": [],
            "1학년 2학기": [],
            "2학년 1학기": [],
            "2학년 2학기": [],
            "3학년 1학기": [],
            "3학년 2학기": [],
            "4학년 1학기": [],
            "4학년 2학기": []
        }

    def __repr__(self):
        return f"User(name={self.name}, student_id={self.student_id}, major={self.major})"

    def add_subject_to_semester_by_name(self, semester, subject_name):
        # 과목 이름으로 일치하는 과목 찾기
        subject = next((subject for subject in subjects if subject.name == subject_name), None)
        
        if subject:
            if semester in self.my_corse_tree:
                self.my_corse_tree[semester].append(subject)
                print(f"'{subject_name}' 과목이 {semester}에 추가되었습니다.")
            else:
                print(f"{semester}은(는) 유효한 학기가 아닙니다.")
        else:
            print(f"'{subject_name}'이라는 과목을 찾을 수 없습니다.")

    # 과목 코드를 기준으로 학기에 과목 추가
    def add_subject_to_semester_by_code(self, semester, subject_code):
        # 과목 코드로 일치하는 과목 찾기
        subject = next((subject for subject in subjects if subject.code == subject_code), None)
        
        if subject:
            if semester in self.my_corse_tree:
                self.my_corse_tree[semester].append(subject)
                print(f"'{subject_code}' 과목이 {semester}에 추가되었습니다.")
            else:
                print(f"{semester}은(는) 유효한 학기가 아닙니다.")
        else:
            print(f"'{subject_code}'이라는 과목을 찾을 수 없습니다.")

    def view_my_corse_tree(self):
        for semester, subjects in self.my_corse_tree.items():
            print(f"{semester}:")
            for subject in subjects:
                print(subject)



# Recreate the list of Subject objects with updated logic
subjects = [
    Subject(
        row['ID'], row['과목명'], row['과목 코드'], row['선수과목 코드'], row['이수구분'],
        row['전공분류'], row['전공필수여부'], row['부전공여부'], row['학점'], row['개설 학기'], row['특이사항']
    )
    for _, row in df.iterrows()
]

def print_subjects_by_semester(num):
    # num이 1 또는 2 이외의 값일 경우 오류 메시지 출력
    if num not in [1, 2]:
        print("잘못된 학기를 입력하였습니다.")
        return
    
    subjects_in_semester = [subject for subject in subjects if subject.semester == num]
    
    print(f"{num}학기에 해당하는 과목 목록:")
    for subject in subjects_in_semester:
        print(subject)

def print_mandatory_subjects():
    # 전공 필수가 True인 과목들 필터링
    mandatory_subjects = [subject for subject in subjects if subject.mandatory]
    
    print("전공 필수 과목 목록:")
    for subject in mandatory_subjects:
        print(subject)
def print_minor_subjects():
    # 부전공 필수가 True인 과목들 필터링
    minor_subjects = [subject for subject in subjects if subject.minor]
    
    print("부전공 필수 과목 목록:")
    for subject in minor_subjects:
        print(subject)
def print_whole_subjects():
    print("전체 과목 목록:")
    for subject in subjects:
        print(subject)

def search_subject_by_name(name):
    # 과목명이 일치하는 과목 찾기
    matching_subject = next((subject for subject in subjects if subject.name == name), None)
    
    if matching_subject:
        print(f"'{name}' 과목에 대한 정보:")
        print(matching_subject)
    else:
        print("잘못된 과목명입니다.")
def search_subject_by_code(code):
    # 과목명이 일치하는 과목 찾기
    matching_subject = next((subject for subject in subjects if subject.code == code), None)
    
    if matching_subject:
        print(f"'{code}' 과목에 대한 정보:")
        print(matching_subject)
    else:
        print("잘못된 과목코드입니다.")


student1 = User("윤우성", "202311123", "전자공학과")
print_mandatory_subjects()


