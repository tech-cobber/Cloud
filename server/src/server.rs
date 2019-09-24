use actix_web::{web, App, HttpServer};
use crate::handlers::{image};

pub fn run() {
    HttpServer::new(|| {
        App::new()
            .route("/image", web::post().to(image))
    })
    .bind("127.0.0.1:8088")
    .unwrap()
    .run()
    .unwrap();
}


