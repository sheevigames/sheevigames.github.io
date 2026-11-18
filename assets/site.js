/* Shivi's Games – shared page behaviour: Apple-style scroll animations and tap-to-play YouTube videos. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Staggered groups: children animate one after another.
  document.querySelectorAll('.chips, .features, .list, .vids, .values, .legal-cards, .others, .socials, .apps').forEach(function (g) {
    g.classList.add('stagger', 'reveal');
    Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty('--i', i); });
  });
  document.querySelectorAll('.shots').forEach(function (s) {
    s.classList.add('reveal-shots');
    Array.prototype.forEach.call(s.children, function (c, i) { c.style.setProperty('--i', i); });
  });

  // Reveal on scroll
  var targets = document.querySelectorAll('.reveal, .reveal-shots');
  if (reduce || !('IntersectionObserver' in window)) {
    targets.forEach(function (e) { e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (e) { io.observe(e); });
  }

  // Scroll-lit statement: split words into spans.
  var statements = [];
  document.querySelectorAll('.statement p').forEach(function (p) {
    var html = p.innerHTML.split(/(\s+)/).map(function (t) {
      if (/^\s+$/.test(t) || !t) return t;
      var hl = t.indexOf('*') === 0;
      if (hl) t = t.slice(1);
      return '<span class="w' + (hl ? ' hl' : '') + '">' + t + '</span>';
    }).join('');
    p.innerHTML = html;
    statements.push({ el: p.closest('.statement'), words: p.querySelectorAll('.w') });
  });

  // Scroll-linked effects (hero parallax + statement), batched with requestAnimationFrame.
  var heroes = document.querySelectorAll('.hero, .ghero');
  var ticking = false;
  function update() {
    ticking = false;
    var vh = window.innerHeight;
    heroes.forEach(function (h) {
      var r = h.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, -r.top / Math.max(1, r.height)));
      h.style.setProperty('--p', p.toFixed(3));
    });
    statements.forEach(function (s) {
      var r = s.el.getBoundingClientRect();
      var total = r.height - vh;
      var sp = Math.min(1, Math.max(0, -r.top / Math.max(1, total)));
      s.el.style.setProperty('--sp', sp.toFixed(3));
      var lit = Math.round(sp * 1.15 * s.words.length);
      s.words.forEach(function (w, i) { w.classList.toggle('on', i < lit); });
    });
  }
  if (!reduce) {
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener('resize', update);
    update();
  } else {
    statements.forEach(function (s) { s.words.forEach(function (w) { w.classList.add('on'); }); });
  }

  // YouTube videos: show the thumbnail first, load the player only when tapped.
  document.querySelectorAll('.vid[data-yt]').forEach(function (b) {
    var id = b.getAttribute('data-yt');
    var img = b.querySelector('img');
    if (img) {
      img.addEventListener('error', function () {
        if (img.dataset.fallback) return;
        img.dataset.fallback = '1';
        img.src = 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg';
      });
    }
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&playsinline=1';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      f.title = b.getAttribute('aria-label') || 'YouTube video';
      var holder = document.createElement('div');
      holder.className = 'vid playing';
      holder.appendChild(f);
      b.replaceWith(holder);
    }, { once: true });
  });
})();
