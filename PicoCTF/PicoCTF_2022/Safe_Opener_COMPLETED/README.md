## <p style="text-align: center;">RPS</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/463/SafeOpener.java

</li>
<br/>
    <li>

By analyzing "SafeOpener.java" we can see that ```encoder``` is a Base64 encoder, and we can also see what the encoded password is

```java
...
6   Base64.Encoder encoder = Base64.getEncoder();
...
31  String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
...
```

 Since we have the password in Base64, we can decode it online, and there we go, we get the password. Now just wrap it up between picoCTF{} and you have the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
</details>