# Gerador de CPF (Hugo)

Situs statis berbasis Hugo untuk https://gerador-de-cpf.github.io/ berisi gerador CPF, konten pilar, dan artikel cluster.

## 1. Persiapan

- Pasang Hugo **extended** (https://gohugo.io/installation/). Cek dengan `hugo version`.
- Jalankan lokal: `hugo server` lalu buka http://localhost:1313
- Build produksi: `hugo --minify` (hasil di folder `public/`, jangan di-commit).

## 2. Struktur folder

```
hugo.toml                 pengaturan situs, menu, ID AdSense
content/
  _index.md               KONTEN PILAR homepage + FAQ
  glossario/              entri glossario (satu file .md per istilah) -> /glossario/
  estatisticas/           hub statistik + 4 halaman spoke -> /estatisticas/
  sobre.md, contato.md, politica-de-privacidade.md
data/estatisticas.yaml    SUMBER TUNGGAL angka statistik (12 baris, lengkap dengan sumber dan tanggal)
scripts/check.py          cek konten: definisi <= 50 kata, 2-3 tautan internal, title <= 55 dan description <= 155 karakter
layouts/
  index.html              susunan homepage (iklan > gerador > iklan > pilar > FAQ)
  _default/               template artikel, halaman, dan daftar artikel
  partials/
    head.html             canonical, meta, schema, font, script AdSense
    resposta.html         kotak jawaban langsung (definicao) + peringatan build jika > 50 kata
    header.html           logo + navbar
    footer.html
    ad.html               slot iklan (dipakai 2x di homepage)
    cpf-tool.html         HTML + JavaScript gerador
assets/css/main.css       seluruh gaya (warna ada di bagian :root)
static/                   robots.txt, ads.txt, favicon.svg (disalin apa adanya)
.github/workflows/hugo.yml  deploy otomatis ke GitHub Pages
```

## 3. Cara mengedit

### Konten pilar dan FAQ
Edit `content/_index.md`.
- Bagian di antara `---` paling atas: `seoTitle` (judul di Google), `description` (deskripsi), dan `faq` (daftar tanya-jawab).
- Setiap FAQ otomatis tampil di halaman **dan** masuk ke schema FAQPage. Format satu item:
  ```
  - q: "Pertanyaan?"
    a: "Jawaban."
  ```
- Isi di bawahnya memakai Markdown (`##` untuk H2, tabel dengan `|`).
- Jaga agar keyword utama (gerador de cpf, cpf valido, dst.) tetap muncul secara wajar, jangan diulang berlebihan.

### Teks dan tampilan gerador
Edit `layouts/partials/cpf-tool.html`.
- Judul, kalimat pengantar, dan catatan "Importante" ada di bagian HTML atas.
- Logika pembuatan CPF ada di blok `<script>` (fungsi `dv` menghitung digit verifikasi, `gen` membuat nomor, tabel `M` memetakan UF ke digit ke-9).

Fitur tambahan di gerador: pilihan **Quantidade** (1-100 CPF tanpa duplikat) dan tombol **Baixar CSV** (muncul hanya jika jumlah > 1). Semua dijalankan di browser; tombol CSV memakai kelas `.ghost` yang sudah ada, jadi tampilan mode 1 CPF tidak berubah.

### Menu (navbar)
Navbar hanya berisi Estatísticas dan Glossário (`[[menus.main]]` di `hugo.toml`). Link Sobre, Contato, dan Privasi ada di footer (`[[menus.footer]]`). `weight` menentukan urutan. Untuk menambah item, salin satu blok dan ubah `name` dan `pageRef` (contoh `pageRef = "/glossario"`).

### Menambah entri glossario
1. Buat `content/glossario/nama-istilah.md` dengan front matter: `title` (istilah, dipakai di indeks A-Z), `pergunta` (H1, mis. "O que é X?"), `description`, `definicao`, `date`, `lastmod`, dan `faq`.
2. `definicao` = jawaban langsung, **maksimal 50 kata**. Tampil di kotak hijau tepat di bawah H1 dan di indeks A-Z. Build memberi peringatan jika lebih dari 50 kata.
3. Isi dengan Markdown, mulai dari H2. Beri **2-3 tautan internal kontekstual** di dalam kalimat (ke entri lain atau ke `/estatisticas/...`).
4. Jalankan `python3 scripts/check.py` sebelum commit.
5. URL lama `/artigos/...` dialihkan lewat `aliases` di front matter 13 entri hasil peleburan.

### Mengubah angka statistik
Edit `data/estatisticas.yaml` (satu item per angka: `numero`, `rotulo`, `periodo`, `frase`, `fonte`, `url`, `atualizado`). Hub dan keempat halaman spoke membaca data ini lewat shortcode `stats` dan `painel`. Jangan menjumlahkan angka dari periode yang berbeda.

### Halaman biasa (Sobre, Contato, Privasi)
Edit file di `content/`. Ganti `seu-email@exemplo.com` di `content/contato.md` dengan email asli.

### Warna, font, ukuran
Edit `assets/css/main.css`. Font: Inter (teks) dan Source Serif 4 (judul), di-host sendiri; letakkan file WOFF2 di `static/fonts/` (lihat `static/fonts/LEIA-ME.txt`). Warna ada di bagian paling atas:
```
:root{--tx:#1b2430;--mu:#5b6675;--ln:#e4e8ee;--ac:#0a7d4f;--ac2:#08663f;--r:8px}
```
`--ac` adalah warna aksen (tombol, tautan), `--r` radius sudut.

### Logo dan favicon
- Logo: SVG di `layouts/partials/header.html`. Ganti dengan `<img>` jika punya file logo (taruh di `static/`).
- Favicon: `static/favicon.svg`.

### Judul dan deskripsi situs
`title` dan `params.description` di `hugo.toml`. Judul halaman lain: front matter `title` masing-masing file.

## 4. AdSense

1. Buka `hugo.toml`, isi:
   ```
   adsenseClient = "ca-pub-XXXXXXXXXXXXXXXX"
   adSlotTop     = "1234567890"   # slot iklan di atas gerador
   adSlotBottom  = "0987654321"   # slot iklan di bawah gerador
   ```
2. Edit `static/ads.txt`, ganti `pub-XXXXXXXXXXXXXXXX` dengan ID editor Anda (tanpa awalan `ca-`).
3. Saat kolom `adsenseClient` kosong, iklan tidak dimuat sama sekali di situs publik. Di `hugo server` muncul kotak putus-putus sebagai penanda posisi.
4. Ubah posisi iklan di `layouts/index.html` (dua baris `partial "ad.html"`). Jangan menaruh iklan menempel dengan tombol "Gerar CPF" agar tidak memicu klik tidak sengaja.
5. Sebelum mengajukan, pastikan halaman Sobre, Contato, dan Política de Privacidade sudah terisi dan situs punya beberapa artikel asli.

## 5. Canonical dan SEO

- Canonical otomatis dari `baseURL` di `hugo.toml` (`https://gerador-de-cpf.github.io/`). Jika pindah ke domain sendiri, ubah `baseURL` saja.
- `sitemap.xml` dibuat otomatis oleh Hugo; alamatnya sudah tercantum di `static/robots.txt`.
- Schema JSON-LD: WebApplication (homepage), FAQPage (dari `faq`), Article (artikel).
- Setelah online: daftarkan situs di Google Search Console dan kirim `https://gerador-de-cpf.github.io/sitemap.xml`.

## 6. Deploy ke GitHub Pages

1. Buat akun atau organisasi GitHub bernama `gerador-de-cpf`, lalu repositori publik bernama **`gerador-de-cpf.github.io`**.
2. Dari folder proyek: `git init`, `git add .`, `git commit -m "init"`, `git branch -M main`, `git remote add origin <url-repo>`, `git push -u origin main`.
3. Di GitHub: **Settings > Pages > Build and deployment > Source: GitHub Actions**.
4. Setiap `git push` ke `main` akan membangun dan menerbitkan situs otomatis (lihat tab Actions). Alamat: https://gerador-de-cpf.github.io/
5. Jika Actions gagal karena versi action usang, perbarui nomor versi di `.github/workflows/hugo.yml`.

## 7. Daftar cek sebelum tayang

- [ ] `hugo server` berjalan tanpa error; menu, gerador, dan halaman terbuka.
- [ ] Email di `content/contato.md` sudah diganti.
- [ ] Baris "Responsável pelo site" di `content/sobre.md` sudah diisi (nama Anda atau nama proyek).
- [ ] `adsenseClient`, slot, dan `static/ads.txt` sudah diisi (setelah AdSense disetujui).
- [ ] Semua artikel punya `description` dan `draft: false`.
- [ ] Uji gerador di HP dan desktop (pilih UF, dengan/tanpa titik, tombol Copiar).
- [ ] Sitemap sudah dikirim ke Search Console.

## 8. Masalah umum

- **Menu tidak muncul / peringatan pageRef:** pastikan file tujuan ada (`content/sobre.md`, dst.).
- **Artikel tidak tampil:** cek `draft` dan `date` (tidak boleh di masa depan).
- **CSS tidak berubah:** hentikan lalu jalankan ulang `hugo server`.
- **Tombol Copiar tidak bekerja di http lokal:** fitur clipboard butuh HTTPS; ada cadangan otomatis, tapi di situs publik (HTTPS) berjalan normal.

## 9. Halaman validador

- Isi: `content/validador-de-cpf.md` (teks, contoh, FAQ). Tampilan dan logika: `layouts/_default/validador.html` (dipilih lewat `layout: "validador"` di front matter).
- FAQ dirender oleh `layouts/partials/faq.html`, dipakai juga oleh homepage.
- `seoTitle` di front matter kini berlaku untuk halaman mana pun.
- Halaman ini tidak ada di navbar dan tidak memakai iklan. Untuk menambah iklan, sisipkan `{{ partial "ad.html" (dict "slot" site.Params.adSlotBottom) }}` di layout.

## 10. Schema (JSON-LD)

| Halaman | Schema | Di mana |
|---|---|---|
| Homepage | Organization + WebSite + WebApplication (@graph) | `layouts/partials/head.html` |
| Validador | WebApplication + BreadcrumbList + FAQPage | `layouts/_default/validador.html` |
| Artikel | Article (datePublished, dateModified, author, publisher) + BreadcrumbList | `layouts/_default/single.html` |
| Semua halaman selain home | BreadcrumbList + trilha navigasi yang terlihat | `layouts/partials/breadcrumb.html` |
| Homepage dan validador | FAQPage (dari `faq` di front matter) | `layouts/partials/faq.html` |

- **Penulis artikel:** atur di `hugo.toml` bagian `[params.author]`. Kosong berarti penulis = nama situs (Organization). Untuk memakai nama pribadi: `name = "Nama Anda"` dan `type = "Person"`.
- **Logo publisher:** memakai `static/favicon.svg`. Jika sudah punya logo PNG (minimal 112x112 px), letakkan di `static/` dan ubah `ld-publisher.html`.
- **Tes setelah online:** Rich Results Test (search.google.com/test/rich-results) dan validator.schema.org.
