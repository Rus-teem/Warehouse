// Изменение CSS-стилей элементов на странице

// Пример обращения к элементу по ID
let elemId = document.getElementById('youtubeiframe764123363');

// Поиск элемента через селектор и перезапись его CSS
let elem = document.querySelector(".t1000__background-image");
elem.style.cssText = 'border: 1px solid black';

// Устанавливает скругление углов и обводку для видео-элементов после загрузки DOM
window.addEventListener("DOMContentLoaded", function () {
    let elemVideo = document.querySelector('.t-video-lazyload');
    let elemIframe = document.querySelector('.t-video-lazyload > iframe');
    if (elemIframe) {
        elemIframe.style.cssText = 'border: 1px solid black; border-radius: 30px';
    }
    if (elemVideo) {
        elemVideo.style.cssText = 'border-radius: 30px';
    }
}, false);
