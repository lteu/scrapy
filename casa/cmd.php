<?php

// chdir('/home/fqmgdsib/public_html/liu/casa');
// $firstParam = "https://www.casa.it/vendita/residenziale/pesaro/";
$firstParam = "https://www.casa.it/vendita/residenziale/mondolfo/";
$out = shell_exec('scrapy crawl avg -a mainurl='.$firstParam);
$pieces = explode(";", $out);
echo $pieces[0];

?>