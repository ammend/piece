package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	wait := sync.WaitGroup{}

	for i := 0; i < 10; i++ {
		wait.Add(1)
		func() {
			fmt.Println(i)
			time.Sleep(time.Second)
			wait.Done()
		}()
	}
	wait.Wait()
}
