import re

def check_email(email):
    # 이메일 주소를 체크하는 정규표현식 패턴
    pattern = r"[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}"
    
    # 이메일 주소가 패턴과 일치하는지 확인
    if re.match(pattern, email):
        return True
    else:
        return False

# 샘플 이메일 주소 10개 생성
sample_emails = [
    "user@example.com",
    "user.name@example.co.kr",
    "user123@example.com",
    "user_name@example.com",
    "user-name@example.com",
    "user+name@example.com",
    "user@subdomain.example.com",
    "user@[192.168.1.1]",
    "user@localhost",
    "invalid-email"
]

# 각 이메일 주소를 체크하고 결과를 출력
for email in sample_emails:
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")

