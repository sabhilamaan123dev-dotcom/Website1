import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>3D Obby Game</title>
  <style>
    body { margin: 0; overflow: hidden; }
    canvas { display: block; }
    #info {
      position: absolute;
      top: 10px;
      left: 10px;
      color: white;
      font-family: sans-serif;
      z-index: 1;
      background: rgba(0,0,0,0.5);
      padding: 8px 12px;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <div id="info">Use WASD + Mouse to move. Reach the end!</div>
  <script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.152.2/examples/js/controls/PointerLockControls.js"></script>

  <script>
    // Basic scene setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x87ceeb); // Sky blue

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Lighting
    const light = new THREE.HemisphereLight(0xffffff, 0x444444, 1);
    scene.add(light);

    // Player controls
    const controls = new THREE.PointerLockControls(camera, document.body);
    document.body.addEventListener('click', () => controls.lock());
    scene.add(controls.getObject());

    const velocity = new THREE.Vector3();
    const direction = new THREE.Vector3();
    const onGround = () => controls.getObject().position.y <= 1.5;

    // Ground
    const groundGeo = new THREE.BoxGeometry(100, 1, 100);
    const groundMat = new THREE.MeshStandardMaterial({ color: 0x228B22 });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.position.y = -0.5;
    scene.add(ground);

    // Platforms (obby style)
    const platformMat = new THREE.MeshStandardMaterial({ color: 0xff0000 });
    for (let i = 0; i < 10; i++) {
      const plat = new THREE.Mesh(new THREE.BoxGeometry(3, 0.5, 3), platformMat);
      plat.position.set(i * 5, 1, (i % 2 === 0 ? 0 : 2));
      scene.add(plat);
    }

    // Win zone
    const goal = new THREE.Mesh(new THREE.BoxGeometry(3, 0.5, 3), new THREE.MeshStandardMaterial({ color: 0x00ff00 }));
    goal.position.set(50, 1, 0);
    scene.add(goal);

    // Controls
    const keys = {};
    window.addEventListener('keydown', e => keys[e.code] = true);
    window.addEventListener('keyup', e => keys[e.code] = false);

    // Game loop
    camera.position.set(0, 2, 0);
    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      velocity.x -= velocity.x * 10.0 * delta;
      velocity.z -= velocity.z * 10.0 * delta;
      velocity.y -= 9.8 * 5.0 * delta; // gravity

      direction.z = Number(keys['KeyW']) - Number(keys['KeyS']);
      direction.x = Number(keys['KeyD']) - Number(keys['KeyA']);
      direction.normalize();

      if (direction.length() > 0) {
        velocity.z -= direction.z * 50.0 * delta;
        velocity.x -= direction.x * 50.0 * delta;
      }

      if (onGround() && keys['Space']) {
        velocity.y = 9;
      }

      controls.moveRight(-velocity.x * delta);
      controls.moveForward(-velocity.z * delta);
      controls.getObject().position.y += velocity.y * delta;

      if (onGround()) {
        velocity.y = Math.max(0, velocity.y);
        controls.getObject().position.y = 1.5;
      }

      // Check for win
      if (controls.getObject().position.distanceTo(goal.position) < 2) {
        alert("🏁 You reached the end! Reload to play again.");
      }

      // Check if player fell
      if (controls.getObject().position.y < -10) {
        controls.getObject().position.set(0, 2, 0);
        velocity.set(0, 0, 0);
      }

      renderer.render(scene, camera);
    }

    animate();
  </script>
</body>
</html>

"""

components.html(html_code, height=800, scrolling=True)
