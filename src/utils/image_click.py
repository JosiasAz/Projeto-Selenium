import time
from typing import Optional, Tuple
import cv2
import pyautogui
import numpy as np

def click_image(template_path: str, confidence: float = 0.8, timeout: float = 5.0) -> Optional[Tuple[int, int]]:
    """Localiza uma imagem na tela e clica no centro (requer tela visível; não funciona em headless).
    Retorna (x, y) do clique ou None se não encontrar.
    """
    end = time.time() + timeout
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise FileNotFoundError(f"Template não encontrado: {template_path}")
    th, tw = template.shape[:2]

    while time.time() < end:
        screenshot = pyautogui.screenshot()
        screen_bgr = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screen_gray = cv2.cvtColor(screen_bgr, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= confidence:
            x, y = max_loc[0] + tw // 2, max_loc[1] + th // 2
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.click()
            return (x, y)
        time.sleep(0.2)
    return None
