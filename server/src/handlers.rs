extern crate image;
use actix_web::{web, HttpResponse, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
pub struct Image {
    name: String,
    buf: Vec<u8>,
    width: u32,
    heigth: u32,
    color: String,
}

pub fn test(image: web::Json<Image>) -> impl Responder {
    println!("Name - {} \nWidth - {} \nHeigth - {} \nColor - {} \nBuf - {:?}\n",
        image.name, 
        image.width, 
        image.heigth, 
        image.color, 
        image.buf);
    image::save_buffer("../images/test.jpg", 
                       &image.buf, 
                       image.heigth,
                       image.width, 
                       image::RGB(8)
                      ).unwrap();
    HttpResponse::Ok().body("OK")
}

pub fn index() -> impl Responder {
    HttpResponse::Ok().body("Hello, Cloud!\n")
}  
