#[allow(dead_code)]
pub fn solve(contents: &str) {
    let (crates_part, instructions_part) = contents.split_at(contents.find("\n\n").unwrap());
    let crates_rows = crates_part.lines().collect::<Vec<_>>();
    let stacks_count = crates_rows[crates_rows.len() - 1].split("   ").count();

    let mut stacks: Vec<Vec<&str>> = vec![Vec::new(); stacks_count];

    for row in crates_rows.iter().rev().skip(1) {
        for col_idx in (0..(row.len())).step_by(4) {
            let crat = &row[col_idx..(col_idx + 3)];
            if crat != "   " {
                stacks[col_idx / 4].push(crat);
            }
        }
    }

    for instruction in instructions_part.lines().skip(2) {
        let numerics: Vec<usize> = instruction
            .split(" ")
            .map(|word| u32::from_str_radix(word, 10))
            .filter(|res| res.is_ok())
            .map(|it| it.unwrap() as usize)
            .collect();

        let (amount, from, to) = (numerics[0], numerics[1] - 1, numerics[2] - 1);

        for idx in 0..amount {
            // solution 1
            // let stack = stacks[from].pop().unwrap();
            // solution 2
            let stack_to_remove = stacks[from].len() - (amount - idx);
            let stack = stacks[from].remove(stack_to_remove);
            stacks[to].push(stack)
        }
    }

    print!(
        "Solution: {:?}",
        stacks
            .iter()
            .map(|vector| vector[vector.len() - 1])
            .map(|crat| crat.split(|c| c == '[' || c == ']').collect::<Vec<_>>()[1])
            .collect::<Vec<_>>()
            .join("")
    );
}
