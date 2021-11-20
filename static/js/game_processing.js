
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
*/
function parseCommands(cmdStack, workspace){

    for (let i = 0; i < cmdStack.length; i++){
        console.log(cmdStack[i].type);

        // check whether all inputs are filled.
        if (cmdStack[i].allInputsFilled() == false){
            alert("Some blocks have empty inputs. Please ensure it has at least one nested command.")
            return false;
        }

        switch(cmdStack[i].type){
            case "upward":
                break;
            case "downward":
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
                    parseCommands(cBlockStack, workspace);

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

/* initLevelLayout
*/
function initLevelLayout(map){

    console.log("hi", map);

    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

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

                console.log(tile);

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
function sendCommandButton(){
    var arr = Blockly.Workspace.getAll();
    console.log(arr[0].getAllBlocks(true));
    // check no. of command stacks
    if (checkCommandStack(arr[0].getTopBlocks(true)) == true){
        parseCommands(arr[0].getAllBlocks(true), arr[0]);
    }
    else if (arr[0].getAllBlocks(true).length == 0)
        alert("Please ensure that there is at least one command in the box.");
    else
        alert("Only one command stack allowed. Please remove the other stray command blocks or combine them together.");

}
