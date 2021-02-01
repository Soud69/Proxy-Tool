try:
    import requests
    import os
    import time
    from os import system, path
    import json
    import threading

    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")
    exit()

a = requests.Session()


def mode():
    print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                            Credit @_agf - Soud#0737

                            """)
    print("This is simple tool by Soud to Grab & Check Proxy\n")
    noe = int(input("""[Choose Mode]
1) HTTP/S Proxy
2) SOCKS4 Proxy
3) SOCKS5 Proxy
4) Proxy Checker
5) Exit\n>> """))
    if noe == 1:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[+] Grabbed & Saved {cou} HTTP/S Proxy")
        with open("HTTPS.txt", "a") as Proxyy:
            Proxyy.write(ress)
            input("Press Any Key To Exit...\n")

    elif noe == 2:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[+] Grabbed & Saved {cou} SOCKS4 Proxy")
        with open("SOCKS4.txt", "a") as Proxyy:
            Proxyy.write(ress)
            Proxyy.close()
            input("Press Any Key To Exit...\n")

    elif noe == 3:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
        res = a.get(url)
        cou = res.text.count(":")
        ress = res.text.replace("\n", "")
        print(f"[+] Grabbed & Saved {cou} SOCKS5 Proxy")
        with open("SOCKS5.txt", "a") as Proxyy:
            Proxyy.write(ress)
            input("Press Any Key To Exit...\n")

    elif noe == 4:
        if path.exists("proxy.txt"):
            threadn = int(input("Enter Your Threads: "))
            threadlist = []
            for t in range(threadn + 1):
                i = threading.Thread(target=chkp)
                i.start()
                threadlist.append(i)
            for i in threadlist:
                i.join()
        else:
            print("Pls Make proxy.txt file and try again")
            time.sleep(3)
            os.system("cls")
            mode()

    elif noe == 5:
        print("[!] Bye Kid...")
        time.sleep(2)
        exit()

    else:
        print("[!] Wrong Mode")
        time.sleep(3)
        os.system("cls")
        mode()


def chkp():
    while 1:
        good = 0
        bad = 0
        checked = 0
        proxx = open("proxy.txt", "r")
        for prox in proxx:
            ip = prox.split(":")[0]
            port = prox.split(":")[1]
            url = "https://onlinechecker.proxyscrape.com/index.php"
            head = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "origin": "https://proxyscrape.com",
                "referer": "https://proxyscrape.com/",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
            }
            data = {
                "ip_addr": ip,
                "port": port
            }
            chk = a.post(url, data=data, headers=head)
            if chk.text.find('working" : true') >= 0:
                good += 1
                checked += 1
                print(f"[+] {ip}:{port}")

                if chk.text.find('type" : "HTTP/S') >= 0:
                    with open("Checked-HTTP.txt", "a") as resu:
                        resu.write(f"{ip}:{port}\n")
                        resu.close()
                elif chk.text.find('type" : "SOCKS4') >= 0:
                    with open("Checked-SOCKS4.txt", "a") as resu:
                        resu.write(f"{ip}:{port}\n")
                        resu.close()
                elif chk.text.find('type" : "SOCKS5') >= 0:
                    with open("Checked-SOCKS5.txt", "a") as resu:
                        resu.write(f"{ip}:{port}\n")
                        resu.close()
                else:
                    with open("Checked-Unknown.txt", "a") as resu:
                        resu.write(f"{ip}:{port}\n")
                        resu.close()
            else:
                bad += 1
                checked += 1
                print(f"[-] {ip}:{port}")


mode()
