from sshcheckers import ssh_checkout, upload_files


def deploy():
    res = []
    upload_files("xxx.xxx.x.xxx", "nameuser", "xxxxxxxx", "tests/p7zip-full.deb", "/home/nameuser/p7zip-full.deb")
    res.append(ssh_checkout("xxx.xxx.x.xxx", "nameuser", "xxxxxxxx", "echo 'xxxxxxxx' | sudo -S dpkg -i /home/nameuser/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("xxx.xxx.x.xxx", "nameuser", "xxxxxxxx", "echo 'xxxxxxxx' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installe"))
    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
