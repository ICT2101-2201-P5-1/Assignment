
/**
* Checks the number of command stack in the workspace
* @param    cmdStack    1-D JavaScript array of Blockly TOP blocks from our workspace
* @return               returns boolean
*/
function checkCommandStack(cmdStack){
    if(cmdStack.length == 1)
        return true;
    else
        return false;
}

/**
* Updates the HTML variable according to the collect coin or car crash scenario.
*/
function collectCoin(){
    var coinsCollected = parseInt(document.getElementById("coinsCollected").innerHTML, 10);
    document.getElementById("coinsCollected").innerHTML = ++coinsCollected;
    console.log("collect coin");
}

function carCrashed(){
    var carCrashes = parseInt(document.getElementById("carCrashes").innerHTML, 10);
    document.getElementById("carCrashes").innerHTML = ++carCrashes;
}

/**
* Sends a post request to CoolMotor controller when game is won.
*/
function winGame(){
    alert("YOU WIN");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        win: 1,
        map_id: document.getElementById("map_id").innerHTML,
        map_difficulty: document.getElementById("map_difficulty").innerHTML,
        game_minutes: document.getElementById("game_minutes").innerHTML,
        game_seconds: document.getElementById("game_seconds").innerHTML,
        dist_travelled: 20 // hardcoded placeholder value.
//        dist_travelled: document.getElementById("dist_travelled").innerHTML
    }));
}

/**
* Sends a post request to CoolMotor controller when game is won.
*/
function sendCommands(commands){
    // alert("sent to cAR");
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        commands: commands
    }));
}



/**
* parse the command stack. recursive function.
* @param    cmdStack    1-D JavaScript array of Blockly blocks from our workspace
* @param    workspace   Blockly workspace object
* @param    map         1-D JavaScript array that holds the map layout. (global variable)
*           map format:
*           0 = empty
*           1 = car
*           2 = wall
*           3 = coin
*           4 = goal
* @param    carPos      holds the car position (int)
* @param    win         determines if the player has won or not (global variable, int)
*/
async function parseCommands(cmdStack, workspace, map){
    var commands = [];

    for (let i = 0; i < map.tiles.length; i++){
        if (map.tiles[i] == "1"){
            carPos = i;
            break;
        }
    }

    // give our for-loop a label so we can break out of it later
    parseCommandsLoop:
    for (let i = 0; i < cmdStack.length; i++){
        console.log(cmdStack[i].type);

        // check whether all inputs are filled.
        if (cmdStack[i].allInputsFilled() == false){
            alert("Some blocks have empty inputs. Please ensure it has at least one nested command.")
            return false;
        }

        switch(cmdStack[i].type){
            case "upward":

                // hit boundary wall
                if ((carPos - 5) < 0){
                    // car crash
                    carCrashed();
                    return 1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos - 5] == 2){
                        // car crash
                        carCrashed();
                        return 1;
                    }

                    // moves to empty space
                    else{

                        // collect coins
                        if (map.tiles[carPos - 5] == 3){
                            collectCoin();
                        }
                        // if next tile is goal
                        else if (map.tiles[carPos - 5] == 4){
                            win = 1;
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos -= 5;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);
                        commands.push("upward");
                        sendCommands(commands);
                        commands = [];

                        // delay for animation purposes
                        await sleep(500);

                        // win game
                        if(win == 1){
                            winGame();
                            return 1;
                        }
                    }
                }
                break;

            case "downward":

                // hit boundary wall
                if ((carPos + 5) > 24){
                    // car crash
                    carCrashed();
                    return 1;
                }
                // allowed to move
                else{

                    // hits virtual wall
                    if (map.tiles[carPos + 5] == 2){
                        // car crash
                        carCrashed();
                        return 1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos + 5] == 3){
                            collectCoin();
                        }
                        // if next tile is goal
                        else if (map.tiles[carPos + 5] == 4){
                            win = 1;
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos += 5;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);
                        commands.push("downward");
                        sendCommands(commands);
                        commands = [];

                        // delay for animation purposes
                        await sleep(500);

                        // win game
                        if(win == 1){
                            winGame();
                            return 1;
                        }
                    }
                }
                break;

            case "left":

                // hit boundary wall
                // NOTE: the LEFT block has an extra check for value '-1' due to the JS negative modulo bug
                if (((carPos - 1) % 5 == 4) || ((carPos - 1) % 5 == -1)){
                    // car crash
                    carCrashed();
                    return 1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos - 1] == 2){
                        // car crash
                        carCrashed();
                        return 1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos - 1] == 3){
                            collectCoin();
                        }
                        // if next tile is goal
                        else if (map.tiles[carPos - 1] == 4){
                            win = 1;
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos -= 1;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);
                        commands.push("left");
                        sendCommands(commands);
                        commands = [];
                        

                        // delay for animation purposes
                        await sleep(500);

                        // win game
                        if(win == 1){
                            winGame();
                            return 1;
                        }
                    }
                }
                break;

            case "right":
                // hit boundary wall
                if ((carPos + 1) % 5 == 0){
                    // car crash
                    carCrashed();
                    return 1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos + 1] == 2){
                        carCrashed();
                        return 1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos + 1] == 3){
                            collectCoin();
                        }
                        // if next tile is goal
                        else if (map.tiles[carPos + 1] == 4){
                            win = 1;
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos += 1;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);
                        commands.push("right");
                        sendCommands(commands);
                        commands = [];

                        // delay for animation purposes
                        await sleep(500);

                        // win game
                        if(win == 1){
                            winGame();
                            return 1;
                        }
                    }
                }
                break;

            case "loop":
                // get the value of how many times to loop.
                loopTimes = cmdStack[i].getInput("loopTimes").fieldRow[1].getValue();

                // thanks to the amazing error checking in sendCommandButton,
                // we can guarantee that getChildren(true)[0] will 101% return a nested block!
                var cBlock = cmdStack[i].getChildren(true)[0];

                // get the whole nested input stack
                var statLength = cBlock.getDescendants();

                for (let cnt = 1; cnt < loopTimes; cnt++){

                    // get children and recursive call
                    var cBlockStack = cmdStack[i].getChildren(true)[0].getDescendants();
                    let ret = await parseCommands(cBlockStack, workspace, map);

                    // check if child-blocks inside LOOP causes a car crash.
                    // if so, break out of the function and do not re-loop.
                    // ret is returned as a Promise.
                    if(ret == 1){
                        break parseCommandsLoop;
                    }

                    // delay for animation purposes
                    await sleep(500);

                }
                break;
        }
    }

}

/**
* Sleep function that causes delay for animation purposes
* @param    ms          the time in milliseconds to pause
* @return   Promise     delay is returned as a Promise.
*/
function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}

/**
* Function to render the map grid and sprites onto index.html.
* Uses Canvas to draw the images.
* @param    map     1-D JavaScript array that holds the map layout. (global variable)
*/
function renderMap(map){

    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    imgTile = new Image();
    imgTile.onload = drawImageActualSize;
    imgTile.src = '/static/img/Sprite/spriteSheet.png';

    map.getTile = function(col, row) {
        return this.tiles[row * map.cols + col]
    }

    function drawImageActualSize(){

        canvas.width = this.naturalWidth/4;
        canvas.height = this.naturalHeight;

        for (var c = 0; c < map.cols; c++) {
            for (var r = 0; r < map.rows; r++) {
                var tile = map.getTile(c, r);

                if (tile != 0) { // 0 => empty tile
                    ctx.drawImage(
                        imgTile, // image
                        (tile - 1) * map.tsize, // source x
                        0, // source y
                        map.tsize, // source width
                        map.tsize, // source height
                        c * 100, // target x
                        r * 100, // target y
                        100, // target width
                        100 // target height
                    );
                }
                else{
                    ctx.fillStyle = "rgb(220,220,220)";
                    ctx.lineWidth = "2";
                    ctx.beginPath();
                    ctx.rect(c * 100, r * 100, 100, 100);
                    ctx.stroke();
                    ctx.closePath();
                }
            }
        }
    }

}

/* onclick event for the 'send command' button.
*/
function sendCommandButton(map){

    var commandsSent = parseInt(document.getElementById("cmdsSent").innerHTML, 10);
    var arr = Blockly.Workspace.getAll();

    // check no. of command stacks
    if (checkCommandStack(arr[0].getTopBlocks(true)) == true){
        document.getElementById("cmdsSent").innerHTML = ++commandsSent;
        parseCommands(arr[0].getAllBlocks(true), arr[0], map);

    }
    else if (arr[0].getAllBlocks(true).length == 0)
        alert("Please ensure that there is at least one command in the box.");
    else
        alert("Only one command stack allowed. Please remove the other stray command blocks or combine them together.");

    return map;
}
