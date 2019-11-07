# Is it alive?

## Deskripsi

p p p p p p p p ping!

[http://52.74.189.105:20006/](http://52.74.189.105:20006/)

author: ariqbasyar

## File(s)

## Hint

<details> 
    <summary>Hint 1</summary>
    <p>rce</p>
</details>

<details> 
    <summary>Hint 2</summary>
    <p>one-liner bash<br>bash injection</p>
</details>

## Solusi

Diberikan website dengan tampilan sebagai berikut.

![alive](img/alive1.png)

Pertama saya coba masukkan `google.com` untuk mengetahui output. Hasil output
terlihat seperti hasil fungsi output di bash.

![alive](img/alive2.png)

![alive](img/alive3.png)

Kemudian saya menduga bahwa input akan dieksekusi di bash dengan format
`ping <input>`. Saya mencoba memasukkan `google.com; ls` dan berharap bisa
mengeluarkan list file yang ada.

![alive](img/alive4.png)

![alive](img/alive5.png)

Terlihat ada list file yang ada dalam file tersebut. Lalu saya masukkan
`google.com; cat secret_file_b9ca6a11a5`.

![alive](img/alive6.png)

![alive](img/alive7.png)

## Flag

`PRCTF{yeah_you_found_a_remote_code_execution_eAFnTxltlW}`
