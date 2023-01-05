## <p style="text-align: center;">rail-fence</p>

<ol>
    <li>
    We download "message.txt"

    $ wget https://en.wikipedia.org/wiki/Rail_fence_cipher
</li>
<br/>
    <li>

We know we are in front of a rail-fence cypher with 4 rails (more on that [here](https://en.wikipedia.org/wiki/Rail_fence_cipher)), so we can decrypt it online or using a python script like the one I found on Github (```decryptor.py``` in this directory) and we get the flag.
</li>
    <li>
    
    $ python3 decryptor.py
    > Encrypted message: Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6
    > Decrypted message: The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}
</details>
