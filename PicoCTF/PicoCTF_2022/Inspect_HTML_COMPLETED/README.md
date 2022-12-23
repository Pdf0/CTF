## <p style="text-align: center;">Inspect HTML</p>
<ol>
    <li>
    This is an easy one, just to get you started in this category.
    Go to the website

    http://saturn.picoctf.net:50920
</li>
<br/>
    <li>
    If we inspect the page source (Ctrl + u) we can find the flag in a commentary (line 20)

```html
...
19      <p> Source: Wikipedia on Histiaeus </p>
20      <!--picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}-->
21  </body>
22</html>
```
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}
</details>