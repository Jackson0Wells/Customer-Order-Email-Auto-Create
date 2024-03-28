## Email Template Generator

This Python script creates a graphical user interface (GUI) using Tkinter to generate email templates quickly and easily.


![Email1](https://github.com/Jackson0Wells/Customer-Order-Email-Auto-Create/assets/165251968/7cc27836-5ffb-4f4e-a560-55624814f5cf)
![Email2](https://github.com/Jackson0Wells/Customer-Order-Email-Auto-Create/assets/165251968/87742ace-f8a8-486c-b785-7fd611d49bcf)

### Features


- Fill in customer information, order details, and item lists to generate email templates.
- Generate subject lines dynamically based on order numbers.
- Copy generated email subject and body to the clipboard for easy sharing or pasting.

### Installation

1. **Clone the Repository:**
   Clone or download the repository containing the `emailautocreate.py` script.

2. **Install Python:**
   Ensure Python is installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

3. **Install Dependencies:**
   Open a terminal or command prompt, then run the following command to install the required dependencies:
   ```sh
   pip install tk
   ```

### Usage

1. **Run the Script:**
   After installing dependencies, execute the script in a terminal or command prompt:
   ```sh
   python emailautocreate.py
   ```

2. **Fill in Information:**
   Enter relevant details such as customer name, order number, address, etc., in the provided fields.

3. **Generate Email:**
   Click the "Generate Email" button to create the email template with the provided information.

4. **Copy Email:**
   Use the "Copy Email" button to copy the generated email to the clipboard for easy sharing or pasting.

### Building the App without Terminal

If you prefer not to use the terminal to build the app, you can build it using PyInstaller directly.

1. **Install PyInstaller (if not already installed):**
   PyInstaller is a tool used to convert Python scripts into standalone executables. If you haven't installed PyInstaller yet, you can do so using pip:
   ```sh
   pip install pyinstaller
   ```

2. **Run PyInstaller to Build the App:**
   Once PyInstaller is installed, navigate to the directory containing the `emailautocreate.py` script using your file explorer. Then, follow these steps:

   - **Step 1:** Hold down the `Shift` key on your keyboard and right-click in the folder containing the script.
   - **Step 2:** From the context menu that appears, select "Open PowerShell window here" or "Open command window here," depending on your system.
   - **Step 3:** In the PowerShell or command window, run the following command to build the Email Template Generator without opening a terminal/console window:
     ```sh
     pyinstaller --onefile --noconsole emailautocreate.py
     ```

     - **--onefile:** This flag tells PyInstaller to bundle the Python script and its dependencies into a single executable file.
     - **--noconsole:** This flag ensures that the built executable does not open a terminal/console window when launched.

   This command will bundle the Python script and its dependencies into a standalone executable file without opening a terminal window when the app is launched.

3. **Find the Executable:**
   After PyInstaller has finished building the app, you can find the executable file in the `dist` directory within the project directory. The executable file will have the same name as your Python script with an added extension (e.g., `emailautocreate.exe` on Windows).

4. **Run the Executable:**
   You can run the executable file directly from your file explorer by double-clicking on it. This will launch the Email Template Generator without the need for Python or any additional dependencies.

## Support Development

If you find this project useful and would like to support further development, you can donate Bitcoin to the following address:

Bitcoin Address: `17Uv9ZgoKFXdi18PNf5UighASk53KMjzxp`

Your contributions will be greatly appreciated and will help in maintaining and improving this project. Thank you for your support!

### Note

Remember to replace the placeholder email `support@placeholder.co.za` in the code with your actual support email address.
