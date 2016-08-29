var i = 0;

while (!global['boom' + i++]) {}

Bomb.CutTheWire(this['boom' + (i - 1)]);
