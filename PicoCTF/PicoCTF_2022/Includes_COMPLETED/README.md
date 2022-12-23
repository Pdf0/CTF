## <p style="text-align: center;">Includes</p>

<ol>
    <li>
    We go to the website

    http://saturn.picoctf.net:54634
and when we click the button "Say hello" we get this nice pop-up

![Alt text](https://i.imgur.com/2TjxKDO.png "screenshot")
</li>
<br/>
    <li>
    If we inspect the page source (Ctrl + u), we can see that it uses a javascript script named "script.js" wich is possibly the one responsible for the pop-up. If we check what's inside, we come across of what it looks like half of the flag

```js
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_df589022}
```
</li>
<br/>
    <li>
    We are still missing the first half, wich with a bit of more digging we can find in the "style.css" file

```css
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```
</li>
<br/>
    <li>
    Now you just need to put the two together and you get the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}
</details>