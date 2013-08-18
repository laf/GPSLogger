<?php
$myFile = "testFile.txt";
$fh = fopen($myFile, 'a') or die("can't open file");

//Send the original message back.
$response['request'] = $decoded;
fwrite($fh, "---------\nAPI Check\n");
fwrite($fh, $decoded);
fclose($fh);
$response['status'] = array(
	     'type' => 'OK;',
		     'value' => 'No JSON value set',
			   );
$encoded = json_encode($response);
header('Content-type: application/json');
# exit($encoded);
exit("OK");
?>
