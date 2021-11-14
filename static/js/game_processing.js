
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
recursive function.
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
function sendCommandButton(){
    var arr = Blockly.Workspace.getAll();
    console.log(arr[0].getAllBlocks(true));
    // check no. of command stacks
    if (checkCommandStack(arr[0].getTopBlocks(true)) == true){
        parseCommands(arr[0].getAllBlocks(true), arr[0]);
    }
    else{
        alert("Only one command stack allowed. Please remove the other stray command blocks.");
    }
}
