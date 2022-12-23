## <p style="text-align: center;">file-run2</p>
<ol>
    <li>
    This one is another simple CTF pretty similar to "file-run1"
</li>
<br/>
    <li>
    We get "run"

    $ wget https://artifacts.picoctf.net/c/351/run
</li>
<br/>
    <li>
    Firstly we need to change the file permissions

    $ chmod +x run; ./run (This way the "run" permissions will change)
</li>
<br/>
    <li>
    In order for the program to execute we need to give it an argument, wich is given to us previously, and we get the flag

    $./run Hello!
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{F1r57_4rgum3n7_be0714da}
</details>