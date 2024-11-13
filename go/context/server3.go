package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func main3() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		// monitor
		go func() {
			for range time.Tick(time.Second) {
				select {
				case <-r.Context().Done():
					fmt.Println("req is outgoing")
					return
				default:
					fmt.Println("req is processing")
				}
			}
		}()

		// assuming req processing takes 3s
		time.Sleep(3 * time.Second)
		w.Write([]byte("hello"))
	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}
