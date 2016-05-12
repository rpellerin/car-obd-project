[Documentation for Python-OBD library.](http://python-obd.readthedocs.io/en/latest/Commands/#obd-ii-adapter-elm327-commands)

Requires Python 3.5+ and the following packages:

- obd
- websockets

They can be installed using `pip`.

# TODO

- Add the path to the device as a mandatory argument ("/dev/ttyUSB0")

# Other ideas

- [How to build a dashcam](http://pidashcam.blogspot.fr/)
- Add TTS (for example when going above the speed limit, and when shifting gears too late/too early):
    - [Android](https://github.com/nolanlawson/SimpleTalker)
    - [Ubuntu](http://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line)
- Full dashboard with tabs and checkboxes to show/hide different parts like:
    - Speed
    - Speed of the engine
    - Temperature(s)
    - Trottle pedal position
    - etc.
    All the parts must fit in the window, there should be no need to scroll in any direction
