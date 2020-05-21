# Harmful functions

``` python
import Harmful.BlockInput
import Harmful.Bsod
import Harmful.Monitor
import Harmful.Power

# Block keyboard & mouse (Admin rights is required)
Harmful.BlockInput.Block(20)
# Create blue screen of death
Harmful.Bsod.bsod()

# Disable monitor
Harmful.Monitor.Off()
# Enable monitor
Harmful.Monitor.On()

# Power control
Harmful.Power.Reboot()
Harmful.Power.Shutdown()
Harmful.Power.Logoff()
Harmful.Power.Hibernate()
```