package main

import (
	"fmt"
	"time"
)

func main() {
	for i := range []int{1, 2, 3} {
		var x int
		x = 10
		fmt.Printf("x=%v\n", x)
		go func(i int) {
			fmt.Println(i)
		}(i)
	}
	time.Sleep(3 * time.Second)
}
