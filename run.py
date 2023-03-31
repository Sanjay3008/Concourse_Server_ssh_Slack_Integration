print("########################## Running Test FIle in server ##############")

from subprocess import check_output, STDOUT
cmd = "mkdir Testing_Folder"
cmd1 = "echo "Text_Content" >> ./Testing_Folder"
check_output(cmd, shell=True, stderr=STDOUT, universal_newlines=True)
check_output(cmd1, shell=True, stderr=STDOUT, universal_newlines=True)

print("########################## End Folder ##############################")
