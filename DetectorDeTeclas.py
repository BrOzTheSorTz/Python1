from pynput.keyboard import Key, Listener

def show(key):
    print('Pulsaste {0}'.format(key))
    if key == Key.delete:
        return False


with Listener(on_press = show) as listener:
    listener.join()
