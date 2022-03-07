#iim-microservice


Dependencies
1. Dependencies for the project are listed in requirements.txt
2. Python 3.10.2 was also installed when this project was created

How to run
1. pull the project and navigate to the project folder
2. install dependencies
3. run the following command in terminal: python manage.py runserver
4. navigate to http://<server_ip>:<server_port>/api/vocab/ to access vocab endpoints
5. navigate to http://<server_ip>:<server_port>/api/prediction/ to access prediction endpoint

Assumptions
1. Made simple assumption that all puncuation except # should be ignored. 
   This made it easier to validate things like "#word,", "#word.", etc. but
   also has issues with potentially invalid vocab being validated. (e.g. "#w,or,d" would be considered valid).
2. Made assumption that vocab words cannot be string.empty or "\s\n\t"
