#Camila Osoria
#801155816
#Prof Carlos Corrada
#Twitter API

#https://apps.twitter.com/app/12493377/keys
#https://pypi.python.org/pypi/twitter/1.17.1#downloads
#https://github.com/basti2342/retweet-bot/blob/master/retweet.py
#https://dev.twitter.com/rest/public/search

#username: tripleta intelectual
#password: desiree

from twitter import *
import json

#Se conecta al API de Twitter
t = Twitter(
            auth=OAuth('743154858824343552-DBPRpivcsDQIMIW6mwvPakokJI2KAeG',
                       '8K52cI0lQohQ5lyNfceQORTthp3dNmZcoPIbZwW70jk98',
                       'gRkgYqfCbsnNE2tN80b8GYrii',
                       '5waAx0ZOuw5sjEJrhFSwmDvIHDNER2T9N8uUBa7KKr1x0Ertvx'))

#Tweet del trabajo escrito

#Coloca en la variable trabajo escrito su "trabajo escrito"
trabajoescrito = ""
array = []
count = 0
temp = ""

#Esto divide el texto del trabajo escrito de 100 en 100
for i in trabajoescrito:
    temp = temp + i
    count+=1
    if count % 100 == 0:
        array.append(temp)
        temp = ""

#Tweet el primer status
b = t.statuses.update(status=array[0])

#Luego Tweetea los demas
for i in range(1,len(array)):
    t.statuses.update(status = array[i], in_reply_to_status_id=b['id'])

    


#lo que se buscara
pregunta = "#Bacalao"

#Busqueda de tweets relacionados
respuesta = t.search.tweets(q=pregunta, count = 5) #count es el numero de tweets que cogera
    
#Itera por los tweets
for tweets in respuesta["statuses"]:
    t.statuses.retweet(id = tweets['id']) #aqui se hace el retweet
    print "Hicistes retweet de " + str(tweets['id'])
    t.friendships.create(user_id=tweets['user']['id']) #aqui se hace el follow a la persona
    print "Te hicistes amigo de " + tweets['user']['name']    
