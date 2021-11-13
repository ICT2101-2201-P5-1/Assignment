Blockly.Blocks['upward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('Move Upward');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(20);
  }
};
Blockly.Blocks['downward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('Move Downward');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(65);
  }
};
Blockly.Blocks['left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('Move Left');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(120);
  }
};
Blockly.Blocks['right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('Move Right');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(160);
  }
};
Blockly.Blocks['loop'] = {
  init: function() {
  this.setInputsInline(true);
    this.appendDummyInput()
        .appendField('repeat')
        .appendField(new Blockly.FieldNumber());
    this.appendDummyInput().appendField('times');
    this.appendStatementInput('DO').appendField('do');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(210);
  }
};
Blockly.Blocks['if_wall'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('If wall');
    this.appendStatementInput('DO').appendField('do');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(230);
  }
};
Blockly.Blocks['if_coin'] = {
  init: function() {
    this.appendDummyInput()
        .appendField('If coin');
    this.appendStatementInput('DO').appendField('do');
    this.setNextStatement(true, 'Action');
    this.setPreviousStatement(true, 'Action');
    this.setColour(260);
  }
};