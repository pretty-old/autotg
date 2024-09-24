import os
import subprocess
import signal
import time
import psutil

os.environ['TELEGRAM_CACHE_LIMIT'] = '100MB'

def open_telegram_accounts():
    base_path = input("Введите путь к папке с аккаунтами: ")

    if not os.path.exists(base_path):
        print("Указанный путь не существует.")
        return

    try:
        count = int(input("Сколько аккаунтов открыть? "))
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        return

    account_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

    for i in range(min(count, len(account_folders))):
        telegram_path = os.path.join(base_path, account_folders[i], "telegram.exe")
        if os.path.exists(telegram_path):
            subprocess.Popen(telegram_path)
        else:
            print(f"telegram.exe не найден в {account_folders[i]}")

        time.sleep(2)

def close_telegram_accounts():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'Telegram.exe':
            proc.send_signal(signal.SIGTERM)


def open_from(start, end):
    base_path = input("Введите путь к папке с аккаунтами: ")

    if not os.path.exists(base_path):
        print("Указанный путь не существует.")
        return

    account_folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

    for i in range(start, min(end, len(account_folders))):
        telegram_path = os.path.join(base_path, account_folders[i], "telegram.exe")
        if os.path.exists(telegram_path):
            subprocess.Popen(telegram_path)
        else:
            print(f"telegram.exe не найден в {account_folders[i]}")

        time.sleep(2)

if __name__ == "__main__":
    while True:
        action = input("Введите 'open' для открытия аккаунтов, 'open from' для открытия из диапазона или 'close' для закрытия: ").strip().lower()
        if action == 'open':
            open_telegram_accounts()
        elif action == 'open from':
            try:
                start = int(input("Введите номер первой папки: "))
                end = int(input("Введите номер последней папки: "))
                open_from(start, end)
            except ValueError:
                print("Пожалуйста, введите корректные числа.")
        elif action == 'close':
            close_telegram_accounts()
        else:
            print("Неверная команда.")

