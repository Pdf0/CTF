## <p style="text-align: center;">Great Snake</p>

<ol>
    <li>
    We get the file

    $ wget https://cryptohack.org/static/challenges/telnetlib_example_dbc6ff5dc4dcfac568d7978a801d3ead.py
</li>
    <li>
    By inspecting the python file, we can see that it connects to their socket and sends the following json:

```py
30  request = {
31      "buy": "clothes"
32  }
33  json_send(request)
```
They say we need to send a json object with the key "buy" and the value "flag", but the one on the python cript has "clothes" as their value, so, if we change that to "flag" and execute the script, we get the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    crypto{sh0pp1ng_f0r_fl4g5}
</details>
