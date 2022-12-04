#[allow(dead_code)]
pub fn solve(contents: &str) {
    let score: i32 = contents
        .lines()
        .map(|line| match line {
            "A X" => 1 + 3,
            "A Y" => 2 + 6,
            "A Z" => 3 + 0,

            "B X" => 1 + 0,
            "B Y" => 2 + 3,
            "B Z" => 3 + 6,

            "C X" => 1 + 6,
            "C Y" => 2 + 0,
            "C Z" => 3 + 3,
            _ => -1,
        })
        .sum();
    println!("Solution 1: {}", score);

    let score2: i32 = contents
        .lines()
        .map(|line| match line {
            "A X" => 3 + 0,
            "A Y" => 1 + 3,
            "A Z" => 2 + 6,

            "B X" => 1 + 0,
            "B Y" => 2 + 3,
            "B Z" => 3 + 6,

            "C X" => 2 + 0,
            "C Y" => 3 + 3,
            "C Z" => 1 + 6,
            _ => -1,
        })
        .sum();
    println!("Solution 2: {}", score2);
}

/*
    Rock      1 A
    Paper     2 B
    Scissors  3 C

    Lose      0 X
    Draw      3 Y
    Win       6 Z
*/
