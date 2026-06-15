document.addEventListener('DOMContentLoaded', () => {
  const trigger  = document.querySelector('.lightbox-trigger');
  const lightbox = document.getElementById('lightbox');
  if (!trigger || !lightbox) return;

  const lbClose    = lightbox.querySelector('.lightbox-close');
  const lbBackdrop = lightbox.querySelector('.lightbox-backdrop');

  function open() {
    lightbox.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    lbClose.focus();
  }

  function close() {
    lightbox.classList.remove('is-open');
    document.body.style.overflow = '';
    trigger.focus();
  }

  trigger.addEventListener('click', open);
  lbClose.addEventListener('click', close);
  lbBackdrop.addEventListener('click', close);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('is-open')) close();
  });
});
