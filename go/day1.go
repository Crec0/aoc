package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

var printf = fmt.Printf
var parseInt = strconv.Atoi

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func read_data(path string) []int {
    file, err := os.Open(path)
    check(err)
    defer file.Close()

    scanner := bufio.NewScanner(file)

    dat := make([]int, 0)

    for scanner.Scan() {
        line := scanner.Text()

        parsedInt, err := parseInt(line)
        check(err)

        dat = append(dat, parsedInt)
    }

    return dat
}

func count_increases(data []int) int {
    count := 0
    for i := 0; i < len(data)-1; i++ {
        if data[i] < data[i+1] {
            count++
        }
    }
    return count
}

func solve_1(dat []int) int {
    return count_increases(dat)
}

func solve_2(data []int) int {
    sums := make([]int, 0)
    l := len(data)

    for i := 0; i < l - l % 3 - 1; i++ {
        tripleSum := 0
        for j := 0; j < 3; j++ {
            tripleSum += data[i + j]
        }
        sums = append(sums, tripleSum)
    }

    return count_increases(sums)
}


func main() {
    // absPath, err := filepath.Abs("./data/day1/input_example.txt")
    absPath, err := filepath.Abs("./data/day1/input.txt")
    check(err)
    
    data := read_data(absPath)
    
    // ans_1 = 1581
    ans_1 := solve_1(data)
    printf("ans 1: %d \n", ans_1)
    
    // ans_2 = 1618
    ans_2 := solve_2(data)
    printf("ans 2: %d \n", ans_2)
}
