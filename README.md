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

![Media type](https://github.com/proffust/ZabbixToClickhouseAlertIntegration/blob/master/DeepinScreenshot_select-area_20191023185348.png)
![Action1](https://github.com/proffust/ZabbixToClickhouseAlertIntegration/blob/master/DeepinScreenshot_select-area_20191023185305.png)
![Action2](https://github.com/proffust/ZabbixToClickhouseAlertIntegration/blob/master/DeepinScreenshot_select-area_20191023185252.png)
