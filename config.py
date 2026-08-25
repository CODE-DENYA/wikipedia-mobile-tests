import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
APP_PATH = os.path.join(BASE_DIR, "app", "wikipedia.apk")
APP_PACKAGE = "org.wikipedia.alpha"
APP_ACTIVITY = "org.wikipedia.main.MainActivity"