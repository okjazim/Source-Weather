# Source Weather

![Cloudy Icon](https://github.com/okjazim/Source-Weather/assets/79494525/757f98b4-f0d5-4dcc-8bc3-f8075c02c23d)

A typical Windows weather application that provides weather information for user-searched cities. This program is completely written in Python and uses Tkinter along with the Tkbootstrap library to provide the GUI and functionality.

## Features

- **Search Bar**: Enter city names to get weather information.
- **Keyboard Shortcut**: Use the Enter/Return key to search.

## Screenshots

![Screenshot 1](https://github.com/okjazim/Source-Weather/assets/79494525/d51c6607-9ad0-496f-b067-b90802f740b6)

![Screenshot 2](https://github.com/okjazim/Source-Weather/assets/79494525/27308b10-cd34-4277-b6a1-67ac7018f7b4)

## Setup

1. **Download and Extract**:
   - Download the latest ZIP file from the [releases tab](https://github.com/okjazim/Source-Weather/releases).
   - Extract the contents to your desired directory. The extracted files should include:
     - `main.py`
     - `cloudy_DIU_icon.ico`
     - `envsample`

2. **Obtain API Key**:
   - [Click here to get your API key](https://openweathermap.org/appid).

3. **Configure Environment File**:
   - Open the `envsample` file and paste your API key into it.
   - Rename the file to `.env`.

4. **Install PyInstaller**:
   - Open a terminal as administrator and install PyInstaller (skip if already installed):
     ```bash
     pip install pyinstaller
     ```

5. **Build the Application**:
   - Navigate to the Source Weather folder in your terminal:
     ```bash
     cd path\to\SourceWeatherFolder
     ```
   - Run the following command to build the application into a single executable file:
     ```bash
     pyinstaller --onefile --noconsole --icon=cloudy_DIU_icon.ico main.py
     ```

6. **Run the Application**:
   - The generated `.exe` file will be located in the `dist` folder within the Source Weather Folder.
   - The program will only run correctly in this folder because the `.env` file is located here.

## References

- [OpenWeatherMap One Call API](https://openweathermap.org/api/one-call-api)
- [PyInstaller Documentation](https://www.pyinstaller.org/en/stable/usage.html)
