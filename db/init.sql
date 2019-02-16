CREATE DATABASE telemedicina;
use telemedicina;

CREATE TABLE siteuser (
  uname VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO siteuser
  (uname, email)
VALUES
  ('hildermes', 'hildermes@gmail.com'),
  ('rodolpho', 'luiz@portaltelemedicina.com.br'),
  ('irving', 'irving.badolato@gmail.com');
