# Binbag  
  
This is the official documentation of the MVP of wastecircles.com.  
Code written to support Binbag, the waste management facility aggregator of India: [binbag.in](https://www.binbag.in/)  
  
**ToC:**  
  
1. [Structure](#structure)  
 - browsing  
2. [Requirements](#requirements) 
 - installation  
 - other  
3. [Updating the database](#database)  
 - structuring the csv file  
 - getting the coordinates of each facility  
 - pushing new files to Github  
5. [IMPORTANT](#important)  

--- 
  
<a name="structure"></a>
## Structure  
  
The website has two pages:  
  
1. The main page  
 - the main page contains a brief of the project along with contact details and search form  
 - the search form has two fields  
   * city  
   * type  
 - if any of these fields is complete, the map returns results given the specific filtering criteria  
 - if both these fields are left empty, the map shows all waste facilities, which are currently in the database  

2. The map page  
 - it shows a list of name + city for all waste facilities  
 - it shows each waste facility as a pin on the map  
 - both the names in the list to the left, and the pin on the map to the right are clickable  
   * when clicked, they send the viewer to the pin on this particuclar waste facility and show a bubble with its full address  
  
---  

<a name="requirements"></a>
## Requirements  

### Installations  
  
Before you start, install these *python libraries* on your computer (one time installation):  
Python is a programming language and we will use it in order to get coordinates for each facility.
  
1. Make sure Python 3.* is installed:  
 - open terminal. It is located in folder *Applications/Utilities*. Click on the *Terminal* application.  
 [![Terminal on Mac](http://blog.teamtreehouse.com/wp-content/uploads/2012/09/Screen-Shot-2012-09-25-at-12.57.00-PM.png)](http://blog.teamtreehouse.com/wp-content/uploads/2012/09/Screen-Shot-2012-09-25-at-12.57.00-PM.png)  
 - type in the following command:  
 ```bash
 python --version
 ```    
 If the result look like, you are alright:  
 ```bash
 Python 3.5.2
 ```  
 If not, contact me.  
  
2. install pip, requests, csv, os and geopy  
 - install pip  
   * use *easy_install* for the installation. Type in these command in terminal, line by line by pressing *Enter* after each line, while waiting for each of them to finish before you proceed. You will know when the command has finished when you are back to line of the Terminal screen that looks like that:  
  ```bash
  your-user-name: $ 
  ```  

  The commands in order of execution are:    
  ```bash
  curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
  sudo easy_install pip
  pip --version
  ```  
    
  When finished, pip should tell you its version, something like:
  ```bash
  pip 9.0.1 from /home/user/.virtualenvs/securaxis/lib/python3.5/site-packages (python 3.5)
  ```  

  - install requests, oc, csv, geopy. Execute each line separately by typing it in terminal and waiting for its competion:  
  ```bash
  pip install requests
  pip install oc
  pip install csv
  pip install geopy
  ```  

### Other  
  
1. Mapbox Access Token:  
  - can be obtained by registering on Mapbox's web page (you have already been registered - same as GitHub registration)    
  - is located here: [https://www.mapbox.com/studio/account/tokens/](https://www.mapbox.com/studio/account/tokens/)  
  - to know how many hits your maps have, go to [https://www.mapbox.com/studio/account/billing/](https://www.mapbox.com/studio/account/billing/)  
  
---  

<a name="database"></a> 
## Updating the database   
  
### Structuring the csv file  
  
*THIS IS VERY IMPORTANT. IF THESE STEPS ARE NOT FOLLOWED, THE FILTERING AND VISUALIZATION WILL NOT WORK*  

1. Keep the original data in a csv file with this specific format:  
   - for each update of the csv file, have:  
     * the exact same column names, all lowercased  
     * no empty rows and columns - check the screenshot with before and after csv look    

   - for each cell of the csv file, have:  
     * no trailing commas and spaces  
     * remove unnecessary abreviations from addresses such as 'Flat No.', 'Shed' and 'Survey No.'   
     * the type of waste is given with small letters and only the identifying word. For exxample, type in *lead* instead of *Lead waste*  

 [![CSV format](https://github.com/GetBinbag/getbinbag.github.io/blob/master/img/readme/csv_format.png)](https://github.com/GetBinbag/getbinbag.github.io/blob/master/img/readme/csv_format.png)  
 <p align='center'> CSV format. The correct file format is shown above the black line, the original - below.</p>   


### Getting the coordinates for each facility  
  
2. Run the small Python script, which automatically extracts coordinates from addresses. It creates the *output.geojson* file, under data/binbag/, which is loaded during visualization  
 - preparatory step: make sure you have the right directory structure  
   * have a folder in *Documents*, example title *waste_circle*, and create to subfolders in it
     - data  
     - helper  
   * go to *data* and create another subfolder called *binbag*  
   * put the csv file, *recyclers.csv*, in this binbag folder  
   * download the [csv_to_geojson.py](https://raw.githubusercontent.com/GetBinbag/getbinbag.github.io/master/helper/csv_to_geojson.py). Click on the link, right click on the page and click 'Save as'. Save it with the same name in the directory *helper*.  
 - in Terminal, navigate to the helper folder, typing this command in followed by 'Enter':    
 ```bash
 cd Documents/waste_circle/helper
 ```   
 - after that, eecute this one:  
 ```bash
 python csv_to_geojson.py
 ```  
  
  [![Python script output](https://github.com/GetBinbag/getbinbag.github.io/blob/master/img/readme/csv_conversion.png)](https://github.com/GetBinbag/getbinbag.github.io/blob/master/img/readme/csv_conversion.png)  
 <p align='center'> Python script: running and output, which tells which facilities, on line number X, in the csv did not have their cooridinates found. Read the N.B. below.</p>   
    
**N.B:** The way the coordinates are extracted is the following:  
- we construct an address with the values of fields *industrial*, *locality*, *city* and *country*  
- if no coordinates are found with this address, we make it broader by using only *locality*, *city* and *country*  
- if again no address is found, we fall back just to *city* and *country*  
  * every time this happens, the Python program will print a message in the terminal telling you which lines of the csv file have coordinates pointing only to the city + country. We will try to work this out and make the full address be recognized for the sake of accuracy.  


3. Update both the ** and *output.geojson* files in Github. See [Pushing New Files to Github](#push) for detailed how-to.    
  
<a name="push"></a> 
### Pushing New Files to Github  

*FOLLOW THESE INSTRUCTIONS EVERY TIME A DATABSE UPDATE IS NEEDED:*  
  * go to and login to Github at [https://github.com/GetBinbag/getbinbag.github.io](https://github.com/GetBinbag/getbinbag.github.io)  
  * click the *Upload Files* button  
  * select the file, which IS named *recyclers.csv*  
  * write a small comment in the text field under **Commit changes**, which hint is *Add files via upload*.
    - an example of the comment is "Added waste facilities for lead".
  * click the green button **Commit changes**  
  * this is it :)  
  
N.B: The web site will not work if the database is not in a file titled **recyclers.csv**.  

--- 

<a name="important"></a> 
## IMPORTANT:  
  
1. We use a map from Mapbox, which has **50,000 free hits** per year and then becomes paid.  
 - when you notice something strange:
   * check if you have reached the limit - link is given above when we speak about Mapbox  
   * else: ping me  

2. The way the coordinates are extracted is the following:  
- we construct an address with the values of fields *industrial*, *locality*, *city* and *country*  
- if no coordinates are found with this address, we make it broader by using only *locality*, *city* and *country*  
- if again no address is found, we fall back just to *city* and *country*  
  * every time this happens, the Python program will print a message in the terminal telling you which lines of the csv file have coordinates pointing only to the city + country. We will try to work this out and make the full address be recognized for the sake of accuracy.    
  