let noiseRes = 0.01;
let noiseSpeed = 0.01;

function setup() {
	createCanvas(windowWidth, windowHeight);
	background(100);
   textFont('Courier New');
   textSize(10);
	fill(255, 30);
	frameRate(20);
   createBinGrid();		
	noStroke();
}

function draw() {
	clear();
	createBinGrid();
}

function createBinGrid() {
	noStroke();
	cellSize = 24;
	for (let y = 0; y < height; y += cellSize) {
		for (let x = 0; x < width; x += cellSize) {
			let alpha = noise(x * noiseRes, y * noiseRes, frameCount * noiseSpeed);
			fill(0, alpha * 200);
			rect(x, y, cellSize - 1, cellSize - 1);
			let digit = round(random())

		}		
	}
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
  }