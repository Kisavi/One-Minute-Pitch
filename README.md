# One-Minute-Pitch
## Author
#### Denis Kisavi
## Description
#### A flask application that requires users to create an account and login before submiting a pitch or viewing other pitches posted by other users and also leave comments and vote on them.
#### A user can perform the following functions
* Create an account by signing up
* Login into there created accounts
* View pitches posted by others in the pitches section.
* Upvote or Downvote the pitches and also leave comments
* Post their own pitches
* Log out from their accounts
## Installation / Setup instruction
## Cloning
* On your terminal, run the following commands:
* $ git clone https://github.com/Kisavi/One-Minute-Pitch.git
* $ cd One-Minute-Pitch
* Create a virtual environment $ pv -m venv --without-pip virtual
* Activate the virtual environment $ source virtual/bin/activate
* Install Dependancies $ pip install -r requirements.txt
* Inside your root directory create a new file ```start.sh``` and add the following:
* ```python(version) manage.py server```
* Run chmod a+x start.sh  
* Run the application $ ./start.sh
## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request
## Technology Used
* python3.8
* flask
* Sqlite
## Known Bugs
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me deniskisavi@gmail.com
## Licence
* MIT License
* Copyright (c) 2022 Denis Kisavi
