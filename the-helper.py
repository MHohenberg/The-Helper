#!/usr/bin/python
#the list comes from Kali Linux Officale Website
#the Script is Coded By Hacker-EG (one of the goods)
import os
def intro():
    cmd = os.system("clear")
    print("""
████████╗██╗  ██╗███████╗    ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║█████╗█████╗███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
   ██║   ██╔══██║██╔══╝╚════╝██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████╗    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                         Coded By Hacker-EG    """)
    print("""
--------------------------------------------------------------------|
|Note : These tools and environments are for Debian and Ubuntu      |
|       only. Some tools will be downloaded in the file of script   |
|       the list comes from Kali Linux offical website              |
|-------------------------------------------------------------------|

(0) Add Kali Linux repositories && update            (10) Programming
(1) Information Gathering                            (11) Sniffing & Spoofing
(2) Vulnerability Analysis                           (12) Password Attacks
(3) Wireless Attacks                                 (13) Maintaining Access
(4) Web Applications                                 (14) Reverse Engineering
(5) Exploitation Tools                               (15) Hardware Hacking
(6) Stress Testing                                   (16) Avoid Av
(7) Forensics Tools                                  (17) Hacking Android
(8) Browsers                                         (18) Desktop Enviroments
(9) Media Players                                    (19) Post Exploitation                    
(21) About me                                        (20) Exit Script
""")
    a = int(input("Enter your choice here : >>> "))
    if a == 0 :
        cmd1 = os.system("wget -q -O - https://www.kali.org/archive-key.asc | gpg --import && dpkg --add-architecture i386")
        cmd  = os.system("echo '\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list && apt-get update && apt-get upgrade")
        cmd2 = os.system("gpg -a --export ED444FF07D8D0BF6 | sudo apt-key add -")
        intro()
    if a == 1 :
        cmd = os.system("clear")
        print("""
1) acccheck                           30) lbd
2) ace-voip                           31) Maltego Teeth
3) Amap                               32) masscan
4) Automater                          33) Metagoofil
5) bing-ip2hosts                      34) Miranda
6) braa                               35) Nmap
7) CaseFile                           36) ntop
8) CDPSnarf                           37) p0f
9) cisco-torch                        38) Parsero
10) Cookie Cadger                     39) Recon-ng
11) copy-router-config                40) SET
12) DMitry                            41) smtp-user-enum
13) dnmap                             42) snmpcheck
14) dnsenum                           43) sslcaudit
15) dnsmap                            44) SSLsplit
16) DNSRecon                          45) sslstrip
17) dnstracer                         46) SSLyze
18) dnswalk                           47) THC-IPV6
19) DotDotPwn                         48) theHarvester
20) enum4linux                        49) TLSSLed
21) enumIAX                           50) twofi
22) exploitdb                         51) URLCrazy
23) Fierce                            52) Wireshark
24) Firewalk                          53) WOL-E
25) fragroute                         54) Xplico
26) fragrouter                        55) iSMTP
27) Ghost Phisher                     56) InTrace
28) GoLismero                         57) hping3
29) goofile                           58) Back to main menu

0) install all information gathering tools
""")
        def informa():
         infor = int(input("Enter the number of the tool : >>> "))
         if infor == 1:
            cmd = os.system("sudo apt-get update && sudo apt-get install acccheck")
         elif infor == 2:
            cmd = os.system("sudo apt-get update && sudo apt-get install ace-voip")
         elif infor == 3:
            cmd = os.system("sudo apt-get update && sudo apt-get install amap")
         elif infor == 4:
            cmd = os.system("sudo apt-get update && sudo apt-get install automater")
         elif infor == 5:
            cmd = os.system("sudo apt-get update && sudo apt-get install bing-ip2hosts")
         elif infor == 6:
            cmd = os.system("sudo apt-get update && sudo apt-get install braa")
         elif infor == 7:
            cmd = os.system("sudo apt-get update && sudo apt-get install casefile")
         elif infor == 8:
            cmd = os.system("sudo apt-get update && sudo apt-get install cdpsnarf")
         elif infor == 9:
            cmd = os.system("sudo apt-get update && sudo apt-get install cisco-torch")
         elif infor == 10:
            cmd = os.system("sudo apt-get update && sudo apt-get install cookie-cadger")
         elif infor == 11:
            cmd = os.system("sudo apt-get update && sudo apt-get install copy-router-config")
         elif infor == 12:
            cmd = os.system("sudo apt-get update && sudo apt-get install dmitry")
         elif infor == 13:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnmap")
         elif infor == 14:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnsenum")
         elif infor == 15:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnsmap")
         elif infor == 16:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnsrecon")
         elif infor == 17:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnstracer")
         elif infor == 18:
            cmd = os.system("sudo apt-get update && sudo apt-get install dnswalk")
         elif infor == 19:
            cmd = os.system("sudo apt-get update && sudo apt-get install dotdotpwn")
         elif infor == 20:
            cmd = os.system("sudo apt-get update && sudo apt-get install enum4linux")
         elif infor == 21:
            cmd = os.system("sudo apt-get update && sudo apt-get install enumiax")
         elif infor == 22:
            cmd = os.system("sudo apt-get update && sudo apt-get install exploitdb")
         elif infor == 23:
            cmd = os.system("sudo apt-get update && sudo apt-get install fierce")
         elif infor == 24:
            cmd = os.system("sudo apt-get update && sudo apt-get install firewalk")
         elif infor == 25:
            cmd = os.system("sudo apt-get update && sudo apt-get install fragroute")
         elif infor == 26:
            cmd = os.system("sudo apt-get update && sudo apt-get install fragrouter")
         elif infor == 27:
            cmd = os.system("sudo apt-get update && sudo apt-get install ghost-phisher")
         elif infor == 28:
            cmd = os.system("sudo apt-get update && sudo apt-get install golismero")
         elif infor == 29:
            cmd = os.system("sudo apt-get update && sudo apt-get install goofile")
         elif infor == 30:
            cmd = os.system("sudo apt-get update && sudo apt-get install lbd")
         elif infor == 31:
            cmd = os.system("sudo apt-get update && sudo apt-get install maltego-teeth")
         elif infor == 32:
            cmd = os.system("sudo apt-get update && sudo apt-get install masscan")
         elif infor == 33:
            cmd = os.system("sudo apt-get update && sudo apt-get install metagoofil")
         elif infor == 34:
            cmd = os.system("sudo apt-get update && sudo apt-get install miranda")
         elif infor == 35:
            cmd = os.system("sudo apt-get update && sudo apt-get install nmap")
         elif infor == 36:
            cmd = os.system("sudo apt-get update && sudo apt-get install ntop")
         elif infor == 37:
            cmd = os.system("sudo apt-get update && sudo apt-get install p0f")
         elif infor == 38:
            cmd = os.system("sudo apt-get update && sudo apt-get install parsero")
         elif infor == 39:
            cmd = os.system("sudo apt-get update && sudo apt-get install recon-ng")
         elif infor == 40:
            cmd = os.system("sudo apt-get update && sudo apt-get install set")
         elif infor == 41:
            cmd = os.system("sudo apt-get update && sudo apt-get install smtp-user-enum")
         elif infor == 42:
            cmd = os.system("sudo apt-get update && sudo apt-get install snmpcheck")
         elif infor == 43:
            cmd = os.system("sudo apt-get update && sudo apt-get install sslcaudit")
         elif infor == 44:
            cmd = os.system("sudo apt-get update && sudo apt-get install sslsplit")
         elif infor == 45:
            cmd = os.system("sudo apt-get update && sudo apt-get install sslstrip")
         elif infor == 46:
            cmd = os.system("sudo apt-get update && sudo apt-get install sslyze")
         elif infor == 47:
            cmd = os.system("sudo apt-get update && sudo apt-get install thc-ipv6")
         elif infor == 48:
            cmd = os.system("sudo apt-get update && sudo apt-get install theharvester")
         elif infor == 49:
            cmd = os.system("sudo apt-get update && sudo apt-get install tlssled")
         elif infor == 50:
            cmd = os.system("sudo apt-get update && sudo apt-get install twofi")
         elif infor == 51:
            cmd = os.system("sudo apt-get update && sudo apt-get install urlcrazy")
         elif infor == 52:
            cmd = os.system("sudo apt-get update && sudo apt-get install wireshark")
         elif infor == 53:
            cmd = os.system("sudo apt-get update && sudo apt-get install wol-e")
         elif infor == 54:
            cmd = os.system("sudo apt-get update && sudo apt-get install xplico")
         elif infor == 55:
            cmd = os.system("sudo apt-get update && sudo apt-get install ismtp")
         elif infor == 56:
            cmd = os.system("sudo apt-get update && sudo apt-get install intrace")
         elif infor == 57:
            cmd = os.system("sudo apt-get update && sudo apt-get install hping3")
         elif infor == 58:
             intro()
         elif infor == 0:
            cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
         else:
            print("Not Found")
         informa()
        informa()
    if a == 2:
        cmd = os.system("clear")
        print("""
1) BBQSQL                               18) Nmap
2) BED                                  19)ohrwurm
3) cisco-auditing-tool                  20) openvas-administrator
4) cisco-global-exploiter               21) openvas-cli
5) cisco-ocs                            22) openvas-manager
6) cisco-torch                          23) openvas-scanner
7) copy-router-config                   24) Oscanner
8) commix                               25) Powerfuzzer
9) DBPwAudit                            26) sfuzz
10) DoonaDot                            27) SidGuesser
11) DotPwn                              28) SIPArmyKnife
12) Greenbone Security Assistant        29) sqlmap
13) GSD                                 30) Sqlninja
14) HexorBase                           31) sqlsus
15) Inguma                              32) THC-IPV6
16) jSQL                                33) tnscmd10g
17) Lynis                               34) unix-privesc-check
                                        35) back to main menu
0) Install all Vulnerability tools 
""")
        def vull():
            d = int(input("Enter the number of the tool : >>> "))
            if d == 1 :
                cmd = os.system("apt-get install bbqsql")
            elif d == 2 :
                cmd = os.system("apt-get install bed")
            elif d == 3 :
                cmd = os.system("apt-get install cisco-auditing-tool")
            elif d == 4 :
                cmd = os.system("apt-get install cisco-global-exploiter")
            elif d == 5 :
                cmd = os.system("apt-get install cisco-ocs")
            elif d == 6 :
                cmd = os.system("apt-get install cisco-torch")
            elif d == 7 :
                cmd = os.system("apt-get install copy-router-config")
            elif d == 8 :
                cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
            elif d == 9 :
                cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
            elif d == 10 :
                cmd = os.system("apt-get install doona")
            elif d == 11 :
                cmd = os.system("apt-get install dotdotpwn")
            elif d == 12 :
                cmd = os.system("apt-get install greenbone-security-assistant")
            elif d == 13 :
                cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
            elif d == 14 :
                cmd = os.system("apt-get install hexorbase")
            elif d == 15 :
                cmd = os.system("sudo apt-get install inguma")
            elif d == 16 :
                cmd = os.system("apt-get install jsql")
            elif d == 17 :
                cmd = os.system("apt-get install lynis")
            elif d == 18 :
                cmd = os.system("apt-get install nmap")
            elif d == 19 :
                cmd = os.system("apt-get install ohrwurm")
            elif d == 20 :
                cmd = os.system("apt-get install openvas-administrator")
            elif d == 21 :
                cmd = os.system("apt-get install openvas-cli")
            elif d == 22 :
                cmd = os.system("apt-get install openvas-manager")
            elif d == 23 :
                cmd = os.system("apt-get install openvas-scanner")
            elif d == 24 :
                cmd = os.system("apt-get install oscanner")
            elif d == 25 :
                cmd = os.system("apt-get install powerfuzzer")
            elif d == 26 :
                cmd = os.system("apt-get install sfuzz")
            elif d == 27 :
                cmd = os.system("apt-get install sidguesser")
            elif d == 28 :
                cmd = os.system("apt-get install siparmyknife")
            elif d == 29 :
                cmd = os.system("apt-get install sqlmap")
            elif d == 30 :
                cmd = os.system("apt-get install sqlninja")
            elif d == 31 :
                cmd = os.system("apt-get install sqlsus")
            elif d == 32 :
                cmd = os.system("apt-get install thc-ipv6")
            elif d == 33 :
                cmd = os.system("apt-get install tnscmd10g")
            elif d == 34 :
                cmd = os.system("apt-get install unix-privesc-check")
            elif d == 35 :
                intro()
            elif d == 0 :
                cmd = os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
            else:
                print("Not Found")
            vull()
        vull()
    if a == 3:
        def wire():
            cmd = os.system("clear")
            print("""
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) RTLSDR Scanner
13) Ghost Phisher                       29) Spooftooph
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              32) Back to main menu
90) airgeddon
91) wifite v2
0) install all wireless tools
""")
            w = int(input("Enter The number of the tool : >>> "))
            if w == 1 :
                cmd = os.system("sudo apt-get update && apt-get install aircrack-ng")
            elif w == 90:
                print("sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
            elif w == 91:
                print("sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git")
            elif w == 2 :
                cmd = os.system("sudo apt-get update && apt-get install asleep")
            elif w == 3 :
                cmd = os.system("sudo apt-get update && apt-get install bluelog")
            elif w == 4 :
                cmd = os.system("sudo apt-get update && apt-get install bluemaho")
            elif w == 5 :
                cmd = os.system("sudo apt-get update && apt-get install bluepot")
            elif w == 6 :
                cmd = os.system("sudo apt-get update && apt-get install blueranger")
            elif w == 7 :
                cmd = os.system("sudo apt-get update && apt-get install bluesnarfer")
            elif w == 8 :
                cmd = os.system("sudo apt-get update && apt-get install bully")
            elif w == 9 :
                cmd = os.system("sudo apt-get update && apt-get install cowpatty")
            elif w == 10 :
                cmd = os.system("sudo apt-get update && apt-get install crackle")
            elif w == 11 :
                cmd = os.system("sudo apt-get update && apt-get install eapmd5pass")
            elif w == 12 :
                cmd = os.system("sudo apt-get update && apt-get install fern-wifi-cracker")
            elif w == 13 :
                cmd = os.system("sudo apt-get update && apt-get install ghost-phisher")
            elif w == 14 :
                cmd = os.system("sudo apt-get update && apt-get install giskismet")
            elif w == 15 :
                cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
            elif w == 16 :
                cmd = os.system("sudo apt-get update && apt-get install kalibrate-rtl")
            elif w == 17 :
                cmd = os.system("sudo apt-get update && apt-get install killerbee-ng")
            elif w == 18 :
                cmd = os.system("sudo apt-get update && apt-get install kismet")
            elif w == 19 :
                cmd = os.system("sudo apt-get update && apt-get install mdk3")
            elif w == 20 :
                cmd = os.system("sudo apt-get update && apt-get install mfcuk")
            elif w == 21 :
                cmd = os.system("sudo apt-get update && apt-get install mfoc")
            elif w == 22 :
                cmd = os.system("sudo apt-get update && apt-get install mfterm")
            elif w == 23 :
                cmd = os.system("sudo apt-get update && apt-get install multimon-ng")
            elif w == 24 :
                cmd = os.system("sudo apt-get update && apt-get install pixiewps")
            elif w == 25 :
                cmd = os.system("sudo apt-get update && apt-get install reaver")
            elif w == 26 :
                cmd = os.system("sudo apt-get update && apt-get install redfang")
            elif w == 27 :
                cmd = os.system("sudo apt-get update && apt-get install rtlsdr-scanner")
            elif w == 28 :
                cmd = os.system("sudo apt-get update && apt-get install spooftooph")
            elif w == 29 :
                cmd = os.system("sudo apt-get update && apt-get install wifi-honey")
            elif w == 30 :
                cmd = os.system("sudo apt-get update && apt-get install wifitap")
            elif w == 31 :
                cmd = os.system("sudo apt-get update && apt-get install wifite")
            elif w == 32 :
                intro()
            elif w == 0 :
                cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
            else:
                print("Not Found")
            wire()
        wire()
    if a == 4:
      def web():
        cmd = os.system("clear")
        print("""
1) apache-users                             21) Parsero
2) Arachni                                  22) plecost
3) BBQSQL                                   23) Powerfuzzer
4) BlindElephant                            24) ProxyStrike
5) Burp Suite                               25) Recon-ng
6) commix                                   26) Skipfish
7) CutyCapt                                 27) sqlmap
8) DAVTest                                  28) Sqlninja
9) deblaze                                  29) sqlsus
10) DIRB                                    30) ua-tester
11) DirBuster                               31) Uniscan
12) fimap                                   32) Vega
13) FunkLoad                                33) w3af
14) Grabber                                 34) WebScarab
15) jboss-autopwn                           35) Webshag
16) joomscan                                36) WebSlayer
17) jSQL                                    37) WebSploit
18) Maltego Teeth                           38) Wfuzz
19) PadBuster                               39) WPScan
20) Paros                                   40) XSSer
                                            41) Back to main menu
0) Install all the web tools

""")
        q = int(input("Enter the number of the tool : >>> "))
        if q == 41 :
            intro()
        elif q == 1 :
            cmd = os.system("apt-get update && apt-get install apache-users")
        elif q == 2 :
            cmd = os.system("apt-get update && apt-get install arachni")
        elif q == 3 :
            cmd = os.system("apt-get update && apt-get install bbqsql ")
        elif q == 4 :
            cmd = os.system("apt-get update && apt-get install blindelephant")
        elif q == 5 :
            cmd = os.system("apt-get install burpsuite")
        elif q == 6 :
            cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
        elif q == 7 :
            cmd = os.system("apt-get install cutycapt")
        elif q == 8:
            cmd = os.system("apt-get install davtest")
        elif q == 9 :
            cmd = os.system("apt-get install deblaze")
        elif q == 10 :
            cmd = os.system("apt-get install dirb")
        elif q == 11 :
            cmd = os.system("apt-get install dirbuster")
        elif q == 12 :
            cmd = os.system("apt-get install fimap")
        elif q == 13 :
            cmd = os.system("apt-get install funkload")
        elif q == 14 :
            cmd = os.system("apt-get install grabber")
        elif q == 15 :
            cmd = os.system("apt-get install jboss-autopwn")
        elif q == 16 :
            cmd = os.system("apt-get install joomscan")
        elif q == 17 :
            cmd = os.system("apt-get install jsql")
        elif q == 18 :
            cmd = os.system("apt-get install maltego-teeth")
        elif q == 19 :
            cmd = os.system("apt-get install padbuster")
        elif q == 20 :
            cmd = os.system("apt-get install paros")
        elif q == 21 :
            cmd = os.system("apt-get install parsero")
        elif q == 22 :
            cmd = os.system("apt-get install plecost")
        elif q == 23 :
            cmd = os.system("apt-get install powerfuzzer")
        elif q == 24 :
            cmd = os.system("apt-get install proxystrike")
        elif q == 25 :
            cmd = os.system("apt-get install recon-ng")
        elif q == 26 :
            cmd = os.system("apt-get install skipfish")
        elif q == 27 :
            cmd = os.system("apt-get install sqlmap")
        elif q == 28 :
            cmd = os.system("apt-get install sqlninja")
        elif q == 29 :
            cmd = os.system("apt-get install sqlsus")
        elif q == 30 :
            cmd = os.system("apt-get install ua-tester")
        elif q == 31 :
            cmd = os.system("apt-get install uniscan")
        elif q == 32 :
            cmd = os.system("apt-get install vega")
        elif q == 33 :
            cmd = os.system("apt-get install w3af")
        elif q == 34 :
            cmd = os.system("apt-get install webscarab")
        elif q == 35 :
            print ("Webshag is unavailable")
        elif q == 36 :
            cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
        elif q == 37 :
            cmd = os.system("apt-get install websploit")
        elif q == 38 :
            cmd = os.system("apt-get install wfuzz")
        elif q == 39 :
            cmd = os.system("apt-get install wpscan")
        elif q == 40 :
            cmd = os.system("apt-get install xsser")
        else:
            print("Not Found")
        web()
      web()
    if a == 5:
      def exploit():
        cmd = os.system("clear")
        print("""
1) Armitage
2) Backdoor Factory
3) BeEF
4) cisco-auditing-tool
5) cisco-global-exploiter
6) cisco-ocs
7) cisco-torch
8) commix
9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia
18) Cobaltstrike v2
19) Back to main menu
0) Install all the exploits tools
""")
        t = int(input("Enter the number of the tool : >> "))
        if t == 1 :
            cmd = os.system("apt-get update && apt-get install armitage")
        elif t == 2 :
            cmd = os.system("apt-get install backdoor-factory")
        elif t == 3 :
            cmd = os.system("apt-get install beef")
        elif t == 4 :
            cmd = os.system("apt-get install cisco-auditing-tool")
        elif t == 5 :
            cmd = os.system("apt-get install cisco-global-exploiter")
        elif t == 6 :
            cmd = os.system("apt-get install cisco-ocs")
        elif t == 7 :
            cmd = os.system("apt-get install cisco-torch")
        elif t == 8 :
            cmd = os.system("apt-get install commix")
        elif t == 9 :
            cmd = os.system("apt-get install crackle")
        elif t == 10 :
            cmd = os.system("apt-get install jboss-autopwn")
        elif t == 11 :
            cmd = os.system("apt-get install linux-exploit-suggester")
        elif t == 12 :
            cmd = os.system("apt-get install maltego-teeth")
        elif t == 13 :
            cmd = os.system("apt-get install set")
        elif t == 14 :
            cmd = os.system("apt-get install shellnoob")
        elif t == 15 :
            cmd = os.system("apt-get install sqlmap")
        elif t == 16 :
            cmd = os.system("apt-get install thc-ipv6")
        elif t == 17 :
            cmd = os.system("apt-get install yersinia")
        elif t == 18 :
            cmd = os.system("apt-get install git && git clone https://github.com/nilotpalbiswas/cobaltstrike-crack")
        elif t == 19 :
            intro()
        elif t == 20 :
            cmd = os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
        else:
            print("Not Found")
        exploit()
      exploit()
    if a == 6 :
      def stree():
        cmd = os.system("clear")
        print("""
1) DHCPig
2) FunkLoad
3) iaxflood
4) Inundator
5) inviteflood
6) ipv6-toolkit
7) mdk3
8) Reaver
9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS
15) Back to main menu

0) Install all Stress Testing tools
""")
        s = int(input("Enter the number of the tool : >> "))
        if s == 1 :
            cmd = os.system("apt-get install dhcping")
        elif s == 2 :
            cmd = os.system("apt-get install funkload")
        elif s == 3 :
            cmd = os.system("apt-get install iaxflood")
        elif s == 4 :
            cmd = os.system("apt-get install inundator")
        elif s == 5 :
            cmd = os.system("apt-get install inviteflood")
        elif s == 6 :
            cmd = os.system("apt-get install ipv6-toolkit")
        elif s == 7 :
            cmd = os.system("apt-get install mdk3")
        elif s == 8 :
            cmd = os.system("apt-get install reaver")
        elif s == 9 :
            cmd = os.system("apt-get install rtpflood")
        elif s == 10 :
            cmd = os.system("apt-get install slowhttptest")
        elif s == 11 :
            cmd = os.system("apt-get install t50")
        elif s == 12 :
            cmd = os.system("apt-get install termineter")
        elif s == 13 :
            cmd = os.system("apt-get install thc-ipv6")
        elif s == 14 :
            cmd = os.system("apt-get install thc-ssl-dos")
        elif s == 15 :
            intro()
        elif s == 0 :
            cmd = os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
        else:
            print("Not Found")
        stree()
      stree()
    if a == 7:
      def forencies():
        cmd = os.system("clear")
        print("""
1) Binwalk                              14) extundelete
2) bulk-extractor                       15) Foremost
3) Capstone                             16) Galleta
4) chntpw                               17) Guymager
5) Cuckoo                               18) iPhone Backup Analyzer
6) dc3dd                                19) p0f
7) ddrescue                             20) pdf-parser
8) DFF                                  21) pdfid
9) diStorm3                             22) pdgmail
10) Dumpzilla                           23) peepdf
11) RegRipper                           24) Back to main menu
12) Volatility
13) Xplico

0) Install all Forensics Tools
""")
        f = int(input("Enter the number of the tool : >>> "))
        if f == 1 :
            cmd = os.system("apt-get install binwalk")
        elif f == 2 :
            cmd = os.system("apt-get install bulk-extractor")
        elif f == 3 :
            cmd = os.system("apt-get install capstone")
        elif f == 4 :
            cmd = os.system("apt-get install chntpw")
        elif f == 5 :
            cmd = os.system("apt-get install cuckoo")
        elif f == 6 :
            cmd = os.system("apt-get install dc3dd")
        elif f == 7 :
            cmd = os.system("apt-get install ddrescue")
        elif f == 8 :
            cmd = os.system("apt-get install dff")
        elif f == 9 :
            cmd = os.system("apt-get install diStorm3")
        elif f == 10 :
            cmd = os.system("apt-get install dumpzilla")
        elif f == 11 :
            cmd = os.system("apt-get install regripper")
        elif f == 12 :
            cmd = os.system("apt-get install volatility")
        elif f == 13 :
            cmd = os.system("apt-get install xplico")
        elif f == 14 :
            cmd = os.system("apt-get install extundelete")
        elif f == 15 :
            cmd = os.system("apt-get install foremost")
        elif f == 16 :
            cmd = os.system("apt-get install galleta")
        elif f == 17 :
            cmd = os.system("apt-get install guymager")
        elif f == 18 :
            cmd = os.system("apt-get install iphone-backup-analyzer")
        elif f == 19 :
            cmd = os.system("apt-get install p0f")
        elif f == 20 :
            cmd = os.system("apt-get install pdf-parser")
        elif f == 21 :
            cmd = os.system("apt-get install pdfid")
        elif f == 22 :
            cmd = os.system("apt-get install pdgmail")
        elif f == 23 :
            cmd = os.system("apt-get install peepdf")
        elif f == 24 :
            intro()
        elif f == 0 :
            cmd = os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
        else:
            print("Not Found")
        forencies()
      forencies()
    elif a == 8 :
      def browsers():
        cmd = os.system("clear")
        print("""
1) Firefox
2) Google Chrome
3) Tor Browser
4) Chromium
5) Iceweasel

6)Back to main menu
""")
        y = int(input("Enter the number of browser : >>>> "))
        if y == 1 :
            cmd = os.system("apt-get update && apt-get install firefox-esr")
        elif y == 2 :
            print("""
1) x64 --->> amd64
2) x32 --->> i386
""")
            google = int(input("Whick System you use? : >>> "))
            if google == 1 :
                cmd = os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                cmd1 = os.system("dpkg -i google-chrome-stable_current_amd64.deb")
            if google == 2 :
                cmd = os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb")
                cmd1 = os.system("dpkg -i google-chrome-stable_current_i386.deb")
            browsers()
        elif y == 3 :
            print("""
1) x64 --->> amd64
2) x32 --->> i386
""")
            tor = int(input("Which system you use ? >>> "))
            if tor == 1 :
                cmd = os.system("")
            if tor == 2 :
                cmd = os.system("")
            browsers()
        elif y == 4 :
            cmd = os.system("apt-get update && apt-get install chromium")
        elif y == 5 :
            cmd = os.system("")
        elif y == 6 :
            cmd = os.system("clear")
            intro()
        else:
            print("Not Found")
        browsers()
      browsers()
    elif a == 9:
      def media():
        cmd = os.system("clear")
        print("""
1) VLC
2) MPV
3) banshee
4) kodi

5) Back to main menu
""")
        er = int(input("Enter the number of the player : >>> "))
        if er == 1 :
            cmd = os.system("apt-get update && apt-get install vlc")
        elif er == 2 :
            cmd = os.system("apt-get update && apt-get install mpv")
        elif er == 3 :
            cmd = os.system("apt-get update && apt-get install banshee")
        elif er == 4 :
            cmd = os.system("apt-get update && apt-get install kodi")
        elif er == 5 :
            cmd = os.system("clear")
            intro()
        else:
            print("Not Found")
        media()
      media()
    elif a == 10:
      def program():
        cmd = os.system("clear")
        print("""
1) idle3 (Based on Python3)
2) Sublime
3) Atom
4) Brackets
5) Eclipse
6) KATE
7) Gedit
8) Geany
9) Bluefish Editor

11) Back to main menu
0) Install all the editors
""")
        zx = int(input("Enter the number of the tool : >>> "))
        if zx == 1 :
            cmd = os.system("apt-get update && apt-get install idle3")
        elif zx == 2 :
            cmd = os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - && sudo apt-get install apt-transport-https && echo 'deb https://download.sublimetext.com/ apt/stable/' | sudo tee /etc/apt/sources.list.d/sublime-text.list && apt-get update && apt-get install sublime-text")
        elif zx == 3 :
            cmd = os.system("apt-get update && apt-get install atom")
        elif zx == 4 :
            cmd = os.system("apt-get update && apt-get install brackets")
        elif zx == 5 :
            cmd = os.system("apt-get update && apt-get install eclipse")
        elif zx == 6 :
            cmd = os.system("apt-get update && apt-get install kate")
        elif zx == 7 :
            cmd = os.system("apt-get update && apt-get install gedit")
        elif zx == 8 :
            cmd = os.system("apt-get update && apt-get install geany")
        elif zx == 9 :
            cmd = os.system("apt-get update && sudo apt-get install bluefish")
        elif zx == 11 :
            intro()
        elif zx == 0 :
            cmd = os.system("apt-get update && apt-get install idle sublime-text atom brackets eclipse kate gedit geany bluefish")
        else:
            print("Not Found")
        program()
      program()
    elif a == 11:
     def snif():
        cmd = os.system("clear")
        print("""
1) Burp Suite                           17) rtpmixsound
2) DNSChef                              18) sctpscan
3) fiked                                19) SIPArmyKnife
4) hamster-sidejack                     20) SIPp
5) HexInject                            21) SIPVicious
6) iaxflood                             22) SniffJoke
7) inviteflood                          23) SSLsplit
8) iSMTP                                24) sslstrip
9) isr-evilgrade                        25) THC-IPV6
10) mitmproxy                           26) VoIPHopper
11) ohrwurm                             27) WebScarab
12) protos-sip                          28) Wifi Honey
13) rebind                              29) Wireshark
14) responder                           30) xspy
15) rtpbreak                            31) Yersinia
16) rtpinsertsound                      32) zaproxy
                                        33) mitmf
00)Back to main menu                    34) Bettercap
0) Install all Sniffing & Spoofing tools
""")
        sniff =int(input("Enter the number of the tool : >>> "))
        if sniff == 1 :
            cmd = os.system("apt-get install burpsuite")
        elif sniff == 2 :
            cmd = os.system("apt-get install dnschef")
        elif sniff == 3 :
            cmd = os.system("apt-get install fiked")
        elif sniff == 4 :
            cmd = os.system("apt-get install hamster-sidejack")
        elif sniff == 5 :
            cmd = os.system("apt-get install hexinject")
        elif sniff == 6 :
            cmd = os.system("apt-get install iaxflood")
        elif sniff == 7 :
            cmd = os.system("apt-get install inviteflood")
        elif sniff == 8 :
            cmd = os.system("apt-get install ismtp")
        elif sniff == 9 :
            cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
        elif sniff == 10 :
            cmd = os.system("apt-get install mitmproxy")
        elif sniff == 11 :
            cmd = os.system("apt-get install ohrwurm")
        elif sniff == 12 :
            cmd = os.system("apt-get install protos-sip")
        elif sniff == 13 :
            cmd = os.system("apt-get install rebind")
        elif sniff == 14 :
            cmd = os.system("apt-get install responder")
        elif sniff == 15 :
            cmd = os.system("apt-get install rtpbreak")
        elif sniff == 16 :
            cmd = os.system("apt-get install rtpinsertsound")
        elif sniff == 17 :
            cmd = os.system("apt-get install rtpmixsound")
        elif sniff == 18 :
            cmd = os.system("apt-get install sctpscan")
        elif sniff == 19 :
            cmd = os.system("apt-get install siparmyknife")
        elif sniff == 20 :
            cmd = os.system("apt-get install sipp")
        elif sniff == 21 :
            cmd = os.system("apt-get install sipvicious")
        elif sniff == 22 :
            cmd = os.system("apt-get install sniffjoke")
        elif sniff == 23 :
            cmd = os.system("apt-get install sslsplit")
        elif sniff == 24 :
            cmd = os.system("apt-get install sslstrip")
        elif sniff == 25 :
            cmd = os.system("apt-get install thc-ipv6")
        elif sniff == 26 :
            cmd = os.system("apt-get install voiphopper")
        elif sniff == 27 :
            cmd = os.system("apt-get install webscarab")
        elif sniff == 28 :
            cmd = os.system("apt-get install wifi-honey")
        elif sniff == 29 :
            cmd = os.system("apt-get install wireshark")
        elif sniff == 30 :
            cmd = os.system("apt-get install xspy")
        elif sniff == 31 :
            cmd = os.system("apt-get install yersinia")
        elif sniff == 32 :
            cmd = os.system("apt-get install zaproxy")
        elif sniff == 33 :
            cmd = os.system("apt-get install mitmf")
        elif sniff == 34 :
            cmd = os.system("apt-get install bettercap")
        elif sniff == 00 :
            intro()
        elif sniff == 0 :
            cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy mitmf bettercap")
        else:
            print("Not Found")
        snif()
     snif()
    elif a == 12:
      def password():
        cmd = os.system("clear")
        print("""
1) acccheck                             19) Maskprocessor
2) Burp Suite                           20) multiforcer
3) CeWL                                 21) Ncrack
4) chntpw                               22) oclgausscrack
5) cisco-auditing-tool                  23) PACK
6) CmosPwd                              24) patator
7) creddump                             25) phrasendrescher
8) crunch                               26) polenum
9) DBPwAudit                            27) RainbowCrack
10) findmyhash                          28) rcracki-mt
11) gpp-decrypt                         29) RSMangler
12) hash-identifier                     30) SQLdict
13) HexorBase                           31) Statsprocessor
14) THC-Hydra                           32) THC-pptp-bruter
15) John the Ripper                     33) TrueCrack
16) Johnny                              34) WebScarab
17) keimpx                              35) wordlists
18) Maltego Teeth                       36) zaproxy

00)Back to main menu 
0) Install all Password Attacks tools
""")
        o = int(input("Enter the number of the tool : >> "))
        if o == 1 :
            cmd = os.system("apt-get install acccheck")
        elif o == 2 :
            cmd = os.system("apt-get install burpsuite")
        elif o == 3 :
            cmd = os.system("apt-get install cewl")
        elif o == 4 :
            cmd = os.system("apt-get install chntpw")
        elif o == 5 :
            cmd = os.system("apt-get install cisco-auditing-tool")
        elif o == 6 :
            cmd = os.system("apt-get install cmospwd")
        elif o == 7 :
            cmd = os.system("apt-get install creddump")
        elif o == 8 :
            cmd = os.system("apt-get install crunch")
        elif o == 9 :
            cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
        elif o == 10 :
            cmd = os.system("apt-get install findmyhash")
        elif o == 11 :
            cmd = os.system("apt-get install gpp-decrypt")
        elif o == 12 :
            cmd = os.system("apt-get install hash-identifier")
        elif o == 13 :
            cmd = os.system("apt-get install hexorbase")
        elif o == 14 :
            cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
        elif o == 15 :
            cmd = os.system("apt-get install john")
        elif o == 16 :
            cmd = os.system("apt-get install johnny")
        elif o == 17 :
            cmd = os.system("apt-get install keimpx")
        elif o == 18 :
            cmd = os.system("apt-get install maltego-teeth")
        elif o == 19 :
            cmd = os.system("apt-get install maskprocessor")
        elif o == 20 :
            cmd = os.system("apt-get install multiforcer")
        elif o == 21 :
            cmd = os.system("apt-get install ncrack")
        elif o == 22 :
            cmd = os.system("apt-get install oclgausscrack")
        elif o == 23 :
            cmd = os.system("apt-get install pack")
        elif o == 24 :
            cmd = os.system("apt-get install patator")
        elif o == 25 :
            cmd = os.system("apt-get install phrasendrescher")
        elif o == 26 :
            cmd = os.system("apt-get install polenum")
        elif o == 27 :
            cmd = os.system("apt-get install rainbowcrack")
        elif o == 28 :
            cmd = os.system("apt-get install rcracki-mt")
        elif o == 29 :
            cmd = os.system("apt-get install rsmangler")
        elif o == 30 :
            cmd = os.system("sudo apt-get install sqldict")
        elif o == 31 :
            cmd = os.system("apt-get install statsprocessor")
        elif o == 32 :
            cmd = os.system("apt-get install thc-pptp-bruter")
        elif o == 33 :
            cmd = os.system("apt-get install truecrack")
        elif o == 34 :
            cmd = os.system("apt-get install webscarab")
        elif o == 35 :
            cmd = os.system("apt-get install wordlists")
        elif o == 36 :
            cmd = os.system("apt-get install zaproxy")
        elif o == 00 :
            intro()
        elif o == 0 :
            cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
        else:
            print("Not Found")
        password()
      password()
    elif a == 13:
      def encyrpt():
        cmd = os.system("clear")
        print("""
1) CryptCat
2) Cymothoa
3) dbd
4) dns2tcp
5) http-tunnel
6) HTTPTunnel
7) Intersect
8) Nishang
9) polenum
10) PowerSploit
11) pwnat
12) RidEnum
13) sbd
14) U3-Pwn
15) Webshells
16) Weevely

00)Back to main menu 
0) Install all Maintaining Access tools
""")
        b = int(input("Enter the number of the tool : >>> "))
        if b == 1 :
            cmd = os.system("apt-get install cryptcat")
        if b == 2 :
            cmd = os.system("apt-get install cymothoa")
        if b == 3 :
            cmd = os.system("apt-get install dbd")
        if b == 4 :
            cmd = os.system("apt-get install dns2tcp")
        if b == 5 :
            cmd = os.system("apt-get install http-tunnel")
        if b == 6 :
            cmd = os.system("apt-get install httptunnel")
        if b == 7 :
            cmd = os.system("apt-get install intersect")
        if b == 8 :
            cmd = os.system("apt-get install nishang")
        if b == 9 :
            cmd = os.system("apt-get install polenum")
        if b == 10 :
            cmd = os.system("apt-get install powersploit")
        if b == 11 :
            cmd = os.system("apt-get install pwnat")
        if b == 12 :
            cmd = os.system("apt-get install ridenum")
        if b == 13 :
            cmd = os.system("apt-get install sbd")
        if b == 14 :
            cmd = os.system("apt-get install u3-pwn")
        if b == 15 :
            cmd = os.system("apt-get install webshells")
        if b == 16 :
            cmd = os.system("apt-get install weevely")
        if b == 0 :
            cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
        if b == 00 :
            intro()
        else:
            print("Not Found")
        encyrpt()
      encyrpt()
    elif a == 14:
      def reverse():
        cmd = os.system("clear")
        print("""
1) apktool
2) dex2jar
3) diStorm3
4) edb-debugger
5) jad
6) javasnoop
7) JD-GUI
8) OllyDbg
9) smali
10) Valgrind
11) YARA

00)Back to main menu 
0) Install all Reverse Engineering tools
""")
        reverses = int(input("Enter the number of the tool : >> "))
        if reverses == 1 :
            cmd = os.system("apt-get install apktool")
        if reverses == 2 :
            cmd = os.system("apt-get install dex2jar")
        if reverses == 3 :
            cmd = os.system("apt-get install distorm3")
        if reverses == 4 :
            cmd = os.system("apt-get install edb-debugger")
        if reverses == 5 :
            cmd = os.system("apt-get install jad")
        if reverses == 6 :
            cmd = os.system("apt-get install javasnoop")
        if reverses == 7 :
            cmd = os.system("apt-get install jd-gui")
        if reverses == 8 :
            cmd = os.system("apt-get install ollydbg")
        if reverses == 9 :
            cmd = os.system("apt-get install smali")
        if reverses == 10 :
            cmd = os.system("apt-get install valgrind")
        if reverses == 11 :
            cmd = os.system("apt-get install YARA")
        if reverses == 00 :
            intro()
        if reverses == 0 :
            cmd = os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
        else:
            print("Not Found")
        reverse()
      reverse()
    elif a == 15:
      def hack():
        cmd = os.system("clear")
        print("""
1) android-sdk
2) apktool
3) Arduino
4) dex2jar
5) Sakis3G
6) smali

00)Back to main menu 
0) Install all Hardware Hacking tools
 """)
        m = int(input("Enter the number 0f the tool : >>> "))
        if m == 1 :
            cmd = os.system("apt-get install android-sdk")
        elif m == 2 :
            cmd = os.system("apt-get install apktool")
        elif m == 3 :
            cmd = os.system("apt-get install arduino")
        elif m == 4 :
            cmd = os.system("apt-get install dex2jar")
        elif m == 5 :
            cmd = os.system("apt-get install sakis3g")
        elif m == 6 :
            cmd = os.system("apt-get install smali")
        elif m == 00 :
            intro()
        elif m == 3 :
            cmd = os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
        else:
            print("Not Found")
        hack()
      hack()
    elif a == 16:
      def av():
        cmd = os.system("clear")
        print("""
1) Veil-Evasion v2
2) Unicorn
3) Shellter
4) AV0id
5) Fat-Rat

note : the tools will be downloaded in the file of script
0) Back to main menu
""")
        gh = int(input("Enter the number of the tool : >> "))
        if gh == 1 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/Veil-Framework/Veil-Evasion.git && cd Veil-Evasion/ && cd setup && setup.sh -c ")
        elif gh == 2 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/trustedsec/unicorn.git ")
        elif gh == 3 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/r00t-3xp10it/venom/tree/master/obfuscate/shellter.git")
        elif gh == 4 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/nccgroup/metasploitavevasion.git")
        elif gh == 5 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/Screetsec/TheFatRat.git && cd TheFatRat/ && chmod +x setup.sh && ./setup.sh")
        elif gh == 0 :
            intro()
        else:
            print("Not Found")
        av()
      av()
    elif a == 17:
      def android() :
        cmd = os.system("clear")
        print("""
1) kwetza

00) Back to main menu 
""")
        k = int(input("Enter the number of the tool : >>> "))
        if k == 1 :
            cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/sensepost/kwetza")
        elif k  == 00 :
            intro()
        else:
            print("Not Found")
        android()
      android()
    elif a == 18 :
      def enviro():
        cmd = os.system("clear")
        print("""
1) Mate
2) KDE
3) LXDE
4) XFCE

00)Back to main menu 
""")
        i = int(input("Enter the number of the environment : >>> "))
        if i == 1 :
            print("If you were asked to configure the lightdm choose 'lightdm'from the list not 'gdm3'")
            cmd = os.system("apt install task-mate-desktop")
        elif i == 2 :
            cmd = os.system("apt-get install kali-defaults kali-root-login desktop-base kde-plasma-desktop")
        elif i == 3 :
            cmd = os.system("apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base")
        elif i == 4 :
            cmd = os.system("apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies && echo xfce4-session > /root/.xsession")
        elif i == 00 :
            intro()
        else:
            print("Not Found")
        enviro()
      enviro()
    elif a == 19 :
        def post():
            cmd = os.system("clear")
            print("""
1) Mimikatz
2) LaZange

0) Back to main menu
""")
            w = int(input("Enter the number 0f the tool : >>> "))
            if w == 1 :
                cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/gentilkiwi/mimikatz.git")
            elif w == 2 :
                cmd = os.system("apt-get update && apt-get install git && git clone https://github.com/AlessandroZ/LaZagne.git")
            elif w == 0 :
                intro()
            else:
                print("Not Found")
            post()
        post()
    elif a == 20 :
        cmd = os.system("clear")
        print("\nBye. Have a nice time")
        quit()
    elif a == 21 :
        cmd = os.system("clear")
        print("""
Hi.
My name is Ahmed Maher (Hacker-EG) from Egypt,
the mother of the world,
you find on Facebook

https://www.facebook.com/ahmedmaher1233
pease
""")
        quit()
    else:
        print("Not Found")
intro()
