var wireCode = 0; // Find the wire.
//console.log(Bomb.toString());

for (let i = 0 ; i < 10 ; i++) {
  //eval('wireCode = boom' + i + ';');
  
  if ( global['boom' + i] !== undefined) {
    Bomb.CutTheWire(global['boom' + i]);
    break;
  }  
}
