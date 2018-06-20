#!/usr/bin/python
#-- coding:utf-8 --

import ConfigParser

import sys
import codecs

sys.path.append('/opt/xml_transfer/xml_listener_auto_process/')


import check_vedio_status
import os

def get_config():
    cp = ConfigParser.SafeConfigParser()

    with codecs.open('config/files.config', 'r', encoding='utf-8') as f:  
        cp.readfp(f)

#log_file = cp.get('log_files','log_today').strip()
        log_file = cp.get('log_files','log_yesrtoday').strip()
        work_dir = cp.get('searchid_files','wk_dir').strip()
        searchid_file_pre_offline = work_dir + cp.get('searchid_files','pre_offline').strip()
        searchid_file_offline = work_dir + cp.get('searchid_files','offline').strip()
        searchid_file_online = work_dir + cp.get('searchid_files','online').strip()
#searchid_file_pre_offline = '/opt/xml_transfer/id.txt.2.pre_offline'
#searchid_file_offline = '/opt/xml_transfer/id.txt.2.pre_offline'
#searchid_file_online = '/opt/xml_transfer/id.txt.2.online'
    print(log_file,searchid_file_pre_offline,searchid_file_offline,searchid_file_online)
    return log_file,searchid_file_pre_offline,searchid_file_offline,searchid_file_online

def searchid_generater(log_file,file_pre_offline,file_online):
    with open(log_file,'r') as f:
        l = f.readline().strip()
        err_online_msg = 'ERROR Build'
        err_offline_msg = 'ERROR Delete'
        err_msg = 'failed with timed out'

        open(file_online,'w').close()
#f = open(file_online,'r+')
#f.truncate()

#f1 = open(file_pre_offline,'r+')
#f1.truncate()
        open(file_pre_offline,'w').close()


        if l.find(err_online_msg) and l.find(err_msg):
            f1 = open(file_online,'a')
            f1.write(l + '\n')
            f1.close()
        elif l.find(err_offline_msg) and l.find(err_msg):
            f2 = open(file_pre_offline,'a')
            f2.write(l + '\n')
            f2.close()
        else:
            pass

        with open(file_online,'r') as f3:
            print(f3.readline())

        
        with open(file_pre_offline,'r') as f4:
            print(f4.readline())




def main():
    log_file,file_pre_offline,file_offline,file_online = get_config()

    searchid_generater(log_file,file_pre_offline,file_online)

    check_vedio_status.check_status(file_pre_offline,file_offline,file_online)

if __name__  == '__main__':
    main()
