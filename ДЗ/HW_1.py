import subprocess
import string

def test_1(cmd,text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode ==0:
        return True
    else:
        return False

if __name__ == '__mane__':
    print(test_1('cat /etc/os-release', 'UBUNTU_CODENAME=JAMMY'))


# ________________________________________2____________________________________

def test_2(cmd,text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,encoding='utf-8')
    for i in string.punctuation:
        s = result.stdout.replace(i, "")
        listout = s.split()
        print(listout)
        if text in listout and result.returncode == 0:
            return True
        else:
            return False


if __name__ == '__mane__':
    print(test_1('cat /etc/os-release', 'UBUNTU_CODENAME=jammy'))
    print(test_1('cat /etc/os-release', 'UBUNTU_CODENAME=Sunny'))
    print(test_1('cat /etc/os-release', 'LTS'))
    print(test_1('cat /etc/os-release', 'jammy'))
