<?php
/**
  * Provides a RPC interface for the PI gpslogger to work with
  *
  * @author Chris Joyce <chris@joyce.id.au>
  */
require_once 'jsonRPCServer.php';
require 'gpslogger.php';
require 'restrictedgpslogger.php';

$myLogger = new restrictedgpslogger();
jsonRPCServer::handle($myLogger)
	or print 'no request';
?>
