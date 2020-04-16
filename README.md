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
    `Source` String,
    `Severity` String
)
ENGINE = ReplacingMergeTree(RecoveryClock)
PARTITION BY toISOWeek(Date)
ORDER BY Eventid
```
<br>Installation:
1. Go to alert script location
1. Create venv for script
    ```python3 -m venv venv_click```
1. Activate venv and install clickhouse_client module
    ```source venv_click/bin/activate
    pip install clickhouse-driver
    deactivate
1. Download script and edit path to venv
1. Add media type
1. Add media to Super Admin user
1. Add actions

Actions text:
<br>Problem
<br>Subject
```{EVENT.VALUE}```
<br>Message:
```
{"datetime":"{EVENT.DATE} {EVENT.TIME}","eventid":{EVENT.ID},"name":"{EVENT.NAME}","groups":"{TRIGGER.HOSTGROUP.NAME}","host":"{HOST.NAME}","tags":"{EVENT.TAGS}","source":"ZabbixSYSLOCAL","severity":"{EVENT.SEVERITY}"}
```
<br>Recovery
<br>Subject
```{EVENT.VALUE}```
<br>Message:
```
{"recoverydatetime":"{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}","eventid":{EVENT.ID},"startdatetime":"{EVENT.DATE} {EVENT.TIME}","name":"{EVENT.NAME}","groups":"{TRIGGER.HOSTGROUP.NAME}","host":"{HOST.NAME}","tags":"{EVENT.TAGS}","source":"ZabbixSYSLOCAL","severity":"{EVENT.SEVERITY}"}
```

<br>Screenshots<br>
<img src="https://i.imgur.com/6b5oNHm.png">
<img src="https://i.imgur.com/5RkArZl.png">
<img src="https://i.imgur.com/tK0EHQk.png">

