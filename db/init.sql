CREATE DATABASE telemedicina;
use telemedicina;

SET GLOBAL max_connections = 400;
SET GLOBAL net_buffer_length = 16384;
SET GLOBAL net_read_timeout = 360;
SET GLOBAL net_retry_count = 10;
SET GLOBAL net_write_timeout = 360;
SET GLOBAL max_allowed_packet = 128*1024*1024;

DROP TABLE IF EXISTS tm_siteuser;
CREATE TABLE tm_siteuser (
  id    INTEGER PRIMARY 
    KEY AUTO_INCREMENT,
  username VARCHAR(100) NOT NULL 
    UNIQUE KEY,
  firstname TEXT NOT NULL,
  middlename TEXT NOT NULL,
  email TEXT NOT NULL,
  birthday DATE NOT NULL,
  t1 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  hashpass CHAR(128) NOT NULL,
  typeid INT(2) NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tm_products;
CREATE TABLE tm_products (
  id INTEGER NOT NULL 
    PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  price TEXT,
  t1 TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  user_id INTEGER,
  INDEX u_id (user_id),
  FOREIGN KEY (user_id)
    REFERENCES tm_siteuser(id)
   ON DELETE CASCADE
   ON UPDATE CASCADE 
) ENGINE=INNODB;;

DROP TABLE IF EXISTS tm_order;
CREATE TABLE tm_order(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  client_id INTEGER NOT NULL REFERENCES tm_user(id),
  INDEX (product_id),
  FOREIGN KEY (product_id)
    REFERENCES tm_products(id)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  INDEX (client_id), 
  FOREIGN KEY (client_id)
    REFERENCES tm_siteuser(id)  
) ENGINE=INNODB;
