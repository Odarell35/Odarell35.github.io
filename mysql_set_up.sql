CREATE DATABASE IF NOT EXISTS eBook_db;
CREATE USER IF NOT EXISTS 'eBook_user'@'localhost' IDENTIFIED BY 'ebook_pwd';
GRANT ALL PRIVILEGES ON eBook_db.* TO 'eBook_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'eBook_user'@'localhost';
