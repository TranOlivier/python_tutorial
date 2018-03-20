#faire un import de sys
#mettre sys.version_info dans une variable
#afficher dans une chaîne de caractère

import sys
version = sys.version_info

for x in version:
    print(x)
vt = ".".join(str(x) for x in version)


print('Version '+vt)