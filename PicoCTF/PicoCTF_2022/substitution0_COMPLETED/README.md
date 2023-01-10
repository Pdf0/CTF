## <p style="text-align: center;">substitution0</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/379/message.txt
</li>
<br/>
    <li>
    
We need to crack a [substitution cypher](https://www.geeksforgeeks.org/substitution-cipher/). Luckily we are given the alphabet at the beginning of the file, so we can easily crack it in an [online decoder](https://www.dcode.fr/monoalphabetic-substitution).
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}
</details>