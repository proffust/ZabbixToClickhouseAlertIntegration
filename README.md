# ZabbixToClickhouseAlertIntegration

<br>Clickhouse table
```
CREATE TABLE zabbix.events
(
    `Date` Date DEFAULT toDate(Clock), 
    `Clock` UInt32, 
    `RecoveryClock` UInt32, 
    `Eventid` UInt64, 
    `Name` String, 
    `Hosts` Array(String), 
    `Groups` Array(String), 
    `Tags` Array(String), 
    `Source` String
)
ENGINE = ReplacingMergeTree(RecoveryClock)
PARTITION BY toISOWeek(Date)
ORDER BY Eventid
```

Actions text:
<br>Problem
<br>Subject
```{EVENT.VALUE}```
<br>Message:
```{
"datetime":"{EVENT.DATE} {EVENT.TIME}",
"eventid":{EVENT.ID},
"name":"{EVENT.NAME}",
"groups":"{TRIGGER.HOSTGROUP.NAME}",
"host":"{HOST.NAME}",
"tags":"{EVENT.TAGS}",
"source":"ZabbixSYSLOCAL",
"severity":"{EVENT.SEVERITY}"
}
```
<br>Recovery
<br>Subject
```{EVENT.VALUE}```
<br>Message:
```{
"recoverydatetime":"{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}",
"eventid":{EVENT.ID},
"startdatetime":"{EVENT.DATE} {EVENT.TIME}",
"name":"{EVENT.NAME}",
"groups":"{TRIGGER.HOSTGROUP.NAME}",
"host":"{HOST.NAME}",
"tags":"{EVENT.TAGS}",
"source":"ZabbixSYSLOCAL",
"severity":"{EVENT.SEVERITY}"
}
```

<br>Screenshots<br>
<img src="https://i.imgur.com/XmBfgw6.png">
<img src="https://i.imgur.com/7aA1TSt.png">
<img src="https://i.imgur.com/tK0EHQk.png">

# Known issue
1. Events with " in name not parsed
