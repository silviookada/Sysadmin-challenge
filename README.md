# Sysadmin-challenge
Sysadmin challenge

8.Using bash write a script to get OS version from multiple Linux servers

        Premisses:
        The script must receive an argument to process, which is the file name (myservers_list.txt);
        You will use 'ssh' command to connect into different servers using 'myuser' as the username ;

        The result should be writted in the file 'servers_version.txt' using the format bellow:
        date (hh:mm:ss mm/dd/yy)    <server name>      <server ip>    <server version> 

        E.g:
        18:53:44 12/10/21    webserver001   192.168.80.5   Linux (none) 2.6.34.14 ##44 Tue Oct 15 20:50:15 CEST 2013 i686 GNU/Linux

9.Using bash write a script to find and remove duplicated fake IP addresses lines of "control_file.txt" file and save the output at /tmp/output_1.txt

        Premisses:
        The script must receive an argument to process, which is the file name (control_file.txt);
        Find duplicated fake IP addresses and keep just the first one. All other duplicated IP addresses must be removed;

        E.g:
        Using the lines below as example, the second one must be deleted:
        540.300.759.124   lnx02csv lnx02csv.02csv.sps     pid=1  ia1=y domain=02csv        myid=2  wsm=PR wid=1 wst=NA,HI,CP,SC,DS # ADM 
        540.300.759.124   lnx02csv lnx02csv.02csv.sps     pid=1  ia1=y domain=02csv        myid=3  wsm=PR wid=1 wst=NA,HI,CP,SC,DS # ADM 

        The final expected result is:
        540.300.759.124   lnx02csv lnx02csv.02csv.sps     pid=1  ia1=y domain=02csv        myid=2  wsm=PR wid=1 wst=NA,HI,CP,SC,DS # ADM

        All comment lines must be kept on the final output file.

10.Using Perl or Python write a script to indent the output file of the bash script (/tmp/output_1.txt) with 3 spaces between the columns except for the first and second columns which are IP address and hostname. For those you must use as much spaces as needed. The result must be saved at /tmp/output_2.txt.

        Premisses:
        No tabs allowed;
        All comment lines must be kept on the final output file as well.

        E.g:
        After processing the final result must be:

        #This is a comment and I need to be on the final file result! :) 
        a.b.c.d                 eeeeeeee   ffffffff.ggggg.hhh   iii=A   jjj=k   llllll=BBmmm   nnnn=CC   ooo=pp   rrr=D   sss=tt,tt,tt,tt,tt,tt   #yyy
        aa.bb.cc.dd         eeeeeeee   ffffffff.ggggg.hhh   iii=A   jjj=k   llllll=BBmmm   nnnn=CC   ooo=pp   rrr=D   sss=tt,tt,tt,tt,tt,tt   #yyy
        aaa.bbb.ccc.ddd   eeeeeeee   ffffffff.ggggg.hhh   iii=A   jjj=k   llllll=BBmmm   nnnn=CC   ooo=pp   rrr=D   sss=tt,tt,tt,tt,tt,tt   #yyy
