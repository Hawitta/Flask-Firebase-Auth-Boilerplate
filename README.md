# Flask-Firebase-Auth-Boilerplate

## Setup Instructions

### 1. Create a new project on the Firebase Console.
Firebase Console ->  Web -> Add application details

### 2. Copy the Firebase config dictionary.

- Go to **Project settings** -> **General** -> Scroll to **Web Apps** -> **SDK Setup and Configuration** -> Select **Config** -> Copy **firebaseConfig** dictionary 


### 3. Configure Firebase Authentication
- Go to **Authentication** → **Sign-in method** -> **Add new provider** -> **Email/Password** 
- This enables **Email/Password** sign-in method.

### 3. Get Repository and Pull it Locally
- Clone the repository to your local machine using the following command:
  
  ```bash
    git clone https://github.com/Hawitta/Flask-Firebase-Auth-Boilerplate.git

### 4. Navigate to project

```bash
  cd Flask-Firebase-Auth-Boilerplate 
```

### 5. Paste config dictionary to config.py
Change the code from Javascript object notation to Python dictionary notation as shown

```bash

config = {
  'apiKey': " ",
  'authDomain': " ",
  'projectId': " ",
  'storageBucket': " ",
  'messagingSenderId': " ",
  'appId': " ",
  'databaseURL': ''
}

```

### 6. Install dependencies
Install flask firebase library by running the following command

```bash
  pip install pyrebase4
```

### 7. Add secret key to main.py
A dummy secret key has been provided under the flask app initialization, change this accordingly


### 8. Run the project
Right click on the main.py code and select Run Code


### 9. Display on browser
A link will be provided under the text, WARNING: This is a development server.

The project is currently being run on a localhost, hence the format will be http://127.0.0.1:<port>

Press the link and CTRL and it will redirect you to open the link on default browser.
