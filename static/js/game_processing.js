function parseCommands(cmdStack){
    for (let i = 0; i < cmdStack.length; i++){
        console.log(cmdStack[i].type);

        switch(cmdStack[i].type){
            case "upward":
                console.log("MOVING UP");
                break;
            case "downward":
                console.log("MOVING DOWN");
                break;
            case "left":
                console.log("MOVING LEFT");
                break;
            case "right":
                console.log("MOVING RIGHT");
                break;
            case "loop":
                console.log("LOOPING");
                break;
            case "if wall":
                console.log("Next block wall");
                break;
            case "if coin":
                console.log("Next block coin");
                break;
        }
    }
}
function sendCommandButton(){
    var arr = Blockly.Workspace.getAll();
    console.log(arr[0].getAllBlocks(true));
    parseCommands(arr[0].getAllBlocks(true));
}
