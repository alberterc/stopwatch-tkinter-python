import tkinter as tk

#init
isRunning = False
second = 0
minute = 0
hour = 0
resetTime = '0:0:0'
master = tk.Tk()
master.title('Stopwatch')
master.minsize(width = 180, height = 140)

def update(timeText):
    def logic():
        if isRunning:
            global second
            global minute
            global hour
            if second == 0:
                text = resetTime
            else:
                strsecond = str(second)
                strminute = str(minute)
                strhour = str(hour)
                text = strhour + ':' + strminute + ':' + strsecond
            timeText['text'] = text
            timeText.after(1000, logic)
            second += 1
            if second % 60 == 0 and second != 0:
                minute += 1
                second = 0
            if minute % 60 == 0 and minute != 0:
                hour += 1
                minute = 0
    logic()

def Start(timeText):
    global isRunning
    isRunning = True
    update(timeText)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global isRunning
    isRunning = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'

def Reset(timeText):
    global second
    second = 0
    minute = 0
    hour = 0
    if (isRunning == False):
        reset['state'] = 'disabled'
        timeText['text'] = resetTime
    else:
        timeText['text'] = resetTime

#window content
title = tk.Label(master,
            text = 'Stopwatch',
            font = ('Arial', 15)
            )
timeText = tk.Label(master,
            text = resetTime,
            font = ('Arial', 20)
            )
start = tk.Button(master,
            text = 'Start',
            width = 5,
            font = ('Arial' , 10),
            command = lambda: Start(timeText)
            )
stop = tk.Button(master,
            text = 'Stop',
            width = 5,
            font = ('Arial', 10),
            command = Stop
            )
reset = tk.Button(master,
            text = 'Reset',
            width = 5,
            font = ('Arial', 10),
            command = lambda: Reset(timeText)
            )

#placing the window contents
title.grid(row = 0, column = 0, pady = 1, columnspan = 3)
timeText.grid(row = 1, column = 0, pady = 1, padx = 20, rowspan = 3, columnspan = 2)
start.grid(row = 1, column = 2, pady = 1)
stop.grid(row = 2, column = 2, pady = 1)
reset.grid(row = 3, column = 2, pady = 1)

master.mainloop()
