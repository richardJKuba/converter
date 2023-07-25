from time import sleep

def converter_process(update_callback):
    for act in range(10):
        update_callback(act)
        sleep(0.5)