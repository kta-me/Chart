import tkinter as tk

import NormalCharts
import SinusChart
import SeabornChart

def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x520")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 25)

# Добавление кнопки и метки для графика 1
btnChart = tk.Button(window, text = "График 1", font = ('Helvetica', 10, 'bold'), command = SinusChart.show_chart)
btnChart.place(x = 40, y = 115, width = 90, height = 30)

lblChart = tk.Label(text = "График синуса matplotlib")
lblChart.place(x = 170, y = 122)

# Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text = "График 2", font = ('Helvetica', 10, 'bold'), command = NormalCharts.one_chart)
btnChart2.place(x = 40, y = 165, width = 90, height = 30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x = 170, y = 172)

# Добавление кнопки и метки для графика 3
btnChart3 = tk.Button(window, text = "График 3", font = ('Helvetica', 10, 'bold'), command = NormalCharts.three_charts)
btnChart3.place(x = 40, y = 215, width = 90, height = 30)

lblChart3 = tk.Label(text = "Нормальное распределение - 3 графика")
lblChart3.place(x = 170, y = 222)

# Добавление кнопки и метки для графика 4
btnChart4 = tk.Button(window, text = "График 4", font = ('Helvetica', 10, 'bold'), command = SeabornChart.show_chart)
btnChart4.place(x = 40, y = 265, width = 90, height = 30)

lblChart4 = tk.Label(text = "Гистограмма Seaborn")
lblChart4.place(x = 170, y = 272)

# Добавление кнопки и метки для графика 5
btnChart5 = tk.Button(window, text = "График 5", font = ('Helvetica', 10, 'bold'), command = SinusChart.show_chart)
btnChart5.place(x = 40, y = 315, width = 90, height = 30)

lblChart5 = tk.Label(text = "Описание графика")
lblChart5.place(x = 170, y = 322)

# Добавление кнопки и метки для графика 6
btnChart6 = tk.Button(window, text = "График 6", font = ('Helvetica', 10, 'bold'), command = SinusChart.show_chart)
btnChart6.place(x = 40, y = 365, width = 90, height = 30)

lblChart6 = tk.Label(text = "Описание графика")
lblChart6.place(x = 170, y = 372)

# Добавление кнопки и метки для графика 7
btnChart7 = tk.Button(window, text = "График 7", font = ('Helvetica', 10, 'bold'), command = SinusChart.show_chart)
btnChart7.place(x = 40, y = 415, width = 90, height = 30)

lblChart7 = tk.Label(text = "Описание графика")
lblChart7.place(x = 170, y = 422)

# Закрытие главного окна
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 330, y = 465, width = 90, height = 30)

window.mainloop()
