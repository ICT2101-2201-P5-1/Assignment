
/* check the number of command stacks.
   only one command stack is allowed,
   so check and send back error message if
   there is > 1 command stack.
*/
function checkCommandStack(cmdStack){
    if(cmdStack.length == 1)
        return true;
    else
        return false;
}

/* parse the command stack.
*/
function parseCommands(cmdStack){
    for (let i = 0; i < cmdStack.length; i++){
        console.log(cmdStack[i].type);

        switch(cmdStack[i].type){
            case "upward":
//                console.log("MOVING UP");
                break;
            case "downward":
//                console.log("MOVING DOWN");
                break;
            case "left":
//                console.log("MOVING LEFT");
                break;
            case "right":
//                console.log("MOVING RIGHT");
                break;
            case "loop":
//                console.log("LOOPING");

                // get the value of how many times to loop.
                console.log(cmdStack[i].getInput("loopTimes").fieldRow[1].getValue());

                // get the nested block, check if there are children.
                var cBlock = cmdStack[i].getChildren()[0];
                if (cBlock != null){
                    // as getChildren() returns at most two items: first nested block and next statement,
                    // check if the first block returned is nested or a next statement block
                    if(cBlock == cmdStack[i].getNextBlock()){
                        alert("Loop block is empty. Please ensure it has at least one nested command.")
                        return false;
                    }
                }
                else{
                    alert("Loop block is empty. Please ensure it has at least one nested command.")
                    return false;
                }

                break;
            case "if_wall":
//                console.log("Next block wall");

                  // get the nested block, check if there are children.
                var cBlock = cmdStack[i].getChildren()[0];
                if (cBlock != null){
                    // as getChildren() returns at most two items: first nested block and next statement,
                    // check if the first block returned is nested or a next statement block
                    if(cBlock == cmdStack[i].getNextBlock()){
                        alert("'If wall' block is empty. Please ensure it has at least one nested command.")
                        return false;
                    }
                }
                else{
                    alert("'If wall' block is empty. Please ensure it has at least one nested command.")
                    return false;
                }
                break;
            case "if_coin":
//                console.log("Next block coin");

                // get the nested block, check if there are children.
                var cBlock = cmdStack[i].getChildren()[0];
                if (cBlock != null){
                    // as getChildren() returns at most two items: first nested block and next statement,
                    // check if the first block returned is nested or a next statement block
                    if(cBlock == cmdStack[i].getNextBlock()){
                        alert("'If coin' block is empty. Please ensure it has at least one nested command.")
                        return false;
                    }
                }
                else{
                    alert("'If coin' block is empty. Please ensure it has at least one nested command.")
                    return false;
                }
                break;
        }
    }
}
function sendCommandButton(){
    var arr = Blockly.Workspace.getAll();
    console.log(arr[0].getAllBlocks(true));
    // check no. of command stacks
    if (checkCommandStack(arr[0].getTopBlocks(true)) == true){
        parseCommands(arr[0].getAllBlocks(true));
    }
    else{
        alert("Only one command stack allowed. Please remove the other stray command blocks.");
    }
}
