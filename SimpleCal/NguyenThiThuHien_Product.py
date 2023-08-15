import tkinter as tk
from tkinter import ttk

def calculate_gpa():
    # Lấy tên học sinh từ trường nhập liệu
    ten_hoc_sinh = ten_var.get()

    # Lấy điểm từng môn từ các biến lưu trữ điểm
    toan = float(toan_var.get())
    van = float(van_var.get())
    anh = float(anh_var.get())
    ly = float(ly_var.get())
    hoa = float(hoa_var.get())

    # Tính điểm trung bình
    diem_tb = (toan + van + anh + ly + hoa) / 5.0
    gpa_var.set("{:.2f}".format(diem_tb))

    # Xếp loại hạnh kiểm
    if diem_tb >= 9.0:
        xep_loai_var.set("Xuất sắc")
    elif 8.5 <= diem_tb < 9.0:
        xep_loai_var.set("Giỏi")
    elif 6.0 <= diem_tb < 8.5:
        xep_loai_var.set("Khá")
    elif 5.0 <= diem_tb < 6.0:
        xep_loai_var.set("Trung bình")
    else:
        xep_loai_var.set("Yếu")

    # Hiển thị tên học sinh và xếp loại kèm theo kết quả GPA
    result_label.config(text=f"Tên học sinh: {ten_hoc_sinh}, GPA: {gpa_var.get()}, Xếp loại: {xep_loai_var.get()}")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Tính điểm trung bình")
#window.iconbitmap("C:\\Users\\hienn\\OneDrive\\Desktop\\Calculator_31111.ico")
window.geometry("500x400")

# Frame chứa tiêu đề và các trường nhập điểm
header_frame = ttk.Frame(window)
header_frame.pack(pady=10)

# Tiêu đề "Nhập thông tin học sinh" trong font chữ Helvetica kích thước 14
ttk.Label(header_frame, text="Nhập thông tin học sinh:", font=("Times New Roman", 14)).grid(row=0, columnspan=2)

# Tạo trường nhập tên học sinh
ttk.Label(header_frame, text="Tên học sinh:", font=("Times New Roman", 12)).grid(row=1, column=0, padx=5, pady=5)
ten_var = tk.StringVar()
ten_entry = ttk.Entry(header_frame, textvariable=ten_var, width=20)
ten_entry.grid(row=1, column=1, padx=5, pady=5)

# Tiêu đề "Nhập điểm các môn" trong font chữ Helvetica kích thước 14
ttk.Label(header_frame, text="Nhập điểm các môn:", font=("Times New Roman", 14)).grid(row=2, columnspan=5)

# Danh sách tên các môn học
mon_hocs = ["Toán", "Văn", "Anh", "Lý", "Hóa"]

# Danh sách biến lưu trữ điểm các môn
toan_var = tk.DoubleVar()
van_var = tk.DoubleVar()
anh_var = tk.DoubleVar()
ly_var = tk.DoubleVar()
hoa_var = tk.DoubleVar()
gpa_var = tk.StringVar()
xep_loai_var = tk.StringVar()

# Tạo trường nhập điểm cho từng môn học
for i in range(len(mon_hocs)):
    ttk.Label(header_frame, text=mon_hocs[i] + ":", font=("Times New Roman", 12)).grid(row=i+3, column=0, padx=5, pady=5)

    # Tạo trường nhập liệu và liên kết với biến tương ứng
    entry = ttk.Entry(header_frame, textvariable=toan_var if i == 0 else van_var if i == 1 else anh_var if i == 2 else ly_var if i == 3 else hoa_var, width=10)
    entry.grid(row=i+3, column=1, padx=5, pady=5)

    # Xóa nội dung trong trường nhập liệu khi người dùng nhấp vào trường đó
    entry.bind("<FocusIn>", lambda event: event.widget.delete(0, tk.END))

# Nút "Tính GPA" để tính điểm trung bình
ttk.Button(window, text="Tính GPA", command=calculate_gpa).pack(pady=15)

# Kết quả GPA và xếp loại hạnh kiểm
result_label = ttk.Label(window, text="", font=("Times New Roman", 12))
result_label.pack(pady=10)

window.mainloop()
