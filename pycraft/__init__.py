import sys
import os
import platform
# caution: path[0] is reserved for script path (or '' in REPL)
directory = os.path.dirname(__file__)

base_folder = directory

if platform.system() == "Linux":
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs//installer"))
    
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs//utility"))
    
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs"))

else:
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs\\installer"))
    
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs\\utility"))
    
    sys.path.insert(1,
        os.path.join(base_folder,
        "programs"))

del sys
del os
del platform
del base_folder
del directory

if (__name__ == "pycraft" or
        __name__ == "__main__"):
    
    print("Thank you for using Pycraft, we are getting it ready for you now!")

from pycraft_main import QueryVersion
from pycraft_main import start