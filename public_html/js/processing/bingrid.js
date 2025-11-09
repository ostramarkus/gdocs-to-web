function setup() {
    createCanvas(windowWidth, windowHeight);
    background(100);
    textFont('Courier New');
    textSize(10);
    fill(255, 30);
    frameRate(1);
    createBinGrid();
}

function draw() {
    if (frameCount % 10 == 0) {
        clear();
        createBinGrid();
    }
}

function createBinGrid() {

    cellSize = 10;
    for (let y = 0; y < height; y += cellSize) {
        for (let x = 0; x < width; x += cellSize) {
            let digit = round(random())
            text(digit, x, y);
        }
    }
}