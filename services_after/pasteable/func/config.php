<?php

//=====================================================================
// variables and configuration:
//=====================================================================

// CIPHER CONFIGURATION
$CIPHER_SECRET = "0123456789ABCDEF";
$CIPHER_RING = "AES-128-CTR";

// APP CONFIGURATION
$APP_SECRET = "012345678905671F";
$APP_HOST = "linux";
$APP_PATH = dirname(__FILE__)."/../";

// DB CONFIGURATION
$DB_HOST = null;
$DB_USER = "www-data";
$DB_PASS = null;
$DB_NAME = "pasteable";

$MYSQLI = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME) or die($MYSQLI->error);
if ($MYSQLI->connect_errno)
    die("Failed to connect to MySQL: " . $MYSQLI->connect_error);

//=====================================================================
