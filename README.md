# hexp-bot
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

###
