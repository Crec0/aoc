mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;

fn main() {
    let contents = std::fs::read_to_string("./src/day6/data.txt").expect("Read the file");
    day6::day6::solve(&contents);
}
