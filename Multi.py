import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from oldnew import main
    main()
elif bit == '32bit':
    from oldnew import main
    main()
