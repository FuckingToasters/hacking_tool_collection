try:
  import os as inject_malware
  import pyfade
  import requests as hackerman
  import time as crime
  import base64 as unhash_colums
  if inject_malware.name == "nt": inject_malware.system("cls") 
  else: inject_malware.system("clear")
except ImportError:
    inject_malware.system("pip install os")
    inject_malware.system("pip install pyfade")
    inject_malware.system("pip install requests")
    inject_malware.system("pip install base64")

def main():
  print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_cyan, '''
  ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗       ██║   ██║   ██║██║   ██║██║     
  ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
  ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
      
  [1] Goverment Website Hacking
  [2] Soon
  [3] Soon'''))
  option_input = input(pyfade.Fade.Horizontal(pyfade.Colors.green_to_cyan, "Please select a option from above: "))
  if option_input == "1": 
    exploit = unhash_colums.b64decode("aHR0cHM6Ly91c2EuZ292")
    resp = hackerman.get(exploit)
    if resp.status_code == 200:
      print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, f"Connected to internal Server | Code: {resp.status_code}"))
      crime.sleep(.5)
      print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, f"Connected to MySQL Database | Code: {resp.status_code}"))
      crime.sleep(.5)
      print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, f"Found 300 Colums with 8569 items in each (Total: {8569 * 300} | Code: {resp.status_code}"))
      crime.sleep(.5)
      print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, f"Found a zero day exploit & bypassed their detection system | Code: {resp.status_code}"))
      crime.sleep(.5)
      with open("result.txt", "a+") as result_file:
        for _ in range(1000 * 3): 
          print(pyfade.Fade.Horizontal(pyfade.Colors.red_to_yellow, f"Starting Workers... | Code: {resp.status_code}"))
          string_q = "SW1hZ2luZSB0cnlpbmcgdG8gSGFjayB0aGUgR292ZXJtZW50IGxtYW8="
          string_x = str(unhash_colums.b64decode(string_q))
          result_file.write(string_x)

      print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, f"Completed the Hack. Result is stored within result.txt! | Code: {resp.status_code}"))

  else: print("invalid option selected!")

main()
