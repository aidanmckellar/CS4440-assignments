#!/usr/bin/python3
import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import *
url = sys.argv[1]

#split up inputtd url
split_url = url.split('token=')
token_commands = split_url[1].split('&user=')
num_commands =len(token_commands[1].split('&'))-1

#create string representing the length of original message from
#secret password to end of commands 
m ='12345678user=' + token_commands[1]
print(m)
padded_m_len =(len(m)  + len(padding((len(m)) * 8)))
#create block starting count after padding
h2 = md5(
        state = token_commands[0],
        count = padded_m_len

    )
#adding final command to h2
command  = '&command3=UnlockAllSafes'
h2.update(command)
parsedUrl = urlparse(url)
q = 'token='+h2.hexdigest()+'&user='+ token_commands[1] + quote(padding(len(m)))+'&command' +str(num_commands)+ '=UnlockAllSafes'

#connecting to new url
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + q)
print(conn.getresponse().read())
