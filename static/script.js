document.addEventListener(
"DOMContentLoaded",
()=>{

const card =
document.querySelector(
".dashboard-card"
);

card.addEventListener(
"mousemove",
(e)=>{

const rect =
card.getBoundingClientRect();

const x =
e.clientX-rect.left;

const y =
e.clientY-rect.top;

const rotateY =
((x/rect.width)-0.5)*8;

const rotateX =
((y/rect.height)-0.5)*-8;

card.style.transform=
`perspective(1000px)
rotateX(${rotateX}deg)
rotateY(${rotateY}deg)`;

});

card.addEventListener(
"mouseleave",
()=>{

card.style.transform=
"perspective(1000px) rotateX(0) rotateY(0)";

});

});