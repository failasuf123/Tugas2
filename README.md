Link Heroku : https://mytugas2pbpkatalog.herokuapp.com/mywatchlist/html/

1. Berfungsi untuk melindungi pengguna dari serangan siber, Penyerang akan mengirim request forgery pada aplikasi user. Sytax {% csrf_token %} akan memastikan bahwa request user bukan request palsu yang dikirim oleh penyerang. serangan ini akan menyerang dari form yang merupakan sebuah input data dari user.

2. Kita dapat memanfaatkan syntax input yang ada pada html, didalam synatax itu terdapat berbagai macam type seperti text (mendisplay satu baris input), radio (untuk membuat radio button), checkbox, submit (untuk mensubmit form), agar secara manual membentuk tampilan seperti {{ form.as_table }} kita hanya membuat syntax table pada form di file html.

3. Pertama user akan menginput data yang ada pada form yang dibuat di html. Kemudian data tersebut diaproses di UserCreationForm yang mengautentikasi data sehingga dapat mengatur cookie. Data yang ada di html akan diisi oleh inputa yang diinput form berdasarkan models dan form.py

4. Pertama kita membuatapp todolist yang kemudian kita registrasi di project_django yang menginisiasi class Task yang ada di models.py, data tersebut berisi dari user, data, date, dan deskripsi, ketiga hal tersebut yang memberikan apa saja data yang akan kita gunakan selanjutnya

pada views.py kita membuat fungsi yang menampilkan fungsi todolist, task, signup, login, logout. todolist akan menampilkkan data dari list dan task adalah membuat data baru yang akan di masukan ke data todolist. kemudaian kita mendaftarkan fungsi tersebut ke urls.py yang ada di folder todolist.

Kita juga membuat file html yang akan menampilkan data-data yang diperlukan user yang ada di folder tamplates

Kita juga akan membuat forms.py yang memiliki class UserCreationForm, fungsi class tersbut untuk mengautentikasi data.

Kita membuat coockies dan memasukanya ke fungsi login, signin, dan delate, coockies tersebut akan manampilakn personalisasi user dangen data-data berdasarkan user tersebut. Kita juga menambahkan reuirements ketika akan mengakses main file todolist, yang digunakan apabila ingin mengakses main file harus maasuk terlebih dahulu
<<<<<<< HEAD

=======
>>>>>>> a0a791bc1c39e481b5b83c5ff189ad99872f1aba
