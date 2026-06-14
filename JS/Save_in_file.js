/*
 * Пример HTML-формы:
 * <form id="form1">
 *   <input type="text" id="name" name="name" value="John">
 *   <input type="text" name="surname" value="Smith">
 *   <input type="submit">
 * </form>
 */

// Обработчик отправки формы — извлекает данные и сохраняет в файл
const formElement = document.getElementById('form1');

if (formElement) {
    formElement.addEventListener('submit', (e) => {
        e.preventDefault();

        const formData = new FormData(formElement);
        const name = formData.get('name');
        const surname = formData.get('surname');

        alert(name);
        alert(surname);

        const years = prompt('Ваше имя?', name);
        alert('Вас ' + years + ' реально так зовут!');

        // Сбор данных в массив
        const data = [name, surname];

        console.info('Data:', data);

        // Создание и скачивание текстового файла
        const blob = new Blob([data.join('\n')], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'form-data.txt';
        link.click();
        URL.revokeObjectURL(link.href);
    });
}