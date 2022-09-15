
Link file :
https://mytugas2pbpkatalog.herokuapp.com/katalog/


1. 	     >>    URLS   >> 
	User 		         Views <<>> Model <<>> Database
	     << Template <<

	
	Pertama user mengakes website menggunakan url, user akan mendapatkan dua hal yaitu data dan layout.
	data berasal dari data base dan layout berasal dari css,html,javascript.
	
	Urls akan menentukan tampilan yang user inginkan sesuai dengan urlsnya, intinya views merupakan percabangan 
       yang menghubungkan urls, model, dan tamplate. views dapat menentukan apa yang akan di render berdasarkan perintah 
       dari views.

	Apabila views membutuhkan data, maka views akan mengambil data dari model, dimana model akan terhubung dengan database
       yang menyimpan data tertentu 

	Kemudian views akan mengembalikan data melalui tamplate yaitu html, html akan mengembalikan tampilan yang sudah diupdate
       kepada user dengan data yang telah berubah.


2. Virtual Environment akan menciptakan suatu project python yang terisolas
   Dari project lainya. Virtual Environment berfungsi apabila dimasa depan terdapat
   update versi yang menyebabkan code yang kita buat saat ini tidak dapat berfungsi lagi
   maka kita tetap bisa mengaksesnya menggunakan virtual environment
3. - saya memprogram views.py dengan mengimport class CatalogItem dari models di folder katalog
     ,didalam class tertebut terdapat keterangan variabel yang memiliki variabel yang menyimpan data
     dari database json. Saya membuat dictionary context yang berisi inputan kepada file
     katalog.html yang akan di render.
    -Saya memetakan data dari views di katalog.html dengan mengganti fill me dengan {{name}} dan {{npm}}
     tentuya name dan npm sesuai dengan key dari dictionary context yang telah dibuat sebelumnya
     . selain itu saya juga melakukan iterasi dari data yang diambil melelui list_katalog, dan mengiterasikannya
     sehingga seluruh data masuk ke tabel.
    - Saya melakukan depolyment ke internet dengan membuat aplikasi di heroku yang kemudian saya mengikuti
     arahan dari tutorial, dimana pada tutorial tersebut say
