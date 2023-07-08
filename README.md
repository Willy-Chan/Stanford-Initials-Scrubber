# Stanford Initials Scrubber
The Stanford Initials Scrubber is a Python program that allows you to scrub through the Stanford Profiles website and retrieve a list of all names that match a specified set of initials.

## Requirements
To use the Stanford Initials Scrubber, you need to have the Selenium library installed. You can install it using the following command:
```shell
pip install selenium
```
Additionally, you will need to download the chromedriver executable file for your version of Chrome. You can find the appropriate version of chromedriver for your Chrome browser [here](https://chromedriver.chromium.org/downloads).  
Once downloaded, replace the executable_path in the code with the file path of the chromedriver executable on your system.

## Usage
To use the Stanford Initials Scrubber, follow these steps:
1. Open the Python script in your preferred code editor.
2. Modify the initials variable to the desired set of initials you want to search for. The default is set to 'AR'.
3. Run the script. It will launch a Chrome browser window and navigate to the Stanford Profiles website.
4. The program will search for names that match the specified set of initials and retrieve the results.
5. The program will output a list of names that match the specified initials.

Please note that this project was done for fun and was inspired by Stanford's marriage pact, which assigns a set of initials to participants :)

## License
The Stanford Initials Scrubber is released under the MIT License. You are free to use, modify, and distribute the code in accordance with the terms and conditions of the license.
