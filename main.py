from pynput import keyboard
from firebase import firebase
IDGRUPO = "-N6VHCoYZwjgMKmS7Ap8"
base = firebase.FirebaseApplication("https://tally-fa988-default-rtdb.firebaseio.com/", None)


def on_press(tecla):
    try:
        key = int(tecla.char)
        cam = "cam{}pgr".format(key)
        datos = {}
        for i in range(1, 5):
            if i != key:
                camara = "cam{}pgr".format(i)
                base.put("camaras/"+IDGRUPO, camara, 0)
        #print(base.post("camaras/", datos))  
        base.put("camaras/"+IDGRUPO, cam, 1) 
    except:
        return

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()