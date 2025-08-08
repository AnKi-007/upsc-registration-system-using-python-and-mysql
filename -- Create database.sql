
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

INSERT INTO registration_information (
    aadhar_no, father_name, mother_name, examination_applied, year, gender,
    date_of_birth, nationality, marital_status, community, minority,
    add_1, add_2, add_3, dist, state, pin_code, pho_no, mobile_no,
    e_mail, education_qualification, preference, p_f_cds_pabt,
    sainik_milt_sch, son_sainik_mil_sch, name
) VALUES (
    123456789012, 'Rajesh Kumar', 'Sunita Devi', 'CDS', 2025, 'Male',
    '2000-04-15', 'Indian', 'Single', 'General', 'No',
    '123 MG Road', 'Sector 5', 'Near Park', 'Lucknow', 'Uttar Pradesh', 226001,
    9123456789, 9876543210, 'anand@example.com', 'B.Sc Physics', 'IMA>OTA>AFA',
    0, 0, 1, 'Anand Kishore'
);

