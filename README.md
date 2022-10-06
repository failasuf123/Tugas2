Link Heroku : https://mytugas2pbpkatalog.herokuapp.com/mywatchlist/html/

1. Perbedaan Inline, Internal, dan External CSS, 
- Inline CSS
    Yaitu melakukan styling pada tag yang ada pada html, untuk membuatnya hanya perlu mengakses style= "..."
    - Kelebihanya
        Untuk styling pada perubahan kecil (satu/dua buah styling) cukup mudah, selain itu kita bisa langsung mengethui tag/bagian mana yang sedang kita styling.
        Selain itu HTTP request relatif lebih kecil
    - Kekuranganya
        Untuk styling dengan jumlah besar akan menghilangkan estetika kode html yang menyebabkan terkesan berantakan
        karena di terapkan pada tiap-tiap tag yang akan di lakukan styling
- Internal CSS
  Yaitu melakukan styling pada berkas yang sama dengan html, dengan, Internal CSS dilakukan di style tag yang ada di head tag.
  - Kelelebihan
    Kita tidak perlu membuka file css untuk melakukan styling hanya perlu di file html, selain itu styling telah terpisah dengan file html sehingga akan menjaga estetika dan kerapihan kode, pada internal css telah tersedua class dan id yang dapat digunakan untuk berbagai tag html
  - Kekurangan
    Perubahan pada internal css hanya terjadi pada halaman css tersebut tidak bisa digunakan pada multiple html file. Untuk kode yang kompleks dan panjang akan menyulitkan karena harus berulang kali scroliing.
- Eksternal CSS
    Yaitu melakukan styiling pada file css terpisah, kita dapat menghubungkan file tersebut menggunakan link, untuk pemrograman pada django pada link tersebut ditambahkan tag django yang menghubungkan pada file css tersebut, file css akan disimpan pada folder static
    - Kelebihan
    Kita dapat membuat satu file css untuk banyak file html sehingga menghindari duplikasi code. selain itu file html menjadi lebih rapi dan terfokus pada kerangka applikasi
    - Kekurangan
    File css yang diletakan di file berbeda juga terdapat kekuranganya yaitu akan susah untuk mengoreksi karena berulang kali mengecek file css dan html

2. Apa itu HTML5?
HTML5 merupakan sebuah markup language yang berfungsi untuk membuat kerangka dari aplikasi webstie yang merupakan hasil penyempurnaan dari HTML, HTML5 memiliki eror handling dan sintax yang lebih sederhana

3. Selector
    - Tag
    Berfungsi untuk mengubah kode yang merujuk pada tag yang ada pada file html , inisalisasinya pada file css hanya tag nya saja tidak usah menggunkan titik contoh div{}
    - Class
    Berfungsi untuk merubah kode susuai dengan classnya, kita dapat menginisalisasikan class pada file html, ketika class di css kita styling maka seluruh class yang ada di html ikut berubah, biasanya class dilakukan pada tipe tag html yang sama
    - ID
    Sama seperti tag namun bersifat khusus untuk satu elemen cara menginialisasi di css menggunakan pagar #
    - Universal
    Kita dapat melakukan styling pada seluruh file html menggunkan ini, biasanya untuk membuat styling default html, kita bisa menginisialisasinya mnenggunakan *{}
    - Pseudo
    Kita dapat merubah styling ketika user melakukan sesuatu menggunakan pseudo contohnya hover, active
    - Atribut
    melakukan styling berdasarkan atribut yang ada pada file html tersebut.
4. Implementasi Checklist
    - Pertama saya memulai merombak kerangka html sesuai kode yang saya inginkan, saya membuat kerangak menggunakan doctype, pada atas kode saya tambahkan django tag {% load static %}
    - Saya melakukan perombakan kode dan mengimplementasikan kode html pada tag body, pada tag head saya mengimport text font 'Ubuntu' dari google dan tag style utunk styling css
    - Kasus ini saya memilih mnggunakann Internal CSS karena code yang dibuat relatif singkat, saya membuat nya dengan melakukan tag style pada head 
    - Kemudian saya kembali lagi pada html dengan menambahkan class dari tag yang dibutuhkan untuk melakukan styling
    - Saya juga membuat folder image pada folder static yang digunakan paad todolist.html, image tersebut berisi icon dan gambar
    - Saya melakukan inisiasi gambar tersebut menggunakan src="" dengan tag django
    - Kemudian saya menghias file html yang saya buat sesuai class dan tag pada file css, saya juga melakukan inisiasi default pada css untuk font, margin, dan padding
    - Saya menerapkan flex dengan cara pada selector ditulis display:"flex", saya juga melakukan flex-direction , yang sebagian besar saya memilih coloum, hal tersbtu berfungsi untuk mendukung website yang responsive
    - Saya juga melakukan hover pada class div yang saya inginkan
    - Untul logout dan add new task pada file html todolist saya merubah buttonya menjadi icon yang lebih menarik dan melakukan hover pada icon tersebut





<<<<<<< HEAD

=======
>>>>>>> a0a791bc1c39e481b5b83c5ff189ad99872f1aba
