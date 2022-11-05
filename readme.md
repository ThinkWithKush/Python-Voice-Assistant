# **Welcome to Friday**
Welcome to my Voice Assistant Project developed using Python and **Speech Recognition** and **pyttsx3** designed specifically for a **Windows OS system**

This Voice Assistant Works as:
* Text messages are converted to speech using a Voice Engine
* Voice Input is taken and converted to Speech Recognition module in python which uses Google to convert speech to text
* Multiple checks are run on the text to check for what task is to be done, and as soon as some condition is passed, the task binded to the condition is executed
* Extra data that might be needed to print is converted to Speech from text
* Friday repeats and waits for next command

# **Dependencies**
Since Friday is made using several modules of python for different tasks like conversion of text-to-speech and speech-to-text
>Below is the Information of the dependencies and Installation process

**pyttsx3** : This is the tool used for conversion of text-to-speech
``` $ pip install pyttsx3 ```

**speech_recognition** : This is the tool used for conversion of speech-to-text
``` $ pip install speechrecognition ```

**wikipedia** : For fetching data from wikipedia 
``` $ pip install wikipedia ```

>Other pre-installed python modules in use

**datetime :** For accessing Date and Time
**subprocess** : Module for calling subprocesses
**os** : OS commands module

# **Installation**
To convert this Voice Assistant Application to an Executable (.exe) File, we will use a python tool called **pyinstaller**

**pyinstaller Installation**
1. Open the scripts folder in the python subdirectories installed in your system.
2. Open powershell or terminal window in the folder.
3. Install pyinstaller using the command ``` $ pip install pyinstaller ```

**Installation of bot as an executable file**
1. Open the folder where your python script of the project (Voice Assistant in this case) is stored and open PowerShell or Terminal Window.
2. Run the command ``` $ pyinstaller friday.py ```

>After the Tool successfully converts python (.py) file to an executable (.exe) file, 2 folders will be created in the same directory named `build` and `dist` respectively.
>The executable file can be found in the `dist` folder.

# **ThankYou Note**
Thanks for checking out this project and finding it worthy enough to be read.

Going forward, it would be great if you try to customize this bot to your own needs.
* I use this in my daily usage for the simple reason that i can bind all my essential quick access tasks to a voice command.
* It is simple for modifications, as all to be done is running processes based on commands, wherein command-queries are available in form of text where we can search for phrases or clauses and run specific processes based on them like opening websites etc. 

For further contacts, connect to me on [LinkedIn](https://www.linkedin.com/in/kushagra2709)