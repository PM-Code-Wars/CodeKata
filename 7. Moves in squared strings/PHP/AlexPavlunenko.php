Moves in squared strings (I)


function vertMirror($s) {
   $result = array();
   foreach($s as $str)
   {
     $result[] = strrev($str);
   }  
   return $result; 
}

function horMirror($s) {
   return array_reverse ($s);      
}

function oper($fct, $s) { 
   $strArray = explode(PHP_EOL, $s);
   $result = $fct($strArray);
   return implode(PHP_EOL, $result);
}


*********
Moves in squared strings (II)

function rot($s) {   
   $strArray = explode(PHP_EOL, $s);  
   $result = array();
   foreach(array_reverse ($strArray) as $str)
   {
     $result[] = strrev($str);
   }  
   return implode(PHP_EOL, $result);  
}

function selfieAndRot($s) {   
   $strArray = explode(PHP_EOL, $s);
   $result = array();

   foreach($strArray as $str)
   {
     $result[] = $str . str_repeat('.', strlen($str));
   }  
   
   $result_str = implode(PHP_EOL, $result);
   
   return $result_str . PHP_EOL . rot($result_str);
}

function oper($fct, $s) {
   return $fct($s);
}

**************
Moves in squared strings (III)

function diag1Sym($s) {
    $strArray = explode(PHP_EOL, $s);
    $element = $strArray[0];
    $result = array();    
    
    for($i = 0; $i < strlen($element); $i++)
    {
        $tr_element = '';
        foreach($strArray as $str)
        {
          $tr_element = $tr_element . $str[$i];
        }
        
        $result[] = $tr_element;
    }   
    
    return implode(PHP_EOL, $result);
}

function rot90Clock($s) {
    $diag = diag1Sym($s);
    $strArray = explode(PHP_EOL, $diag);
    $result = array();
    
    foreach($strArray as $str)
    {
      $result[] = strrev($str);
    }  
    
    return implode(PHP_EOL, $result); 
    
}

function selfieAndDiag1($s) {
    $result = array();
    $diag = explode(PHP_EOL, diag1Sym($s));
    $strArray = explode(PHP_EOL, $s);
    
    for($i = 0; $i < count($strArray); $i++)
    {
       $result[] = $strArray[$i] . '|' . $diag[$i];
    }  
    
    return implode(PHP_EOL, $result);
}

function oper($fct, $s) {  
   return $fct($s);
}
************
Moves in squared strings (IV)

function rot90Counter($s) {
    $diag = diag2Sym($s);
    $strArray = explode(PHP_EOL, $diag);
    $result = array();
    
    foreach($strArray as $str)
    {
      $result[] = strrev($str);
    }  
    
    return implode(PHP_EOL, $result); 
}

function diag2Sym($s) {
    $strArray = array_reverse(explode(PHP_EOL, $s));
    $element = $strArray[0];
    $result = array();    
    
    for($i = 0; $i < strlen($element); $i++)
    {
        $tr_element = '';
        foreach($strArray as $str)
        {
          $tr_element = $tr_element . $str[$i];
        }
        
        $result[] = $tr_element;
    }   
    
    return implode(PHP_EOL,  array_reverse($result));
}

function selfieDiag2Counterclock($s) {
    $result = array();
    $diag = explode(PHP_EOL, diag2Sym($s));
    $rotate = explode(PHP_EOL, rot90Counter($s));
    $strArray = explode(PHP_EOL, $s);
    
    for($i = 0; $i < count($strArray); $i++)
    {
       $result[] = $strArray[$i] . '|' . $diag[$i] . '|' . $rotate[$i];
    }  
    
    return implode(PHP_EOL, $result);
}
function oper($fct, $s) {
    return $fct($s);
}
**************
