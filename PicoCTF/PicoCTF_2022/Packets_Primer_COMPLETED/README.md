## <p style="text-align: center;">morse-code</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/199/network-dump.flag.pcap
</li>
</br>
    <li>
    We can do this one in many ways, but I'll show you two of them
</li>
</br>
    <li>
    The first one is using Wireshark for analyzing the packet capture file, you can see the flag if you follow the TCP stream.
</li>
    <li>
    The second and quickest one is to use "strings" to find the flag:

    $ strings "network-dump.flag.pcap" | grep "p i c o" | tr -d " "

Let me explain the commands:
* ```strings "network-dump.flag.pcap"``` - prints readable contents of the file
* ```grep "p i c o"``` - searches for lines containing the word "p i c o"
* ```tr -d " "``` - deletes every space
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{p4ck37_5h4rk_ceccaa7f}
</details>