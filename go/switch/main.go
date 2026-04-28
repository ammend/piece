package main

import "fmt"

func main() {

	switch {
	case 1 > 0:
		fmt.Println("1")
	case 2 > 0:
		fmt.Println("2")
	default:
		fmt.Println("default")
	}
}
