import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

import time
import urllib.request #用來建立請求
import urllib.parse
from bs4 import BeautifulSoup

def Write_Webpage(Webpage,Filename):
    DiePath = 'D:\AFU'
    f = open(DiePath+'\\'+Filename+'.txt','a')
    f.write(Webpage)


def search_ticket(html_page,group,DisName1,DisName2,ticket_release_time):
    localtime = time.asctime( time.localtime(time.time()) )
    print('=========================================')
    print(DisName1)
    print(DisName2)
    print('  '+localtime)
    #try:
    #    page = urllib.request.urlopen(html_page,timeout=1)
    #except Exception as e:
    #    print(e)
        
    page = urllib.request.urlopen(html_page)
    soup = BeautifulSoup(page, 'html.parser')
    #Write_Webpage(str(soup.prettify()),DisName1)
    Total_Ticket = 0
    Soldout_Check = 0
    for g in range(0,group,1):
        area_list = soup.find('ul',{'id':"group_"+str(g),'class':"area-list"})
        #print(area_list)        
        list_buy = area_list.find_all('li',{'class':"select_form_b"})
        Total_Ticket = Total_Ticket + len(list_buy)
        #print(Total_Ticket)
        list_soldout = area_list.find_all('li')
        
        for d in list_soldout:
            font_test = d.find_all('font',{'color':"#AAAAAA"})
            Soldout_Check = Soldout_Check + 1
            #print(font_test)
            #for f in font_test:
            #    print(f.get_text())
        
        for b in list_buy:
            print('  '+b.get_text())
            #for gg in span_test:
            #    print(gg.get_text())
    if( Total_Ticket == 0 & Soldout_Check != 82):
        color.write('        暫無票捲 \n',"COMMENT")
    else:
        color.write('!!!!!!!! 快來搶票 !!!!!!!! \n',"COMMENT")
    if( len(list_buy) != 0):
        ticket_release_time = ticket_release_time + 1

    color.write('釋票次數 : '+str(ticket_release_time)+' , 剩餘區塊 : '+str(Total_Ticket)+' , 售完區塊 : '+str(Soldout_Check)+'\n',"STRING")
    #print(soup.prettify())
    return ticket_release_time

quote_page0 = 'https://tixcraft.com/ticket/area/18_Charlie/4262'
quote_page1 = 'https://tixcraft.com/ticket/area/18_BTS/4335'
quote_page2 = 'https://tixcraft.com/ticket/area/18_BTS/4391'
run = True
ticket_release_time0 = 0
ticket_release_time1 = 0
ticket_release_time2 = 0

while run == True:
    
    #ticket_release_time0 = search_ticket(quote_page0,5,'CHARLIE PUTH THE VOICENOTES TOUR','     查理2018台灣演唱會',ticket_release_time0)
    #time.sleep(1)
    ticket_release_time1 = search_ticket(quote_page1,9,'BTS WORLD TOUR LOVE YOURSELF TAOYUAN','     2018/12/08 18:00 (六)',ticket_release_time1)
    time.sleep(1)
    ticket_release_time2 = search_ticket(quote_page2,9,'BTS WORLD TOUR LOVE YOURSELF TAOYUAN','     2018/12/09 18:00 (日)',ticket_release_time2)
    time.sleep(1)
