package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	// monitor
	go func() {
		// for range time.Tick(time.Second) {
		// 	select {
		// 	case <-ctx.Done():
		// 		fmt.Println("context done")
		// 		return
		// 	default:
		// 		fmt.Println("monitor woring")
		// 	}
		// }
		<-ctx.Done()
		fmt.Println("context done")
	}()

	for {
		time.Sleep(4 * time.Second)
		cancel()
	}
}
