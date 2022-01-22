import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mk2022 import main
    main()
elif bit == '32bit':
    from mk2022 import main
    main()
