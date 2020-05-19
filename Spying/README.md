# Spying functions

``` python
import Spying.ActiveWindow
import Spying.Clipboard
import Spying.Desktop
import Spying.Microphone
import Spying.Webcam

# Get active window title
print("Current active window title is : " + Spying.ActiveWindow.Get())
# Get all open window titles
print(Spying.ActiveWindow.GetAll())

# Get text from clipboard
print("Text in clipboard : " + Spying.Clipboard.Get())
# Set text to clipboard
Spying.Clipboard.Set("Hello world")

# Create desktop screenshot
Spying.Desktop.Screenshot(filename="image.jpg")
# Record audio from microphone
Spying.Microphone.Record(filename="recording.wav", time=40)
# Create webcam screenshot
Spying.Webcam.Screenshot(filename="image.jpg", delay=4500, camera=1)
```