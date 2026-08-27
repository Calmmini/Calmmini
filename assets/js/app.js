/* CALMMINI — front-end logic (vanilla, no dependencies) */
(function () {
  "use strict";
  var BASE = window.CALMMINI_BASE || "";
  var PRODUCTS = window.CALMMINI_PRODUCTS || [];
  var PMAP = {};
  PRODUCTS.forEach(function (p) { PMAP[p.slug] = p; });
  var CART_KEY = "calmmini_cart_v1";
  var SHIP_NOTE = "Verzendkosten worden berekend bij het afrekenen.";

  /* ---------- helpers ---------- */
  function eur(v) { return "€ " + v.toFixed(2).replace(".", ","); }
  function $(s, c) { return (c || document).querySelector(s); }
  function $all(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function imgFor(slug) { return BASE + "assets/img/products/" + slug + ".jpg"; }
  function urlFor(slug) { return BASE + "product/" + slug + "/"; }

  /* ---------- cart store ---------- */
  function readCart() {
    try { return JSON.parse(localStorage.getItem(CART_KEY)) || []; }
    catch (e) { return []; }
  }
  function writeCart(c) {
    try { localStorage.setItem(CART_KEY, JSON.stringify(c)); } catch (e) {}
    syncBadge();
  }
  function cartQty() { return readCart().reduce(function (n, i) { return n + i.qty; }, 0); }
  function cartTotal() {
    return readCart().reduce(function (s, i) {
      var p = PMAP[i.slug]; return s + (p ? p.price * i.qty : 0);
    }, 0);
  }
  function addToCart(slug, qty) {
    if (!PMAP[slug]) return;
    qty = qty || 1;
    var c = readCart(), f = c.filter(function (i) { return i.slug === slug; })[0];
    if (f) f.qty += qty; else c.push({ slug: slug, qty: qty });
    writeCart(c);
    toast(PMAP[slug].name + " toegevoegd aan winkelwagen");
  }
  function setQty(slug, qty) {
    var c = readCart();
    if (qty <= 0) { c = c.filter(function (i) { return i.slug !== slug; }); }
    else { c.forEach(function (i) { if (i.slug === slug) i.qty = qty; }); }
    writeCart(c); renderCart(); renderCheckout();
  }
  function removeItem(slug) {
    writeCart(readCart().filter(function (i) { return i.slug !== slug; }));
    renderCart(); renderCheckout();
  }
  function syncBadge() {
    var n = cartQty();
    $all("[data-cart-count]").forEach(function (el) {
      el.textContent = n; el.hidden = n === 0;
    });
  }

  /* ---------- toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "toast";
      toastEl.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5" stroke-linecap="round" stroke-linejoin="round"/></svg><span></span>';
      document.body.appendChild(toastEl);
    }
    $("span", toastEl).textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }

  /* ---------- add-to-cart buttons ---------- */
  document.addEventListener("click", function (e) {
    var add = e.target.closest("[data-add]");
    if (add) {
      e.preventDefault();
      var slug = add.getAttribute("data-add");
      var qtyInput = add.closest("[data-qty-scope]") ?
        $(".qty input", add.closest("[data-qty-scope]")) : null;
      addToCart(slug, qtyInput ? parseInt(qtyInput.value, 10) || 1 : 1);
    }
  });

  /* ---------- quantity steppers ---------- */
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".qty [data-step]");
    if (!btn) return;
    var input = $("input", btn.parentNode);
    var v = parseInt(input.value, 10) || 1;
    v += parseInt(btn.getAttribute("data-step"), 10);
    if (v < 1) v = 1;
    input.value = v;
    var line = btn.closest("[data-cart-slug]");
    if (line) setQty(line.getAttribute("data-cart-slug"), v);
  });

  /* ---------- PDP gallery thumbs ---------- */
  $all("[data-gallery]").forEach(function (g) {
    var main = $(".main img", g);
    $all(".pdp-thumbs button", g).forEach(function (b) {
      b.addEventListener("click", function () {
        $all(".pdp-thumbs button", g).forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        main.src = $("img", b).src;
      });
    });
  });

  /* ---------- mobile nav ---------- */
  var drawer = $(".mobile-nav"), scrim = $(".scrim"), filters = $(".filters");
  function closeAll() {
    if (drawer) drawer.classList.remove("open");
    if (filters) filters.classList.remove("open");
    if (scrim) scrim.classList.remove("open");
    document.body.style.overflow = "";
  }
  $all("[data-open-nav]").forEach(function (b) {
    b.addEventListener("click", function () {
      drawer && drawer.classList.add("open");
      scrim && scrim.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  });
  $all("[data-open-filters]").forEach(function (b) {
    b.addEventListener("click", function () {
      filters && filters.classList.add("open");
      scrim && scrim.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  });
  $all("[data-close]").forEach(function (b) { b.addEventListener("click", closeAll); });
  scrim && scrim.addEventListener("click", closeAll);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeAll(); closeSearch(); } });

  /* ---------- search ---------- */
  var searchPanel = $(".search-panel"), searchInput = searchPanel ? $("input", searchPanel) : null;
  function closeSearch() { searchPanel && searchPanel.classList.remove("open"); }
  $all("[data-open-search]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (!searchPanel) return;
      searchPanel.classList.toggle("open");
      if (searchPanel.classList.contains("open") && searchInput) searchInput.focus();
    });
  });

  /* ---------- collection: filter + sort + search ---------- */
  var grid = $("[data-grid]");
  if (grid) {
    var cards = $all(".card", grid);
    var countEl = $("[data-count]");
    var sortSel = $("[data-sort]");
    var params = new URLSearchParams(location.search);
    var q = (params.get("q") || "").toLowerCase().trim();

    // preselect category from ?cat
    var pcat = params.get("cat");
    if (pcat) {
      var cb = $('[data-filter-cat][value="' + pcat + '"]');
      if (cb) cb.checked = true;
    }
    if (q && searchInput) searchInput.value = params.get("q");

    function activeCats() {
      return $all("[data-filter-cat]:checked").map(function (c) { return c.value; });
    }
    function activePrice() {
      var r = $('[data-filter-price]:checked'); return r ? r.value : "all";
    }
    function apply() {
      var cats = activeCats(), price = activePrice(), shown = 0;
      cards.forEach(function (card) {
        var cardCats = (card.getAttribute("data-cat") || "").split(" ");
        var okCat = !cats.length || cats.some(function (c) { return cardCats.indexOf(c) > -1; });
        var p = parseFloat(card.getAttribute("data-price"));
        var okPrice = price === "all" ||
          (price === "lt10" && p < 10) ||
          (price === "10to20" && p >= 10 && p <= 20) ||
          (price === "gt20" && p > 20);
        var okQ = !q || (card.getAttribute("data-name") || "").toLowerCase().indexOf(q) > -1;
        var show = okCat && okPrice && okQ;
        card.style.display = show ? "" : "none";
        if (show) shown++;
      });
      if (countEl) countEl.textContent = shown + (shown === 1 ? " product" : " producten");
    }
    function sortCards() {
      var v = sortSel ? sortSel.value : "featured";
      var arr = cards.slice();
      arr.sort(function (a, b) {
        if (v === "price-asc") return a.getAttribute("data-price") - b.getAttribute("data-price");
        if (v === "price-desc") return b.getAttribute("data-price") - a.getAttribute("data-price");
        if (v === "name") return (a.getAttribute("data-name") || "").localeCompare(b.getAttribute("data-name") || "");
        return a.getAttribute("data-index") - b.getAttribute("data-index");
      });
      arr.forEach(function (c) { grid.appendChild(c); });
    }
    $all("[data-filter-cat],[data-filter-price]").forEach(function (c) {
      c.addEventListener("change", apply);
    });
    sortSel && sortSel.addEventListener("change", sortCards);
    $all("[data-clear-filters]").forEach(function (b) {
      b.addEventListener("click", function () {
        $all("[data-filter-cat]").forEach(function (c) { c.checked = false; });
        var allP = $('[data-filter-price][value="all"]'); if (allP) allP.checked = true;
        q = ""; if (searchInput) searchInput.value = "";
        apply();
      });
    });
    apply(); sortCards();
  }

  /* ---------- cart page ---------- */
  function renderCart() {
    var host = $("[data-cart-lines]");
    if (!host) return;
    var cart = readCart();
    var wrapEl = $("[data-cart-wrap]"), empty = $("[data-cart-empty]");
    if (!cart.length) {
      if (wrapEl) wrapEl.hidden = true;
      if (empty) empty.hidden = false;
      return;
    }
    if (wrapEl) wrapEl.hidden = false;
    if (empty) empty.hidden = true;
    host.innerHTML = cart.map(function (i) {
      var p = PMAP[i.slug]; if (!p) return "";
      return '<div class="cart-line" data-cart-slug="' + p.slug + '">' +
        '<a href="' + urlFor(p.slug) + '"><img src="' + imgFor(p.slug) + '" alt="' + p.name + '" loading="lazy"></a>' +
        '<div><div class="ttl"><a href="' + urlFor(p.slug) + '">' + p.name + '</a></div>' +
        '<div class="price" style="font-size:.95rem;margin:.3rem 0">' + eur(p.price) + '</div>' +
        '<div class="qty"><button data-step="-1" aria-label="Minder">–</button>' +
        '<input value="' + i.qty + '" readonly aria-label="Aantal"><button data-step="1" aria-label="Meer">+</button></div>' +
        '<button class="rm" data-rm="' + p.slug + '">Verwijderen</button></div>' +
        '<div class="price">' + eur(p.price * i.qty) + '</div></div>';
    }).join("");
    updateSummary();
  }
  function updateSummary() {
    var sub = cartTotal();
    $all("[data-subtotal]").forEach(function (e) { e.textContent = eur(sub); });
    $all("[data-total]").forEach(function (e) { e.textContent = eur(sub); });
  }
  document.addEventListener("click", function (e) {
    var rm = e.target.closest("[data-rm]");
    if (rm) { e.preventDefault(); removeItem(rm.getAttribute("data-rm")); }
  });

  /* ---------- checkout ---------- */
  function renderCheckout() {
    var host = $("[data-checkout-lines]");
    if (!host) return;
    var cart = readCart();
    if (!cart.length) { location.href = BASE + "winkelwagen/"; return; }
    host.innerHTML = cart.map(function (i) {
      var p = PMAP[i.slug]; if (!p) return "";
      return '<div class="summary-line" style="display:flex;gap:.8rem;align-items:center;padding:.6rem 0;border-bottom:1px solid var(--line-soft)">' +
        '<div style="position:relative;flex:0 0 auto"><img src="' + imgFor(p.slug) + '" alt="' + p.name + '" style="width:52px;height:64px;object-fit:cover;border-radius:8px" loading="lazy">' +
        '<span style="position:absolute;top:-8px;right:-8px;background:var(--gold);color:var(--espresso);width:20px;height:20px;border-radius:100px;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center">' + i.qty + '</span></div>' +
        '<div style="flex:1;font-size:.9rem">' + p.name + '</div>' +
        '<div class="price" style="font-size:.9rem">' + eur(p.price * i.qty) + '</div></div>';
    }).join("");
    updateSummary();
    var form = $("[data-checkout-form]");
    if (form && !form._bound) {
      form._bound = true;
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var ok = $("[data-order-confirm]");
        if (ok) {
          writeCart([]);
          $("[data-checkout-wrap]").hidden = true;
          ok.hidden = false;
          window.scrollTo({ top: 0, behavior: "smooth" });
        }
      });
    }
  }

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    $all(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    $all(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- init ---------- */
  syncBadge();
  renderCart();
  renderCheckout();
})();
