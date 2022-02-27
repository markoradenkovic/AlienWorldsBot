
## STEP 1
Make sure pyinstaller module is installed on system

## STEP 2
Run following command in terminal from inside \alienworldsbot\version_2.0>
* pyinstaller --hidden-import='cv2' cli.py

## STEP 3
This will have created following items:
* /build
* /dist
* cli.spec

## STEP 4
* Copy the /build and /dist folder elsewhere on the system in a folder
* Open the /dist folder and paste all the content from 'version_2.0\dist_modules' into \dist\cli folder

## STEP 5 - BOT ACCOUNTS CONFIGURATION
* The bot acounts can be found under \dist\cli\alienworlds_program_data\configs\accounts.json
* Open the accounts.json file in an optional text editing program.

## STEP 6 - CONFIGURE ACCOUNTS FOR 1 ACCOUNT
Follow the following format:
```json
[
  {
    "username": "youremail@gmail.com",
    "password": "yourwaxpassword"
  }
]
```
## STEP 7 - CONFIGURE ACCOUNTS FOR MULTIPLE ACCOUNTS
Follow the following format:
```json
[
  {
    "username": "youremail1@gmail.com",
    "password": "yourwaxpassword"
  },
  {
    "username": "youremail2@gmail.com",
    "password": "yourwaxpassword"
  },
  {
    "username": "youremail3@gmail.com",
    "password": "yourwaxpassword"
  }
]
```

### STEP 8
You might need to test the bot first. If the bot cant recognize the "Mine" & "Claim-Mine" Buttons -->
1. You will have to take similar screenshots from your own pc.
2. Then paste them and replace the old images inside "\dist\cli\alienworlds_program_data\images\"

### STEP 9
RUN THE PROGRAM
* Find the cli.exe file inside the following path: "\dist\cli\cli.exe"
* Run the application
* Enjoy