from db_config import get_connection

conn = get_connection()
c1 = conn.cursor()

# Login
user = input("Enter username: ")
passwd = input("Enter password: ")

c1.execute("SELECT username, password FROM login_info")
login_data = c1.fetchall()

if (user, passwd) in login_data:
    print("\n=== UPSC REGISTRATION SYSTEM ===")
    print("1: Add Registration Details")
    print("2: View Registered Details")
    print("3: Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Collect registration inputs
        v_ea = input("Examination applied: ")
        v_yr = int(input("Year: "))
        v_name = input("Name: ")
        v_gen = input("Gender: ")
        v_dob = input("Date of birth (DD/MM/YYYY): ")
        v_f_na = input("Father's name: ")
        v_m_na = input("Mother's name: ")
        v_nat = input("Nationality: ")
        v_mar_st = input("Marital status: ")
        v_comm = input("Community: ")
        v_min = input("Minority (Yes/No): ")
        v_add1 = input("Address line 1: ")
        v_add2 = input("Address line 2: ")
        v_add3 = input("Address line 3: ")
        v_dist = input("District: ")
        v_state = input("State: ")
        v_pin = int(input("PIN code: "))
        v_pho = int(input("Phone number: "))
        v_mob = int(input("Mobile number: "))
        v_ema = input("Email: ")
        v_edu = input("Education qualification: ")
        v_aadh = int(input("Aadhar number: "))
        v_pre = input("Preference: ")
        v_p_f = int(input("Failed in CPSS/PABT (1/0): "))
        v_stu_sa = int(input("Student of Sainik/Military School (1/0): "))
        v_son_mil = int(input("Son of Military Personnel in Sainik School (1/0): "))

        # Insert into database (excluding reg_no)
        query = """
        INSERT INTO registration_information (
            aadhar_no, father_name, mother_name, examination_applied, year, gender,
            date_of_birth, nationality, marital_status, community, minority,
            add_1, add_2, add_3, dist, state, pin_code, pho_no, mobile_no,
            e_mail, education_qualification, preference, p_f_cds_pabt,
            sainik_milt_sch, son_sainik_mil_sch, name
        ) VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s
        )
        """

        values = (
            v_aadh, v_f_na, v_m_na, v_ea, v_yr, v_gen, v_dob, v_nat, v_mar_st, v_comm,
            v_min, v_add1, v_add2, v_add3, v_dist, v_state, v_pin, v_pho, v_mob, v_ema,
            v_edu, v_pre, v_p_f, v_stu_sa, v_son_mil, v_name
        )

        c1.execute(query, values)
        conn.commit()
        reg_no = c1.lastrowid  # Auto-generated reg_no
        print(f"\nSuccessfully registered. Your Registration No. is: {reg_no}")

    elif choice == 2:
        reg = int(input("Enter registration number: "))
        c1.execute("""
            SELECT reg_no, aadhar_no, father_name, mother_name, examination_applied, year,
            gender, date_of_birth, nationality, marital_status, community, minority,
            add_1, add_2, add_3, dist, state, pin_code,
            pho_no, mobile_no, e_mail, education_qualification, preference,
            p_f_cds_pabt, sainik_milt_sch, son_sainik_mil_sch, name
            FROM registration_information
            WHERE reg_no = %s
        """, (reg,))
        data = c1.fetchone()

        if data:
            print("\n--- Registration Details ---")
            labels = [
                "Registration No", "Aadhar No", "Father's Name", "Mother's Name", "Examination Applied", "Year",
                "Gender", "Date of Birth", "Nationality", "Marital Status", "Community", "Minority",
                "Address Line 1", "Address Line 2", "Address Line 3", "District", "State", "PIN Code",
                "Phone Number", "Mobile Number", "Email", "Education Qualification", "Preference",
                "CPSS/PABT Failed", "Student of Sainik School", "Son of Military in Sainik School", "Candidate Name"
            ]
            for label, value in zip(labels, data):
                print(f"{label}: {value}")
        else:
            print("No data found with this Registration Number.")

    elif choice == 3:
        print("Exiting the system...")

    else:
        print("Invalid choice.")

else:
    print("Login failed. Check username or password.")

conn.close()
