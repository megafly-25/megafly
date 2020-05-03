var swiper = new Swiper('.s1', {
    slidesPerView: 7,
    spaceBetween: 3,
    slidesPerGroup: 7,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },


});

var swiper2 = new Swiper('.s2', {
    spaceBetween: 5,
    centeredSlides: true,
    autoplay: {
        delay: 5500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    debugger: true,
});
var swiper3 = new Swiper('.s3', {
    slidesPerView: 3,
    spaceBetween: 3,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },


});