package main

import (
	"fmt"
	"sync"
)

type A struct {
	Val int
}

func main() {
	arr := []*A{
		{
			Val: 1,
		},
		{
			Val: 2,
		},
	}

	wait := sync.WaitGroup{}
	wait.Add(2)
	for _, value := range arr {
		func() {
			fmt.Println(value.Val)
			wait.Done()
		}()
	}
	wait.Wait()
}
