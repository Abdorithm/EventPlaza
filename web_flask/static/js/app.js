// Define Global Variables
const doc = document;
const win = window;
const fragment = doc.createDocumentFragment();
const nav_container = doc.getElementById('nav-container');


// mobile phone nav
const slideNav = () => {

    const nav_button = doc.querySelector('.custom-nav-icon');
    let t = 0;

    nav_button.addEventListener('click', () => {

        // toggle the nav
        nav_container.classList.toggle('nav-container-yes');
        nav_container.classList.toggle('nav-container-no');

        // animate the nav button
        doc.querySelector('.custom-nav-icon').setAttribute('name',
            t % 2 === 0 ? 'chevron-up-outline' : 'chevron-down-outline');
        t++;

    });

};
slideNav();


const flash_button = doc.getElementById('close-flash');
const flash_div = doc.getElementById('flash-body');

const close_flash_message = () => {

    flash_button.addEventListener('click', () => {

        if (!flash_div.classList.contains('hidden')) {
            flash_div.classList.add('hidden');
        }

    });

};
close_flash_message();