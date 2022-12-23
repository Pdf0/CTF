## <p style="text-align: center;">File types</p>

<ol>
    <li>
    We get "flag.pdf"

    $ wget https://artifacts.picoctf.net/c/323/Flag.pdf
</li>
    <li>
    The file appears to be a pdf, but if we check wich type of yle it is using the command "file flag.pdf", it's says it is a "shell archive text", wich we can extract just by executing it

    $ chmod +x Flag.pdf; sh Flag.pdf
</li>
    <li>
    For now on you will need to unzip every file until you reach an ASCII text, wich we can see it's in hexadecimal. If we convert it from hex, we get the flag. 
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
</details>