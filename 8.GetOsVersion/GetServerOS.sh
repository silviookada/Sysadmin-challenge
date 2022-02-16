#!/bin/bash
#servers=`cat $1`
servers=`cat  myservers_list.txt`
for server in $servers
do
  output=`ssh master@$server "printf '%(%H:%M:%S %m/%d/%y)T\n  ';hostname;echo ' ';hostname -I;echo ' ';uname -v"`
  echo -e "$output"|tr -d "\n" >> servers_version.txt
  echo "" >> servers_version.txt
done
