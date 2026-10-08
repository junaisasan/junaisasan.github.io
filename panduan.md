# Panduan Deploy Hugo ke GitHub Pages

Proyek ini dibangun menggunakan framework **Hugo**. Cara terbaik dan direkomendasikan untuk men-deploy (mempublikasikan) proyek Hugo ke GitHub Pages adalah dengan menggunakan **GitHub Actions**. 

Berikut adalah langkah-langkah yang jelas untuk mendeploy website ini:

## Langkah 1: Siapkan Konfigurasi `baseURL`
Pastikan URL situs Anda sudah benar. Pada file `hugo.toml`, pastikan `baseURL` sudah mengarah ke domain GitHub Pages Anda:
```toml
baseURL = "https://gerador-de-cpf.github.io/"
```
*(Saat ini pengaturan di proyek Anda sudah disetel dengan benar)*

## Langkah 2: Gunakan GitHub Actions (Sudah Disiapkan)
Untuk membangun dan mempublikasikan situs Anda secara otomatis setiap kali ada pembaruan kode, Anda memerlukan file konfigurasi Workflow GitHub Actions.
Saya telah membuatkan file konfigurasi ini untuk Anda di: `.github/workflows/hugo.yml`.

File ini akan secara otomatis memberikan perintah ke server GitHub untuk menginstal Hugo, melakukan proses build, dan mendeploy hasilnya ke GitHub Pages setiap kali Anda melakukan `push` ke branch `main` atau `master`.

## Langkah 3: Push Kode ke Repositori GitHub
Jika Anda memiliki pembaruan kode dan belum mem-push ke GitHub, buka terminal, arahkan ke folder proyek Anda, dan jalankan perintah berikut:

```bash
git add .
git commit -m "Siapkan deployment untuk GitHub Pages"

# Push kode ke GitHub (ubah 'main' menjadi 'master' jika branch utama Anda adalah master)
git push -u origin main
```

## Langkah 4: Konfigurasi GitHub Pages di Repository
Setelah kode di-push ke GitHub, Anda perlu memberi tahu GitHub untuk menggunakan GitHub Actions sebagai sumber website (source) untuk GitHub Pages Anda.

1. Buka halaman repositori GitHub Anda di browser (yaitu halaman `gerador-de-cpf.github.io`).
2. Klik tab **"Settings"** (Pengaturan).
3. Di menu sebelah kiri, cari dan klik opsi **"Pages"**.
4. Pada bagian **"Build and deployment"**:
   - Untuk opsi **Source**, ubah dari opsi default menjadi **"GitHub Actions"**.
5. Setelah Anda mengubahnya, GitHub secara otomatis akan mendeteksi file konfigurasi yang telah saya buat dan memulai alur kerja (workflow) untuk mempublikasikan website.

## Langkah 5: Pantau Proses Deployment
1. Di repositori GitHub Anda, klik tab **"Actions"**.
2. Anda akan melihat proses (workflow) dengan nama `Deploy Hugo site to Pages` sedang berjalan (biasanya akan berwarna oranye, kemudian hijau jika berhasil).
3. Tunggu beberapa detik/menit hingga proses tersebut selesai.
4. Selesai! Website Anda sekarang sudah dapat diakses dan tayang di `https://gerador-de-cpf.github.io/`.

## Bagaimana Cara Memperbarui Website di Masa Depan?
Setelah deployment awal sukses, pengaturan ini sudah otomatis. Anda hanya perlu membuat perubahan pada file lokal Anda (misalnya membuat postingan/artikel baru, mengedit layout, dll), lalu commit dan push ke GitHub seperti biasa:

```bash
git add .
git commit -m "Update konten website"
git push
```
GitHub Actions secara otomatis akan mendeteksi perubahan tersebut, membangun ulang website Anda, dan menayangkannya dalam beberapa menit.
