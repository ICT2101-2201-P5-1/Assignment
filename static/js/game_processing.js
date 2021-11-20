
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
            console.log("CarPOS", carPos);
            break;
        }
    }

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
                    break;
                }
                // allowed to move
                else{
                    // hits virtual wall
                    if (map.tiles[carPos - 5] == 2){
                       // car crash
                       break;
                    }
                    else{
                        // update car position on map
                        map.tiles[carPos] = "0"
                        carPos -= 5;
                        map.tiles[carPos] = "1";

                        // render map..
                        initLevelLayout(map);
                        console.log("delaying");
                        await sleep(1000);
                    }
                }

                break;
            case "downward":

                // hit boundary wall
                if ((carPos + 5) > 24){
                    // car crash
                    break;
                }
                // allowed to move
                else{

                    // hits virtual wall
                    if (map.tiles[carPos + 5] == 2){
                       // car crash
                       break;
                    }
                    else{
                        // update car position on map
                        map.tiles[carPos] = "0"
                        carPos += 5;
                        map.tiles[carPos] = "1";

//                        setTimeout(() => {  initLevelLayout(map); }, 2000);
                        // render map..
                        initLevelLayout(map);
                        console.log("delaying");
                        await sleep(1000);
                    }
                }

                break;
            case "left":

                break;
            case "right":
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
                    parseCommands(cBlockStack, workspace, map);
                    await sleep(1000);

                }

                break;
            case "if_wall":
//                console.log("Next block wall");

                var cBlock = cmdStack[i].getChildren(true)[0];
                // get the whole nested input stack

                break;
            case "if_coin":
//                console.log("Next block coin");
                break;
        }
    }

}

function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}


/*
*/

function renderMap(map){


}

/* initLevelLayout
*/
function initLevelLayout(map){

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
    var arr = Blockly.Workspace.getAll();
//    console.log(arr[0].getAllBlocks(true));

    console.log(map);
    // check no. of command stacks
    if (checkCommandStack(arr[0].getTopBlocks(true)) == true){
        parseCommands(arr[0].getAllBlocks(true), arr[0], map);
        console.log("eof",map);
    }
    else if (arr[0].getAllBlocks(true).length == 0)
        alert("Please ensure that there is at least one command in the box.");
    else
        alert("Only one command stack allowed. Please remove the other stray command blocks or combine them together.");

    return map;
}
