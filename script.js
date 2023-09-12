const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
let drawing = false;
let points = [];
let img = new Image();

document.getElementById("imageUpload").addEventListener("change", function (e) {
  const file = e.target.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0, img.width, img.height);
    };
    img.src = e.target.result;
  };

  reader.readAsDataURL(file);
});

document.getElementById("clearBtn").addEventListener("click", function () {
    clearPoints();
  });

canvas.addEventListener("mousedown", function (e) {
  const x = e.clientX - canvas.offsetLeft;
  const y = e.clientY - canvas.offsetTop;
  points.push({ x, y });
  drawPolygon();
});

document.getElementById("exportBtn").addEventListener("click", function () {
  exportPointsToTxt();
});

function drawPolygon() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, 0, 0, img.width, img.height);

  if (points.length > 0) {
    ctx.beginPath();
    ctx.moveTo(points[0].x, points[0].y);

    for (let i = 1; i < points.length; i++) {
      ctx.lineTo(points[i].x, points[i].y);
    }

    if (points.length > 2) {
      ctx.closePath();
    }

    ctx.fillStyle = "red";
    points.forEach(function(point) {
      ctx.fillRect(point.x - 2, point.y - 2, 4, 4);
    });

    ctx.strokeStyle = "red";
    ctx.stroke();
  }
}

function exportPointsToTxt() {
  const pointsStr = points.map(p => `${p.x},${p.y}`).join('\n');
  const blob = new Blob([pointsStr], { type: 'text/plain' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'points.txt';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function clearPoints() {
    points = [];
    drawPolygon();
  }