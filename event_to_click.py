#!/etc/zabbix/alertscripts/venv_click/bin/python
#-*- coding: utf-8 -*-
import clickhouse_driver
import argparse
import json
import datetime

parser = argparse.ArgumentParser(description='Write zabbix events to clickhouse')
parser.add_argument('alertsubject', type=int)
parser.add_argument('alertmessage', type=str)
parser.add_argument('--clickhouse-host', type=str, default="127.0.0.1")
parser.add_argument('--clickhouse-port', type=int, default=9000)
parser.add_argument('--clickhouse-db', type=str, default="zabbix")
parser.add_argument('--clickhouse-table', type=str, default="events")
args = parser.parse_args()

fixes = [('\xa0', ' '),('"',"'"),("{'",'{"'),("','", '","'),(",'", ',"'),("':'", '":"'),("':", '":'),("''", '\'\"'), ("'}",'"}')]
alertmessage = args.alertmessage
for fix in fixes:
    alertmessage = alertmessage.replace(*fix)
event = json.loads(alertmessage)
print(event)
client = clickhouse_driver.Client(host=args.clickhouse_host, port=args.clickhouse_port,
                database=args.clickhouse_db)

if(args.alertsubject==1):
    client.execute("INSERT INTO {0}.{1} (Clock, Eventid, Name, Groups, Hosts, Tags, Source, Severity) VALUES".format(
                                                                            args.clickhouse_db, args.clickhouse_table),
			    [{"Clock":int(datetime.datetime.strptime(event["datetime"], "%Y.%m.%d %H:%M:%S").timestamp()),
                  "Eventid": event["eventid"],"Name": event["name"],"Groups":event["groups"].replace(", ",",").split(","),
                  "Hosts": event["host"].replace(", ",",").split(","), "Tags":event["tags"].split(","), "Source": event["source"], "Severity": event["severity"]}])
else:
    client.execute("INSERT INTO {0}.{1} (Clock, RecoveryClock, Eventid, Name, Groups, Hosts, Tags, Source, Severity) VALUES".format(
                                                                                            args.clickhouse_db, args.clickhouse_table),
		    [{"Clock":int(datetime.datetime.strptime(event["startdatetime"], "%Y.%m.%d %H:%M:%S").timestamp()),
		      "RecoveryClock": int(datetime.datetime.strptime(event["recoverydatetime"], "%Y.%m.%d %H:%M:%S").timestamp()),
              "Eventid": event["eventid"], "Name": event["name"],"Groups":event["groups"].replace(", ",",").split(","),
              "Hosts": event["host"].replace(", ",",").split(","), "Tags":event["tags"].split(","), "Source": event["source"], "Severity": event["severity"]}])

client.disconnect()
