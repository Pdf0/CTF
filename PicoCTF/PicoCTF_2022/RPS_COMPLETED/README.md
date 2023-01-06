## <p style="text-align: center;">RPS</p>

<ol>
    <li>
    We get the file

    $ wget https://artifacts.picoctf.net/c/442/game-redacted.c
</li>
<br/>
    <li>
    We know our objective: Beat the program at rock, paper, scissors 5 times in a row. It's very unlikely you can do this just by guessing, so we need to analyse "game-redacted.c" to see if we can exploit it.
</li>
<br/>
    <li>
    
The computer randomly chooses a number between 0 and 2. Then it goes to the array ```hands[]```, gets the option it's going to play based on the random number and the option that counters it on ```loses[]``` array. It then sees if the option we wrote is the same as the one it picked from ```loses[]```.
</li>
<br/>
    <li>
    The way it compares is where the weird thing happens:

```py
100  if (strstr(player_turn, loses[computer_turn])) {
101    puts("You win! Play again?");
102    return true;
```

We see that the program uses ```strstr(str1, str2)``` to compare the strings. This funtion sees if str2 is in str, if it is it returns a pointer, if not it returns NULL. Well, if it only sees if the correct answer is in ```str1```, we can give all the three answers as the input, so they all are inside ```str1```
</li>
<br/>
    <li>
    So, if we always give "rockpaperscissors" as input, we always win.
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{50M3_3X7R3M3_1UCK_58F0F41B}
</details>