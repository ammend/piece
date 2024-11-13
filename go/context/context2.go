package main

import (
	"context"
	"fmt"
	"time"
)

func main5() {
	ctx, _ := context.WithTimeout(context.Background(), 5*time.Second)

	// defer cancel()

	for {
		select {
		case <-time.After(4 * time.Second):
			fmt.Println("overslept")
		case <-ctx.Done():
			fmt.Println("context done")
			fmt.Println(ctx.Err())
			return
		}
	}
}
