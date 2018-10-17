# Innovaccer-Platform-intern 
Summer Internship Hiring Challenge-Innovaccer 

### Prerequisites
All the Scripts that I have created have been tested on **Redhat Linux** with **python version 3.6**.The Mail is sent to User via 
**Ansible** and the version used is 2.7 .

### Why Ansible
Ansible is an open source IT Configuration Management, Deployment & Orchestration tool. It aims to provide large productivity gains to a wide variety of automation challenges.This tool is very simple to use yet powerful enough to automate complex multi-tier IT application environments.
Ansible uses a simple syntax written in **YAML** called **playbooks**.It is **completely agentless**. There are no agents/software or additional firewall ports that you need to install on the  client systems or hosts which you want to automate. You do not have to separately set up a management infrastructure which includes managing your entire systems, network and storage. It further reduces the effort required for your team to start automating right away.

### How It Works
Here, the user enters the Email-Id and his Favourite TV-Series which gets stored in the MYSQL Database as shown in the fig:
![alt text](https://github.com/visheshks/Innovaccer-Platform-intern/blob/master/images/sqldata.PNG)

Web Scrapping Function is called passing TV Series Name.**IMDbPY**(Python package for retreiving and managing IMDB movie database)
is used to search for the particular TV Series with its Unique Series Id.
The Request to the Imdb Website is made for that particular series entered by the user with its unique Id and through that URL Web data is Scrapped(TV Series Season and Year).Beautiful Soup Library is used for fetching data from IMDB Website.It is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML.
After taking the usefull data (.i.e. Last Season and its Data-Month-Year).It is then Compared with different cases and Current Date.The three Condition get finalised at last:
> The Tv Series Streaming is Over |
> Its Next Episode will air on Year-Month-date |
> The Next Episode Begins in Year

The Mail is Sent to User via Running **Ansible Playbook**.The Mail is Sent using **SMTP**,a protocol for sending E-mail messages between servers.The Final Output of Mail,for sending to User in the Playbook (YAML file)looks like:
![alt text](https://github.com/visheshks/Innovaccer-Platform-intern/blob/master/images/maildata.PNG)
