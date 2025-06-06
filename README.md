<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Insiders Guide to Hong Kong</title>
  <style>
    body {
      margin: 0;
      padding: 20px;
      font-family: Arial, sans-serif;
      position: relative;
      color: white; /* Ensure text is readable over animated background */
    }

    /* Canvas for screensaver effect */
    #backgroundCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1; /* Place behind content */
    }

    .MainHeader {
      color: red; /* Matches your original red headers */
      text-align: center;
    }

    .FirstPara, .SecondPara {
      color: white;
      text-align: center;
    }

    .content-div {
      border: 1px solid red;
      padding: 10px;
      margin-bottom: 20px;
      background: rgba(0, 0, 0, 0.5); /* Semi-transparent background for readability */
      border-radius: 5px;
    }

    img {
      display: block;
      margin: 0 auto;
    }

    iframe {
      display: block;
      margin: 0 auto;
    }

    .youtube-button {
      background-color: rgba(200, 0, 0);
      color: white;
      border: none;
      height: 36px;
      width: 105px;
      border-radius: 5px;
      cursor: pointer;
      margin-right: 8px;
    }

    .facebook-button {
      background-color: rgb(2, 158, 255);
      color: rgb(242, 243, 245);
      border: none;
      height: 40px;
      width: 95px;
      border-radius: 18px;
      font-weight: bold;
      font-size: 15px;
      cursor: pointer;
    }

    .button-container {
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- Canvas for screensaver background -->
  <canvas id="backgroundCanvas"></canvas>

  <h1 title="You are hovering over my header" class="MainHeader">
    The Insiders Guide to Hong Kong
  </h1>

  <h3 title="You are hovering over my header" class="MainHeader">
    Hong Kong Hacks, Adventures, and Lifestyle Tips
  </h3>

  <div class="content-div">
    <p class="FirstPara">
      Here is an AI-generated image I made:
    </p>
    <img src="https://github.com/merulzthecryptoverse/merulzthecryptoverse.github.io/blob/Images/465237508_122101090316596174_6996163836068378838_n%20-%20Copy.jpg?raw=true" alt="Surfs up in HongKong">
  </div>

  <div class="content-div">
    <p class="FirstPara">
      Here is an AI-generated video I made:
    </p>
    <iframe width="308" height="174" src="https://www.youtube.com/embed/kns6AtI2XQE?si=qx2LNgDLWe4p4W0J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>

  <div class="content-div">
    <p class="SecondPara">
      Here are some buttons I made:
    </p>
    <div class="button-container">
      <button onclick="window.location.href='https://www.youtube.com/@HongKongHacks';" class="youtube-button">
        YOUTUBE
      </button>
      <button onclick="window.location.href='https://www.facebook.com/pit.shoster.200585';" class="facebook-button">
        FACEBOOK
      </button>
    </div>
    <p class="SecondPara">
      I hope you enjoy clicking around.
    </p>
  </div>

  <script>
    // Mystify Your Mind-inspired screensaver
    const canvas = document.getElementById('backgroundCanvas');
    const ctx = canvas.getContext('2d');

    // Set canvas size to window size
    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Line object for animation
    class Line {
      constructor() {
        this.x1 = Math.random() * canvas.width;
        this.y1 = Math.random() * canvas.height;
        this.x2 = this.x1 + (Math.random() * 100 - 50);
        this.y2 = this.y1 + (Math.random() * 100 - 50);
        this.vx1 = (Math.random() * 4 - 2);
        this.vy1 = (Math.random() * 4 - 2);
        this.vx2 = (Math.random() * 4 - 2);
        this.vy2 = (Math.random() * 4 - 2);
        this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
      }

      update() {
        this.x1 += this.vx1;
        this.y1 += this.vy1;
        this.x2 += this.vx2;
        this.y2 += this.vy2;

        // Bounce off walls
        if (this.x1 < 0 || this.x1 > canvas.width) this.vx1 *= -1;
        if (this.y1 < 0 || this.y1 > canvas.height) this.vy1 *= -1;
        if (this.x2 < 0 || this.x2 > canvas.width) this.vx2 *= -1;
        if (this.y2 < 0 || this.y2 > canvas.height) this.vy2 *= -1;
      }

      draw() {
        ctx.beginPath();
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 2;
        ctx.moveTo(this.x1, this.y1);
        ctx.lineTo(this.x2, this.y2);
        ctx.stroke();
      }
    }

    // Create multiple lines
    const lines = Array.from({ length: 20 }, () => new Line());

    // Animation loop
    function animate() {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.1)'; // Fade effect
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      lines.forEach(line => {
        line.update();
        line.draw();
      });

      requestAnimationFrame(animate);
    }
    animate();
  </script>
</body>
</html>
