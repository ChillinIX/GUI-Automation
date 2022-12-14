import pyautogui

pyautogui.click(100, 200); pyautogui.write("Sending a String from the Keyboard The pyautogui.write() function sends virtual keypresses to the computer. What these keypresses do depends on what window is active and what text field has focus. You may want to first send a mouse click to the text field you want in order to ensure that it has focus. As a simple example, let’s use Python to automatically type the words Hello, world! into a file editor window. First, open a new file editor window and position it in the upper-left corner of your screen so that PyAutoGUI will click in the right place to bring it into focus. Next, enter the following into the interactive shell: >>> Notice how placing two commands on the same line, separated by a semicolon, keeps the interactive shell from prompting you for input between running the two instructions. This prevents you from accidentally bringing a new window into focus between the click() and write() calls, which would mess up the example. Python will first send a virtual mouse click to the coordinates (100, 200), which should click the file editor window and put it in focus. The write() call will send the text Hello, world! to the window, making it look like Figure 20-6. You now have code that can type for you!")

fw = pyautogui.getActiveWindow()

print ()

print (fw)