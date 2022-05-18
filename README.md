# YunoRIP.py - Download wakarimasen archive .webm
Download webm files from https://archive.wakarimasen.moe/ threads with Python (Windows)

Step 0: Install the required libraries:
```
pip install requests
pip install tqdm
pip install bs4
```
Step 1: `python YunoRIP.py [thread_link] [full_folder_path]` (`[full_folder_path]` is optional)
```
python YunoRIP.py https://archive.wakarimasen.moe/wsg/thread/4192349/ "C:\Program Files"
```
Or \
Run `WideRIP.py` and enter the thread link in the prompt. Eg:
```
Enter thread link: https://archive.wakarimasen.moe/wsg/thread/4192349/
```

Step 2: Wait. Files are saved inside `[full_folder_path]\[Thread_num]` (`YunoRIP`) or `[current]\[Thread_num]` by default/`WideRIP.py`.

Step 3: Enjoy your cum. `[Thread_num].csv` is created inside aformentioned folder.


~~Current bug: Can't download the OP post.~~

![](https://github.com/FuouM/wakarimasen-webm-download/blob/main/running.gif)
