First create a file named "control_file.txt" with the proper content and run the command line:
  sort -u -k1,1 control_file.txt >  /tmp/output_1.txt

an script can be created with this code and in order to receive file name to be processed as a parameter just change the command in the script as following:
  sort -u -k1,1 $1 >  /tmp/output_1.txt

as an example, considering the script name is "excludedup.sh", you should specify the source file after the script name, e.g.: ./excludedup.sh control_file.txt


sample files:
./excludedup.sh (script sample hardcoded to process file control_file.txt)
./control_file.txt (file to be processed)
./tmp/output_1.txt (resulting file)
