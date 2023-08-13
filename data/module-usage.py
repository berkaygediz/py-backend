import importlib as imp
from modules import bgmodule as modul

modul.print_username("Berkay Gediz")
modul.display_age(25)

module_dir = dir(modul)
print("Module properties:", module_dir)

imp.reload(modul)
