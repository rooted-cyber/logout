# Thanks to rootedcyber. 
# logout idea by chrome app...
# Kang with credits
from random import choice as c
from sys import exit as ep
from os import system as s,listdir as ls, chdir as cd
try:
  from colorama import Fore as f
except:
  s("pip3 install colorama")
  from colorama import Fore as f 

p = print
col = f.LIGHTRED_EX,f.LIGHTGREEN_EX,f.LIGHTYELLOW_EX,f.LIGHTBLUE_EX,f.LIGHTCYAN_EX,f.LIGHTMAGENTA_EX
rc = f"{c(col)}"
r = f.WHITE
p(f"{rc}\n\n Logout your github account in your browser\n")
ans = input(f"{c(col)} Logout your github ({r}y/n{c(col)}) {r}")
def logout():
  lnk = '<a href="https://github.com/logout"><h1><b>click here to open in browser</b></h1></a>'
  with open("a.html","w") as ll:
    ll.write(lnk)
    s("""xdg-open a.html""")

if ans.lower() == "y":
  p(f"\n\n\033[3;93m logouting your account......\n")
  logout()
else:
  p(f"{rc} Exiting....\n\n")