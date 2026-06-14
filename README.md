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

## Tambah Menu Baru

Lihat komentar di dalam `index.html` (sebelum closing `</div>` product-grid) untuk panduan lengkap menambah produk baru.
