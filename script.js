const element = document.getElementById("menu");
element.addEventListener("click", myFunction);

function myFunction() {
 	$(".navigation").slideToggle();
}

gsap.from("#txt", {
	scrollTrigger: {
		scrub: true
	},
	x: 350
});
gsap.from("#m1", {
	scrollTrigger: {
		scrub: true
	},
	y: 100
});
gsap.from("#m2", {
	scrollTrigger: {
		scrub: true
	},
	y: 50
});
gsap.from("#m3", {
	scrollTrigger: {
		scrub: true
	},
	y: 200
});
gsap.from("#m4", {
	scrollTrigger: {
		scrub: true
	},
	y: 150
});
gsap.from("#tr", {
	scrollTrigger: {
		scrub: true
	},
	y: 150
});
gsap.from("#crs", {
	scrollTrigger: {
		scrub: true
	},
	y: 100
});
gsap.from("#house", {
	scrollTrigger: {
		scrub: true
	},
	y: 50
});
// Initialize Particle.js for the welcome section
particlesJS("particles-js", {
    "particles": {
        "number": {
            "value": 50,   // Number of particles
            "density": {
                "enable": true,
                "value_area": 800  // Area for particles to spread
            }
        },
        "color": {
            "value": "#ffffff"  // Particle color (white)
        },
        "shape": {
            "type": "circle",  // Shape of the particles (circle)
            "stroke": {
                "width": 0,
                "color": "#000000"
            }
        },
        "opacity": {
            "value": 0.5,
            "random": true,  // Random opacity for particles
            "anim": {
                "enable": true,
                "speed": 1,
                "opacity_min": 0.1
            }
        },
        "size": {
            "value": 5,
            "random": true,  // Random size for particles
            "anim": {
                "enable": true,
                "speed": 1,
                "size_min": 0.1
            }
        },
        "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",  // Line color connecting particles
            "opacity": 0.4,
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 3,
            "direction": "none",
            "random": true,
            "straight": false,
            "out_mode": "out",
            "bounce": false
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"  // Particles will move away when mouse hovers over them
            },
            "onclick": {
                "enable": true,
                "mode": "push"  // New particles will be added when clicked
            }
        }
    },
    "retina_detect": true
});
