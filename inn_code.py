import mysql.connector
from bs4 import BeautifulSoup
import requests
import subprocess as sp
import imdb
from imdb import IMDb
import config_pass


#Function for creating Mysql Database

#def database():
    

#    mycursor.execute("Create database tv_series_")
 #   mycursor.execute("Use tv_series_")

  #  mycursor.execute("Create table input(email varchar(100), tv_series varchar(500))")


     
#Function for Web Scrapping

def scrapper(s):
    for x in s:
        mov=tv.search_movie(x)[0]                                              #Searching for the Tv Series, given by the user                     
        sid=tv.get_imdbID(mov)                                                 #fetching the Unique Series Id of Particular TV_Series
        
        page = requests.get("https://www.imdb.com/title/tt{}".format(sid))
        soup = BeautifulSoup(page.content,'html.parser')
        name_box=soup.findAll('div',attrs={'class':'seasons-and-year-nav'})    #The Given Class contains data of Seasons and Realease Year       
        value=[]
        for i in name_box:
            value=i.text.strip()
        value=value.split("\xa0\xa0\n")
        temp=value[0].split("\n")
        name=temp[len(temp)-1]

        npage = requests.get("https://www.imdb.com/title/tt{0}/episodes?season={1}&ref_=tt_eps_sn_{1}".format(sid,name))
        soup = BeautifulSoup(npage.content,'html.parser')
        name_box=soup.findAll('div',attrs={'class':'airdate'})

        n=[]
        for i in name_box:
            n.append(i.text.strip())

        t=n
        ol=len(n)

        while '' in t:
            t.remove('')
        tl=len(t)



        month={"Jan.":1,"Feb.":2,"Mar.":3,"Apr.":4,"May":5,"Jun.":6,"Jul.":7,"Aug.":8,"Sep.":9,"Oct.":10,"Nov.":11,"Dec.":12}
        from datetime import date
        import datetime
        today=str(date.today())
        today=today.split("-")


        if len(n[1].split()) == 1:
            Status="The next season begins in {}".format(n[1])
        else:
            flag=0
            for i in t:
                a=i.split(" ")
                a[1]=month.get(a[1])
                if datetime.date(int(a[2]),int(a[1]),int(a[0])) > datetime.date(int(today[0]),int(today[1]),int(today[2])):
                    flag=1
                    break
            if flag==0:
                if tl<ol:
                    Status="Latest episode was released on {}-{}-{}".format(a[2],a[1],a[0])
                else:
                    Status="The show has finished streaming all its episodes"
            else:
                Status="Next episode airs on {}-{}-{}".format(a[2],a[1],a[0])


        fh.write("""
        Tv series name:{}
        Status:{}\n""".format(x,Status))


    fh.write("id: {}".format(email))    
    fh.close()




#Function for Sending mail to user via Ansible

def mail():
    fh=open("/ws/mail.yml","w")
    fh.write("""
    - hosts: localhost
      tasks:
       - include_vars: "/ws/mail_output.yml"
       - mail:
           body: "{{var}}"
           username: "config_pass.email"
           password: "config_pass.password"
           subject: "Notification for your fav tv series"
           to: '{{id}}'
           host: smtp.gmail.com
           port: 587
    """)
    fh.close()

    sp.getoutput("sudo ansible-playbook /ws/mail.yml")


conn=mysql.connector.connect(user='root',password='Redhatsql@98',host='localhost',auth_plugin='mysql_native_password',database="My_database03")
mycursor=conn.cursor()
#database()
tv=IMDb()
while True:
    email=input("Email address: ")
    Tv_series=input("Tv Series:")

    params=(email,Tv_series.lower())
    

    mycursor.execute("Insert into input(email,tv_series) values (%s,%s)",params)
    conn.commit()
    mycursor.execute("select * from input")
    data=mycursor.fetchall()
    a=data[len(data)-1]
    s=a[1].split(',')
    
    fh=open('/ws/mail_output.yml','w')
    fh.write("var: |")
    
    scrapper(s)
    mail()
