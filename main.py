import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Parkour Obby Game", layout="wide")
st.title("🏃 Parkour Obby Game (Playable in Browser)")

# Embed JS/HTML game
components.html("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Parkour Obby</title>
  <style>
    body {
      margin: 0;
      overflow: hidden;
    }
    canvas {
      display: block;
      background: #e0f7fa;
    }
  </style>
</head>
<body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.min.js"></script>
<script>
let player;
let platforms = [];
let gravity = 0.6;
let jumpStrength = -12;
let level = 1;
let jumps = 0;
let goalReached = false;

function setup() {
  createCanvas(windowWidth, 400);
  player = new Player();
  generatePlatforms();
}

function draw() {
  background(224, 247, 250);
  
  for (let plat of platforms) {
    plat.show();
  }

  player.update();
  player.show();

  fill(0);
  textSize(18);
  text("Level: " + level + " / 5", 20, 30);
  text("Jumps: " + jumps + " / 25", 20, 55);

  if (goalReached) {
    fill(0, 200, 0);
    textSize(40);
    textAlign(CENTER);
    text("🏁 YOU WIN!", width/2, height/2);
    noLoop();
  }
}

function keyPressed() {
  if (key === ' ' || key === 'ArrowUp' || key === 'w') {
    if (player.onGround()) {
      player.vel.y = jumpStrength;
      jumps++;
      checkLevelProgress();
    }
  }
  if (key === 'ArrowRight' || key === 'd') {
    player.vel.x = 5;
  }
  if (key === 'ArrowLeft' || key === 'a') {
    player.vel.x = -5;
  }
}

function keyReleased() {
  if (key === 'ArrowRight' || key === 'ArrowLeft' || key === 'a' || key === 'd') {
    player.vel.x = 0;
  }
}

function checkLevelProgress() {
  if (level < 5 && jumps >= level * 5) {
    level++;
    generatePlatforms();
    player.pos.x = 50;
    player.pos.y = 50;
  }
  if (level === 5 && jumps >= 25) {
    goalReached = true;
  }
}

function generatePlatforms() {
  platforms = [];
  for (let i = 0; i < 6; i++) {
    platforms.push(new Platform(150 * i + 100, random(250, 350), 100, 20));
  }
  if (level === 5) {
    platforms.push(new Platform(900, 200, 100, 20)); // goal platform
  }
}

class Player {
  constructor() {
    this.pos = createVector(50, 50);
    this.vel = createVector(0, 0);
    this.size = 30;
  }

  update() {
    this.vel.y += gravity;
    this.pos.add(this.vel);

    if (this.pos.y + this.size > height) {
      this.pos.y = height - this.size;
      this.vel.y = 0;
    }

    for (let plat of platforms) {
      if (this.pos.x + this.size > plat.x && this.pos.x < plat.x + plat.w &&
          this.pos.y + this.size > plat.y && this.pos.y + this.size < plat.y + plat.h &&
          this.vel.y >= 0) {
        this.pos.y = plat.y - this.size;
        this.vel.y = 0;
      }
    }

    this.pos.x = constrain(this.pos.x, 0, width - this.size);
  }

  onGround() {
    if (this.pos.y + this.size >= height) return true;
    for (let plat of platforms) {
      if (this.pos.x + this.size > plat.x && this.pos.x < plat.x + plat.w &&
          this.pos.y + this.size === plat.y) {
        return true;
      }
    }
    return false;
  }

  show() {
    fill(255, 100, 100);
    rect(this.pos.x, this.pos.y, this.size, this.size);
  }
}

class Platform {
  constructor(x, y, w, h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  show() {
    fill(100, 200, 255);
    rect(this.x, this.y, this.w, this.h);
  }
}
</script>
</body>
</html>
""", height=450)

