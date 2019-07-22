package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		fmt.Println(&r)
		w.Write([]byte("hello"))
	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
