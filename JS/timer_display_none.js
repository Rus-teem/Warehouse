/**
 * Скрывает элемент в заданное время.
 * @param {string} selector - CSS-селектор элемента
 * @param {number} year - год
 * @param {number} month - месяц (1-12)
 * @param {number} day - день
 * @param {number} hour - часы
 * @param {number} minute - минуты
 * @param {number} [second=0] - секунды
 */
function hideAtDateTime(selector, year, month, day, hour, minute, second = 0) {
    const target = new Date(year, month - 1, day, hour, minute, second, 0);
    const now = new Date();
    const delay = target.getTime() - now.getTime();

    const hide = () => {
        const el = document.querySelector(selector);
        if (el) el.style.display = "none";
    };

    if (delay <= 0) {
        hide();
        return;
    }

    setTimeout(hide, delay);
}

// Пример: скрыть #myBlock 1 марта 2026 в 00:00
hideAtDateTime("#myBlock", 2026, 3, 1, 0, 0);
