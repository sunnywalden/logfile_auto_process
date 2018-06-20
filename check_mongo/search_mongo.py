#!/usr/bin/python
#-- coding:utf-8 --

import os
from pymongo import MongoClient
import ConfigParser
import codecs
import sys
sys.path.append("/opt/xml_transfer/xml_listener_auto_process")

cp = ConfigParser.SafeConfigParser()
with codecs.open('config/files.config', 'r', encoding='utf-8') as f:
    cp.readfp(f)
    
    host = cp.get('mongo','host').strip()
    port = int(cp.get('mongo','port').strip())


client=MongoClient(host, port)

db=client.migu_video

def check_status(searchid):
    if searchid:
        cursor = db.program.find({'searchId':searchid},{'_id':0,'active':1})
        for search_res in cursor:
            print(search_res)
            return search_res


