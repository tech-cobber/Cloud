extern crate yaml_rust;
use crate::handlers::{image};
use crate::utils::{read_config};
use actix_web::{web, App, HttpServer};

pub struct Config {
    pub bot_name: String,
    pub bot_token: String,
}

pub fn run() {
    HttpServer::new(|| {
        App::new()
            .data( Config {
                bot_name: read_config()[0]["name"]
                    .as_str().unwrap().to_string(), // TODO cuz it sucks
                bot_token: read_config()[0]["token"]
                    .as_str().unwrap().to_string(), // 
            })
            .route("/image", web::post().to(image)) 
    })
    .bind("127.0.0.1:8088")
    .unwrap()
    .run()
    .unwrap();
}


