(function() {
    // 1) Ваш список сайтов
    const valuesToCheck = [
      "103.by", 
      "adme.media",
      "aif.ru",
      // ... Добавьте все нужные домены ...
    ];
  
    // 2) Основная функция — отрабатывает один раз
    function checkAllCheckboxesOneTime() {
      console.log("Скрипт выполняется ОДИН РАЗ — отмечаем чекбоксы...");
  
      // Ищем все чекбоксы
      const checkboxes = document.querySelectorAll('input[type="checkbox"]');
      console.log("Найдено чекбоксов:", checkboxes.length);
  
      checkboxes.forEach(checkbox => {
        const row = checkbox.closest('tr');
        if (!row) return;
  
        // Текст строки, в нижнем регистре
        const rowText = row.innerText.toLowerCase();
  
        for (const domain of valuesToCheck) {
          if (rowText.includes(domain.toLowerCase())) {
            console.log(`Совпадение: "${domain}" → отмечаем чекбокс`, checkbox);
            checkbox.checked = true;
            // Можно сгенерировать событие при необходимости:
            // checkbox.dispatchEvent(new Event("change", { bubbles: true }));
            break;
          }
        }
      });
  
      console.log("Скрипт отработал один раз и завершается.");
    }
  
    // 3) Запускаем отработку один раз и всё
    checkAllCheckboxesOneTime();
  
    // Нет никакого MutationObserver или таймера → скрипт не повторяется.
  })();
  