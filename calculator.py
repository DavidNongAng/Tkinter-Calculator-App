from settings import *
import customtkinter as ctk
import darkdetect
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class Calculator(ctk.CTk):
    # Constructor
    def __init__(self, is_dark):
        
        # Window Setup
        super().__init__(fg_color = (WHITE, BLACK))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False,False)
        self.title('')
        self.iconbitmap('hidden.ico')
        self.title_bar_color(is_dark)
        
        # Grid Layout
        self.rowconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')
        
        
        
        # Run
        self.mainloop()
        
    def title_bar_color(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass


if __name__ == '__main__':
    Calculator(darkdetect.isDark())  
