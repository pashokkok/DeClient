import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
 
██████╗░███████╗░█████╗░██╗░░██╗███████╗░█████╗░
██╔══██╗██╔════╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░██║█████╗░░██║░░╚═╝███████║█████╗░░██║░░╚═╝
██║░░██║██╔══╝░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗
██████╔╝███████╗╚█████╔╝██║░░██║███████╗╚█████╔╝
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░   """+G+"""v1.4"""+G+"""

             
     by DeClient author !! With IP-icker code

"""+CY+"""𝕯𝖊𝕮"""+G+"""----"""+CY+""" DeClient project"""+G+"""----"""+CY+"""𝕯𝖊𝕮""")
        
    def m3():
        try:
            print(CY+"""\n
𝕯𝖊𝕮"""+G+""" Выберите функцию"""+G+"""

[1]"""+CY+""" Пробить свой IP"""+G+"""
[2]"""+CY+""" Пробить другой IP"""+G+"""
[3]"""+CY+""" Выйти
""")
            ch=int(input(G+"DeClient ==> "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                print(Y+"End"+W)
            else:
                print(R+"\nНеверно набрана функция!\n")
                m3()
        except ValueError:
            print(R+"\nНеверно набрана функция!\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)
                ip=data['query']
                org=data['org']
                c=data['city']
                cont=data['country']
                reg=data['regionName']
                latt=data['lat']
                lonp=data['lon']

                print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(Y+'\n>>>'+CY+' IP address details\n ')
                print(G+"1) IP Address : "+Y,ip,'\n')
                print(G+"2) Org : "+Y,org,'\n')
                print(G+"3) City : "+Y,c,'\n')
                print(G+"4) Region : "+Y,reg,'\n')
                print(G+"5) Country : "+Y,cont,'\n')
                print(G+"6) Location\n")
                print(G+"\tLattitude : "+Y,latt,'\n')
                print(G+"\tLongitude : "+Y,lonp,'\n')
                l='https://www.google.com/maps/place/'+str(latt)+'+'+str(lonp)
                print(R+"\n#"+Y+" Google Map link : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Открыть ссылку в браузере??"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nПробейте другой IP или выйдите командой Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nНеверно набрана функция!\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Открыть ссылку в браузере?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y+"\nПробейте другой IP или выйдите командой Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\nНеверно набрана функция!\n")
                        m3()
                return
            except KeyError:
                print(R+"\nОшибка! Неправильный IP или Вебсайт\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" Пожалуйста, проверьте свое интернет соединение!\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"Укажите IP адрес:"+W+" ")
        if u=="":
            print(R+"\nУкажите правильный IP адрес!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\n."+W)
