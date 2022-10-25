import os
import subprocess
import ctypes, sys

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

if is_admin():
	drive = input("Enter drive Letter: ").upper()
	code = drive+":\\"
	cwd = os.getcwd()

	os.chdir(code)

	print("New directory is: {0}".format(os.getcwd()))
	del_link = os.system("del *.lnk")
	rem_perm = os.system("attrib -s -r -h *.* /s /d /l")

	if del_link == 0 and rem_perm == 0:
		print("Success...")
	else:
		print("Failed...")
else:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "  ".join(sys.argv), None,1) 

