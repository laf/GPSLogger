<?php
require_once 'jsonRPCClient.php';
$myExample = new jsonRPCClient('http://192.168.1.3/webAPI/server.php');

$pos = array(
	"posid" => 244,
  	"lat" => -54.34344,
	"long" => 123.456434,
	"trip" => 4,
	"speed" => .234,
	"utc" => "utc",
	"alt" => 1.2
  );


// performs some basic operation
echo '<b>Attempt to perform basic operations</b><br />'."\n";
try {

 	echo 'API status <i>'.$myExample->apiStatus('ZZZXXX').'</i><br />'."\n";
	echo 'API sequence <i>'.$myExample->sequence('ZZAAXX').'</i><br />'."\n";
	echo 'API position <i>';
	$POS = $myExample->position('ZZAAXX',$pos) ;
	echo $POS['posid'];
	echo $POS['status'];
	echo '</i><br />'."\n";
	echo 'giveMeSomeData <i>'.$myExample->giveMeSomeData('name').'</i><br />'."\n";
	$myExample->changeYourState('I am using this function from the network');
	echo 'Your status request has been accepted<br />'."\n";
} catch (Exception $e) {
	echo nl2br($e->getMessage()).'<br />'."\n";
}

// performs some strategic operation, locally allowed
echo '<br /><b>Attempt to store strategic data</b><br />'."\n";
try {
	$myExample->writeSomething('Strategic string!');
	echo 'Strategic data succefully stored';
} catch (Exception $e) {
	echo nl2br($e->getMessage());
}
?>
