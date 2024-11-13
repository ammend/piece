package main

import (
	"fmt"
	"reflect"
)

type Event interface {
	Hello()
}

type Test struct {
}

func (t Test) Hello() {
	fmt.Println("hello")
}

func main() {
	test1 := Test{}
	typeOfTest1 := reflect.TypeOf(test1)
	fmt.Println(typeOfTest1.Name(), typeOfTest1.Kind())

	test2 := get()
	typeOfTest2 := reflect.TypeOf(test2)
	fmt.Println(typeOfTest2.Name(), typeOfTest2.Kind())

}

func get() Event {
	return Test{}
}
