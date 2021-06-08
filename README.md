# radiotops
Little program for radio tops scheduling

Radio Stations normally use hardware radio top equipment to play well known radio tops at every hour (or anything in between). 
This project uses the combination of a RaspberryPi (in the sake of cheapness) + a little Python script to trigger tops at a cutom schedule. The Pi has to be very in sync with a reliable NTP server. 

You could use any other hardware platform, maybe you would have to adapt the script.

The best is to run it through a process manager to make sure that the script will run in the event of a reboot or a crash. I use PM2 (https://github.com/Unitech/pm2)

PM2 has an internal Pyhton interpreter so you can run the script with:

```bash
$ pm2 start tops.py
```

After that you can check if its running with:

```bash
$ pm2 list
```

And if everything is ok, you save that task so it restarts automatically after reboot with:

```bash
$ pm2 save
```

You can stop it with:

```bash
$ pm2 stop tops
```

You can delete it from PM2 with:

```bash
$ pm2 delete tops
```

The logs are at:

```bash
$ pm2 logs
```

TODOs:

- [ ] A GUI (Tkinter) or a webGUI to control scheduling but not really sure it's worthy, since initial schedullings barely ever change
