// Game logic
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            debug: false
        }
    },

    scene: {
        preload: preload,
        create: create, 
        update: update
    }
};

//const - no reassignment
const game = new phaser.Game(config);

//global var
let car;
let cursors;

/**
 * preload - load images
 * create - places objects on screen
 * update - runs 60 times/sec - movement and logic
 */


// scene functions
function preload(){
    this.load.image("rb21", "assets/rb-19/png");
}

function create(){
    // center of the screen is 400, 300
    // will need to adjust the dimensions in config if need to change
    car = this.physics.add.sprite(400,300, "rb21")
    
    // adjusting the car size -- will change maybe
    car.setScale(0.5)

    //reducing the bounce
    car.setCollideWorldBounds(true)

    //getting the arrow keys
    cursors = this.input.keyboard.createCursorKeys();
}

function update(){
    //TODO: handle movement
}
