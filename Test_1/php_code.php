<?php

$str = "hi its me . hi its me .hello its me hi a a a a";

$array = explode(" ",$str);

$array = array_count_values($array);

arsort($array);

$highest = current($array);

foreach($array as $key=>$value)
    if($value == $highest)
        $repeat[] = $key;

$sliced_array = array_slice($repeat, 0, 5);        
print_r($sliced_array);
?>