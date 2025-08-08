CREATE TABLE registration_information (
    reg_no INT AUTO_INCREMENT PRIMARY KEY,
    aadhar_no BIGINT NOT NULL,
    father_name VARCHAR(100) NOT NULL,
    mother_name VARCHAR(100) NOT NULL,
    examination_applied VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    date_of_birth DATE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    marital_status VARCHAR(50) NOT NULL,
    community VARCHAR(50) NOT NULL,
    minority VARCHAR(10) NOT NULL,
    add_1 VARCHAR(255),
    add_2 VARCHAR(255),
    add_3 VARCHAR(255),
    dist VARCHAR(100),
    state VARCHAR(100),
    pin_code INT,
    pho_no BIGINT,
    mobile_no BIGINT,
    e_mail VARCHAR(100),
    education_qualification VARCHAR(255),
    preference VARCHAR(100),
    p_f_cds_pabt BOOLEAN,
    sainik_milt_sch BOOLEAN,
    son_sainik_mil_sch BOOLEAN,
    name VARCHAR(100) NOT NULL
);


-- INSERT INTO registration_information (
--     aadhar_no, father_name, mother_name, examination_applied, year, gender,
--     date_of_birth, nationality, marital_status, community, minority,
--     add_1, add_2, add_3, dist, state, pin_code, pho_no, mobile_no,
--     e_mail, education_qualification, preference, p_f_cds_pabt,
--     sainik_milt_sch, son_sainik_mil_sch, name
-- ) VALUES (
--     302477658125, 'abc Kumar', 'xyz Kumari', 'CDS', 22, 'Male',
--     '2003-06-07', 'Indian', 'Unmarried', 'Hindu', 'No',
--     'fl. no. 103', 'lohegaon', 'Pune', 'Pune', 'Maharashtra', 411047,
--     1245325698, 9142352698, 'jaishreeram007@gmail.com',
--     'Appearing for Final Year (B.Tech Data Science)', 'AFA>IMA>OTA', 0,
--     0, 0, 'Anand Kishore'
-- );

  -- you can insert values like this while your registration.