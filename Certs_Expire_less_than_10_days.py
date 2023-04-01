from datetime import datetime, date
from subprocess import check_output, STDOUT
from subprocess import getoutput

def check_certificate_expiry_less_than_10_days(Hostname):
    cmd = f"curl https://{Hostname} -vI --stderr - | grep \"expire date\""
    print(cmd)
    v = check_output(cmd, shell=True, stderr=STDOUT,
                     universal_newlines=True).rstrip('\n')
    print(v)
    c = v[16::]
    
    ele = c.split(" ")
   
    if "" in ele:
        ele.remove("")
   
    m, d, y = ele[0], ele[1], ele[3]
    expiry_date = y+"-"+m+"-"+d
    print(expiry_date)
    exp = str(datetime.strptime(expiry_date, '%Y-%b-%d'))
    print(exp)
    exp_date = exp.split(" ")
    print(exp_date)
    cur_date = str(datetime.now().date())
    print(cur_date)
    d1 = datetime.strptime(exp_date[0], "%Y-%m-%d")
    d2 = datetime.strptime(cur_date, "%Y-%m-%d")
    difference_days = (d1-d2).days
    print(difference_days)
    if (difference_days <10):
        return True
    else:
        return False

def filter_hosts_that_expire_less_than_10_days():

    host_file = "./hostnames.txt"
    filter_results = "./filtered_hosts.txt"
    with open(host_file,"r") as hostlist, open(filter_results,"w") as filtered:
        for host in hostlist:
            status = check_certificate_expiry_less_than_10_days(host.rstrip("\n"))
            if(status):
                filtered.write(host)



def main():
    filter_hosts_that_expire_less_than_10_days()

main()
