const formElement = document.getElementById('form1'); // извлекаем элемент формы
formElement.addEventListener('submit', (e) => {

    e.preventDefault(); // Отменяем стандартное исполненеи

    const formData = new FormData(formElement); // создаём объект FormData, передаём в него элемент формы

    // теперь можно извлечь данные
    const name = formData.get('name'); // 'John'
    const surname = formData.get('surname'); // 'Smith'
    alert(name)
    alert(surname)
    let years = prompt('Ваше имя?', name);
    alert('Вас ' + years + '  реально так зовут!')

    // Добавление данных в массив
    let arr = [];
    arr.push(name);
    arr.push(surname);

    // Вывод данных в консоль 
    console.info(arr)
    console.error(arr)
    console.warn(arr)

    //Загрузка данных в файл 
    //В массив записываем данные данные
    const blob = new Blob([arr], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'filename.txt';
    link.click();
    URL.revokeObjectURL(link.href);
});