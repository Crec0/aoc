use std::collections::HashSet;

fn collect_common_priorties(strings: Vec<&str>) -> Vec<u32> {
    let mut intersection_set = HashSet::from_iter(strings[0].chars());
    for string in strings {
        intersection_set = intersection_set
            .intersection(&string.chars().collect::<HashSet<char>>())
            .map(|a| *a)
            .collect()
    }
    return intersection_set
        .iter()
        .map(|a| *a)
        .map(|c| match c {
            'a'..='z' => c as u32 - 97 /* a - 1 */ + 1,
            'A'..='Z' => c as u32 - 65 /* A - 1 */ + 1 + 26,
            _ => 0,
        })
        .collect();
}

#[allow(dead_code)]
pub fn solve(contents: &str) {
    let score_1: u32 = contents
        .lines()
        .map(|line| line.split_at(line.len() / 2))
        .flat_map(|(first, second)| collect_common_priorties(vec![first, second]))
        .sum();

    println!("Solution 1: {:?}", score_1);

    let lines = contents.lines().collect::<Vec<&str>>();

    let mut score_2 = 0;
    for idx in (0..lines.len()).step_by(3) {
        score_2 += collect_common_priorties(vec![lines[idx], lines[idx + 1], lines[idx + 2]])
            .iter()
            .sum::<u32>();
    }

    println!("Solution 2: {:?}", score_2);
}
