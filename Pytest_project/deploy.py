from sshcheckers import ssh_checkout, upload_files


def deploy():
    res = []
    upload_files("192.168.0.109", "vboxuser", "alex5883", "tests/p7zip-full.deb", "/home/vboxuser/p7zip-full.deb")
    res.append(ssh_checkout("192.168.0.109", "vboxuser", "alex5883", "echo 'alex5883' | sudo -S dpkg -i /home/vboxuser/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("192.168.0.109", "vboxuser", "alex5883", "echo 'alex5883' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installe"))
    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
