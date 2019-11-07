# Only Admin 2

## Deskripsi

let's see that you can get the admin privileges (2)

[http://52.74.189.105:20002/](http://52.74.189.105:20002/)

author: ariqbasyar

## File(s)

## Hint

<details> 
    <summary>Hint 1</summary>
    <p>base64</p>
</details>

<details> 
    <summary>Hint 2</summary>
    <p>Eyeyeyey</p>
</details>

## Solusi

Diberikan website dengan tampilan berikut.

![admin2](img/admin2-1.png)

Hal yang pertama dilakukan adalah mengecek cookies dengan dev tools.

![admin2](img/admin2-2.png)

Terlihat ada dua cookies dan salah satunya admin. Pertama saya coba mengganti
nilai cookies admin menjadi true lalu refresh.

![admin2](img/admin2-3.png)

Hasilnya malah di-redirect ke link youtube
[https://www.youtube.com/watch?v=UAlIq7BKNxg](https://www.youtube.com/watch?v=UAlIq7BKNxg)

![admin2](img/admin2-4.png)

Lalu saya melihat cookies yang satunya lagi. Terlihat bahwa cookie tersebut
berawalan `ey` yang kemungkinan besar merupakan json yang di encode ke base64.

![admin2](img/admin2-5.png)

Saya lalu menggunakan [base64 decoder](https://www.base64decode.org/).

![admin2](img/admin2-6.png)

Kemudian dengan [base64 encoder](https://www.base64encode.org/) saya ubah json
yang sudah diubah nilai adminnya menjadi true ke base64.

![admin2](img/admin2-7.png)

Kemudian saya ubah cookies is_admin dengan base64 yang baru tersebut.

![admin2](img/admin2-8.png)

## Flag

`PRCTF{congratz_haha_ez_admin_2_73cefa5bb5800}`
