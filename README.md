# How to protect your passwords
1.  Create a `.env` file and put your passwords in it as a variables
2.  Add `.env` file to your `.gitignore` so that it doesnt get pushed to github
3.  Enable env variables by installing library to env
    -   `pip install python-dotenv`
4.  In files that need private passwords/api keys
    -   `from dotenv import load_env`
    -   `import os`
    -   `load_env()`
    -   `password = os.getenv(password)`