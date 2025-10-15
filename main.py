import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>3D World</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #quitMessage {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-family: Arial, sans-serif;
            font-size: 24px;
            display: none;
        }
    </style>
</head>
<body>
    <div id="quitMessage">Quitting Game</div>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/PointerLockControls.js"></script>
    <script>
        // Your entire JS code here...
        // (I will leave it unchanged)
        
        // Scene setup
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x87CEEB);

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.y = 0.75;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        const controls = new THREE.PointerLockControls(camera, document.body);
        document.addEventListener('click', () => controls.lock());

        const ambientLight = new THREE.AmbientLight(0x646464, 0.5);
        scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(1, 1, 1);
        scene.add(directionalLight);

        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(2, 2, 2);
        scene.add(pointLight);

        const groundGeometry = new THREE.PlaneGeometry(100, 100);
        const groundMaterial = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
        const ground = new THREE.Mesh(groundGeometry, groundMaterial);
        ground.rotation.x = -Math.PI / 2;
        ground.position.y = 0;
        scene.add(ground);

        const ground1Geometry = new THREE.PlaneGeometry(100, 100);
        const ground1Material = new THREE.MeshStandardMaterial({
            color: 0x000000,
            opacity: 0.33,
            transparent: true
        });
        const ground1 = new THREE.Mesh(ground1Geometry, ground1Material);
        ground1.rotation.x = -Math.PI / 2;
        ground1.position.set(1, 1, 1);
        scene.add(ground1);

        const cubeTexture = new THREE.TextureLoader().load('tb.bmp');
        const cubeMaterial = new THREE.MeshStandardMaterial({ map: cubeTexture });

        const darkCubeMaterial = new THREE.MeshStandardMaterial({ color: 0x333333 });

        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        function onMouseDown(event) {
            if (event.button === 0) {
                const cube = new THREE.Mesh(
                    new THREE.BoxGeometry(1.5, 1.5, 1.5),
                    cubeMaterial
                );
                cube.position.copy(controls.getObject().position);
                cube.position.y -= 0.75;
                scene.add(cube);
            } else if (event.button === 2) {
                raycaster.setFromCamera(mouse, camera);
                const intersects = raycaster.intersectObjects(scene.children);
                if (intersects.length > 0) {
                    const normal = intersects[0].face.normal.clone();
                    const position = intersects[0].point.add(normal.multiplyScalar(0.75));
                    const cube = new THREE.Mesh(
                        new THREE.BoxGeometry(1.5, 1.5, 1.5),
                        darkCubeMaterial
                    );
                    cube.position.copy(position);
                    scene.add(cube);
                }
            }
        }

        function onKeyDown(event) {
            if (event.key === 'Escape') {
                document.getElementById('quitMessage').style.display = 'block';
                setTimeout(() => {
                    document.body.innerHTML = '<h1>Game Closed</h1>';
                }, 1000);
            }
        }

        window.addEventListener('mousedown', onMouseDown, false);
        window.addEventListener('keydown', onKeyDown, false);
        window.addEventListener('mousemove', (event) => {
            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
        });

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        function animate() {
            requestAnimationFrame(animate);

            if (controls.getObject().position.length() > 100) {
                document.getElementById('quitMessage').style.display = 'block';
                setTimeout(() => {
                    document.body.innerHTML = '<h1>Game Closed (Boundary Reached)</h1>';
                }, 1000);
            }

            renderer.render(scene, camera);
        }

        animate();
    </script>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=True)
