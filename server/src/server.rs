use actix_web::{web, App, HttpServer};
use crate::handlers::{index, test};

pub fn run() {
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(index))
            .route("/test", web::post().to(test))
    })
    .bind("127.0.0.1:8088")
    .unwrap()
    .run()
    .unwrap();
}


