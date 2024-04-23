const doc = document;
const win = window;
const fragment = doc.createDocumentFragment();
const button_menu = doc.getElementById('user-menu-button');
const profile_menu = doc.getElementById('user-profile-menu');


const profile_menu_drop = () => {

    button_menu.addEventListener('click', () => {

        // toggle the menu on click

        profile_menu.classList.toggle('profile-menu-enter');
        profile_menu.classList.toggle('profile-menu-leave');

    });

    doc.addEventListener('click', event => {

        // close the menu when the user clicks outside

        const outsideClick = (!profile_menu.contains(event.target)
            && !button_menu.contains(event.target));

        if (outsideClick === true) {

            profile_menu.classList.remove('profile-menu-enter');
            profile_menu.classList.add('profile-menu-leave');

        }

    });

};
profile_menu_drop();


const mobile_menu_button = doc.getElementById('mobile-menu-button');
const mobile_menu = doc.getElementById('mobile-menu');
const menu_dashes = doc.querySelectorAll('.menu-dash');

const mobile_menu_drop = () => {

    mobile_menu_button.addEventListener('click', () => {

        // toggle the mobile menu on click
        mobile_menu.classList.toggle('hidden');
        // mobile_menu.classList.toggle('-translate-x-64');

        menu_dashes.forEach(dash => {
            dash.classList.toggle('hidden');
            dash.classList.toggle('block');
        });

    });

};
mobile_menu_drop();


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