extern crate reqwest;
use crate::server::Config;
use actix_web::{web, HttpResponse, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
pub struct Image {
    name: String,
    path: String,
}

pub fn image(image: web::Json<Image>, data: web::Data<Config>) -> impl Responder {
    let token = &data.bot_token;
    let url = format!("https://api.telegram.org/file/bot{}/{}", token, image.path);
    let mut resp = reqwest::get(&url).unwrap();
    let mut buf: Vec<u8> = vec![];
    resp.copy_to(&mut buf).unwrap();
    let path = format!("../images/{}.jpg", image.name);
    std::fs::write(&path, buf).unwrap();
    HttpResponse::Ok().body("OK")
}

