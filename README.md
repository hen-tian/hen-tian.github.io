# HEN TIÁN — Brownies & Cookies Artisan

Website landing page untuk HEN TIÁN, brand artisan brownies dan cookies premium.

🔗 **Live:** [hen-tian.github.io](https://hen-tian.github.io/)

---

## Fitur

### Navbar
- Sticky navigation dengan glassmorphism effect
- Navigasi ke Produk, Tentang, dan Pesan
- Mobile responsive hamburger menu

### Hero Section
- Badge "Preorder Only · Artisan Brownies & Cookies"
- Logo HEN TIÁN
- CTA button "Lihat Menu" dengan smooth scroll
- Gradient background dengan dekorasi radial

### Produk
- **Fudgy Brownies** — 3 ukuran (Large, Medium, Small) dengan interactive size selector yang mengganti foto sesuai ukuran
- **Monster Cookie** — chunky cookies dengan coklat, oat, dan M&M
- **Matcha Cookie** — cookies matcha premium
- **Classic Cookie** — chocolate chip cookies klasik
- Add to cart button dengan animasi checkmark

### Shopping Cart
- Floating cart badge di pojok kanan bawah
- Slide-in drawer dari kanan
- Tambah/kurang jumlah item (qty +/−)
- Hapus item dari keranjang
- Counter badge dengan animasi
- Persist di localStorage (tidak hilang saat refresh)

### Order via WhatsApp
- Auto-compose pesan dari isi keranjang
- Redirect langsung ke WhatsApp (`wa.me/6287876441888`)
- Format pesan otomatis: "Kak aku mau pesan [produk] [ukuran] [jumlah]"

### About Section
- 3 stat cards: Fresh, Premium, Artisan
- Dark theme section dengan accent hijau

### Order Section
- WhatsApp card (jam operasional 08.00–17.00 WIB)
- Instagram card (@hen.tian)

### Footer
- Brand logo, copyright © 2025–2026

### Lainnya
- Scroll animation (fade-up on viewport)
- Responsive mobile-first design
- Single HTML file — no build tools, no database
- Template komentar di kode untuk panduan tambah menu baru

---

## Deployment

Static site di GitHub Pages. Push ke `main` branch otomatis live.

```bash
git add -A
git commit -m "update"
git push
```

## Tambah Menu Baru (Manual)

Website ini **hardcoded** — satu file `index.html`, tidak ada database atau CMS. Untuk menambah menu baru, edit langsung file `index.html` dan push ke GitHub.

### Langkah 1: Siapkan Foto Produk

- Format: `.webp` (direkomendasikan) atau `.jpg`
- Ukuran minimal: lebar 600px, rasio ~5:3 (landscape)
- Kompres agar ringan (target < 100KB per foto)
- Simpan di folder: `assets/`
- Contoh: `assets/kue-coklat.webp`

### Langkah 2: Tambah Card Produk di HTML

Buka `index.html`, cari bagian `<div class="product-grid">`. Copy-paste blok di bawah ini, tempatkan **sebelum komentar template**:

```html
<div class="product-card fade-up">
  <div class="product-img">
    <span class="product-tag">KATEGORI</span>
    <div class="product-photo-wrap">
      <img src="assets/nama-foto.webp"
           alt="Nama Produk"
           class="product-photo">
    </div>
  </div>
  <div class="product-info">
    <h3 class="product-name">Nama Produk</h3>
    <p class="product-desc">Deskripsi singkat produk.</p>
    <button class="add-to-cart-btn" onclick="addToCart('Nama Produk', false, this)">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"/></svg>
    </button>
  </div>
</div>
```

Ganti:
- `KATEGORI` → "Brownies", "Cookies", atau kategori baru
- `assets/nama-foto.webp` → path foto yang sudah disimpan
- `Nama Produk` → nama produk (muncul di card dan keranjang)
- `Deskripsi singkat produk.` → deskripsi produk
- `addToCart('Nama Produk', false, this)` → nama di parameter harus sama dengan di `.product-name`

### Langkah 3 (Opsional): Produk dengan Beberapa Ukuran

Jika produk punya beberapa ukuran seperti Fudgy Brownies:

1. Siapkan foto per ukuran di `assets/` (misal `brownies-large.webp`, `brownies-medium.webp`, `brownies-small.webp`)

2. Tambahkan selector di dalam `<div class="product-info">`:
```html
<div class="size-selector">
  <button class="size-btn active" onclick="changeBrownieSize('large', this)">Large</button>
  <button class="size-btn" onclick="changeBrownieSize('medium', this)">Medium</button>
  <button class="size-btn" onclick="changeBrownieSize('small', this)">Small</button>
</div>
```

3. Tambahkan entry di object `browniesPhotos` di bagian `<script>`:
```javascript
const browniesPhotos = {
  large:  'assets/brownies-large.webp',
  medium: 'assets/brownies-medium.webp',
  small:  'assets/brownies-small.webp',
  // tambah ukuran baru di sini
};
```

4. Ubah parameter `addToCart` menjadi `true`:
```html
<button class="add-to-cart-btn" onclick="addToCart('Nama Produk', true, this)">
```

### Langkah 4: Push ke GitHub

```bash
cd ~/sketches/hen-tian-website
git add -A
git commit -m "tambah menu: Nama Produk"
git push
```

Website otomatis update dalam 1-2 menit di [hen-tian.github.io](https://hen-tian.github.io/).

---

### Tips

- **Hapus produk:** tinggal hapus blok `<div class="product-card">...</div>` yang tidak dipakai
- **Urutan produk:** card paling atas di HTML = tampil paling kiri di website
- **Ganti foto:** replace file di `assets/` dengan nama yang sama, push ulang
- **Edit deskripsi:** ubah teks di `<p class="product-desc">` lalu push
