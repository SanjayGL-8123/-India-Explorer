import React, { useEffect, useRef, useState } from "react";
import * as THREE from "three";

export default function Globe(): React.JSX.Element {
  const containerRef = useRef<HTMLDivElement>(null);
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    // Dimensions
    let width = Math.min(container.clientWidth || 400, 480);
    let height = width;

    // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
    camera.position.z = 2.8;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(width, height);
    container.appendChild(renderer.domElement);

    // Globe Group for rotation
    const globeGroup = new THREE.Group();
    // Tilt globe roughly matching Earth's 23.5-degree axial tilt
    globeGroup.rotation.z = (23.5 * Math.PI) / 180;
    scene.add(globeGroup);

    // 1. Core Sphere (Dark navy blue with subtle glow)
    const sphereGeo = new THREE.SphereGeometry(1, 48, 48);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0x0f172a,
      transparent: true,
      opacity: 0.85,
    });
    const coreSphere = new THREE.Mesh(sphereGeo, sphereMat);
    globeGroup.add(coreSphere);

    // 2. Latitude & Longitude Wireframe Grid
    const wireframeMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      wireframe: true,
      transparent: true,
      opacity: 0.22,
    });
    const gridMesh = new THREE.Mesh(sphereGeo, wireframeMat);
    globeGroup.add(gridMesh);

    // 3. Equator and Prime Meridian Highlight Rings
    const ringGeo = new THREE.RingGeometry(1.002, 1.006, 64);
    const ringMat = new THREE.MeshBasicMaterial({
      color: 0xf59e0b,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.4,
    });
    const equator = new THREE.Mesh(ringGeo, ringMat);
    equator.rotation.x = Math.PI / 2;
    globeGroup.add(equator);

    // 4. Outer Atmosphere Glow
    const atmosGeo = new THREE.SphereGeometry(1.04, 32, 32);
    const atmosMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.08,
      side: THREE.BackSide,
    });
    const atmosphere = new THREE.Mesh(atmosGeo, atmosMat);
    scene.add(atmosphere);

    // 5. India Location Coordinates (Lat: ~20.59° N, Lon: ~78.96° E)
    const lat = 20.59;
    const lon = 78.96;
    const phi = (90 - lat) * (Math.PI / 180);
    const theta = (lon + 180) * (Math.PI / 180);
    const radius = 1.01;

    const x = -(radius * Math.sin(phi) * Math.cos(theta));
    const z = radius * Math.sin(phi) * Math.sin(theta);
    const y = radius * Math.cos(phi);

    // Marker Pin for India
    const pinGroup = new THREE.Group();
    pinGroup.position.set(x, y, z);

    // Center dot (Saffron)
    const pinGeo = new THREE.SphereGeometry(0.035, 16, 16);
    const pinMat = new THREE.MeshBasicMaterial({ color: 0xf97316 });
    const pin = new THREE.Mesh(pinGeo, pinMat);
    pinGroup.add(pin);

    // Pulsing outer beacon ring
    const beaconGeo = new THREE.RingGeometry(0.045, 0.065, 32);
    const beaconMat = new THREE.MeshBasicMaterial({
      color: 0xfbbf24,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.8,
    });
    const beacon = new THREE.Mesh(beaconGeo, beaconMat);
    // Align ring to sphere normal
    beacon.lookAt(new THREE.Vector3(x * 2, y * 2, z * 2));
    pinGroup.add(beacon);

    globeGroup.add(pinGroup);

    // 6. Interactive Drag Controls
    let isDragging = false;
    let previousMousePosition = { x: 0, y: 0 };
    let dragVelocity = { x: 0.0025, y: 0 };

    const onPointerDown = (e: PointerEvent) => {
      isDragging = true;
      previousMousePosition = { x: e.clientX, y: e.clientY };
    };

    const onPointerMove = (e: PointerEvent) => {
      if (!isDragging) return;
      const deltaX = e.clientX - previousMousePosition.x;
      const deltaY = e.clientY - previousMousePosition.y;

      globeGroup.rotation.y += deltaX * 0.008;
      globeGroup.rotation.x += deltaY * 0.008;

      dragVelocity = { x: deltaX * 0.001, y: deltaY * 0.001 };
      previousMousePosition = { x: e.clientX, y: e.clientY };
    };

    const onPointerUp = () => {
      isDragging = false;
    };

    const domElement = renderer.domElement;
    domElement.style.touchAction = "none";
    domElement.addEventListener("pointerdown", onPointerDown);
    window.addEventListener("pointermove", onPointerMove);
    window.addEventListener("pointerup", onPointerUp);

    // Resize observer for responsive canvas
    const handleResize = () => {
      if (!container) return;
      const newWidth = Math.min(container.clientWidth || 400, 480);
      camera.aspect = 1;
      camera.updateProjectionMatrix();
      renderer.setSize(newWidth, newWidth);
    };
    window.addEventListener("resize", handleResize);

    // Animation Loop
    let animId = 0;
    let pulseScale = 1;
    let pulseDirection = 1;

    const animate = () => {
      animId = requestAnimationFrame(animate);

      if (!isDragging) {
        // Natural rotation & inertia dampening
        globeGroup.rotation.y += dragVelocity.x;
        globeGroup.rotation.x += dragVelocity.y;
        dragVelocity.x = THREE.MathUtils.lerp(dragVelocity.x, 0.003, 0.02);
        dragVelocity.y = THREE.MathUtils.lerp(dragVelocity.y, 0, 0.02);
      }

      // Marker pulse effect
      pulseScale += 0.015 * pulseDirection;
      if (pulseScale > 1.4) pulseDirection = -1;
      if (pulseScale < 0.9) pulseDirection = 1;
      beacon.scale.set(pulseScale, pulseScale, pulseScale);

      renderer.render(scene, camera);
    };
    animate();

    return () => {
      cancelAnimationFrame(animId);
      domElement.removeEventListener("pointerdown", onPointerDown);
      window.removeEventListener("pointermove", onPointerMove);
      window.removeEventListener("pointerup", onPointerUp);
      window.removeEventListener("resize", handleResize);
      renderer.dispose();
      sphereGeo.dispose();
      wireframeMat.dispose();
      sphereMat.dispose();
      if (container.contains(domElement)) {
        container.removeChild(domElement);
      }
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="globe-container"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      aria-label="Interactive 3D Globe of India"
    >
      <div className={`globe-hint ${isHovered ? "visible" : ""}`}>
        🖱️ Drag to rotate • India beacon highlighted
      </div>
    </div>
  );
}
