# log-parser
Access log parser. v1.1 Python version.

This log parser can:
* Read an access log file
* Resolve Country and State from IP address (GeoLite2 Country database used)
* Translate user agent to device type (Mobile, Desktop, Tablet) and Browser(Safari, Chrome, etc)
* Combine new Geo & Device fields with existing fields on access log file and output result to CSV

**Author:** Sergei Safarov <inbox@sergeysafarov.com>
 
 
## To get started

### Files and folders in the project directory

    .\
    \log  #folder for inbound access.log file
    \tests  #folder with test files
    \.gitignore  #Ignore rules for git
    \Dockerfile  #Docker configuration file  
    \LICENSE  #License file
    \parser.py #parser script
    \README.MD  #This file 

### How to run
Since the script was contenirized we have two options for run:

##### 1. As a local application 
##### Prerequisites
You'll need to have Python 3 installed with the following modules:
* csv: ```pip install python-csv```
* geoip2: ```pip install geoip2```
* user-agents: ```pip install user_agents```
* wget: ```pip install wget```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these modules.



##### Build and run flow
1. **(optional since 1.1)** Place **access.log** file to log folder.
    >Please note: script in this version works only with file named **access.log** if you copy file into log folder manually. In other case it will try download it from default remote location
2. Open the console goto project folder and run following command: ```python -m unittest tests\test_parser.py```
3. Run following command: ```python parser.py```
4. CSV file with the name either **access.csv** or **downloaded_file.csv** will be created in the same folder where is **parser.py** script located.   

##### 1. Application in docker container
##### Prerequisites
You'll need to have docker installed on your system

##### Build and run flow
1. Open the console and goto project folder 
2. Run following command to build container: ```docker build -t <container-name>```
3. Next run created container by the command: ```docker run -it -rm <container-name>```
    > `<container-name>` - user defined container name 
4. CSV file with the name either **access.csv** or **downloaded_file.csv** will be created in the same folder where is **parser.py** script located **inside container**.   

## License
[MIT](http://opensource.org/licenses/MIT)
 
### Changelog

* 1.1 Changes:
    * Added geo ip database handling: System will try download geo ip database if not find it locally
    * Added access file handling: System will try download access.log from from default remote location if it not find local file.

* 1.0 Initial basic version. Need to have geo ip database locally and access.log file downloaded and copied into log folder