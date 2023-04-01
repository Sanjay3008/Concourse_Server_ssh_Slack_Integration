print("########################## Running Test FIle in server - Dynamic Inventory ##############")

from subprocess import check_output, STDOUT
cmd = "mkdir Dynamic_Folder"
cmd1 = "echo \"Text_Content\" >> ./Dynamic_Folder/test.txt"
check_output(cmd, shell=True, stderr=STDOUT, universal_newlines=True)
check_output(cmd1, shell=True, stderr=STDOUT, universal_newlines=True)

print("########################## End Folder ##############################")
