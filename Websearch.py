import pyautogui
import random
import time
import keyboard

file_path = 'search_terms.txt'

def read_search_terms(file_path):
    with open(file_path, 'r') as file:
        search_terms = file.readlines()
    search_terms = [term.strip() for term in search_terms]
    return search_terms

search_terms = read_search_terms(file_path)

print("Please focus the search bar of Microsoft Edge. Press 'q' to quit the script.")

running = True

def paste_random_search():
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete') 

    random_search = random.choice(search_terms)
    pyautogui.write(random_search)  
    pyautogui.press('enter')
    print(f"Pasted and searched: {random_search}")

def stop_script(event):
    global running
    print("Script stopped by user.")
    running = False

keyboard.on_press_key('q', stop_script)

while running:
    paste_random_search()

    wait_time = random.uniform(6.50, 8.00)
    time.sleep(wait_time)

keyboard.unhook_all()
