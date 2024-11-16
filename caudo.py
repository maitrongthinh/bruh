import tkinter as tk
import random

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Trò chơi câu đố")
root.geometry("600x400")
root.configure(bg='#FFD700')

# Tạo câu hỏi
question = tk.Label(root, text="bạn có gay ko?", font=("Arial", 20, "bold"), bg='#FFD700', fg='#8B0000')
question.pack(pady=50)

# Hàm hiển thị thông điệp 
def show_love():
    new_window = tk.Toplevel(root)
    new_window.title("Chúc mừng !")
    new_window.geometry("600x400")
    new_window.configure(bg='#ADD8E6')
    congrats_label = tk.Label(new_window, text="Chúc mừng bạn,bạn đã thành gay!", font=("Arial", 24, "bold"), fg='#8B0000', bg='#ADD8E6')
    congrats_label.pack(expand=True)

# Hàm dịch chuyển nút không  đến vị trí ngẫu nhiên
def move_button(event):
    new_x = random.randint(0, root.winfo_width() - button_no.winfo_width())
    new_y = random.randint(0, root.winfo_height() - button_no.winfo_height())
    button_no.place(x=new_x, y=new_y)

# Tạo nút có
button_yes = tk.Button(root, text="Có", font=("Arial", 15, "bold"), bg='#32CD32', fg='white', command=show_love)
button_yes.pack(side="left", padx=100)

# Tạo nút không  và gán sự kiện dịch chuyển khi di chuột qua
button_no = tk.Button(root, text="Không", font=("Arial", 15, "bold"), bg='#FF6347', fg='white')
button_no.place(x=300, y=248)
button_no.bind("<Enter>", move_button)

# Chạy vòng lặp chính của cửa sổ
root.mainloop()
