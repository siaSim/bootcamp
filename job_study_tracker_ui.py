import tkinter as tk
from tkinter import messagebox, ttk

job_posts = []
study_logs = []


def add_job_post():
    company = company_entry.get().strip()
    position = position_entry.get().strip()
    status = status_entry.get().strip()
    deadline = deadline_entry.get().strip()

    if not company or not position or not status or not deadline:
        messagebox.showwarning(
            "입력 오류",
            "채용공고 정보를 모두 입력해주세요."
        )
        return

    job = {
        "company": company,
        "position": position,
        "status": status,
        "deadline": deadline
    }

    job_posts.append(job)
    messagebox.showinfo("완료", "채용공고가 추가되었습니다.")

    company_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

    refresh_job_list()


def refresh_job_list():
    job_listbox.delete(0, tk.END)

    if not job_posts:
        job_listbox.insert(tk.END, "등록된 채용공고가 없습니다.")
        return

    for i, job in enumerate(job_posts, start=1):
        text = (
            f"[{i}] 회사명: {job['company']} | "
            f"직무: {job['position']} | "
            f"지원 상태: {job['status']} | "
            f"마감일: {job['deadline']}"
        )
        job_listbox.insert(tk.END, text)


def add_study_log():
    date = study_date_entry.get().strip()
    topic = topic_entry.get().strip()
    hours_text = hours_entry.get().strip()
    memo = memo_entry.get().strip()

    if not date or not topic or not hours_text or not memo:
        messagebox.showwarning(
            "입력 오류",
            "공부기록 정보를 모두 입력해주세요."
        )
        return

    try:
        hours = float(hours_text)
    except ValueError:
        messagebox.showerror(
            "입력 오류",
            "공부 시간은 숫자로 입력해주세요."
        )
        return

    study = {
        "date": date,
        "topic": topic,
        "hours": hours,
        "memo": memo
    }

    study_logs.append(study)
    messagebox.showinfo("완료", "공부기록이 추가되었습니다.")

    study_date_entry.delete(0, tk.END)
    topic_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)
    memo_entry.delete(0, tk.END)

    refresh_study_list()
    show_total_study_hours()


def refresh_study_list():
    study_listbox.delete(0, tk.END)

    if not study_logs:
        study_listbox.insert(tk.END, "등록된 공부기록이 없습니다.")
        return

    for i, study in enumerate(study_logs, start=1):
        text = (
            f"[{i}] 날짜: {study['date']} | "
            f"주제: {study['topic']} | "
            f"공부 시간: {study['hours']}시간 | "
            f"메모: {study['memo']}"
        )
        study_listbox.insert(tk.END, text)


def show_total_study_hours():
    total = 0
    for study in study_logs:
        total += study["hours"]

    total_hours_label.config(
        text=f"총 공부 시간: {total}시간"
    )


root = tk.Tk()
root.title("채용공고 / 공부기록 관리기")
root.geometry("1000x700")
root.configure(bg="#f5f7fb")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Title.TLabel",
    font=("맑은 고딕", 18, "bold"),
    background="#f5f7fb",
    foreground="#222222"
)

style.configure(
    "Section.TLabelframe",
    background="white"
)

style.configure(
    "Section.TLabelframe.Label",
    font=("맑은 고딕", 12, "bold")
)

style.configure(
    "TLabel",
    background="white",
    font=("맑은 고딕", 10)
)

style.configure(
    "TButton",
    font=("맑은 고딕", 10, "bold"),
    padding=6
)

style.configure(
    "TEntry",
    padding=5
)

title_label = ttk.Label(
    root,
    text="채용공고 / 공부기록 관리기",
    style="Title.TLabel"
)
title_label.pack(pady=20)

main_frame = tk.Frame(root, bg="#f5f7fb")
main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

left_frame = tk.Frame(main_frame, bg="#f5f7fb")
left_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10
)

right_frame = tk.Frame(main_frame, bg="#f5f7fb")
right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=10
)

job_frame = ttk.LabelFrame(
    left_frame,
    text="채용공고 추가",
    style="Section.TLabelframe",
    padding=15
)
job_frame.pack(fill="x", pady=10)

ttk.Label(job_frame, text="회사명").grid(
    row=0,
    column=0,
    sticky="w",
    pady=5
)
company_entry = ttk.Entry(job_frame, width=30)
company_entry.grid(row=0, column=1, pady=5, padx=5)

ttk.Label(job_frame, text="직무").grid(
    row=1,
    column=0,
    sticky="w",
    pady=5
)
position_entry = ttk.Entry(job_frame, width=30)
position_entry.grid(row=1, column=1, pady=5, padx=5)

ttk.Label(job_frame, text="지원 상태").grid(
    row=2,
    column=0,
    sticky="w",
    pady=5
)
status_entry = ttk.Entry(job_frame, width=30)
status_entry.grid(row=2, column=1, pady=5, padx=5)

ttk.Label(job_frame, text="마감일").grid(
    row=3,
    column=0,
    sticky="w",
    pady=5
)
deadline_entry = ttk.Entry(job_frame, width=30)
deadline_entry.grid(row=3, column=1, pady=5, padx=5)

job_add_button = ttk.Button(
    job_frame,
    text="채용공고 추가",
    command=add_job_post
)
job_add_button.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)

job_list_frame = ttk.LabelFrame(
    left_frame,
    text="채용공고 목록",
    style="Section.TLabelframe",
    padding=15
)
job_list_frame.pack(fill="both", expand=True, pady=10)

job_listbox = tk.Listbox(
    job_list_frame,
    font=("맑은 고딕", 10),
    height=15,
    bd=0,
    highlightthickness=0
)
job_listbox.pack(fill="both", expand=True)

study_frame = ttk.LabelFrame(
    right_frame,
    text="공부기록 추가",
    style="Section.TLabelframe",
    padding=15
)
study_frame.pack(fill="x", pady=10)

ttk.Label(study_frame, text="날짜").grid(
    row=0,
    column=0,
    sticky="w",
    pady=5
)
study_date_entry = ttk.Entry(study_frame, width=30)
study_date_entry.grid(row=0, column=1, pady=5, padx=5)

ttk.Label(study_frame, text="공부 주제").grid(
    row=1,
    column=0,
    sticky="w",
    pady=5
)
topic_entry = ttk.Entry(study_frame, width=30)
topic_entry.grid(row=1, column=1, pady=5, padx=5)

ttk.Label(study_frame, text="공부 시간").grid(
    row=2,
    column=0,
    sticky="w",
    pady=5
)
hours_entry = ttk.Entry(study_frame, width=30)
hours_entry.grid(row=2, column=1, pady=5, padx=5)

ttk.Label(study_frame, text="메모").grid(
    row=3,
    column=0,
    sticky="w",
    pady=5
)
memo_entry = ttk.Entry(study_frame, width=30)
memo_entry.grid(row=3, column=1, pady=5, padx=5)

study_add_button = ttk.Button(
    study_frame,
    text="공부기록 추가",
    command=add_study_log
)
study_add_button.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)

study_list_frame = ttk.LabelFrame(
    right_frame,
    text="공부기록 목록",
    style="Section.TLabelframe",
    padding=15
)
study_list_frame.pack(fill="both", expand=True, pady=10)

study_listbox = tk.Listbox(
    study_list_frame,
    font=("맑은 고딕", 10),
    height=12,
    bd=0,
    highlightthickness=0
)
study_listbox.pack(fill="both", expand=True)

total_hours_label = tk.Label(
    right_frame,
    text="총 공부 시간: 0시간",
    font=("맑은 고딕", 12, "bold"),
    bg="#f5f7fb",
    fg="#222222"
)
total_hours_label.pack(pady=10)

refresh_job_list()
refresh_study_list()

root.mainloop()