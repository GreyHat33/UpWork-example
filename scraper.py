from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import base64
from solver import PuzleSolver


def solve_captcha_slider(driver):
    background_image_data = driver.execute_script(
        "return arguments[0].toDataURL('image/png').substring(21);",
        driver.find_element(By.CSS_SELECTOR, ".geetest_canvas_bg.geetest_absolute")
    )
    slice_image_data = driver.execute_script(
        "return arguments[0].toDataURL('image/png').substring(21);",
        driver.find_element(By.CSS_SELECTOR, ".geetest_canvas_slice.geetest_absolute")
    )

    # Decode the Base64-encoded image data into bytes
    background_image_bytes = base64.b64decode(background_image_data)
    slice_image_bytes = base64.b64decode(slice_image_data)

    # Save the images to files
    with open('background.png', 'wb') as background_file:
        background_file.write(background_image_bytes)

    with open('piece.png', 'wb') as piece_file:
        piece_file.write(slice_image_bytes)

    solver = PuzleSolver("piece.png", "background.png")
    solution = solver.get_position()
    print(solution)


URL = 'https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-kaufen?enteredFrom=one_step_search'

options = Options()
ua = UserAgent()
user_agent = ua.random

options.add_argument(f'--user-agent={user_agent}')
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.get(URL)

# Click captcha
captcha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
captcha.click()

time.sleep(4)

# Solve captcha slider
solve_captcha_slider(driver)

time.sleep(4)

driver.quit()
