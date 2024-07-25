// Ждем загрузки DOM элементов
window.addEventListener("DOMContentLoaded", function () {
    // получили значение по селектору
    const phoneNum = document.querySelector('.t228__right_descr > div:nth-child(1) > a:nth-child(1)')
    
    // Кладем полученное значение в массив
    let arrPhone = [String(phoneNum)];

    // Вычленяем значение 
    let now1 = String(arrPhone[0].slice(4, 16))
    // преобразуем значение
    fullPhone = now1.slice(0, 2) + " (" + now1.slice(2, 5) + ") " + now1.slice(5, 8) + " - " + now1.slice(8, 10) + " - " + now1.slice(10, 12)
    // получаем дату
    let date = new Date(Date.now() + 86400e3);
    date = date.toUTCString();

    // Кладем значение в куки
    document.cookie = "managerPhone = " + fullPhone + "; SameSite=Lax; expires=" + date;
    document.cookie = "managerPhoneTel = " + arrPhone[0] + "; SameSite=Lax; expires=" + date;

    // Получаем значение cookie
    function getCookie(name) {
        let cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
        return cookie ? cookie.split('=')[1] : null;
    };
    // Кладем значение cookie в переменную 
    let managerPhoneCookie = getCookie('managerPhone')
    let managerPhoneTelCookie = getCookie('managerPhoneTel')

    console.log(this.document.cookie)
    console.log(managerPhoneTelCookie)

}, false);
