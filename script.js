document.addEventListener("DOMContentLoaded", function () {

    // 1. 滾動淡入動畫 (Intersection Observer)
    const fadeElements = document.querySelectorAll('.fade-in-section');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // 當區塊進入視窗時，加上 is-visible 觸發 CSS 動畫
                entry.target.classList.add('is-visible');
                // 觸發後即停止監聽該元素，讓動畫只跑一次
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15 // 元素露出 15% 時觸發
    });

    fadeElements.forEach(element => {
        observer.observe(element);
    });

    // 2. 生活紀錄分頁切換
    const lifePageEls = document.querySelectorAll('.life-page');
    const lifeDotEls = document.querySelectorAll('.life-page-dot');
    let currentLifePage = 0;

    function showLifePage(index) {
        lifePageEls.forEach(function (p) { p.classList.add('d-none'); });
        lifeDotEls.forEach(function (d) { d.classList.remove('active'); });
        lifePageEls[index].classList.remove('d-none');
        lifeDotEls[index].classList.add('active');
        currentLifePage = index;
    }

    document.getElementById('lifePrevBtn').addEventListener('click', function () {
        showLifePage((currentLifePage - 1 + lifePageEls.length) % lifePageEls.length);
    });

    document.getElementById('lifeNextBtn').addEventListener('click', function () {
        showLifePage((currentLifePage + 1) % lifePageEls.length);
    });

    lifeDotEls.forEach(function (dot, i) {
        dot.addEventListener('click', function () { showLifePage(i); });
    });

    // 3. 導覽列滾動陰影特效
    const navbar = document.querySelector('.custom-navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            // 往下滾動超過 50px 時，加上淡淡的陰影
            navbar.style.boxShadow = '0 5px 20px rgba(74, 60, 49, 0.08)';
        } else {
            // 回到頂部時取消陰影
            navbar.style.boxShadow = 'none';
        }
    });

});