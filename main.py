import tkinter as tk

import ChartExample2
import ChartExample3

def do_close():
    window.destroy()

window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 25)

btnChart = tk.Button(window, text = "График 1", font = ('Helvetica', 10, 'bold'), command = ChartExample2.plot_chart)
btnChart.place(x = 40, y = 115, width = 90, height = 30)

lblChart = tk.Label(text = "График синуса matplotlib")
lblChart.place(x = 170, y = 122)

btnChart2 = tk.Button(window, text = "График 2", font = ('Helvetica', 10, 'bold'), command = ChartExample3.plot_chart)
btnChart2.place(x = 40, y = 165, width = 90, height = 30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x = 170, y = 172)

btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 330, y = 400, width = 90, height = 30)

window.mainloop()
