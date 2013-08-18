<?php
/**
 * An immaginative class.
 * for the managment of gps logger data
 * you can immagine a DB interface instead of the development interfaces
 *
 * @author Chris Joyce <chris@joyce.id.au>
 */
class gpslogger {
	/**
	 * An immaginative array of data
	 *
	 * @var array
	 */
	private $someData = array (
							'name' => 'Some Proper Name',
							'attr' => 'Some Personal Attribute'
							);

	/**
     * An apiStatus  public method.
	 *
	 * Will return ok if the webAPI is ready yo recive data or process requests
	 *
	 * @param string $device
	 * @return string
 	 */
	public function apiStatus($device) {
	/*
	 Have a very complex code here
	 */
		// if ($device == 'ZZZXXX') {
			return 'OK' ;
		// } else {
		// 	return 'DOWN' ;
		// }

	}



	public function position($device,$data) {
//event, sequence, trip, latitude, longitude, timeutc, systimeutc, altitude, eps, epx, epv, ept, speed, climb, track, mode, satellites, distance
	 $myFile = "pos.txt";
	 $fh = fopen($myFile, 'a') or die("can't open file");

	 foreach ($data as $key => $value) {
	 	fwrite($fh, $key . ':' . $value . ",");
	 }

	 fwrite($fh, "\n");

	 //foreach ($data as $POS) {
	 // 		fwrite($fh, $POS.".\t");
	 //}
	 fclose($fh);

//	 	$file = '/tmp/sequence.txt';
//		$my_variable=unserialize(file_get_contents($file));
//		$my_variable[$device] = $my_variable[$device] + 1;
//	 	$content = serialize($my_variable);
//	 	file_put_contents($file, $content);
//	 	// $content = unserialize(file_get_contents($file));

//		if ($tmpFile = fopen ('/tmp/sequence.txt','a')) {
//		 	return $my_variable[$device];
//		} else {
//		 	throw new Exception('Unable to change the internal state');
//		}
	 	$someData = array (
		'posid' => $data['posid'],
		'status' => 200
		);
			return $someData ;
	}


	public function sequence($device) {
	 	$file = '/tmp/sequence.txt';
		$my_variable=unserialize(file_get_contents($file));
		$my_variable[$device] = $my_variable[$device] + 1;
	 	$content = serialize($my_variable);
	 	file_put_contents($file, $content);
	 	// $content = unserialize(file_get_contents($file));

		if ($tmpFile = fopen ('/tmp/sequence.txt','a')) {
		 	return $my_variable[$device];
		} else {
		 	throw new Exception('Unable to change the internal state');
		}
			return 1 ;
	}


	/**
	 * An immaginative private method.
	 * Since it is a private method, it WILL NOT be served as RPC.
	 *
	 * @param integer $min
	 * @param integer $max
	 * @return integer
	 */
	private function reserved($min,$max) {
		return rand($min,$max);
	}

	/**
	 * An immaginative public method.
	 * Since it is a public method, it WILL be served as RPC.
	 * If you want to plug out this method, extend this class with a dummy method.
	 *
	 * This method returns a significative value and must be implemented as a RPC request.
	 *
	 * @param string $param
	 * @return mixed
	 */
	public function giveMeSomeData($param) {
		/*
		You can have a very complex code here
		*/

		if (array_key_exists($param,$this->someData)) {
			return $this->someData[$param];
		} else {
			throw new Exception('Invalid parameter '.$param);
		}
	}

	/**
	 * An immaginative public method.
	 * Since it is a public method, it WILL be served as RPC.
	 * If you want to plug out this method, extend this class with a dummy method.
	 *
	 * This method return a trivial value and can be implemented as a RPC notification.
	 *
	 * @param string $state
	 * @return boolean
	 */
	public function changeYourState($state) {
		/*
		You can have a very complex code here
		*/

		// happy folks are not allowed to overcharge the host
		$state = substr($state,0,32);

		if ($tmpFile = fopen ('/tmp/state.txt','a')) {
			fwrite($tmpFile,date('r').' - '.$state."\n");
			fclose($tmpFile);
			return true;
		} else {
			throw new Exception('Unable to change the internal state');
		}
	}

	/**
	 * An immaginative public method.
	 * Since it is a public method, it WILL be served as RPC.
	 * If you want to plug out this method, extend this class with a dummy method.
	 *
	 * We suppose that this method alter strategic data and that we don't want to serve it as RPC.
	 *
	 * @param string $something
	 * @return boolean
	 */
	public function writeSomething($something) {
		/*
		You can have a very complex code here
		*/

		if ($tmpFile = fopen ('/tmp/storeData.txt','a')) {
			fwrite($tmpFile,date('r').' - '.$something."\n");
			fclose($tmpFile);
			return true;
		} else {
			throw new Exception('Unable to change the internal state');
		}
	}
}
?>
