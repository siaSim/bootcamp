'''
*채용공고 관리
지원 회사 추가
지원 목록 보기
지원 상태 수정
회사명으로 검색

*공부기록 관리
공부 기록 추가
공부 기록 보기
총 공부 시간 계산
과목별 조회
'''

job_posts = []
study_logs = []


def add_job_post():
    company = input("회사명: ")
    position = input("직무: ")
    status = input("지원 상태: ")
    deadline = input("마감일(예: 2026-03-25): ")

    job = {
        "company": company,
        "position": position,
        "status": status,
        "deadline": deadline
    }

    job_posts.append(job)
    print("채용공고가 추가되었습니다.")


def view_job_posts():
    if not job_posts:
        print("등록된 채용공고가 없습니다.")
        return

    for i, job in enumerate(job_posts, start=1):
        print(f"\n[{i}]")
        print(f"회사명: {job['company']}")
        print(f"직무: {job['position']}")
        print(f"지원 상태: {job['status']}")
        print(f"마감일: {job['deadline']}")


def add_study_log():
    date = input("날짜(예: 2026-03-25): ")
    topic = input("공부 주제: ")
    hours = float(input("공부 시간: "))
    memo = input("메모: ")

    study = {
        "date": date,
        "topic": topic,
        "hours": hours,
        "memo": memo
    }

    study_logs.append(study)
    print("공부기록이 추가되었습니다.")


def view_study_logs():
    if not study_logs:
        print("등록된 공부기록이 없습니다.")
        return

    for i, study in enumerate(study_logs, start=1):
        print(f"\n[{i}]")
        print(f"날짜: {study['date']}")
        print(f"공부 주제: {study['topic']}")
        print(f"공부 시간: {study['hours']}시간")
        print(f"메모: {study['memo']}")


def show_total_study_hours():
    total = 0
    for study in study_logs:
        total += study["hours"]
    print(f"총 공부 시간: {total}시간")


def main():
    while True:
        print("\n== 관리 프로그램 ==")
        print("1. 채용공고 추가")
        print("2. 채용공고 조회")
        print("3. 공부기록 추가")
        print("4. 공부기록 조회")
        print("5. 공부시간")
        print("0. 종료")

        choice = input("메뉴 선택: ")

        if choice == "1":
            add_job_post()
        elif choice == "2":
            view_job_posts()
        elif choice == "3":
            add_study_log()
        elif choice == "4":
            view_study_logs()
        elif choice == "5":
            show_total_study_hours()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


main()
