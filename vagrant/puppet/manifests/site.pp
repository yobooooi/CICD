include baseconfig

if $server_type == 'webserver' {
	include webserver
}

if $server_type == 'jenkins' {
	include jenkins
}

if $server_type == 'mysql' {
	include mysql
}
