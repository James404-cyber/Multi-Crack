import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	import Fip
	Fip._site_view_()
	Fip.folder()
elif 'aarch' in arc:
	import Fip64
	Fip64._site_view_()
	Fip64.folder()
else:
	exit(f' Unknow device machine {arc}')
