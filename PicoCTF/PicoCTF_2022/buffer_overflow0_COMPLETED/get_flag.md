<ol>
    <li>
    We get "vuln.c" and "vuln"
    
    $ wget https://artifacts.picoctf.net/c/520/vuln; wget https://artifacts.picoctf.net/c/520/vuln.c
</li>
<br/>
    <li>
    We connect to the program

    $ nc saturn.picoctf.net 53935
</li>
<br/>
    <li>
    From inspecting vuln.c file, we can see that the array buf2 has a length of 16 characters, but the input that is being copied to buf2 has a max length of 100 characters, and since we are using strcpy to copy, we can cause a seg fault by typing an input longer than buf2's length
</li>
<br/>
</ol>

<details>
    <summary> Flag </summary>
    
    picoCTF{ov3rfl0ws_ar3nt_that_bad_a065d5d9}
</details>
