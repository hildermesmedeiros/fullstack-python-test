CREATE DATABASE telemedicina;
use telemedicina;
SET sql_mode = '';
DROP TABLE IF EXISTS tm_siteuser;
CREATE TABLE tm_siteuser (
  id    INTEGER NOT NULL 
    PRIMARY KEY AUTO_INCREMENT,
  uname VARCHAR(100) NOT NULL 
    UNIQUE KEY,
  fname TEXT NOT NULL,
  mname TEXT NOT NULL,
  email TEXT NOT NULL,
  niver DATE NOT NULL,
  t1 TIMESTAMP NOT NULL 
    ON UPDATE CURRENT_TIMESTAMP,
  hashpass CHAR(128) NOT NULL,
  typeid INT(2) NOT NULL
)ENGINE=INNODB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tm_client;
CREATE TABLE tm_client(
  id INTEGER NOT NULL PRIMARY KEY,
  user_id INTEGER,
  INDEX u_ind (user_id),
  FOREIGN KEY (user_id)
    REFERENCES tm_siteuser(id)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tm_products;
CREATE TABLE tm_products (
  id INTEGER NOT NULL 
    PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  price TEXT,
  t1 TIMESTAMP NOT NULL 
    ON UPDATE CURRENT_TIMESTAMP,
  user_id INTEGER,
  INDEX u_id (user_id),
  FOREIGN KEY (user_id)
    REFERENCES tm_client(user_id)
)ENGINE=INNODBD DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tm_order;
CREATE TABLE tm_order(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  client_id INTEGER NOT NULL REFERENCES tm_user(id),
  INDEX (product_id),
  INDEX (client_id),
  
  FOREIGN KEY (product_id)
    REFERENCES tm_products(id)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  
  FOREIGN KEY (client_id)
    REFERENCES tm_client(id)
  
)ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO tm_siteuser(
  uname, fname, mname, email, niver, hashpass,typeid
)
VALUES
  ('test', 'teste', 'teste', 'teste','1987-12-04', 'cf23df2207d99a74fbe169e3eba035e633b65d94', '2');

