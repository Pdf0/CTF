## <p style="text-align: center;">Sleuthkit Intro</p>

<ol>
    <li>
    We get the image file

    $ wget https://artifacts.picoctf.net/c/114/disk.img.gz
</li>
<br/>
    <li>

We need to get the Linux partition size inside the downloaded image using ```mmls```

    $ mmls disk.img

```bash 
> DOS Partition Table
  Offset Sector: 0
  Units are in 512-byte sectors
      Slot      Start        End          Length       Description
  000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
  001:  -------   0000000000   0000002047   0000002048   Unallocated
  002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
</li>
<br/>
    <li>
    If we connect to the given server and enter the Linux partition size (202752), we get the flag
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{mm15_f7w!}
</details>