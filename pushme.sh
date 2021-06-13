#!/bin/bash
a=`whoami`
echo $a
if [ "$a" != "root" ]; then 
    echo "Start this script from root privilages"
    exit 1
fi
echo $0
#cd /tmp
/usr/bin/apt -y install virtualenv mysql-server xcb
/usr/bin/apt -y install --reinstall libxcb-xinerama0
/usr/bin/wget --content-disposition https://github.com/killreal101/project_download/blob/main/myProject.tar?raw=true
/usr/bin/tar zxvf myProject.tar
/usr/bin/rm myProject.tar
/usr/bin/chmod -R 777 myProject


/usr/bin/virtualenv myProject/Scripts/env
source myProject/Scripts/env/bin/activate
pip install -r myProject/Scripts/requirements.txt
/usr/bin/chmod -R 777 myProject
/usr/bin/mysql -e "CREATE DATABASE IF NOT EXISTS MoES DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; CREATE USER IF NOT EXISTS 'kairos'@'localhost' IDENTIFIED BY '1'; GRANT ALL PRIVILEGES ON * . * TO 'kairos'@'localhost'; FLUSH PRIVILEGES;"
deactivate
cd myProject
p=`pwd`
echo "Please run $p/OpenApp.sh"

