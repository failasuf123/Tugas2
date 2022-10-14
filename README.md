Link Heroku : https://mytugas2pbpkatalog.herokuapp.com/mywatchlist/html/

1. Perbedaan Asyncrhonous dan Sycncrhonous programming
    Syncrhonous programming akan menjalankan program secara sequential artinya program akan dieksekusi satu persatu berdasarkan antrian request, kemudian apabila user melakukan request, laman akan refresh terlebih dahulu untuk memperbarui data.

    Asyncrhonous programming akan memberkan user melakukan request dan tetap dapat berinteraksi dengan laman tanpa harus dilakukan refresh page, dengan kata lain Asyncrhonous dapat melakukan pekerjaan tanpa terikat dengan proses lain

2. Penerapan Asynchonous programming pada ajax
    Ajax merupakan sebuah platform berbasis java script dan xml dimana akan memberikan sistem asynchronous pada web. Dimana cara kerjanya browser akan memanggil JavaScript yang akan mengaktifkan XMLHttprRequst. Pada web browser akan mengirimkan request ke http server, kemudian server akan menerima dan mengirimkan data kembali ke web browser dan web browsermenerima data tanpa harus melakukan proses relode terlebih dahulu.
3. Saya membuat view baru yang mengembalikan data task dalam bentuk json data tersebut akan menampilkan json pada path /todolist/json, saya juga mengembalikan data task tersebut pada halaman todolist, saya membuat show_json pada views.py untuk menampilkan data json pada path tersebut, saya juga membuat fungsi ajax_mode yang menampilkan data dari task yang ada pada class Task yang diimport dari models.

Pada file HTML saya mengambil button trigger modal dari bootstrap yanng didalamnya terdapat form untuk membuat judul dengan tampilan yang singkronus pada.


<<<<<<< HEAD

=======
>>>>>>> a0a791bc1c39e481b5b83c5ff189ad99872f1aba
