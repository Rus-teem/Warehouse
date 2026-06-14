/**
 * Заменяет текст в указанном элементе на актуальную дату
 * Используется для динамического обновления срока действия акции
 */

// Поиск контейнера для вставки даты
const dateContainer = document.querySelector("body > div");
if (!dateContainer) {
    console.warn('Container for date not found');
} else {
    // Формирование текущей даты в формате ДД.ММ.ГГГГ
    const now = new Date();
    const day = String(now.getDate());
    const month = String(now.getMonth() + 1);
    const year = String(now.getFullYear());
    const fullDate = day + '.' + month + '.' + year;

    // HTML-код с акционной вставкой
    const promoHtml = '<div class="tn-atom" field="tn_text_1708341700199" style="line-height: 20px;">'
        + 'Скидка на дизайн, ремонт 15% до <strong>' + fullDate + ' *</strong></div>';

    dateContainer.innerHTML = promoHtml;
}