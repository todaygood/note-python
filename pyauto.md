

python pyautoit 窗口导入_pyautoit 模拟操作windows软件

PyAutoGUI gives you the option to send keyboard and mouse clicks and do screenshots, not much more.

Pywinauto tries to let you interact with the element of a windows application, so also works, if the program is not in the foreground.

I've played with Pywinauto and am not entirely happy. If you want to automate a complicated GUI program, one that contantly opens and closes windows and message boxes, their approach of locating the part of the program that you want to react to can drive you mad. I had to write a lot of try/catch code to get it to work at all.

PyWinGUI alas isn't better for this usecase, but at least very easy to use.

On windows 10 you also have the option of getting autohotkey (not python, but its own language) which does a much better job at automating, but has horrible syntax and no data structures...


https://www.reddit.com/r/Python/comments/8bymeo/pyautogui_vs_pywinauto/

