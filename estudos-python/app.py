import turtle
import time
import random

# Configurações iniciais da tela
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Feliz Dia dos Namorados")


# Função para desenhar um coração
def draw_heart(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 200)
    t.left(120)
    t.circle(-size/2, 200)
    t.forward(size)
    t.end_fill()
    t.penup()
    t.home()

# Função para desenhar um fogo de artifício
def draw_firework(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(36):
        t.forward(size)
        t.backward(size)
        t.left(10)
    t.penup()
    t.home()

# Função para escrever a mensagem
def write_message(t, message, x, y, color, font_size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.write(message, align="center", font=("Arial", font_size, "bold"))
    t.penup()
    t.home()

# Configuração da tartaruga
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Lista de corações e fogos de artifício
hearts = []
fireworks = []

# Desenhando corações
colors = ["red", "pink", "purple", "violet"]
for i in range(6):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(50, 100)
    color = random.choice(colors)
    draw_heart(t, x, y, size, color)

# Desenhando fogos de artifício
for i in range(5):
    x = random.randint(-300, 300)
    y = random.randint(0, 300)
    size = random.randint(50, 150)
    color = random.choice(colors)
    draw_firework(t, x, y, size, color)

# Função para animar corações
def animate_hearts():
    for i in range(5):
        for x, y, size, color in hearts:
            draw_heart(t, x, y, size + i*10, color)
        screen.update()
        time.sleep(0.1)
        t.clear()

# Função para animar fogos de artifício
def animate_fireworks():
    for _ in range(3):
        for x, y, size, color in fireworks:
            draw_firework(t, x, y, size, color)
        screen.update()
        time.sleep(0.5)
        t.clear()
    
# Escrevendo mensagem de Dia dos Namorados
write_message(t, "Feliz Dia dos Namorados!", 0, -150, "white", 24)

# Escrevendo citação de Carl Sagan
write_message(t, "Na vastidão do espaço e na imensidão do tempo,", 0, -200, "white", 16)
write_message(t, "é uma alegria compartilhar um planeta e uma época", 0, -230, "white", 16)
write_message(t, "com você.", 0, -260, "white", 16)
time.sleep(5)

# Animando corações e fogos de artifício]
while True:
  animate_hearts()
  animate_fireworks()

screen.update()
time.sleep(2000)

# Mantendo a janela aberta
turtle.done()
