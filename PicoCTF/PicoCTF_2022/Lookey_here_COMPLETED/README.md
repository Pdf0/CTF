## <p style="text-align: center;">Lookey here</p>

<ol>
    <li>
    It seems that what we need to do in this ctf is to find the flag in a massive file full of text.
</li>
<br/>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/294/anthem.flag.txt
</li>
<br/>
    <li>
    We can easily search for the flag using grep

    $  grep -iE picoctf{.*} anthem.flag.txt
</li>

A quick resume about the command:
- ``-i`` - assumes everything in text is lowercase 
- ``-E`` - allows the use of Extended Regex
- ``picoctf{.*}`` - searches for the pattern picoctf{} with anything inside the curly braces ("." representes anything and "*" represents anytimes)
- ``anthem.flag.txt`` - where to search in

</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{gr3p_15_@w3s0m3_4c479940}
</details>
