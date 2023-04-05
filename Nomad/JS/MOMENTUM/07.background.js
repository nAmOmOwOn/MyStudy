const images = ["0.jpg", "1.JPG", "2.JPG"]; // 이미지 파일에 있는 것과 같은 배열이여야 함.

const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img"); // html 에 태그를 추가하는 코드

bgImage.src = `img/${chosenImage}`;

document.body.appendChild(bgImage);