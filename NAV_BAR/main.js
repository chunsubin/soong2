// toogleBtn으로 쓰여진 클래스를 toggleBtn에 연결해준다
const toggleBtn = document.querySelector('.navbar__toogleBtn');
const menu=document.querySelector('.navbar__menu');
const icons=document.querySelector('.navbar__icons');

// 버튼이 클릭될때의 함수 작성
toggleBtn.addEventListener('click',() => {
    menu.classList.toggle('active');
    icons.classList.toggle('active');
    // 토글링해주는가정
    // active가 있다면 active를 빼고, acvie가 없다면 넣어준다.
    // 켰다 꺼졌다 기능을 해주는 것
});
