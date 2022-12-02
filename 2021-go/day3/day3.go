package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
)

var printf = fmt.Printf

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func read_data(path string) []string {
    file, err := os.Open(path)
    check(err)

    defer file.Close()

    scanner := bufio.NewScanner(file)
    dat := make([]string, 0)

    for scanner.Scan() {
        dat = append(dat, scanner.Text())
    }

    return dat
}

func count_ones_in_columns(data []string, index int) int {
    ones := 0
    for _, num := range data {
        if num[index] == '1' {
            ones++
        }
    }
    return ones
}

func get_common_bit(totalSize int, ones int, matchMost bool) string {
    zeros := totalSize - ones
    if (ones >= zeros) != matchMost {
        return "1"
    }
    return "0"
}

func common_counter(data []string, matchMost bool, depth int) string {
    if depth == len(data[0]) {
        return ""
    }
    ones := count_ones_in_columns(data, depth)
    common_bit := get_common_bit(len(data), ones, matchMost)

    return common_bit + common_counter(data, matchMost, depth + 1)
}

func solve_1(data []string) int64 {
    gamma := common_counter(data, true, 0)
    epsilon := common_counter(data, false, 0)
    c_gamma, _ := strconv.ParseInt(gamma, 2, 64)
    c_epsilon, _ := strconv.ParseInt(epsilon, 2, 64)
    return c_gamma * c_epsilon 
}

func solve_2(data []string) int {
    panic("unimplemented")
}

func main() {
    // absPath, err := filepath.Abs("./data/day3/input_example.txt")
    absPath, err := filepath.Abs("./data/day3/input.txt")
    check(err)

    data := read_data(absPath)

    ans_1 := solve_1(data)
    printf("ans 1: %d \n", ans_1)

    // ans_2 := solve_2(data)
    // printf("ans 2: %d \n", ans_2)
}