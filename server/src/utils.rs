use std::io::Read;
use yaml_rust::{YamlLoader};

pub fn read_config() -> std::vec::Vec<yaml_rust::Yaml> {
    let mut config_file = std::fs::File::open("../config.yml").unwrap();
    let mut config_string = String::new();
    config_file.read_to_string(&mut config_string).unwrap();
    let config = YamlLoader::load_from_str(&config_string).unwrap();
    config
}