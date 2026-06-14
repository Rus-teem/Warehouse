/**
 * Автоматически отмечает чекбоксы в таблице, если строка содержит домен из списка.
 * Запускается один раз после загрузки скрипта.
 */
(function() {
    const valuesToCheck = [
        "103.by",
        "adme.media",
        "aif.ru",
    ];

    function checkAllCheckboxesOneTime() {
        console.log("Скрипт выполняется ОДИН РАЗ — отмечаем чекбоксы...");

        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        console.log("Найдено чекбоксов:", checkboxes.length);

        checkboxes.forEach(checkbox => {
            const row = checkbox.closest('tr');
            if (!row) return;

            const rowText = row.innerText.toLowerCase();

            for (const domain of valuesToCheck) {
                if (rowText.includes(domain.toLowerCase())) {
                    console.log(`Совпадение: "${domain}" → отмечаем чекбокс`, checkbox);
                    checkbox.checked = true;
                    break;
                }
            }
        });

        console.log("Скрипт отработал один раз и завершается.");
    }

    checkAllCheckboxesOneTime();
})();
