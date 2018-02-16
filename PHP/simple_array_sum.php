<?php

$handle = fopen ("php://stdin", "r");
function simpleArraySum($n, $ar) {
    $result = 0;
    foreach($ar as $num)
    {
     $result+=$num;   
    }
    print $result;
}

fscanf($handle, "%i",$n);
$ar_temp = fgets($handle);
$ar = explode(" ",$ar_temp);
$ar = array_map('intval', $ar);
$result = simpleArraySum($n, $ar);
echo $result . "\n";

?>
