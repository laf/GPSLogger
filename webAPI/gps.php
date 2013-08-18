<?php
$myFile = "testFile.txt";
$fh = fopen($myFile, 'a') or die("can't open file");

if (isset($_REQUEST['json'])) {
   $decoded = json_decode(stripslashes($_REQUEST['json']), TRUE);
     if (is_null($decoded)) {
	      $response['status'] = array(
			      'type' => 'error',
				        'value' => 'Invalid JSON value found',
						    );
		      $response['request'] = $_REQUEST['json'];
			    }
	   else {
		    $response['status'] = array(
			        'type' => 'message',
					      'value' => 'Valid JSON value found',
						      );
			    //Send the original message back.
			    $response['request'] = $decoded;
				fwrite($fh, $decoded);
				fclose($fh);
				  }
}
else {
   $response['status'] = array(
	     'type' => 'error',
		     'value' => 'No JSON value set',
			   );
     $response['request'] = $_REQUEST['json'];
}
$encoded = json_encode($response);
header('Content-type: application/json');
exit($encoded);

?>
