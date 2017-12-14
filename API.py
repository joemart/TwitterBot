#https://apps.twitter.com/app/12493377/keys
#https://pypi.python.org/pypi/twitter/1.17.1#downloads
#https://github.com/basti2342/retweet-bot/blob/master/retweet.py
#https://dev.twitter.com/rest/public/search

#username: tripleta intelectual
#password: desiree

####################################################################
#The purpose of this program is to tweet about a specific topic and
#follow any account that has done a recent tweet about the topic.
#####################################################################

from twitter import *
import json

#Se conecta al API de Twitter
#Connect to the Twitter API
t = Twitter(
            auth=OAuth('743154858824343552-DBPRpivcsDQIMIW6mwvPakokJI2KAeG',
                       '8K52cI0lQohQ5lyNfceQORTthp3dNmZcoPIbZwW70jk98',
                       'gRkgYqfCbsnNE2tN80b8GYrii',
                       '5waAx0ZOuw5sjEJrhFSwmDvIHDNER2T9N8uUBa7KKr1x0Ertvx'))

#Tweet del trabajo escrito
#Tweet

#Coloca en la variable trabajo escrito su "trabajo escrito"
#Put in the variable "trabajoescrito" your search
trabajoescrito = ""
array = []
count = 0
temp = ""

#Esto divide el texto del trabajo escrito de 100 en 100
#This divides the text 100 characters

for i in trabajoescrito:
    temp = temp + i
    count+=1
    if count % 100 == 0:
        array.append(temp)
        temp = ""

#Tweet el primer status
#Tweet the first status
b = t.statuses.update(status=array[0])

#Luego Tweetea los demas
#Tweet the next statuses
for i in range(1,len(array)):
    t.statuses.update(status = array[i], in_reply_to_status_id=b['id'])

    


#lo que se buscara
#what we will be looking for
pregunta = "#Bacalao"

#Busqueda de tweets relacionados
#Searching for related tweets
respuesta = t.search.tweets(q=pregunta, count = 5) #count es el numero de tweets que cogera
                                                   #count is the number of tweets that will take
    
#Itera por los tweets
#Iterate through tweets
for tweets in respuesta["statuses"]:
    t.statuses.retweet(id = tweets['id']) #aqui se hace el retweet
                                          #The tweet is done here
    print "Hicistes retweet de " + str(tweets['id'])
    t.friendships.create(user_id=tweets['user']['id']) #aqui se hace el follow a la persona
                                                       #The follow is done here
    print "Te hicistes amigo de " + tweets['user']['name']    
