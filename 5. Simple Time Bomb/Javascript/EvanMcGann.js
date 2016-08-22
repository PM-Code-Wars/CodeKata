/*

console.log(CutTheWire.toString());

Output:
function (wireCode){
 Test.expect(typeof wireCode === 'number', 'BOOM! You have to specify which wire to cut!');
  Test.expect(wireCode === global[theWire], 'BOOM! You cut the wrong wire!');
  delete this[theWire];
}

==> Expecting global[theWire]
*/

CutTheWire(this[theWire]);
