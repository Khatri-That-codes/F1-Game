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
const game = new Phaser.Game(config);

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
    this.load.image("rb19", "assets/rb-19.png");
}

function create(){
    // center of the screen is 400, 300
    // will need to adjust the dimensions in config if need to change
    car = this.physics.add.sprite(400,300, "rb19")
    
    // adjusting the car size -- will change maybe
    car.setScale(0.1)
    car.body.setSize(50,100)

    //reducing the bounce
    car.setCollideWorldBounds(true)

    //getting the arrow keys
    cursors = this.input.keyboard.createCursorKeys();


    car.setAngle(0); //facing upward

    //adding some physics stuff
    car.setDamping(true);
    car.setDrag(0.9); // this is to add friction
    car.setMaxVelocity(200)
    car.setAngularDrag(400)  //slowing rotation when not turning
    car.setVelocity(0,0) // this is to have no initial drift

}

function update(){
    //making sure not moving when no key pressed
    car.setAcceleration(0);
    car.setAngularVelocity(0);

    if (cursors.up.isDown){
        //move forward
        this.physics.velocityFromRotation(car.rotation - Math.PI / 2, 200, car.body.acceleration);

    }
    if (cursors.down.isDown){
        //move backward
        this.physics.velocityFromRotation(car.rotation - Math.PI / 2, -100, car.body.acceleration);

    }
    if (cursors.left.isDown){
        //rotate left
        car.setAngularVelocity(-150);
    }
    else if (cursors.right.isDown){
        //rotate right
        car.setAngularVelocity(150);
    }

}
