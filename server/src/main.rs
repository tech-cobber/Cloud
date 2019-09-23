extern crate reqwest;
mod server;
mod handlers;

fn main() {
    let mut resp = reqwest::get("https://i.ytimg.com/vi/Eh1lIGK_o9c/maxresdefault.jpg").unwrap();
    let mut buf: Vec<u8> = vec![];
    resp.copy_to(&mut buf).unwrap();
    std::fs::write("it_works.jpg", buf).unwrap();
    //server::run();  
}
