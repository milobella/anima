package main

import (
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"io/ioutil"
	"log"
	"milobella/anima/pkg/anima"
	"net/http"
)

// fun main()
func main() {
	router := mux.NewRouter()
	router.HandleFunc("/restitute", RestituteRequest).Methods("POST")
	log.Fatal(http.ListenAndServe(":8444", router))
}

func RestituteRequest(w http.ResponseWriter, r *http.Request) {

	// Read the request
	nlg, err := ReadRequest(r)
	if err != nil {
		http.Error(w, err.Error(), 500)
	}

	// Build the response
	fmt.Fprintf(w, nlg.Sentence)
}

func ReadRequest(r *http.Request) (req anima.NLG, err error) {
	b, err := ioutil.ReadAll(r.Body)
	defer r.Body.Close()
	if err != nil {
		return
	}
	err = json.Unmarshal(b, &req)
	return
}