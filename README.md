![cloudy_DIU_icon-5](https://github.com/okjazim/Source-Weather/assets/79494525/82d0ff49-c692-4533-8ce3-ff991c02de4d)
# Source Weather
A typical windows weather application that provides weather information of user searched cities. This program is completely written in Python and Tkinter as well as Tkbootstrap library was used to provide the GUI along with the functionality for this program.

## Usability
The search bar is used as normal.
Enter/Return key can be also used to search.

## Screenshots

![Screenshot 2024-03-15 045209](https://github.com/okjazim/Source-Weather/assets/79494525/d51c6607-9ad0-496f-b067-b90802f740b6)
 
![Screenshot 2024-03-15 045403](https://github.com/okjazim/Source-Weather/assets/79494525/27308b10-cd34-4277-b6a1-67ac7018f7b4)

## Setup
Download the latest zip file from the releases tab. It contains 'main.py', 'cloudy_DIU_icon.ico' and 'envsample'. Extract it to your desired file directory.

[Click for attaining the api key](https://openweathermap.org/appid)

After getting the api key, open 'envsample' and paste it. Also rename the file to '.env'.


Open terminal as administrator and install pyinstaller module (skip this if have this already)

`pip install pyinstaller`


Redirect the file directory to the destination of Source Weather folder.

Now use the following command to build the files in a single .exe file.

`pyinstaller --onefile --noconsole --icon cloudy_DIU_icon.ico main.py`


The .exe file will now be generated in the 'dist' folder which will be in the Source Weather Folder. The program will only run in this folder since '.env' file is there.

## References
[https://openweathermap.org/api/one-call-api](https://openweathermap.org/api/one-call-api)
[https://www.pyinstaller.org/en/stable/usage.html](https://www.pyinstaller.org/en/stable/usage.html)
