function hideAtDateTime(selector, year, month, day, hour, minute, second = 0) {
    // month: 1-12 (как обычно у людей), внутри переведём в 0-11
    const target = new Date(year, month - 1, day, hour, minute, second, 0);
    const now = new Date();
    const delay = target.getTime() - now.getTime();

    const hide = () => {
        const el = document.querySelector(selector);
        if (el) el.style.display = "none";
    };

    if (delay <= 0) {
        hide(); // дата уже прошла — скрываем сразу
        return;
    }

    setTimeout(hide, delay);
}

// пример: скрыть #myBlock 30 января 2026 в 14:05
hideAtDateTime("#myBlock", 2026, 3, 1, 0, 0);