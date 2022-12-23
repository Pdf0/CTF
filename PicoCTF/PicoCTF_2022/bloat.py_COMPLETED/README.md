## <p style="text-align: center;">bloat.py</p>

<ol>
    <li>
    We get "bloat.flag.py" and "flag.txt.enc"

    $ wget https://artifacts.picoctf.net/c/428/bloat.flag.py; wget https://artifacts.picoctf.net/c/428/flag.txt.enc
</li>
<br/>

  <li>While examining "bloat.flag.py" code, when can see that the password can be obtained in the "arg133" function: 
    
</li>


```python
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    ...
```
<br/>
<li> We can take the "a" alphabet and get the characters from those indexes to get secret password.</li>
<br/>
<li>I wrote this Python script to help me get the the flag:</li>

```python
import os

a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

password = a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]

os.system(f"echo {password} | python3 bloat.flag.py")
```

</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{d30bfu5c4710n_f7w_b8062eec}
</details>