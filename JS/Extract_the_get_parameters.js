// Некоторые другие свойства объекта window.location:

// href - весь URL
// protocol - протокол URL
// host - имя хоста и порт URL
// hostname - имя хоста URL
// port - номер порта
// pathname - путь в URL (та часть, которая идёт после первого слэша /)
// search - часть запроса URL (та часть, которая идёт после знака вопроса ?)
// hash - часть URL (та часть, которая идёт после знака решётки #)

// Получение и разбор GET-параметров из URL

// Текущий URL страницы
const currentUrl = window.location.href;
console.log('Current URL:', currentUrl);

// Пример 1: извлечение параметров через URLSearchParams (современный способ)
const exampleUrl1 = new URL("http://www.example.com/page.html?param1=value1&param2=value2&param3=value3");
const params1 = new URLSearchParams(exampleUrl1.search);
const param3value = params1.get('param3');
console.log('param3 (URLSearchParams):', param3value);

// Пример 2: ручной разбор строки запроса (альтернативный способ)
const exampleUrl2 = "http://www.example.com/page.html?param1=value1&param2=value2&param3=value3";
const queryParts = exampleUrl2.split('?')[1].split('&');
let param3manual;
for (let i = 0; i < queryParts.length; i++) {
    let pair = queryParts[i].split('=');
    if (pair[0] === 'param3') {
        param3manual = pair[1];
    }
}
console.log('param3 (manual):', param3manual);
}