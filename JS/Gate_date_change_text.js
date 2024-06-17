{/* <script> */}
    // Получаю  данные по селектору 
    let getDateOnClass = document.querySelector("body > div");
    //let getDateOnClass = document.querySelector('html.no-touch body.t-body div#allrecords.t-records div#rec708404688.r.t-rec.t-rec_pt_0.t-rec_pb_0 div.t396 div.t396__artboard.rendered.t396__artboard_scale div.t396__elem.tn-elem.tn-elem__7084046881708341700199.t-animate.t-animate_started div.tn-atom__scale-wrapper div.tn-atom');
    // Получил дату сегодня
    let nowDate = new Date();
    //Вынул из даты значения
    let nowDate2 = {
        a: nowDate.getDate(),
    // Прибавляю месяц 
    b: nowDate.getMonth() + 1,
    c: nowDate.getFullYear(),
    };
    // Получил значение даты в строке 
    day = String(nowDate2.a);
    month = String(nowDate2.b);
    year = String(nowDate2.c);
    empty = "."
    // Получил полную дату 
    fullDate = day + empty + month + empty + year;
    // Подготовил новые стили и текст для замены 
    changeDateClass =
    '<div class="tn-atom" field="tn_text_1708341700199" style="line-height: 20px;">Скидка на дизайн, ремонт 15% до <strong>';
        changeDateClass2 = " *</strong></div> ";
    // Полный текст для замены 
    changeDateClass3 = changeDateClass + fullDate + changeDateClass2;
    // Заменил значение на странице 
    getDateOnClass.innerHTML = changeDateClass3;
{/* </script> */}