import tkinter as tk


class SumOfTwoNumbers(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sum of 2 Numbers")
        self.geometry("300x300")
        self.A = tk.IntVar()
        self.B = tk.IntVar()
        self.A.trace_add("write", self.cal_sum)
        self.B.trace_add("write", self.cal_sum)

        self.create_widgets()

    def create_widgets(self):
        self.A_label = tk.Label(self, text="A: ")
        self.B_label = tk.Label(self, text="B: ")

        self.A_entry = tk.Entry(self, textvariable=self.A)
        self.B_entry = tk.Entry(self, textvariable=self.B)

        self.sum_label = tk.Label(self, text="Sum: ")
        self.result_label = tk.Label(self, text=self.A.get() + self.B.get())

        self.A_label.grid(row=0, column=0, padx=5, pady=5)
        self.A_entry.grid(row=0, column=1, padx=5, pady=5)
        self.B_label.grid(row=1, column=0, padx=5, pady=5)
        self.B_entry.grid(row=1, column=1, padx=5, pady=5)
        self.sum_label.grid(row=2, column=0, padx=5, pady=5)
        self.result_label.grid(row=2, column=1, padx=5, pady=5)

    def calculate_sum(self, *args):
        try:
            num_a = self.A.get()
        except:
            num_a = 0

        try:
            num_b = self.B.get()
        except:
            num_b = 0

        self.result_label['text'] = num_a + num_b

app = SumOfTwoNumbers()
app.mainloop()