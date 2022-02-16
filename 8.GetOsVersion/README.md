First create a file named "myservers_list.txt" with the servers hostnames and run ./GetServerOS.sh

The script is hardcoded to get the server list from "myservers_list.txt" file but can be modified to receive the source file by changing the variable "servers":
change from:
  servers=`cat  myservers_list.txt`
to:
  servers=`cat $1`

in this case you should specify the servers source file after the script name, e.g.: ./GetServerOS.sh myservers_list.txt

Sample files:
./GetServerOS.sh (hardcoded to get the server list from "myservers_list.txt" file)
./myservers_list.txt (source servers file to be processed)
./servers_version.txt (resulting file)
