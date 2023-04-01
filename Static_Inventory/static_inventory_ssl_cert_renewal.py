print("This is Static inventory Python File")

print("########################## Running Test FIle in server ##############")

from subprocess import check_output, STDOUT
cmd = "mkdir Static_Folder"
cmd1 = "echo \"Static_Inventory\" >> ./Testing_Folder/test.txt"
check_output(cmd, shell=True, stderr=STDOUT, universal_newlines=True)
check_output(cmd1, shell=True, stderr=STDOUT, universal_newlines=True)

print("########################## End Folder ##############################")
