import ctypes
 
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
className = ctypes.create_string_buffer(256)
GetClassNameA = ctypes.windll.user32.GetClassNameA

class windowHwnd:
    def __init__(self, hwnd, name):
        self.hwnd = hwnd
        self.name = name

    def __str__(self):
        return f"window(hwnd={self.hwnd}, name={self.name})"

titles = []
chrome_hwnds = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append(windowHwnd(hwnd, buff.value))
    return True

def getWindowIds():
    titles.clear()
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return titles

