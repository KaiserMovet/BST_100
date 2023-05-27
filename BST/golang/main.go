package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"time"
)

func getNumbers(path string, amount int) []int {
	data, _ := ioutil.ReadFile(path)
	lines := strings.Split(string(data), "\n")
	numbers := make([]int, 0, len(lines))
	for _, line := range lines {
		if len(numbers) == amount {
			break
		}
		for _, strNum := range strings.Fields(line) {
			num, _ := strconv.Atoi(strNum)
			numbers = append(numbers, num)
		}
	}
	return numbers
}


func main() {
    amount, _ := strconv.Atoi(os.Args[1])

	addNumbers := getNumbers("/datasets/add.txt", amount)
	checkNumbers := getNumbers("/datasets/check.txt", amount)

	bst := Tree{}

	// Add elements
	startTime := time.Now()
	for _, num := range addNumbers {
		bst.Add(num)
	}
	endTime := time.Now()
	fmt.Printf("ADD_TEST:%.12f\n", endTime.Sub(startTime))

	// Check elements
	startTime = time.Now()
	for _, num := range checkNumbers {
		bst.Contain(num)
	}
	endTime = time.Now()
	fmt.Printf("CHECK_TEST:%.12f\n", endTime.Sub(startTime))

	// Len elements
	startTime = time.Now()
	for _ = range make([]int, 10) {
		bst.Length()
	}
	endTime = time.Now()
	fmt.Printf("LEN_TEST:%.12f\n", endTime.Sub(startTime).Seconds()/10)

	// Height elements
	startTime = time.Now()
	for _ = range make([]int, 10) {
		bst.Height()
	}
	endTime = time.Now()
	fmt.Printf("HEIGHT_TEST:%.12f\n", endTime.Sub(startTime).Seconds()/10)

	fmt.Print("VALIDATION:", bst.Length(), ":", bst.Height(), "\n")
}