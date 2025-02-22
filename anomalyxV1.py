__all__ =[]#line:1
import requests #line:3
import time #line:4
import nmap #line:5
from colorama import Fore ,init #line:6
init (autoreset =True )#line:9
def O0O0OOO0O0OOOOO00 ():#line:12
    try :#line:13
        OOOOOOOO000OO0O00 =requests .get ('https://ipinfo.io/json')#line:15
        O0OO0OO000OOOO0O0 =OOOOOOOO000OO0O00 .json ()#line:16
        O0OO0OO0000OOOO0O =O0OO0OO000OOOO0O0 .get ('ip')#line:18
        O00000OOOOO00OOO0 =O0OO0OO000OOOO0O0 .get ('city')#line:19
        O0O0OOOOOOOOOO000 =O0OO0OO000OOOO0O0 .get ('region')#line:20
        O00000OO0O0O0O000 =O0OO0OO000OOOO0O0 .get ('country')#line:21
        OOO000O0OO0OOOOOO =O0OO0OO000OOOO0O0 .get ('loc')#line:22
        print (f"IP Address: {O0OO0OO0000OOOO0O}")#line:25
        print (f"City: {O00000OOOOO00OOO0}")#line:26
        print (f"Region: {O0O0OOOOOOOOOO000}")#line:27
        print (f"Country: {O00000OO0O0O0O000}")#line:28
        print (f"Location (GPS): {OOO000O0OO0OOOOOO}")#line:29
    except requests .exceptions .RequestException as OOO000000000O0OO0 :#line:31
        print (f"Error: {OOO000000000O0OO0}")#line:32
def OO00O0OOOO00000OO (O00OOOO0O0000OO0O ):#line:36
    O0OOOO0O0OO0OO00O =nmap .PortScanner ()#line:38
    O0OOOO0O0OO0OO00O .scan (hosts =O00OOOO0O0000OO0O ,arguments ='-sn')#line:41
    O0OO0OO0OO0000OOO =[]#line:44
    for OOO0000OOO0O00000 in O0OOOO0O0OO0OO00O .all_hosts ():#line:45
        O000OOO0O00OO0O0O =O0OOOO0O0OO0OO00O [OOO0000OOO0O00000 ].hostname ()if O0OOOO0O0OO0OO00O [OOO0000OOO0O00000 ].hostname ()else "Unknown"#line:47
        OO00OOOO0OO000OOO ={"ip":OOO0000OOO0O00000 ,"hostname":O000OOO0O00OO0O0O ,"status":O0OOOO0O0OO0OO00O [OOO0000OOO0O00000 ].state ()}#line:53
        O0OO0OO0OO0000OOO .append (OO00OOOO0OO000OOO )#line:54
    return O0OO0OO0OO0000OOO #line:56
def OOO00OOO0O000O0OO (O00OO000OO0O0OOOO ):#line:59
    print ("Perangkat yang terhubung ke jaringan Wi-Fi:")#line:60
    print ("IP Address\t\tHostname\t\tStatus")#line:61
    print ("--------------------------------------------")#line:62
    for OO00OOO0O0OO00OO0 in O00OO000OO0O0OOOO :#line:63
        print (f"{OO00OOO0O0OO00OO0['ip']}\t\t{OO00OOO0O0OO00OO0['hostname']}\t\t{OO00OOO0O0OO00OO0['status']}")#line:64
def O00O000OOOO0O0O00 (OOO0OO0000OO00000 ):#line:71
    OO0000O0OO00OO000 =f"http://ipinfo.io/{OOO0OO0000OO00000}/json"#line:73
    try :#line:75
        OOO0OOO0000OOOOOO =requests .get (OO0000O0OO00OO000 )#line:76
        O0OOO0O0000OOOO00 =OOO0OOO0000OOOOOO .json ()#line:77
        if OOO0OOO0000OOOOOO .status_code ==200 :#line:80
            print (f"Informasi IP Address {OOO0OO0000OO00000}:")#line:81
            print (f"IP: {O0OOO0O0000OOOO00.get('ip')}")#line:82
            print (f"Hostname: {O0OOO0O0000OOOO00.get('hostname')}")#line:83
            print (f"Location: {O0OOO0O0000OOOO00.get('city')}, {O0OOO0O0000OOOO00.get('region')}, {O0OOO0O0000OOOO00.get('country')}")#line:84
            print (f"Org: {O0OOO0O0000OOOO00.get('org')}")#line:85
        else :#line:86
            print (f"Gagal mendapatkan data untuk IP {OOO0OO0000OO00000}")#line:87
    except requests .exceptions .RequestException as O0O000O000O0000OO :#line:88
        print (f"Terjadi kesalahan: {O0O000O000O0000OO}")#line:89
while True :#line:95
    time .sleep (3 )#line:96
    print ("\n")#line:97
    print (Fore .YELLOW +" + Anomalyx Tools v1 by Danvastra + ")#line:98
    print ("\n")#line:99
    print ("This Tools :")#line:100
    print ("[1] Auto Check My IP Address")#line:101
    print ("[2] Scanning IP Address")#line:102
    print ("[3] Track IP Address")#line:103
    print ("[4] Exit the Tools")#line:104
    print ("\n")#line:105
    O00O0OO00O0OO0OO0 =(input ("Please Select the Tools(Ex. 1/2) : "))#line:107
    time .sleep (3 )#line:108
    print ("\n")#line:109
    if O00O0OO00O0OO0OO0 =="1":#line:110
        O0O0OOO0O0OOOOO00 ()#line:111
    elif O00O0OO00O0OO0OO0 =="2":#line:112
        OO00O00OO00OOOO0O ="180.244.62.0/24"#line:114
        O00OO000OOO0000OO =OO00O0OOOO00000OO (OO00O00OO00OOOO0O )#line:116
        OOO00OOO0O000O0OO (O00OO000OOO0000OO )#line:118
    elif O00O0OO00O0OO0OO0 =="3":#line:120
        if __name__ =="__main__":#line:122
            O00O00O0OOO0O00O0 =input ("Masukkan IP address: ")#line:123
            O00O000OOOO0O0O00 (O00O00O0OOO0O00O0 )#line:124
    elif O00O0OO00O0OO0OO0 =="4":#line:125
        print ("Thanks For the Using This Program Tools!")#line:126
        break #line:127
    else :#line:128
        print ("Error this Program, Please Try Again!")#line:129
        print ("\n")#line:130
