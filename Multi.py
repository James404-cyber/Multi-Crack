import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	import Rank
	Rank.ninex()
elif 'aarch' in arc:
	import Rank
	Fip64.ninex()
else:
	exit(f' Unknow device machine {arc}')
