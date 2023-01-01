## <p style="text-align: center;">patchme.py</p>

<ol>
    <li>
    We get the files

    $ wget https://artifacts.picoctf.net/c/386/patchme.flag.py; wget https://artifacts.picoctf.net/c/386/flag.txt.enc
</li>
<br/>
    <li>
    When we execute "pathme.flag.py" we need to give a password, wich we don't know, and when the wrong password is given the program exits
</li>
<br/>
    <li>
    Giving a look at the "pathcme.flag.py" code, we can clearly see what the flag is by looking at these few lines:

```py
19    if( user_pw == "ak98" + \
20                "-=90" + \
21                "adfjhgj321" + \
22                "sleuth9000"):
23        print("Welcome back... your flag, user:")
24        decryption = str_xor(flag_enc.decode(), "utilitarian")
25        print(decryption)
```
</li>
<br/>
    <li>
    Lastly we just need to put together those four password framents and the program gives us the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
</details>