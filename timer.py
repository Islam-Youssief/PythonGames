import simplegui

seconds = 0
finish = True
tries = 0
time_to_stop = 0


def made_calculations(sec):
    """Display the proper format after calculating seconds and minutes."""
    only_seconds = seconds % 10
    total_sec = seconds / 10
    sec = total_sec % 60
    minute = total_sec / 60
    if sec < 10:
        sec = "0" + str(sec)
    return str(minute) + ':' + str(sec) + ':' + str(only_seconds)


def start():
    """Time continue to consume seconds."""
    global finish
    finish = False


def stop():
    """Stop the timer and add one on the top."""
    global finish
    global tries
    global time_to_stop
    if not finish:
        tries = tries + 1
        if seconds % 10 == 0:
            time_to_stop = time_to_stop + 1
    finish = True


def reset():
    """Reset values of seconds and tries."""
    global seconds
    global finish
    global tries
    global time_to_stop

    finish = True
    seconds = 0
    tries = 0
    time_to_stop = 0


def increase_time_handler():
    """Control time hundler."""
    global seconds
    seconds_limit = 10 * 60 * 60
    if not finish:
        seconds = seconds + 1
    if seconds >= seconds_limit:
        seconds = 0


def draw(canvas):
    """Control the canvas and the view."""
    canvas.draw_text(made_calculations(seconds), [100, 120], 48, "#fcada7")
    canvas.draw_text(str(time_to_stop) + "/" +
                     str(tries), [230, 30], 30, "#48e1e5")
def create_frame():
    # create frame
    frame = simplegui.create_frame("~~ Stopwatch ~~", 300, 200)
    frame.add_button("Start", start, 180)
    frame.add_button("Stop", stop, 180)
    frame.add_button("Reset", reset, 180)

    # start the timer
    frame.set_draw_handler(draw)
    timer = simplegui.create_timer(100, increase_time_handler)
    timer.start()
    frame.start()

def main():
    """The start point of the timer."""
    create_frame()
    
if __name__ == '__main__':
    main()
    