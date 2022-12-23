## <p style="text-align: center;">GDB Test Drive</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/115/gdbme
</li>
<br/>
    <li>
    Now we just need to follow the instructions given by the enunciation

    $ chmod +x gdbme

    $ gdb gdbme

    (gdb) layout asm

    (gdb) break *(main+99)
</li>
And you get the flag
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{d3bugg3r_dr1v3_197c378a}
</details>