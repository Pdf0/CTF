## <p style="text-align: center;">file-run1</p>

<ol>
    <li>
    We get "run"

    $ wget https://artifacts.picoctf.net/c/308/run
</li>
<br/>
    <li>
    This is a very simple CTF, we just need to change the executable permissions so we can run it. We can do that using

    $ sudo ./run (You'll be able to run the file but the permissions won't change)
    or
    $ chmod +x run; ./run (This way the "run" permissions will change)
</li>
And there is the flag
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
</details>