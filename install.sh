#!/bin/sh

sudo apt update;
sudo apt dist-upgrade -y;
sudo apt autoclean -y;
sudo apt autoremove -y;
sudo apt install -y python3-pygame;

if [ ! -f /etc/systemd/system/photoframepygame.service ]; then
    sudo cp /usr/share/photo-frame-pygame/photo-frame-pygame/photoframepygame.service /etc/systemd/system/photoframepygame.service;
    sudo chown root:root /etc/systemd/system/photoframepygame.service;
    sudo chmod 644 /etc/systemd/system/photoframepygame.service;
    sudo systemctl daemon-reload;
    sudo systemctl enable photoframepygame.service;
fi

if [ ! -d /usr/share/photo-frame-pygame/photo-frame-pygame ]; then
    cd /usr/share/photo-frame-pygame;
    git clone http://github.com/cjsmocjsmo/photo-frame-pygame.git;
    cd;
else
    cd /usr/share/photo-frame-pygame/photo-frame-pygame;
    git pull;
    cd;
fi

sudo systemctl start photoframepygame.service;
 