#!/usr/bin/python
#-- coding:utf-8 --

import ConfigParser
import os,sys
sys.path.append("..")
import check_mongo.search_mongo
import time


def get_searchid(file):
    if os.path.exists(file):
#f = open(file)
#searchid = f.readline().strip()
        for line in open(file,'r'):
#while searchid:
#searchid = f.readline().strip()
#if searchid:
            searchid = line.strip()
            print('searchid generaled in get_searchid',searchid)
            yield searchid
        yield False
#searchid = f.readline().strip()
#continue
#            else:
#                break
#        else:
#            print('None')
#            break
#f.close()        
    else:
        print('%s file not exit') % (file)
        exit(1)
    

def check_status(pre_offline_file, offline_file,online_file):
    #chek file before deal with them
    print(pre_offline_file, offline_file,online_file)
    
    #truncate offline searchid list file before update it
    f = open(offline_file,'r+')
    f.truncate()

    get_sid = get_searchid(pre_offline_file)
    while get_sid:
#get_sid = get_searchid(pre_offline_file)
#if get_sid:
        searchid = next(get_sid)
        if searchid:
            print('searchid returned by func get_searchid',searchid)
            res = search_mongo.check_status(searchid)
            print('response of mongo',type(res),res)
        #time.sleep(30)
            vedio_statu = eval(str(res))['active']

            print(vedio_statu)

            if vedio_statu:
                todo_file = online_file

            else:
                todo_file = offline_file

            with open(todo_file,'a') as f:
                f.write(searchid)
        else:
            print('We finished here!')
            print('*' * 20)
            break
