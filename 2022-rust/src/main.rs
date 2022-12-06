mod day1;
mod day2;
mod day3;
mod day4;
mod day5;

fn main() {
    let contents = std::fs::read_to_string("./src/day5/data.txt").expect("Read the file");
    day5::day5::solve(&contents);
}
