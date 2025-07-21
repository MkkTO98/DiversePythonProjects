import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.20

# After five work sessions a long break is granted, making one run-through:
# TIME_TO_BE_WORKING = (WORK_MIN+SHORT_BREAK_MIN)*5 +(LONG_BREAK_MIN-SHORT_BREAK_MIN) for a default value of 170 min (2h and 50min)
# The SHORT_BREAK_MIN is subtracted as for the long break not to be SHORT_BREAK_MIN + LONG_BREAK_MIN


current_time = int(WORK_MIN*60)
current_timer_step = 0
has_been_reset = False

# ---------------------------- TIMER RESET ------------------------------- #

def start_timer():
    global current_time, has_been_reset
    has_been_reset = False
    current_time = int(WORK_MIN*60)
    advance_timer()


def reset_timer():
    global current_time, check_marks
    if current_timer_step == 0:
        current_time = int(WORK_MIN * 60)
    elif current_timer_step%2==0 and current_timer_step<9:
        current_time = int(WORK_MIN*60)
    elif current_timer_step%2==1 and current_timer_step<9:
        current_time = int(SHORT_BREAK_MIN*60)
    elif current_timer_step==9:
        current_time = int(LONG_BREAK_MIN*60)


def reset_working_schedule():
    global current_time, check_marks, current_timer_step, has_been_reset
    current_timer_step = 0
    current_time = 0
    check_marks.config(text='')
    has_been_reset = True
    title_label.config(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
    display_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def display_timer():
    global current_time
    sec = current_time % 60
    minutes = int(current_time / 60)
    displayed_sec = '00'
    displayed_min = '00'
    if sec < 10:
        displayed_sec = '0' + str(sec)
    else:
        displayed_sec = str(sec)
    if minutes < 10 <= 60:
        displayed_min = '0' + str(minutes)
    else:
        displayed_min = str(minutes)
    canvas.itemconfig(canvas_text, text=displayed_min + ':' + displayed_sec)

def create_check_mark():
    global  check_marks
    check_marks.config(text=check_marks.cget('text')+'✔')
    check_marks.grid(row=3, column=2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def advance_timer():
    global current_time, current_timer_step
    if current_time>0 and current_timer_step <=9:
        current_time -= 1
        window.after(100, advance_timer)
    elif current_time==0 and not has_been_reset:
        window.lift()
        if current_timer_step%2==0:
            create_check_mark()
        current_timer_step+=1
        if current_timer_step%2==0:
            title_label.config(text='Work', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
        elif current_timer_step%2==1:
            title_label.config(text='Break', bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, 'bold'))
        reset_timer()
        if current_timer_step<=9:
            advance_timer()
        elif current_timer_step==10:
            reset_working_schedule()
    elif current_timer_step==10:
        current_timer_step = 0
    display_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
title_label.grid(row=1, column=2)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(101, 140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)



start_button = tkinter.Button(bg='white', activebackground=GREEN, text='start', command=start_timer)
start_button.grid(row=3, column=1)
reset_button = tkinter.Button(bg='white', activebackground=GREEN, text='reset', command=reset_working_schedule)
reset_button.grid(row=3, column=3)

check_marks = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, 'bold'))



window.mainloop()