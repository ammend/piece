package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func main2() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		go func() {
			for range time.Tick(time.Second) {
				fmt.Println("req is processing.")
			}
		}()

		// assume req processing takes 3s
		time.Sleep(3 * time.Second)
		w.Write([]byte("hello"))
	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
