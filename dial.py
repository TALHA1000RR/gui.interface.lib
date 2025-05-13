import tkinter as tk
import math

class AnalogClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio 0...9")
        self.root.configure(bg='yellow')

        # Entrada de texto
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Botão
        self.button = tk.Button(root, text="0...9", command=self.start_animation, font=("Arial", 14))
        self.button.pack(pady=10)

        # Canvas para desenhar o "relógio"
        self.canvas_size = 300
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack(pady=10)

        # Centro e raio
        self.center = self.canvas_size // 2
        self.radius = self.canvas_size // 2 - 30

        self.pointer = None
        self.current_number = 0

        self.draw_clock()
        self.draw_pointer(0)

    def draw_clock(self):
        # Círculo do relógio
        self.canvas.create_oval(
            self.center - self.radius, self.center - self.radius,
            self.center + self.radius, self.center + self.radius,
            outline="black"
        )
        # Marcar os números de 0 a 9
        for i in range(10):
            angle = math.radians(i * 36 - 90)  # 360/10 = 36 graus por número
            x = self.center + math.cos(angle) * (self.radius - 20)
            y = self.center + math.sin(angle) * (self.radius - 20)
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))

    def draw_pointer(self, number):
        if self.pointer:
            self.canvas.delete(self.pointer)

        angle = math.radians(number * 36 - 90)
        x = self.center + math.cos(angle) * (self.radius - 40)
        y = self.center + math.sin(angle) * (self.radius - 40)
        self.pointer = self.canvas.create_line(self.center, self.center, x, y, width=4, fill="red")

    def start_animation(self):
        try:
            target = int(self.entry.get())
            if not (0 <= target <= 9):
                raise ValueError
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Digite 0 a 9")
            return

        self.current_number = 0
        self.animate_to(target)

    def animate_to(self, target):
        if self.current_number > target:
            return
        self.draw_pointer(self.current_number)
        self.current_number += 1
        if self.current_number <= target:
            self.root.after(1500, lambda: self.animate_to(target))

# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalogClockApp(root)
    root.mainloop()

