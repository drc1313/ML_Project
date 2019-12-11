
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');

var painting = document.getElementById('paint');
var paint_style = getComputedStyle(painting);
canvas.width = parseInt(28);
canvas.height = parseInt(28);
var mouse = {x: 0, y: 0};

canvas.addEventListener('mousemove', function(e) {
mouse.x = e.pageX - this.offsetLeft;
mouse.y = e.pageY - this.offsetTop;
}, false);

ctx.lineWidth = 3;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = '#00CC99';

canvas.addEventListener('mousedown', function(e) {
ctx.beginPath();
ctx.moveTo(mouse.x, mouse.y);

canvas.addEventListener('mousemove', onPaint, false);
}, false);

canvas.addEventListener('mouseup', function() {
canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function() {
ctx.lineTo(mouse.x, mouse.y);
ctx.stroke();







};
function myFunction() {
   var img = canvas.toDataURL("image/png");
   document.write('<img src="'+img+'"/>');
}
