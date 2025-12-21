// Game logic
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scale: {
        mode: Phaser.Scale.RESIZE,
        autoCenter: Phaser.Scale.CENTER_BOTH
    },
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
    // place car at the current center of the canvas
    car = this.physics.add.sprite(this.scale.width / 2, this.scale.height / 2, "rb19");

    // compute a base scale relative to the original design (800x600)
    const baseScale = Math.min(this.scale.width / 800, this.scale.height / 600) || 1;
    car.setScale(0.1 * baseScale);
    car.body.setSize(50 * baseScale, 100 * baseScale);

    // ensure physics world bounds match canvas size
    this.physics.world.setBounds(0, 0, this.scale.width, this.scale.height);
    car.setCollideWorldBounds(true);

    //getting the arrow keys
    cursors = this.input.keyboard.createCursorKeys();

    // orient the sprite so 'up' moves it forward
    car.setAngle(-90);

    //adding some physics stuff
    car.setDamping(true);
    car.setDrag(0.9); // this is to add friction
    car.setMaxVelocity(200);
    car.setAngularDrag(400);  //slowing rotation when not turning
    car.setVelocity(0,0); // this is to have no initial drift

    // handle window / canvas resize: update bounds, reposition and rescale
    this.scale.on('resize', (gameSize) => {
        const width = gameSize.width;
        const height = gameSize.height;

        this.physics.world.setBounds(0, 0, width, height);

        // reposition to center (optional: you may prefer to keep position)
        car.setPosition(width / 2, height / 2);

        const newBase = Math.min(width / 800, height / 600) || 1;
        car.setScale(0.1 * newBase);
        car.body.setSize(50 * newBase, 100 * newBase);
    });

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
