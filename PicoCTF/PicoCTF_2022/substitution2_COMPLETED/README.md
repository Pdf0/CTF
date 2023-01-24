## <p style="text-align: center;">substitution2</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/107/message.txt
</li>
<br/>
    <li>
    
Here we have another [substitution cypher](https://www.geeksforgeeks.org/substitution-cipher/) ctf. If you haven't done one yet I recomend you starting with "substitution0" first and follow the mini-series.
</li>
<br/>
    <li>

To crack this text we can use a [frequency attack](https://www.geeksforgeeks.org/program-to-perform-a-letter-frequency-attack-on-a-monoalphabetic-substitution-cipher/). I used this [website](https://www.dcode.fr/monoalphabetic-substitution) to automatically solve the cypher and get the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    PICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
</details>