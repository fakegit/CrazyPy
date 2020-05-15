
# Import modules
import ctypes

__strcpy = ctypes.cdll.msvcrt.strcpy
__ocb = ctypes.windll.user32.OpenClipboard
__ecb = ctypes.windll.user32.EmptyClipboard
__gcd = ctypes.windll.user32.GetClipboardData
__scd = ctypes.windll.user32.SetClipboardData
__ccb = ctypes.windll.user32.CloseClipboard
__ga = ctypes.windll.kernel32.GlobalAlloc
__gl = ctypes.windll.kernel32.GlobalLock
__gul = ctypes.windll.kernel32.GlobalUnlock
__GMEM_DDESHARE = 0x2000

""" Get text from clipboard """
def Get():
  __ocb(None)
  pcontents = __gcd(1)
  data = ctypes.c_char_p(pcontents).value
  __ccb()
  return data.decode()

""" Set text to clipboard """
def Set(text):
  __ocb(None)
  __ecb()
  hCd = __ga(__GMEM_DDESHARE, len(bytes(text, "ascii")) + 1)
  pchData = __gl(hCd)
  __strcpy(ctypes.c_char_p(pchData), bytes(text, "ascii"))
  __gul(hCd)
  __scd(1, hCd)
  __ccb()