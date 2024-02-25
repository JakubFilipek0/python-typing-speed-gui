import tkinter
import random

FONT_NAME = "Courier"
texts = [
    "Podczas gdy światło padające przez moje okna zataczało srebrne kółka na mojej podłodze, zrozumiałam, że czasem nawet najmniejsze szczęście wydaje się nierealne, ale to wcale nie znaczy, że jest ono niemożliwe do osiągnięcia.",
    "W czasach wielkiego kryzysu, gdy ludzkość zmaga się z wewnętrznymi i zewnętrznymi demonami, nie tracimy nadziei na lepsze jutro. Bo to właśnie w najtrudniejszych chwilach poznajemy swoją prawdziwą siłę i determinację.",
    "Czy jesteśmy tylko sumą naszych decyzji, czy może los prowadzi nasze kroki niezależnie od naszej woli? To pytanie nurtuje umysły od wieków, jednak odpowiedź pozostaje wciąż nieuchwytna, tak jak światło migoczące na horyzoncie w czasie burzy.",
    "W przestrzeni między snem a rzeczywistością tkwi tajemnica naszego istnienia. To właśnie tam rodzą się marzenia, które prowadzą nas przez labirynt życia, kierując naszymi krokami w nieznane.",
    "Gdybyśmy mogli zmierzyć czas, który spędzamy na marzenia, odkrylibyśmy, że jest on tak samo realny jak każdy inny moment naszego życia. Bo marzenia mają moc zmieniania rzeczywistości i nadawania sensu naszym dniom."
]

root = tkinter.Tk()
root.title('Python Typing Speed')
root.geometry('800x500')

time_running = False
text_number = 0


def start_timer():
    global time_running
    time_running = True
    update_timer()


def stop_timer():
    global time_running
    time_running = False


def update_timer():
    if time_running:
        current_time = timer_var.get()
        current_time += 1
        timer_var.set(current_time)
        calculate_wpm()
        root.after(1000, update_timer)


def generate_text():
    global text_number
    text_number = random.randint(0, 4)
    text_label.configure(text=texts[text_number])


def entry_changed(event):
    global time_running
    if not time_running:
        start_timer()


def calculate_wpm():
    test = random.randint(0, 10)
    user_text = text_text.get('1.0', 'end-1c')
    word_counter = 0
    for word in user_text:
        if word == ' ':
            word_counter += 1
    print(word_counter)
    current_time = timer_var.get()
    current_time = current_time / 60
    user_wpm = word_counter / current_time
    user_wpm = round(user_wpm, 2)
    score_label.configure(text=f'WPM: {user_wpm}')


timer_var = tkinter.IntVar()
timer_var.set(0)

greeting_title = tkinter.Label(text='Hello in Python Typing Speed!', font=(FONT_NAME, 20, 'bold'))
greeting_title.pack(pady=10)

time_label = tkinter.Label(textvariable=timer_var, font=(FONT_NAME, 16, 'bold'))
time_label.pack(pady=10)

score_label = tkinter.Label(text=f'WPM: 0', font=(FONT_NAME, 16, 'bold'), wraplength=700)
score_label.pack(pady=10)

text_label = tkinter.Label(text='', font=(FONT_NAME, 16, 'bold'), wraplength=700)
text_label.pack(pady=10)

generate_text_button = tkinter.Button(text='Generate text', font=(FONT_NAME, 12, 'bold'), command=generate_text)
generate_text_button.pack()

text_text = tkinter.Text(width=100, height=100, font=(FONT_NAME, 16, 'bold'))
text_text.pack(pady=10, padx=10)
text_text.bind('<KeyRelease>', entry_changed)

root.mainloop()
