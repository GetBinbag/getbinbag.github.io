# Binbag  
  
This is the official documentation of the MVP of wastecircles.com.  
Code written to support Binbag, the waste management facility aggregator of India: [binbag.in](https://www.binbag.in/)  
  
**ToC:**  
  
1. Structure  
 - browsing  
2. [Requirements](#requirements) 
 - installation  
 - other  
3. [Updating the database](#database)  
 - structuring the csv file  
 - getting the locations of each facility  
 - pushing new files to Github  
5. [IMPORTANT](#important)  

--- 
  
<a name="requirements"></a>
## Requirements  

### Installations  
  
Before you start, install these *python libraries* on your computer (one time installation):  
Python is a programming language and we will use it in order to get coordinates for each facility.

1. pip, requests, csv, os and geopy  
 - open terminal. It is located in folder *Applications/Utilities*. Click on the *Terminal* application.  
 [![Terminal on Mac](http://blog.teamtreehouse.com/wp-content/uploads/2012/09/Screen-Shot-2012-09-25-at-12.57.00-PM.png)](http://blog.teamtreehouse.com/wp-content/uploads/2012/09/Screen-Shot-2012-09-25-at-12.57.00-PM.png)  
 - install pip  
  - use *easy_install* for the installation. Type in these command in terminal, line by line, while waiting for each of them to finish before you proceed. You will know when the command has finished when you are back to line of the Terminal screen that looks like that:  
  ```bash
  your-user-name: $ 
  ```  

  The commands in order of execution are:    
  ```bash
  curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
  sudo easy_install pip
  pip --version
  ```  

### Other  
  
1. Mapbox Access Token:  
  - can be obtained by registering on Mapbox's web page (you have already been registered - same as GitHub registration)    
  - is located here: [https://www.mapbox.com/studio/account/tokens/](https://www.mapbox.com/studio/account/tokens/)  
  - to know how many hits your maps have, go to [https://www.mapbox.com/studio/account/billing/](https://www.mapbox.com/studio/account/billing/)  
 
<a name="database"></a> 
## Updating the database   
  
## Pushing New Files to Github  
  

<a name="important"></a> 
## IMPORTANT:  
  
1. We use a map from Mapbox, which has 50,000 free hits per year and then becomes paid.    
  - ping me when you notice something strange, maybe you have reached the 50,000 hits    
  