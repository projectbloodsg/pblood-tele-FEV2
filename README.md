# pblood-tele-FEV2
in the event of a reconfiguring:

setup a psql server first
set up the backend
set up telebot/FE independently. 

service for telebot is set up @ /etc/systemd/system/telebot.service. Configure that file to let it run, and remember to include ENVIRONMENT as a variable. else it doenst know where to get packages from. 
