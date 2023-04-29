let query = document.querySelector('.srch');
let searchbtn = document.querySelector('.btn');

searchbtn.onclick = function(){
    let url = 'https://www.google.com/search?q='+query.value;
    window.open(url);
}