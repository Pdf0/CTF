## <p style="text-align: center;">Enhance!</p>

<ol>
    <li>
    I tried exiftool to look into the metadata, hexeditor to see it's binaries... Nothing
</li>
<br/>
    <li>
    Since it's an SVG, we can easily open it in our editor and see what's inside. If we search for curly brackets, we see that the flag is split into two:

```svg
id="tspan3764">F { 3 n h 4 n </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.11588"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
```
</li>
<br/>
    <li>
    If we copy those two fragments and add PicoCTF on the start, we get the flag.
</li>
</ol>
<br/>

<details>
    <summary> Flag </summary>
    
    picoCTF{3nh4nc3d_aab729dd}
</details>
