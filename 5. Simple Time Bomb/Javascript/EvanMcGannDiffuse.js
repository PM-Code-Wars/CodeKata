/* 1
   console.log(Bomb);
   Output:
     { key: 42, diffuse: [Function] }
*/
Bomb.diffuse(42);

/* 2
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'just keep trying' }
*/
for (var i = 0; i < 5; i++) { Bomb.diffuse(i); }

/* 3
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'Check the globals' }
  
  console.log(global);
  Output:
    {
      ...
      BombKey: ...,
      ...
    }
*/
Bomb.diffuse(global.BombKey);

/* 4
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'Is something missing?' }
  
  console.log(Bomb.diffuse.toString());
  Output:
    function (){
      try{
        if( diffuseTheBomb() ){
          next();
        }
      }catch(err){
      }
    }
*/
diffuseTheBomb = function () { return true; }
Bomb.diffuse();

/* 5
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'VGhlIGtleSBpcyAiMy4xNDE1OSI= (base64)' }
    
  // Had to use browser console to get atob() to run because node v0.10.33 doesn't have a native implementation
  atob('VGhlIGtleSBpcyAiMy4xNDE1OSI=')
  Output:
    "The key is "3.14159""
*/
Bomb.diffuse('3.14159');

/* 6
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'Exactly 4 years ago...' }
*/
Bomb.diffuse(new Date().setFullYear(new Date().getFullYear() - 4));

/* 7
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'Is it freezing in here?' }
  
  console.log(Bomb.diffuse.toString());
  Output:
    function ( code ){
      code.key = 42;
      check( code.key === 43 );
    }
*/
var obj = { key: 43 };
Object.freeze(obj);
Bomb.diffuse(obj);

/* 8
  console.log(Bomb);
  Output:
    { diffuse: [Function], hint: 'Sorry, no more hints!!' }
    
  console.log(Bomb.diffuse.toString());
  Output:
    function ( obj ){
      check( ( obj < 10 ) && ( obj > 10 ) );
    }
*/
function Num(val) {
  this.val = val;  
}
Num.prototype = Number.prototype;
Num.prototype.valueOf = function () { var orig = this.val; this.val += 2; return orig; }
Bomb.diffuse(new Num(9));

/* 9
  console.log(Bomb.diffuse.toString());
  Output:
    function ( code ){
      check(
           ( code === 42 )
        && ( Math.random() * Math.random() * Math.random() === 0.5 )
      );
    }
*/
var calls = 0;
Math.random = function () { return calls++ < 2 ? 1 : .5; }
Bomb.diffuse(42);

/* 10
  console.log(Bomb.diffuse.toString());
  Output:
    function ( code ){
      check(
        \/* Did you enjoy this little challenge? *\/
        new Buffer( code, 'base64' ).toString( 'ascii' )
        , [ 1, 2, 3 ] + [ 3 ] + [ 3, 4, 5, 6, 7, 8 ] == 42
      );
    }
*/
Array.prototype.toString = function () { var sum = 0; for (var i = 0; i < this.length; i++) { sum += this[i]; } return sum; }
Bomb.diffuse('eWVz');
