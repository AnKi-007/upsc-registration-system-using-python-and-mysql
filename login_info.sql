CREATE TABLE IF NOT EXISTS login_info (
    username VARCHAR(50),
    password VARCHAR(50)
);

-- Optional: insert a default login
INSERT INTO login_info (username, password) VALUES ('admin', 'admin123');
