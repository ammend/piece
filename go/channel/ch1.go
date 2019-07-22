package main

import (
	"fmt"
	"time"
)

var a chan int

var b chan int

func init() {
	a = make(chan int)
	b = make(chan int)
}

func f1() {
	for {
		a <- 1
		fmt.Println("exec f1")
		b <- 1
		time.Sleep(1 * time.Second)
	}
}

func f2() {
	for {
		<-a
		b <- 1
		fmt.Println("f2")
		<-b
		time.Sleep(1 * time.Second)
	}
}

func main() {
	go f1()
	go f2()
	time.Sleep(60 * time.Second)
}
