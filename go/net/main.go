package main

import (
	"fmt"
	"net"
	"strconv"
)

func main() {
	ipv4Host := "127.0.0.1"
	ipv6Host := "fe80::5ca5:6a48:e96f:6a46"
	port := 8080
	fmt.Printf("ipv4 hostport %v\n", net.JoinHostPort(ipv4Host, strconv.Itoa(port)))
	fmt.Printf("ipv6 hostport %v\n", net.JoinHostPort(ipv6Host, strconv.Itoa(port)))
}
