// Пример получения значения url 
const currentUrl = window.location.href;
console.log(currentUrl); // => https://ru.hexlet.io/qna

let url = new URL("http://www.example.com/page.html?param1=value1&amp;param2=value2&amp;param3=value3");
let params = new URLSearchParams(url.search);
 
let param3 = params.get('param3'); // "value3"

// пример 2
let url = "http://www.example.com/page.html?param1=value1&amp;param2=value2&amp;param3=value3";
//разбиваем значение
let params = url.split('?')[1].split('&amp;'); 
let param3;
 
for(let i = 0; i &lt; params.length; i++) {
    let pair = params[i].split('=');
    if(pair[0] == 'param3') {
        param3 = pair[1];
    }
}