# hexp-bot by Neel Bhalla (c) 2016
## This is a selenium webdriver version of hexpbot using 46.0 firefox
## Installation (I use Python 2.7.12) which can be downloaded of python.org
## DO NOT USE 3.X as it is different syntax.
## Libraries
## Selenium -> Pip install selenium (use pip 8.1.x)
---------------------------------------------------------------------
## NOTE: This can be used as a python API or a general-purpose-bot.

### List of functions and applications:

### hexp_login(usr = "username",pwd = "pass")
This function is used to log in. re-captcha must be done by user :).

### loadlogin()
This takes the user to the login page if they arent logged in
otherwise it takes you to the control panel.

### goindex()
Pretty similar to loadlogin() it takes you to the index.

### gosoftware()
This takes you to YOUR software(not the internet-software tab).

### internet(ip = "None")
This is the internet function it will take you to the internet tab under the ip that you specify.

### softwareid(pid) returns boolean
This is an internal function.  It runs check-cases to validate whether an HTML element is a piece of software or just a web-element

### getTask1time() returns int
IF you are on the tasks page, then it SHOULD give you the time till completion of the FIRST task.
note: This may crash, i dont recommend using it.

### getSoftwares() returns list in the form of [program Name, program ID]
If you are on the site that displays the softwares(softwares tab), the it will scan for the softwares(viruses that are installed also found).  Anything that is hidden from the user can't be found as it wasnt rendered as an HTML object in the first place.
note: This function takes a considerable amount of time to run as it grabbs ALL The css elements from the site.

### discover_ip(ip)
This function (very useful) does a bruteforce hack on the ip(via the cracker) and logs in.  It takes care of the logs while also giving you a sense of what is in the log with the ScrappedLoggs.txt function.
CRASHES: If this function crashes, try logging out and then run it.
CRASHES 2: Create the file ScrappedLoggs.txt and set it to be empty.  Then try to run it.

### readlog() returns string[unicode] of the stuff in your log
This function returns the stuff in your log use print readlog() to format the items in the IDLE Shell

### clearlog()
This function clears YOUR log

### viewbankaccount() reutrns int
Once you are on the "account page" in the bank, it scrapps the money value
note: do not try to do this on your account, it will just get it hacked as once you log in, your # will be on the the bank ip logs.

### hackip(ip = "None")
This function runs the cracker on an ip. It will wait until you reach the login page.
If you cracker is incompetent with the other's hasher, it will still run, but the login will fail.
It takes on average 30sec(No more that 30s), but the printout doesnt give the time atm so just be patient with it.

### downloadviaID(ID,ip = "None",bf = True,loginip = True,clearlogs = True)
This function takes the program ID(found using inspect element or getSoftwares() function) and the ip.  bf means whether or not the password is in the hacked database. loginip is if you need to logout of another ip, clearlogs is for if you want to clear the logs upon arrival to the site.  If you encounter a server such as download center which doesnt have logs, the program will not crash and will notify you that it failed to find the location of the logs.

### getDollarsBalance()
This is the safe way to get YOUR money value off of hexp. It uses the finances object in the website in order to do this rather than the bank ip - login method.

### login(ip = "None",clearlogs = True)
This is the login method for logging into an ip.  It is used by many of the functions such as discover_ip. Clearlogs toggles wether or not you want the logs to be cleared upon arrival.

### logout()
To prevent errors while "surfing" the web, use the logout function to safely transition from one ip to the other.

### deleteSoftwareviaID(ID,ip = "None",logged_in = False,bf = True,clearlogs = True)
This function allows you to delte a software on an ip rather than download. The parameters are the same as downloadviaID(read the meaning of the parameters there).

### deleteSoftwareMission() 
This function can execute a mission based on the mission-page.  Run it on the mission page, it will extract all the data it needs from the garbage text they give you. Not polished yet, but you shouldnt expect any crashing from it.  You may need to feed it the ip since the data parsing part is quite rusty.

### getbankaccount() returns (acc#,ip)(int,int)
This is used for extracting your own details in a way that will not interput the system but is still dynamic.

### tfmoney(acc1,ip1,acc2,ip2)
This transferrs money.  There are two toggles -> reload and returnquantity.  Returnquantity is for printing amount transferred, reload is for choosing between logging into acc1 via ip1 or disabliing it if it had already happened.
