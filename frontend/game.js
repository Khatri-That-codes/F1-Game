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
    //TODO: add car sprite
    //TODO: enable keyboard controls
}

function update(){
    //TODO: handle movement
}
