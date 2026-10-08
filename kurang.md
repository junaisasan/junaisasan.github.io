# kurang.md: cek teknis yang masih kurang

Tanggal audit: 8 Oktober 2026. Situs: `https://gerador-de-cpf.github.io/`.

**Batas audit ini:** Hugo tidak terpasang di lingkungan saya dan jaringan mati, jadi **situs belum pernah di-build** dan JSON-LD belum diuji di Rich Results Test. Semua temuan di bawah berasal dari pembacaan file, bukan dari HTML hasil build. Langkah 0 harus dilakukan lebih dulu.

## Sudah diperiksa dan aman

| Item | Hasil |
|---|---|
| Sintaks YAML semua front matter dan `data/estatisticas.yaml` | Valid (12 item) |
| `<title>` ≤ 55 dan meta description ≤ 155 karakter, tanpa duplikat | Lolos (`scripts/check.py`) |
| Definisi ≤ 50 kata di glosarium dan statistik | Lolos |
| Tautan internal di konten | 0 tautan putus; homepage menaut ke 19 entri dan 5 halaman statistik |
| Canonical | Dari `.Permalink`, ikut `baseURL` baru |
| Redirect `/artigos/...` | Lewat `aliases` (meta refresh, bukan 301) |
| `robots.txt`, sitemap | Otomatis dari Hugo, bot AI diizinkan |
| Keseimbangan tag template (`if`/`range`/`end`) | Seimbang |

## Prioritas tinggi

### 0. Build belum diuji
Jalankan `hugo server` dan `hugo --minify`, lalu buka beberapa halaman. Perhatikan peringatan `definicao com N palavras` (dari `resposta.html`). Template baru yang paling mungkin bermasalah adalah `glossario/list.html` (indeks A–Z), shortcode `stats` dan `painel`, serta `dateFormat` pada string tanggal di YAML. Versi Hugo di workflow (`0.161.1`) juga perlu dipastikan memang ada di halaman rilis; jika tidak, build di GitHub Actions akan gagal.

### 1. Tidak ada halaman 404
Tidak ada `layouts/404.html`, jadi GitHub Pages menampilkan 404 bawaan tanpa navbar. Setelah ada alias dan URL baru, halaman ini perlu untuk pengunjung yang masuk lewat URL lama yang salah. Tambahkan:

```html
{{ define "main" }}
<div class="prose page">
  <h1>Página não encontrada</h1>
  <p>O endereço não existe. Tente o <a href="/">gerador de CPF</a>, o <a href="/glossario/">glossário</a> ou as <a href="/estatisticas/">estatísticas</a>.</p>
</div>
{{ end }}
```

Beri `<meta name="robots" content="noindex">` di halaman ini lewat kondisi `{{ if eq .Kind "404" }}` di `head.html`.

### 2. Placeholder yang masih tampil di situs
- `content/sobre.md` baris 7: "[preencha com seu nome ou o nome do projeto]" tampil apa adanya di halaman publik.
- `static/ads.txt`: berisi `pub-XXXXXXXXXXXXXXXX`. Entri palsu sebaiknya dihapus sampai AdSense disetujui.
- `hugo.toml`: `params.author.name` kosong, jadi tidak ada nama penulis atau peninjau di mana pun.

### 3. File font belum ada
CSS sudah memanggil `/fonts/inter-latin-var.woff2` dan `/fonts/source-serif-4-latin-var.woff2`. Tanpa file itu browser mencatat 404 pada tiap halaman, dan tampilan memakai font cadangan. Panduan ada di `static/fonts/LEIA-ME.txt`.

### 4. Domain lama
`geradorcpf.github.io` tidak otomatis mengarah ke domain baru. Buat repo stub dengan meta refresh dan canonical ke `gerador-de-cpf.github.io`, lalu daftarkan properti baru di Search Console dan kirim sitemap. Properti lama jangan dihapus dulu.

## Prioritas sedang

### 5. Schema (JSON-LD)
- **Statistik:** hanya `WebPage` + `FAQPage`. Sumber (Serpro, Serasa Experian, TCU, dan seterusnya) tidak ditandai. Pertimbangkan `Dataset` atau properti `citation`/`isBasedOn` per angka, atau setidaknya `ItemList` dari 12 angka.
- **Penulis dan peninjau:** `ld-author.html` kini tidak dipakai. Halaman glosarium dan statistik hanya punya `publisher`. Karena topiknya pajak dan identitas, nama penulis atau peninjau (`author`, `reviewedBy`) akan memperkuat sinyal kepercayaan.
- **Logo Organization:** menunjuk `favicon.svg`. Banyak validator mengharapkan raster minimal 112×112 px. Buat `logo.png` dan arahkan `ld-publisher.html` ke sana.
- **Organization:** belum ada `sameAs` atau kontak. Tambahkan jika ada profil resmi.
- **Hub dan indeks:** `og:type` bernilai `article` di semua halaman non-home, termasuk `/glossario/` dan `/estatisticas/`. Untuk halaman daftar lebih tepat `website`.
- Uji hasil build di <https://search.google.com/test/rich-results> dan <https://validator.schema.org> (hub, 1 spoke, 1 entri, dan homepage).

### 6. `lastmod` di sitemap
Halaman yang tidak punya `lastmod` di front matter (homepage, validador, sobre, kontak, privasi) tampil tanpa tanggal di sitemap. Workflow sudah memakai `fetch-depth: 0`, jadi cukup tambahkan `enableGitInfo = true` di `hugo.toml`. Hugo lalu mengambil tanggal dari riwayat Git.

### 7. Meta sosial
- `twitter:title`, `twitter:description`, dan `twitter:image` tidak ada (platform memakai Open Graph sebagai cadangan, jadi ini kosmetik).
- Tidak ada `article:modified_time`.
- `og:image` memakai infografik 1024×1536 sebesar ±1,7 MB. Rasio portrait dipotong di banyak pratinjau. Buat gambar 1200×630 yang ringan untuk OG.
- Gambar yang sama ada dua kali (`assets/img` dan `static`), total ±3,5 MB di repo.

### 8. Ikon
Hanya ada `favicon.svg`. Tambahkan `favicon.ico` atau PNG 32×32 dan `apple-touch-icon.png` (180×180) untuk browser dan perangkat yang belum mendukung SVG.

### 9. Risiko drift angka
Angka statistik tertulis di tiga tempat: `data/estatisticas.yaml`, homepage, dan beberapa entri glosarium (CIN, CNPJ, IRPF, Serpro, fraude de identidade). Jika satu berubah, yang lain bisa tertinggal. Saran: tambahkan ke `check.py` pemeriksaan bahwa angka-angka kunci (mis. `226 milhões`, `44.498.717`, `70.085.591`) di konten sama dengan YAML.

### 10. RSS
Hugo masih membuat `index.xml` untuk situs ini. Tidak ada blog, jadi umpan itu tidak berguna. Matikan dengan menambahkan `"rss"` ke `disableKinds`, atau biarkan jika memang ingin.

## Prioritas rendah

- `<html lang>` menghasilkan `pt-br` (huruf kecil). Valid, tapi `pt-BR` lebih umum: pakai `site.Language.LanguageCode`.
- Tidak ada tautan "lewati ke konten" (skip link) untuk pembaca layar.
- `layouts/_default/list.html` tidak dipakai lagi oleh section mana pun.
- Tambahkan `llms.txt` jika ingin memudahkan AI membaca struktur situs (opsional).
- Aturan 2–3 tautan di `check.py` hanya dicek di sumber Markdown, bukan di HTML hasil build.

## Urutan kerja yang disarankan

1. Build lokal, perbaiki error atau peringatan (butir 0).
2. `404.html`, isi `sobre.md`, hapus `ads.txt` palsu, taruh file font (butir 1, 2, 3).
3. Push ke repo baru, cek Actions, lalu uji schema di build produksi (butir 5).
4. Search Console baru, stub domain lama (butir 4).
5. Perbaikan menengah dan rendah.
