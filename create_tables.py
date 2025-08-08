from db_config import get_connection

conn = get_connection()
c1 = conn.cursor()

# Create registration_information table
c1.execute("""
CREATE TABLE IF NOT EXISTS registration_information (
    reg_no INT AUTO_INCREMENT PRIMARY KEY,
    aadhar_no BIGINT UNIQUE,
    father_name VARCHAR(50),
    mother_name VARCHAR(50),
    examination_applied VARCHAR(50),
    year INT,
    gender VARCHAR(10),
    date_of_birth VARCHAR(10),
    nationality VARCHAR(20),
    marital_status VARCHAR(15),
    community VARCHAR(20),
    minority VARCHAR(5),
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
)
""")

# Create login_info table
c1.execute("""
CREATE TABLE IF NOT EXISTS login_info (
    user VARCHAR(20) PRIMARY KEY,
    pass VARCHAR(30)
)
""")

conn.commit()
conn.close()
print("Tables created successfully!")
