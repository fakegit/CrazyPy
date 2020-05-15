
# Import modules
import ctypes

""" Detect sanbox """
def Check():
    # List
    sandbox_dll_list = (
        "SbieDll.dll",
        "SxIn.dll",
        "Sf2.dll",
        "snxhk.dll",
        "cmdvrt32.dll"
    )
    # Kernel32
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel32.GetModuleHandleW.restype = ctypes.wintypes.HMODULE
    kernel32.GetModuleHandleW.argtypes = [ctypes.wintypes.LPCWSTR]
    # Check
    for dll in sandbox_dll_list:
        hMod = kernel32.GetModuleHandleW(dll)
        if hMod == None:
            continue
        else:
            del(kernel32)
            return True

    del(kernel32)
    return False