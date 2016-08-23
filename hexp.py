from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
base_link = "https://legacy.hackerexperience.com/"

def loadlogin():
    driver.get(base_link)
def goindex():
    print "[CONSOLE]: Went to Index Page."
    driver.get(base_link+"index")
    
def gosoftware():
    print "[SOFTWARE]: Going to the softwares page."
    driver.get(base_link+"software")
    if driver.current_url == base_link+"index":
        print "[SOFTWARE]: I think that you are logged out."
        
def internet(ip = "None"):
    if ip == "None":
        driver.get(base_link+"internet")
    elif ip.count(".") != 3:
        print "[INTERNET]: Failed 3P checksum"
        return None
    else:
        driver.get(base_link+"internet?ip="+ip)

        #  driver.find_element(By.id("someid")).getAttribute("value")
def softwareid(pid):
    try:
        int(pid)
        return len(str(pid)) ==7
    except:
        return False
def getTask1time():
    return driver.find_element_by_xpath("//*[@id='process0']/div[3]")
def getSoftwares():
    #Note this is for the current Page.
    #Our scheme requires a seven digit software code which is directly linked to the software at hand.
    p = []
    c = driver.find_elements_by_css_selector("*")
    for i in c:
        id = i.get_attribute("id")
        try:
            if len(id) == 7 and softwareid(id):
                p.append([i.text,id])
        except:
            print "[GSOFT]faulty element, %s"%(id)
    return p
def discover_ip(ip):
    logout()
    try:
        hackip(ip = ip)
        login(ip = ip)
    except:
        print "[DISCOVERIP]: Does this IP EXIST?"
        
def readlog():
    
    driver.get(base_link+"log")
    text = driver.find_element(by= "name",value = "log").text
    return text

def clearlog():
    print "[CLEARLOG]: Log was cleared."
    driver.get(base_link+"log")
    driver.find_element(by= "name",value = "log").clear()
    #Use this.
    driver.find_element_by_xpath("//form[input/@type='submit']").submit()
    while not "log" in driver.current_url:
        print "[LOGEDIT]: In Progress"
        time.sleep(2)

def viewbankaccount():
    try:
        c  = driver.find_element_by_class_name("right")
        money = int(c.text[1:])
        return money
    except:
        print "[VIEWBACC]: You aren't on the transfer-money-page yet."
        return None

def hackip(ip = "None"):
    if ip == "None":
        print "[HACKIP]: no ip was provided."
    else:
        print "[HACKIP]: Step1"
        internet(ip)
        print "[HACKIP]: Running bf param"
        driver.get(base_link+"internet?action=hack&method=bf")
        
        while not "login" in driver.current_url:
            print "[HACKIP]: bf hack on %s in progress.."%(ip)
            time.sleep(4)
def hexp_login(usr = "<enter here>",pwd = "pwd here"):
    if usr == "<enter here>":
        print "[HEX LOGIN]: Please enter username upon capatcha."
    if pwd == "pwd here":
        print "[HEX LOGIN]: Please enter password upon capatcha."
    goindex()
    try:
        driver.find_element_by_id("login-username").send_keys(usr)
        driver.find_element_by_id("password").send_keys(pwd)
    except:
        print "[HEX LOGIN]: You arent on the login page. Are you already logged in?"




def downloadviaID(ID,ip = "None",bf = True,loginip = True,clearlogs = True):
    # Based on https://legacy.hackerexperience.com/internet?view=software&cmd=dl&id=8723282 version
    if loginip:
        print "[DOWNLOAD]: Logging out of internet"
        logout()
    if bf:
        print "[DOWNLOAD]: Running bf @ %s"%(ip)
        hackip(ip = ip)
    print "[DOWNLOAD]: Attempting login @ %s"%(ip)
    login(ip,clearlogs = True)
    print "[DOWNLOAD]: Searching for object ID %s on server..."%(ID)
    try:
        c = driver.find_element_by_id(ID).text
        print "[DOWNLOAD]: Starting download on %s"%(c)
        driver.get(base_link+"internet?view=software&cmd=dl&id=%s"%(ID))
        print "[DOWNLOAD]: Switching to passive monitoring"
        while base_link+"software" != driver.current_url:
            c1 = driver.find_element_by_class_name("elapsed").text.split(":")
            pcent = driver.find_element_by_class_name("percent").text
            if c1 == "Finished":
                c1 = ["0h","0m","0s"]
            c = ':'.join(c1)
            c1[0] = int(c1[0][:-1])
            c1[1] = int(c1[1][:-1])
            c1[2] = int(c1[2][:-1])
            timeleft = (3600 * c1[0] )+( 60 * c1[1] )+ c1[2]
            print "[DOWNLOAD]:%s  @ %s(%s sec left)"%(c,pcent,timeleft)
            time.sleep(max(0.5,int(timeleft/2)))
    except:
        print "[DOWNLOAD]: Failed Download."
def clearinternetlogs():
    try:
        print "[CIL]: Cleaning internet logs..."
        driver.get(base_link+"internet?view=logs")
        c = driver.find_element_by_class_name("logarea")
        data = c.text
        c.clear()
        driver.find_element_by_xpath("//form[input/@type='submit']").submit()
        xm = open("ScrappedLoggs.txt","a")
        xm.write("\n"+data)
        xm.close()
        while "id" in driver.current_url:
            print "[CIL]: WAITING"
            time.sleep(2)
        
    except:
        print "[CIL]: Couldnt find the logs."
def getbtcrate():
    return int(driver.find_element_by_xpath(".//*[@id='btc-total']").text)
def convertMoneytoBTC():
    try:
        print "[CMTB]: Opening Market ..."
        logout()
        driver.get(base_link+ "internet?ip=214.87.50.225")
        driver.find_element_by_id("btc-login").click()
        clearlog()
    except:
        print "[CMTB]: Already logged in."
    driver.get(base_link+ "internet?ip=214.87.50.225")
    mymoney = getDollarsBalance()
    driver.find_element_by_class_name("quick-actions").find_element_by_id("btc-buy").click()
    print "[CMTB]: Opened Buy Box."
    c = getbtcrate()
    bitcoins = int(10 * (mymoney / float(c)))
    bitcoins /= 10.0
    driver.find_element_by_id("btc-amount").clear()
    print "[CMTB]: Buying %s BTC -> %s Dollars"%(bitcoins,bitcoins * c)
    driver.find_element_by_id("btc-amount").send_keys(str(bitcoins))
    driver.find_element_by_id("btc-submit").click()
    clearlog()
def getDollarsBalance():
    try:
        c = driver.find_element_by_class_name("finance-info").text[1:]
        c = c.replace(",","")
        return int(c)
    except:
        print "[MONEYIND]: Unable to read your balance."
def login(ip = "None",clearlogs = True):
    if ip == "None":
        print "[LOGINIP]: no ip was provided."
    elif ip.count(".") != 3:
        print "[LOGINIP]: 3P checksum not met."
        return None
    else:
        internet(ip)

        driver.get(base_link+"internet?action=login")
        #[OLD LOGIN VERSION]driver.find_element(by="value",value="Login").submit()
        #[NEW VIA FIREPATH]: .//*[@id='loginform']/div[3]/span[3]/input
        driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/span[3]/input").submit()
        print "[LOGINIP]: LOGIN ATTEMPTED."
        if clearlogs:
            try:
                # Pack function for other purposes.
                clearinternetlogs()
                '''
                driver.get(base_link+"internet?view=logs")
                c = driver.find_element_by_class_name("logarea")
                data = c.text
                c.clear()
                driver.find_element_by_xpath("//form[input/@type='submit']").submit()
                xm = open("ScrappedLoggs.txt","a")
                xm.write("\n"+data)
                xm.close()
                while "id" in driver.current_url:
                    print "[LOGINIP]: WAITING"
                    time.sleep(2)
                '''
            except:
                print "Error, this ip clearly doesnt have logs."
        driver.get(base_link + "internet?view=software")

def logout():
    print "[INETLOGOUT]: Succesffuly logged out of the internet."
    driver.get(base_link+"internet?view=logout")
def validIP(ip):
    c = ip.split(".")
    for i in c:
        try:
            int(i)
            if 0 < int(i) and int(i) < 256:
                pass
            else:
                
                return False
        except:
            return False
    if len(c) != 4:
        return False
    return True

def deletelocalSoftware(ID,clearlogs = True):
    print "[DELETESOFTWARE]: Running local version."
    print "[DELETESOFTWARE]Searching for object %s"%(ID)
    try:
        c = driver.find_element_by_id(ID).text
    except:
        print "[DELTETSOFTWARE]: not found"
        return None
    # l-format https://legacy.hackerexperience.com/software?action=del&id=8732666
    print "[DELETESOFTWARE]: Starting download on %s"%(c)
    driver.get(base_link+"software?action=del&id=%s"%(ID))
    print "[DELETESOFTWARE]: Switching to passive monitoring"
    while "del" in driver.current_url:
        c1 = driver.find_element_by_class_name("elapsed").text.split(":")
        pcent = driver.find_element_by_class_name("percent").text
        if c1 == "Finished":
            c1 = ["0h","0m","0s"]
        c = ':'.join(c1)
        c1[0] = int(c1[0][:-1])
        c1[1] = int(c1[1][:-1])
        c1[2] = int(c1[2][:-1])
        timeleft = (3600 * c1[0] )+( 60 * c1[1] )+ c1[2]
        print "[DELETESOFTWARE]:%s  @ %s(%s sec left)"%(c,pcent,timeleft)
        time.sleep(max(0.5,int(timeleft/2)))
    print "[DELETESOFTWARE]: Testing deletion of software."
    try:
        c = driver.find_element_by_id(ID).text
        print "new_software: ",c
        print "[DELETESOFTWARE]: We are still picking up scent of the software, running delete method again."
        deletelocalSoftware(ID,clearlogs = True)
    except:
        print "[DELETESOFTWARE]: Software not found on server anymore."
        if clearlogs:
            clearlog()
def serverStats():
    # Runs server-stats on current-ip
    c = getSoftwares()
    data = {}
    for  i in c:
        if driver.find_element_by_id(i[1]).get_attribute("class") == u"installed":
            #print "[SSTAT]: found %s"%(i[0])
            if ".hash" in i[0]:
                data["hasher"] = i
            elif ".crc" in i[0]:
                data["cracker"] = i
            elif ".hdr" in i[0]:
                data["hider"] = i
            elif ".skr" in i[0]:
                data["seeker"] = i
        else:
            pass
            #print "[SSTAT]: %s prog with class of [%s]"%(i[0],driver.find_element_by_id(i[1]).get_attribute("class"))
    return data

def deleteobject(obj,local = False,log_in = True,ip = "None"):
    if not local:
        print "[DOBJ]: Deleting object of type %s"%(obj)
        if not validIP(ip):
            return "error not a valid ip"
        if log_in:
            login(ip = ip)
        print "[DOBJ]: Extracting programs ... "
        activeprograms = serverStats()
        try:
            p_stat = activeprograms[obj]
        except:
            print "[DOBJ]: Didnt find object of type \"%s\""%(obj)
            return None
        print "[DOBJ]: Deleting %s with id %s"%(p_stat[0],p_stat[1])
        deleteSoftwareviaID(p_stat[1],ip = ip,logged_in = True,bf = False,clearlogs = True)
    else:
        print "[DOBJ]: Deleting object of type %s"%(obj)
        activeprograms = serverStats()
        try:
            p_stat = activeprograms[obj]
        except:
            print "[DOBJ]: Didnt find object of type \"%s\""%(obj)
            return None
        print "[DOBJ]: Deleting %s with id %s"%(p_stat[0],p_stat[1])
        deletelocalSoftware(p_stat[1])
    
def deleteSoftwareviaID(ID,ip = "None",logged_in = False,bf = True,clearlogs = True):
    if not validIP(ip):
        print "[DELETESOFTWARE]: This isnt a valid ip."
        return None
    
    if bf and not logged_in:
        print "[DELETESOFTWARE]: Clearly you have not been to this ip before."
        discover_ip(ip)
        deleteSoftwareviaID(ip,logged_in = True,bf = False,clearlogs = False)

    else:
        if not logged_in:
            login(ip = ip)
        print "[DELETESOFTWARE]Searching for object %s"%(ID)
        try:
            c = driver.find_element_by_id(ID).text
        except:
            print "[DELTETSOFTWARE]: not found"
            return None
        
        print "[DELETESOFTWARE]: Starting download on %s"%(c)
        driver.get(base_link+"internet?view=software&cmd=del&id=%s"%(ID))
        print "[DELETESOFTWARE]: Switching to passive monitoring"
        while "del" in driver.current_url:
            c1 = driver.find_element_by_class_name("elapsed").text.split(":")
            pcent = driver.find_element_by_class_name("percent").text
            if c1 == "Finished":
                c1 = ["0h","0m","0s"]
            c = ':'.join(c1)
            c1[0] = int(c1[0][:-1])
            c1[1] = int(c1[1][:-1])
            c1[2] = int(c1[2][:-1])
            timeleft = (3600 * c1[0] )+( 60 * c1[1] )+ c1[2]
            print "[DELETESOFTWARE]:%s  @ %s(%s sec left)"%(c,pcent,timeleft)
            # New implementation max(0.5,int(timeleft/2)) to prevent asymptotic printing where timeleft = 0.5 and sleep < 0.5 sec
            time.sleep(max(0.5,int(timeleft/2)))
        print "[DELETESOFTWARE]: Testing deletion of software."
        try:
            c = driver.find_element_by_id(ID).text
            print "new_software: ",c
            print "[DELETESOFTWARE]: We are still picking up scent of the software, running delete method again."
            deleteSoftwareviaID(ID,ip = ip,logged_in = True,bf = False,clearlogs = True)
        except:
            print "[DELETESOFTWARE]: Software not found on server anymore."
            if clearlogs:
                clearinternetlogs()

def downloadobject(obj,log_in = True,ip = "None"):
    print "[DOBJ]: Downloading object of type %s"%(obj)
    if not validIP(ip):
        return "error not a valid ip"
    if log_in:
        login(ip = ip)
    print "[DOBJ]: Extracting programs ... "
    activeprograms = serverStats()
    try:
        p_stat = activeprograms[obj]
    except:
        print "[DOBJ]: Didnt find object of type \"%s\""%(obj)
        return None
    print "[DOBJ]: Downloading %s with id %s"%(p_stat[0],p_stat[1])
    downloadviaID(p_stat[1],ip = ip,loginip = True,bf = False,clearlogs = True)
def extractBankcheckData():
    import string

    c = driver.find_element_by_class_name("article-post").text
    banknum = c[c.index("#")+1:c.index("#")+10]
    sidx = c.index("#") + 11
    eidx = c.index("#") + 10
    pcount = 0
    numbers = False
    lmoney = False
    cidx = sidx
    while pcount != 4:
        if not numbers and c[cidx] in string.digits and not lmoney:
            numbers = True
            sidx = cidx
        elif not numbers and c[cidx] in string.digits and  lmoney:
            pass
        elif numbers and c[cidx] == "." and not lmoney:
            pcount += 1
        elif not numbers and c[cidx] == "$":
            lmoney  = True
        elif c[cidx] == ",":
            pass
        else:
            lmoney  = False


        cidx += 1
    eidx = cidx
    rest = c[sidx:eidx].split(".")
    constr = ""
    rest = rest[:-1] 
    for i in rest:
        constr+= str(int(i))+"."
    constr = constr[:-1]
    return banknum,constr

def checkbankaccstatusmission():
    banknum,bankip = extractBankcheckData()
    
    print "[MILVL2]: Mission Data"
    print "[MILVL2]: b-number: %s"%(banknum)
    print "[MILVL2]: bank-ipa: %s"%(bankip)
    mynum,myip = getbankaccount()
    print "[MILVL2]: m-number: %s"%(mynum)
    print "[MILVL2]: mbank-ip: %s"%(myip)
    dinacc = tfmoney(banknum,bankip,mynum,myip)

    driver.find_element_by_xpath(".//*[@id='amount-input']").send_keys(str(dinacc))
    cm = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div/div/div[2]/div/div[1]/span[1]").click()
    buy = driver.find_element_by_xpath(".//*[@id='modal-submit']")
    try:
        buy.submit()
    except:
        buy.click()
    print "[MILVL2]: Complete! Running converter now."
    convertMoneytoBTC()
def tfmoney(a1,ip1,a2,ip2,reload = True,returnquantity = True):
    if reload:
        logout()
        internet(ip = ip1)
        # l-method https://legacy.hackerexperience.com/internet?action=hack&type=bank
        driver.get(base_link+"internet?action=hack&type=bank")
        bnumbox = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/form/div[1]/div/input")
        bnumbox.clear()
        bnumbox.send_keys(a1)
        hackbutton = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/form/div[2]/button")
        hackbutton.submit()
        while not "login" in driver.current_url:
            #Account number .//*[@id='content']/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/form/div[1]/div/input
            c1 = driver.find_element_by_class_name("elapsed").text.split(":")
            pcent = driver.find_element_by_class_name("percent").text
            if c1 == "Finished":
                c1 = ["0h","0m","0s"]
            try:
                c = ':'.join(c1)
                c1[0] = int(c1[0][:-1])
                c1[1] = int(c1[1][:-1])
                c1[2] = int(c1[2][:-1])
                timeleft = (3600 * c1[0] )+( 60 * c1[1] )+ c1[2]
            except:
                c = "unable to load"
            
            print "[TRANSFERMONEY]:%s  @ %s(%s sec left)"%(c,pcent,timeleft)
            # New implementation max(0.5,int(timeleft/2)) to prevent asymptotic printing where timeleft = 0.5 and sleep < 0.5 sec
            time.sleep(max(0.5,int(timeleft/2)))

            
        del hackbutton, bnumbox
        print "[TRANSFERMONEY]: Going to Account login button."
        accloginbutton = driver.find_element_by_xpath(".//*[@id='loginform']/div[3]/span[3]/input")

        accloginbutton.submit()
    if returnquantity:
        tr =  viewbankaccount()
    else:
        tr = -1
    print "[TFM]: At login state."
    try:
        driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[2]/input").send_keys(a2) # fill in acc #
        driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div[4]/input").send_keys(ip2)# fill in bip #
        driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/button").submit()            # submit the form
    except:
        print "[TFM]: error this account was already hacked please transfer it manually if required."
        return a1,ip1,a2,ip2
    return tr
    
    
def deleteSoftwareMission():
    article_data =driver.find_element_by_class_name("article-post").text
    article_data = article_data.split("file")[1]
    program = article_data.split("recieve")[0]
    program = program.split(".")
    program = "."+program[1]
    
    program.strip(" ")
    program.strip(".")
    # New update to prevent whitespace corruption
    print "[DELETEMISSION]: Program detection method: %s"%(program)
    try:
        ip = article_data.split("at")[2]
    except:
        ip = article_data.split("at")[1]
    ip = ip.split("We")[0]
    ip = ip.strip(" ")
    ip = ip.strip(".")
    print "[DELETEMISSION]: IP to delete from: %s"%(ip)
    if not validIP(ip):
        print "We couldnt find the IP Please enter it now"
        ip = raw_input("IP: ")
    ## Data parsing Done.
    
    discover_ip(ip)
    t = getSoftwares()
    p_id = "Undefined"
    for i in t:
        if program in i[0]:
            p_id = i[1]
    if p_id == "Undefined":
        return "Unable to find program on server."
    print "[DELETEMISSION]: Found ID: %s"%(p_id)

    deleteSoftwareviaID(p_id,ip = ip,logged_in = True,bf = False,clearlogs = True)
    print "[DELETEMISSION]: Claiming Prize"
    driver.get(base_link+"missions")
    cmb = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div/div/div[2]/div/div[1]/span[1]")
    cmb.click()
    try:
        finish = driver.find_element_by_id("modal-submit").submit()
    except:
        time.sleep(0.5)
        driver.find_element_by_id("modal-submit").click()
    # use l-format like https://legacy.hackerexperience.com/internet?view=software&cmd=del&id=8726969
def getbankaccount():
    print "[GBA]: saving current url..."
    last_spot = driver.current_url
    driver.get(base_link + "finances")
    myacc = driver.find_element_by_xpath(".//*[@id='acc1']/div").text
    myacc = myacc[myacc.index("#")+1:myacc.index("#") + 10]
    iphoster = driver.find_element_by_xpath(".//*[@id='content']/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/a[2]/span").click()
    iphoster = driver.find_element_by_class_name("browser-bar").get_attribute("value")
    print "[GBA]: restoring url..."
    driver.get(last_spot)
    return myacc,iphoster


    

