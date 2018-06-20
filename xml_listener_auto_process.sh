#!/usr/bin/bash

#log_file='/var/log/db_doc_onoff.log.1'

#grep -i 'ERROR Build' ${log_file}| grep 'failed with timed out'|awk '{print $6}' > /opt/xml_transfer/id.txt.2.online
#grep -i 'ERROR Delete' ${log_file}|grep 'failed with timed out'|awk '{print $6}' > /opt/xml_transfer/id.txt.2.pre_offline

#echo 'searchids to parse'
#echo '*****************************************'

#cat /opt/xml_transfer/id.txt.2.online
#cat /opt/xml_transfer/id.txt.2.pre_offline

echo '*****************************************'
echo 'processing start'

cd /opt/xml_transfer/xml_listener_auto_process/
python main/xml_listener_auto.py
echo '*****************************************'

cd /opt/xml_transfer/
bash /opt/xml_transfer/doc_online_zhangbo.sh
bash /opt/xml_transfer/doc_offline_zhangbo.sh
