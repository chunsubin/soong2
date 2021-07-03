// toogleBtn으로 쓰여진 클래스를 toggleBtn에 연결해준다
const toggleBtn = document.querySelector('.navbar__toogleBtn');
const menu=document.querySelector('.navbar__menu');
const icons=document.querySelector('.navbar__icons');

// 버튼이 클릭될때의 함수 작성
toggleBtn.addEventListener('click',() => {
    menu.classList.toggle('active');
    icons.classList.toggle('active');
});
