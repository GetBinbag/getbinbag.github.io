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
  
3. Install git - this is the program, which allows for database updates (in our current scenario)  
 - download from [here](https://git-scm.com/download/mac)  
 -  follow the installation instructions  
 [![Git on Mac](https://git-scm.com/book/en/v2/images/git-osx-installer.png)](https://git-scm.com/book/en/v2/images/git-osx-installer.png)  
 - that should be it  

### Other  
  
1. Mapbox Access Token:  
  - can be obtained by registering on Mapbox's web page (you have already been registered - same as GitHub registration)    
  - is located here: [https://www.mapbox.com/studio/account/tokens/](https://www.mapbox.com/studio/account/tokens/)  
  - to know how many hits your maps have, go to [https://www.mapbox.com/studio/account/billing/](https://www.mapbox.com/studio/account/billing/)  
  
---  

<a name="database"></a> 
## Updating the database   
  
### Structuring the csv file  

### Getting the coordinates for each facility  

### Pushing New Files to Github  

*THE FOLLOWING INSTRUCTIONS ARE RAN EVERY TIME A DATABSE UPDATE IS NEEDED:*  
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
  - ping me when you notice something strange, maybe you have reached the 50,000 hits    
  