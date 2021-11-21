
/* check the number of command stacks.
   only one command stack is allowed,
   so check and send back error message if
   there is > 1 command stack.

   @cmdStack = an array of Blockly blocks.
   returns boolean.
*/
function checkCommandStack(cmdStack){
    if(cmdStack.length == 1)
        return true;
    else
        return false;
}

function collectCoin(){
    var coinsCollected = parseInt(document.getElementById("coinsCollected").innerHTML, 10);
    document.getElementById("coinsCollected").innerHTML = ++coinsCollected;
    console.log("collect coin");
}

function carCrashed(){
    var carCrashes = parseInt(document.getElementById("carCrashes").innerHTML, 10);
    document.getElementById("carCrashes").innerHTML = ++carCrashes;
}

function winGame(){
    alert("YOU WIN");
}
/* parse the command stack. recursive function.
* @cmdStack = an array of Blockly blocks.
* @workspace = Blockly workspace object.
* map format:
0 = empty
1 = car
2 = wall
3 = coin
4 = goal

*/

async function parseCommands(cmdStack, workspace, map){

    console.log("hi2", map);

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
                    return -1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos - 5] == 2){
                        // car crash
                        carCrashed();
                        return -1;
                    }

                    // moves to empty space
                    else{

                        // collect coins
                        if (map.tiles[carPos - 5] == 3){
                            collectCoin();
                        }

                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos -= 5;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);

                        // delay for animation purposes
                        await sleep(500);
                    }
                }
                break;

            case "downward":

                // hit boundary wall
                if ((carPos + 5) > 24){
                    // car crash
                    carCrashed();
                    return -1;
                }
                // allowed to move
                else{

                    // hits virtual wall
                    if (map.tiles[carPos + 5] == 2){
                        // car crash
                        carCrashed();
                        return -1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos + 5] == 3){
                            collectCoin();
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos += 5;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);

                        // delay for animation purposes
                        await sleep(500);
                    }
                }
                break;

            case "left":

                // hit boundary wall
                // NOTE: the LEFT block has an extra check for value '-1' due to the JS negative modulo bug
                if (((carPos - 1) % 5 == 4) || ((carPos - 1) % 5 == -1)){
                    // car crash
                    carCrashed();
                    return -1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos - 1] == 2){
                        // car crash
                        carCrashed();
                        return -1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos - 1] == 3){
                            collectCoin();
                        }
                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos -= 1;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);

                        // delay for animation purposes
                        await sleep(500);
                    }
                }
                break;

            case "right":

                // hit boundary wall
                if ((carPos + 1) % 5 == 0){
                    // car crash
                    carCrashed();
                    return -1;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos + 1] == 2){
                        carCrashed();
                        return -1;
                    }
                    else{
                        // collect coins
                        if (map.tiles[carPos + 1] == 3){
                            collectCoin();
                        }

                        // update car position on map
                        map.tiles[carPos] = "0";
                        carPos += 1;
                        map.tiles[carPos] = "1";

                        // render map..
                        renderMap(map);

                        // delay for animation purposes
                        await sleep(500);
                    }
                }

                break;
            case "loop":

                // get the value of how many times to loop.
                loopTimes = cmdStack[i].getInput("loopTimes").fieldRow[1].getValue();

                // thanks to the amazing error checking above,
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
                    if(ret == -1){
                        break parseCommandsLoop;
                    }

                    // delay for animation purposes
                    await sleep(500);

                }
                break;
        }
    }

}

// sleep function that causes delay for animation purposes
function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}


/* rendersMap
*/
function renderMap(map){

    console.log("hi", map);

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

        canvas.width = this.naturalWidth;
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
        console.log("eof",map);
    }
    else if (arr[0].getAllBlocks(true).length == 0)
        alert("Please ensure that there is at least one command in the box.");
    else
        alert("Only one command stack allowed. Please remove the other stray command blocks or combine them together.");

    return map;
}
