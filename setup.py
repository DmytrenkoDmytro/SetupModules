#---------------Setup modules----------
import sys
import subprocess
import pkg_resources

required = {'numpy','pandas','progress','openpyxl'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed


if missing:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',*missing])
#-------------------  End setup modules -------------