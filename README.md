# ZabbixToClickhouseAlertIntegration

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

<br>Screenshots


