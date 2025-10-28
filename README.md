# Source Weather

![Cloudy Icon](https://github.com/okjazim/Source-Weather/assets/79494525/757f98b4-f0d5-4dcc-8bc3-f8075c02c23d)

A typical Windows weather application that provides weather information for user-searched cities. This program is completely written in Python and uses Tkinter along with the Tkbootstrap library to provide the GUI and functionality. Compiled using [Pyinstaller](https://github.com/pyinstaller/pyinstaller).

## Features

- **Search Bar**: Enter city names to get weather information.
- **Keyboard Shortcut**: Use the Enter/Return key to search.
- **Full Screen Toggle**: You can toggle the application to Full Screen.
- **New Themes**:You can toggle between themes.
- And many more to be added...

## Screenshots

<img width="809" height="637" alt="Screenshot (89)" src="https://github.com/user-attachments/assets/4e1ec9f5-c687-4714-b849-44843d869412" />

<img width="799" height="639" alt="Screenshot (90)" src="https://github.com/user-attachments/assets/4a4a79b2-5bfe-4407-a0b2-5b76c1a9f14a" />

## Setup

1. **Download and Extract**:
  - Download the latest ZIP file from the [releases tab](https://github.com/okjazim/Source-Weather/releases).
  - Extract the contents to your desired directory. The extracted files should include:
    - `main.exe`
    - `cloudy_DIU_icon.ico`
    - `envsample`

2. **Obtain API Key**:
  - [Click here to get your API key](https://openweathermap.org/appid).

3. **Configure Environment File**:
  - Open the `envsample` file and paste your API key into it.
  - Rename the file to `.env`.

6. **Run the Application**:
  - Click on the `.exe` file to finally run the application.
  - The program will only run correctly when the `.env` file is present there!

## References

- [OpenWeatherMap One Call API](https://openweathermap.org/api/one-call-api)
- [PyInstaller Documentation](https://www.pyinstaller.org/en/stable/usage.html)
