// Define Global Variables
const doc = document;
const win = window;
const fragment = doc.createDocumentFragment();
const nav_container = doc.getElementById('nav-container');

console.log(nav_container);

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