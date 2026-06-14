// Извлекает номер телефона из DOM и сохраняет в куки

window.addEventListener("DOMContentLoaded", function () {
    // Поиск ссылки с номером телефона по селектору
    const phoneLink = document.querySelector('.t228__right_descr > div:nth-child(1) > a:nth-child(1)');
    if (!phoneLink) return;

    // Извлечение номера из href (tel:XXXXXXXXXXXX) или текста ссылки
    const phoneRaw = phoneLink.href || phoneLink.textContent || '';

    // Очистка номера от всего кроме цифр
    const digits = phoneRaw.replace(/\D/g, '');
    // Форматирование в вид: XX (XXX) XXX - XX - XX
    const fullPhone = digits.slice(0, 2) + ' (' + digits.slice(2, 5) + ') ' + digits.slice(5, 8) + ' - ' + digits.slice(8, 10) + ' - ' + digits.slice(10, 12);

    // Дата истечения куки (1 день)
    const expires = new Date(Date.now() + 86400e3).toUTCString();

    // Сохранение в куки
    document.cookie = 'managerPhone=' + fullPhone + '; SameSite=Lax; expires=' + expires;
    document.cookie = 'managerPhoneTel=' + phoneRaw + '; SameSite=Lax; expires=' + expires;

    // Возвращает значение куки по имени
    function getCookie(name) {
        const match = document.cookie.split('; ').find(row => row.startsWith(name + '='));
        return match ? match.split('=')[1] : null;
    }

    const managerPhoneCookie = getCookie('managerPhone');
    const managerPhoneTelCookie = getCookie('managerPhoneTel');

    console.log('Cookies:', document.cookie);
    console.log('Phone tel:', managerPhoneTelCookie);
}, false);
