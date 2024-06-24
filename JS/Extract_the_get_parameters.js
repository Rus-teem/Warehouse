// Некоторые другие свойства объекта window.location:

// href - весь URL
// protocol - протокол URL
// host - имя хоста и порт URL
// hostname - имя хоста URL
// port - номер порта
// pathname - путь в URL (та часть, которая идёт после первого слэша /)
// search - часть запроса URL (та часть, которая идёт после знака вопроса ?)
// hash - часть URL (та часть, которая идёт после знака решётки #)

// Пример получения значения url 
const currentUrl = window.location.href;
console.log(currentUrl); 

let url = new URL("http://www.example.com/page.html?param1=value1&amp;param2=value2&amp;param3=value3");
let params = new URLSearchParams(url.search);
 
let param3 = params.get('param3'); // "value3"

// пример 2
let url = "http://www.example.com/page.html?param1=value1&amp;param2=value2&amp;param3=value3";
//разбиваем значение split('?')[1] - тут получаем элемент по индексу 
let params = url.split('?')[1].split('&amp;'); 
let param3;
 
for(let i = 0; i &lt; params.length; i++) {
    let pair = params[i].split('=');
    if(pair[0] == 'param3') {
        param3 = pair[1];
    }
}