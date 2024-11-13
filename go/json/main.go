package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

func AreEqualJSON(s1, s2 string) (bool, error) {
	var o1 interface{}
	var o2 interface{}

	var err error
	err = json.Unmarshal([]byte(s1), &o1)
	if err != nil {
		return false, fmt.Errorf("Error mashalling string 1 :: %s", err.Error())
	}
	err = json.Unmarshal([]byte(s2), &o2)
	if err != nil {
		return false, fmt.Errorf("Error mashalling string 2 :: %s", err.Error())
	}

	return reflect.DeepEqual(o1, o2), nil
}

func main() {

	s1 := `{"dog": 5, "cat": 3}`
	s2 := `{"cat":3, "dog": 5}`

	fmt.Println("s1:: ", s1)
	fmt.Println("s2:: ", s2)

	areEqual, err := AreEqualJSON(s1, s2)
	if err != nil {
		fmt.Println("Error mashalling strings", err.Error())
	}

	fmt.Println("Equal:: ", areEqual)
}
