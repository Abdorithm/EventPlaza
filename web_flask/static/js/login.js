const doc = document;
const win = window;
const fragment = doc.createDocumentFragment();


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