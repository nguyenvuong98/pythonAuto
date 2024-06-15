import win32api, win32gui, win32con
import pyautogui

namePg = 'Ngọc Rồng Huyền Thoại - Profile 1 - Microsoft​ Edge'


def getHwndFromName(name):
    hWnd = win32gui.FindWindow(None, name)
    return hWnd

def makelong(low, high):
    return (high << 16) | (low & 0xFFFF)

def draw_marker(x, y):
    # Draw a small circle marker at the specified coordinates
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
def get_window_position(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x, y, width, height = rect
    return (x, y)

def click_pg(name, x, y):
    hWnd = getHwndFromName(name)
    windowPosition = get_window_position(hWnd)
    posX = x - windowPosition[0]
    posY = y - windowPosition[1]
    click = win32api.MAKELONG(posX, posY)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
    win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, None, click)
    win32api.PostMessage(hWnd, win32con.BM_CLICK, posX, posY)

def resizeWindow(name, width, height):
    hWnd = getHwndFromName(name)
    windowPosition = get_window_position(hWnd)
    win32gui.ShowWindow(hWnd, win32con.SW_RESTORE)
    win32gui.MoveWindow(hWnd, windowPosition[0], windowPosition[1], width, height, True)
 
