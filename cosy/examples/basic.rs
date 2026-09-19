//! A basic example of parsing cosense syntax using the `cosy`.
//!
//! This example shows how to use the default `parse` function to process
//! a string containing consense-style markup and links.
//!
//! Usage: wl-paste | cargo run --example basic

use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .expect("failed to read input from stdin");

    let result = cosy::parse(&input, &());

    match result {
        Ok(nodes) => println!("{:#?}", nodes),
        Err(e) => println!("Error: {}", e),
    }
}
