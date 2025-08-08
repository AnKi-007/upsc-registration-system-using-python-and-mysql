-- Create database
CREATE DATABASE IF NOT EXISTS upsc;
USE upsc;

-- Create login_info table
CREATE TABLE IF NOT EXISTS login_info (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL
);

-- Optionally insert test login (you can remove this in production)
INSERT INTO login_info (username, password) VALUES ('admin', 'admin123');

-- Create registration_information table
CREATE TABLE IF NOT EXISTS registration_information (
    reg_no INT AUTO_INCREMENT PRIMARY KEY,
    aadhar_no BIGINT,
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    examination_applied VARCHAR(100),
    year INT,
    gender VARCHAR(10),
    date_of_birth VARCHAR(20),
    nationality VARCHAR(50),
    marital_status VARCHAR(20),
    community VARCHAR(20),
    minority VARCHAR(10),
    add_1 VARCHAR(100),
    add_2 VARCHAR(100),
    add_3 VARCHAR(100),
    dist VARCHAR(50),
    state VARCHAR(50),
    pin_code INT,
    pho_no BIGINT,
    mobile_no BIGINT,
    e_mail VARCHAR(100),
    education_qualification VARCHAR(100),
    preference VARCHAR(50),
    p_f_cds_pabt INT,
    sainik_milt_sch INT,
    son_sainik_mil_sch INT,
    name VARCHAR(100)
);
