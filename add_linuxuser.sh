#!/bin/bash
echo Введите логин пользователя
read user
if grep $user /etc/passwd
then
echo "Такой пользователь существует"
else
    while true; do
        read -p "Хотите ли создать нового пользователя?" yn
        case $yn in
            [Yy]* ) pass=$(pwgen 10 -1)
            sudo useradd -m -g users -s /bin/bash $user ; echo $user:$pass | chpasswd; 
                echo $user >> $user.txt
                echo $pass >> $user.txt
                echo Вы создали пользователя, его имя и пароль указаны в файле "$user" по адрессу: \n /home/hall-pc/userfolderid/; 
                mv $user.txt /home/hall-pc/userfolderid/; break;;
            [Nn]* ) echo Вы не создали пользователя; exit;;
            * ) echo "Ответьте yes или no";;
        esac
    done    
        while true; do
           read -p "Хотите ли вы дать пользователю $user sudo права?" yn
           case $yn in
               [Yy]* ) sudo usermod -aG sudo $user;
               echo Вы дали пользователю $user sudo права; break;;
               [Nn]* ) 
               echo Вы не дали пользователю $user sudo права; exit;;
                * ) echo "Ответьте yes или no";;
           esac
        done   
fi

