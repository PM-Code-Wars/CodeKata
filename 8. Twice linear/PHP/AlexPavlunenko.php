function dblLinear($n) {
    
    $linear = array(1);
    //$storage = new SplFixedArray(1000);    
    $storage = array();
    $counter = 0;
    $max = 0;
    
    while($counter < 30000)
    {
       $x = $linear[$counter];
       $storage[$x] = $x;
       
       $y = 2 * $x + 1;              
       $linear[] = $y;       
       $storage[$y] = $y;
       
       $z = 3 * $x + 1;          

       $linear[] = $z;
       $storage[$z] = $z;
        
       $max = $z;       
              
       $counter++;
    }
    
  //  print_r($storage); 
    sort($storage);
   // print_r($storage);   
    
    return $storage[$n];
}
