/* ── Nav scroll ── */
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  });
  // Set active nav link
  const links = nav.querySelectorAll('.nav-links a');
  links.forEach(a => {
    if (a.getAttribute('href') === window.location.pathname) {
      a.classList.add('active');
    }
  });
}

/* ── Mobile menu ── */
function toggleMenu() {
  document.getElementById('mobile-menu').classList.toggle('open');
}
window.toggleMenu = toggleMenu;

/* ── FAQ accordion ── */
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.parentElement;
    const answer = item.querySelector('.faq-a');
    const isOpen = item.classList.contains('open');
    // Close all
    document.querySelectorAll('.faq-item.open').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-a').style.maxHeight = '0';
    });
    if (!isOpen) {
      item.classList.add('open');
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});

/* ── Scroll reveal ── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* ── Contact form ── */
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('.form-submit');
    btn.textContent = 'Sending…';
    btn.disabled = true;
    try {
      const res = await fetch('/contact', {
        method: 'POST',
        body: new FormData(contactForm),
      });
      if (res.ok) {
        contactForm.style.display = 'none';
        document.getElementById('form-success').style.display = 'block';
      }
    } catch {
      btn.textContent = 'Send Message →';
      btn.disabled = false;
    }
  });
}
