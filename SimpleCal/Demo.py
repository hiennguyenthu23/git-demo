# Nhập điểm số từ người dùng
toan = float(input("Nhập điểm môn Toán: "))
van = float(input("Nhập điểm môn Văn: "))
anh = float(input("Nhập điểm môn Anh: "))
# Tính điểm trung bình
diem_trung_binh = (toan + van + anh) / 3
print("Điểm là ", diem_trung_binh)
#Xếp loại
if (diem_trung_binh < 5):
  print("Học lực yếu")
elif (diem_trung_binh >= 5 and diem_trung_binh < 7):
  print("Học lực trung bình")
elif (diem_trung_binh >= 7 and diem_trung_binh < 9):
  print("Học lực khá")
elif (diem_trung_binh >= 9):
  print("Học lực giỏi")
