let close = document.querySelectorAll(".fa-plus");
let box = document.querySelectorAll(".hid");

let events = (index) => {
    box[index].style.display = (box[index].style.display == 'none') ? 'block' : 'none';
};

close.forEach((element, index) => {
    element.addEventListener('click', () => events(index));
});
