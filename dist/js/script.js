// navbar fixed
window.addEventListener('scroll', function() {
  const header = document.querySelector('header');
  const fixedNav = header.offsetTop;
  const toTop = document.querySelector('#to-top');
  
  if(window.pageYOffset > fixedNav) {
    header.classList.add('navbar-fixed');
    toTop.classList.remove('hidden');
    toTop.classList.add('flex');
  } else {
    header.classList.remove('navbar-fixed');
    toTop.classList.remove('flex');
    toTop.classList.add('hidden');
  }
});

// hamburger and close menu functionality
const hamburger = document.querySelector('#hamburger');
const navMenu = document.querySelector('#nav-menu');

function toggleMenu() {
  hamburger.classList.toggle('hamburger-active');
  navMenu.classList.toggle('hidden');
}

hamburger.addEventListener('click', toggleMenu);
window.addEventListener('click', function(e) {
  if(e.target != hamburger && e.target != navMenu && !e.target.classList.contains('hamburger-line')) {
    toggleMenu();
  }
});

// dark mode toggle
const darkToggle = document.querySelector('#dark-toggle');
const html = document.querySelector('html');

function toggleDarkMode() {
  if(darkToggle.checked) {
    html.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    html.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
}

darkToggle.addEventListener('click', toggleDarkMode);

// Move toggle based on mode
if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  darkToggle.checked = true;
} else {
  darkToggle.checked = false;
}




const scriptURL = 'https://script.google.com/macros/s/AKfycbxqE3V1by7HCjSWqyCMLkiiDablI7aF8RhFHVYEu0_R-ZrIPQoioPNXncRoP5XD_wC2/exec'
    const form = document.forms['gform']
    const btnKirim = document.querySelector('.btn-kirim')
    const btnLoading = document.querySelector('.btn-loading')
    const myAlert = document.querySelector('.my-alert')
    const btnClose = document.querySelector('#btn-close')
   var submitted = false;
   
    form.addEventListener('submit', function(e) {
     e.preventDefault();
 btnLoading.classList.toggle('hidden')
 btnKirim.classList.toggle('hidden')
 fetch(form.action, {
  method: 'POST', body: new FormData(form)})
      .then(response => {
        btnLoading.classList.toggle('hidden')
        btnKirim.classList.toggle('hidden')
        myAlert.classList.toggle('hidden')
        form.reset();
        console.log('Success!', response)
      })
      .catch(error => {
        btnLoading.classList.toggle('hidden')
        btnKirim.classList.toggle('hidden')
        myAlert.classList.toggle('hidden')
      console.error('Pesan Terikirim dengan Gangguan', error.message);
      form.reset();
       
      })
})
    btnClose.addEventListener("click", function() {
     myAlert.classList.toggle('hidden')
    }) 
    /* form.addEventListener('submit', e => {
      e.preventDefault()
      btnLoading.classList.toggle('hidden')
      btnKirim.classList.toggle('hidden')
      fetch(scriptURL, {
        method: 'POST', body: new FormData(form)})
      .then(response => {
        btnLoading.classList.toggle('hidden')
        btnKirim.classList.toggle('hidden')
        myAlert.classList.toggle('hidden')
        form.reset();
        console.log('Success!', response)
      })
      .catch(error => console.error('Error!', error.message))
    })
    
    btnClose.addEventListener("click", function() {
     myAlert.classList.toggle('hidden')
    }) */
 


  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
   document.documentElement.classList.add('dark')
  } else {
   document.documentElement.classList.remove('dark')
  }
 