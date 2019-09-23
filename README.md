# log-parser
Access log parser. v1.0 Python version.

**Author:** Sergei Safarov <inbox@sergeysafarov.com>
 
 
## To get started

### Prerequisites
You'll need to have Python 3 installed with the following modules:
* sys: ```pip install sys```
* re: ```pip install re```
* csv: ```pip install csv```
* geoip2: ```pip install geoip2```
* parse: ```pip install sys```

### Files and folders in the project directory


    .\
    \log  #folder for inbound log file
    \tests  #folder with test files
    \.gitignore  #Ignore rules for git
    \GeoLite2-Country.mmdb  #Ip2Country database
    \LICENSE  #License file
    \parser.py #parser script
    \README.MD  #Thi file 

### How to run
1. Place **access.log** file to log folder.
    `Please note: script in this version works only with file named **access.log**`
2. Open the console and run following command: ```python -m unittest tests\test_parser.py```
3. Run following command: ```python parser.py```
4. CSV file with the name **access.csv** will be created in the same folder where is **parser.py** script located.   
