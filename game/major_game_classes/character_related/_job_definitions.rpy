# LIST OF GENERIC JOBS #

label instantiate_jobs():
    python:
        unemployed_job = Job("Unemployed", unemployed_role, work_days = [], work_times = [])

        ## HR Jobs ##
        hr_job = Job("Personnel Manager", employee_role, job_location = mc.business.h_div, hire_function = setup_employee_stats,
            mandatory_duties = [hr_work_duty], available_duties = [] + general_duties_list + general_hr_duties)
        #TODO: Personal secretary job

        ## Market Jobs ##
        market_job = Job("Sales Representative",  employee_role, job_location = mc.business.m_div, hire_function = setup_employee_stats,
            mandatory_duties = [market_work_duty], available_duties = [] + general_duties_list + general_market_duties)


        ## R&D Jobs ##
        head_researcher_job = Job("Head Researcher", [employee_role, head_researcher], job_location = mc.business.r_div, hire_function = setup_employee_stats,
            mandatory_duties = [research_work_duty, head_researcher_duty], available_duties = [] + general_duties_list + general_rd_duties)
        rd_job = Job("R&D Scientist", employee_role, job_location = mc.business.r_div, hire_function = setup_employee_stats,
            seniority_level = 2, mandatory_duties = [research_work_duty], available_duties = [] + general_duties_list + general_rd_duties)


        ## Supply Jobs ##
        supply_job = Job("Logistics Manager", employee_role, job_location = mc.business.s_div, hire_function = setup_employee_stats,
            mandatory_duties = [supply_work_duty], available_duties = [] + general_duties_list + general_supply_duties)

        ## Production Jobs ##
        production_job = Job("Production Line Worker", employee_role, job_location = mc.business.p_div, hire_function = setup_employee_stats,
            mandatory_duties = [production_work_duty], available_duties = [] + general_duties_list + general_production_duties)

        # intern jobs
        student_intern_rd_job = Job("Student (Biology)", generic_student_role, job_location = university, work_times = [1,2], hire_function = college_intern_hire,
            mandatory_duties = [research_work_duty], available_duties = [] + general_duties_list + general_rd_duties, quit_function = college_intern_quit)
        student_intern_production_job = Job("Student (Chemistry)", generic_student_role, job_location = university, work_times = [1,2], hire_function = college_intern_hire,
            mandatory_duties = [production_work_duty], available_duties = [] + general_duties_list + general_production_duties, quit_function = college_intern_quit)
        student_intern_market_job = Job("Student (Graphic Design)", generic_student_role, job_location = university, work_times = [1,2], hire_function = college_intern_hire,
            mandatory_duties = [market_work_duty], available_duties = [] + general_duties_list + general_market_duties, quit_function = college_intern_quit)
        student_intern_hr_job = Job("Student (Psychology)", generic_student_role, job_location = university, work_times = [1,2], hire_function = college_intern_hire,
            mandatory_duties = [hr_work_duty], available_duties = [] + general_duties_list + general_hr_duties, quit_function = college_intern_quit)
        student_intern_supply_job = Job("Student (Business)", generic_student_role, job_location = university, work_times = [1,2], hire_function = college_intern_hire,
            mandatory_duties = [supply_work_duty], available_duties = [] + general_duties_list + general_supply_duties, quit_function = college_intern_quit)

        # Jobs with existing effects #TODO Some of these should leave new roles (ex-stripper, etc.) when you hire someone.
        student_job = Job("Student", generic_student_role, job_location = university, work_times = [1,2]) #Note that this is different from Emily's Student role, which is really a "tutee" role.

        stripper_job = Job("Stripper", stripper_role, job_location = strip_club, work_days = [0,1,2,3,4,5,6], work_times = [3,4], hire_function = stripper_hire, quit_function = stripper_replace)
        prostitute_job = Job("Prostitute", prostitute_role, job_location = downtown, work_days = [0,1,2,3,4,5,6], work_times = [3,4])

        # Random city roles, with no specific stuff related to them.
        secretary_job = Job("Secretary", unimportant_job_role, job_location = mom_office_lobby, work_days = [0,1,2,3,4], work_times = [1,2])

        barista_job = Job("Barista", unimportant_job_role, job_location = coffee_shop, work_days = [0,1,2,3,4,5], work_times = [1,2])
        bartender_job = Job("Bartender", unimportant_job_role, job_location = downtown_bar, work_days = [2,3,4,5,6], work_times = [3,4])
        waitress_job = Job("Waitress", unimportant_job_role, job_location = downtown_bar, work_days = [2,3,4,5,6], work_times = [3,4])

        hotel_receptionist_job = Job("Receptionist", unimportant_job_role, job_location = downtown_hotel, work_days = [2,3,4,5,6], work_times = [1,2])
        hotel_maid_job = Job("Maid", unimportant_job_role, job_location = downtown_hotel, work_days = [0,2,4,6], work_times=[1,2])
        hotel_maid_job2 = Job("Maid", unimportant_job_role, job_location = downtown_hotel, work_days = [1,3,5], work_times=[1,2,3])
        hotel_chef_job = Job("Chef", unimportant_job_role, job_location = downtown_hotel, work_days = [0,2,3,4,5,6], work_times = [2, 3])

        clothing_cashier_job = Job("Cashier", unimportant_job_role, job_location = clothing_store, work_days = [0,1,2,3,4], work_times = [1,2])
        sex_cashier_job = Job("Cashier", unimportant_job_role, job_location = sex_store, work_days = [0,1,2,3,4], work_times = [1,2])
        electronics_cashier_job = Job("Cashier", unimportant_job_role, job_location = electronics_store, work_days = [0,1,2,3,4,5], work_times = [1,2])
        electronics_support_job = Job("Customer Support", unimportant_job_role, job_location = electronics_store, work_days = [0,1,2,3,4], work_times = [1,2])
        supply_cashier_job = Job("Cashier", unimportant_job_role, job_location = office_store, work_days = [0,1,2,3,4,5], work_times = [1,2])
        home_improvement_cashier_job = Job("Cashier", unimportant_job_role, job_location = home_store, work_days = [0,1,2,3,4,5], work_times = [1,2])
        home_improvement_support_job = Job("Customer Support", unimportant_job_role, job_location = home_store, work_days = [0,1,2,3,4], work_times = [1,2])
        salon_hairdresser_job = Job("Hairdresser", unimportant_job_role, job_location = mall_salon, work_days=[1,2,3,4,5], work_times = [1, 2])
        store_assistant_job = Job("Store Assistant", unimportant_job_role, job_location = mall, work_days = [0,1,2,3,4], work_times = [1,2])
        store_clerk_job = Job("Store Clerk", unimportant_job_role, job_location = office_store, work_days = [0,1,2,3,4], work_times = [1,2])

        gym_instructor_job = Job("Gym Instructor", unimportant_job_role, job_location = gym, work_days = [0,1,2,3,4], work_times = [1,2])
        yoga_teacher_job = Job("Yoga Teacher", unimportant_job_role, job_location = gym, work_days = [0,1,2,3,4], work_times = [2,3])

        doctor_job = Job("Doctor", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        nurse_job = Job("Nurse", unimportant_job_role, job_location = downtown, work_days = [0,1,2,3,4,5], work_times = [1,2])
        night_nurse_job = Job("Night Nurse", unimportant_job_role, job_location = downtown, work_days = [1,2,3,4,5,6], work_times = [3,4])
        office_worker_job = Job("Office Worker", unimportant_job_role, job_location = mom_office_lobby, work_days = [0,1,2,3,4], work_times = [1,2])
        lawyer_job = Job("Lawyer", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        architect_job = Job("Architect", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        interior_decorator_job = Job("Interior Decorator", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        fashion_designer_job = Job("Fashion Designer", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        pro_gamer_job = Job("Pro Gamer", critical_job_role, job_location = gaming_cafe, work_days = [2,4,5,6], work_times = [2, 3])
        university_professor_job = Job("Professor", critical_job_role, job_location = university, work_days = [0,1,2,3,4], work_times = [1, 2])

        list_of_jobs.append([unemployed_job, 20])
        list_of_jobs.append([secretary_job, 3])

        list_of_jobs.append([barista_job, 3])
        list_of_jobs.append([bartender_job, 3])
        list_of_jobs.append([waitress_job, 3])

        list_of_jobs.append([hotel_receptionist_job, 3])
        list_of_jobs.append([hotel_maid_job, 3])
        list_of_jobs.append([hotel_maid_job2, 3])
        list_of_jobs.append([hotel_chef_job, 3])

        list_of_jobs.append([clothing_cashier_job, 3])
        list_of_jobs.append([sex_cashier_job, 3])
        list_of_jobs.append([electronics_cashier_job, 3])
        list_of_jobs.append([electronics_support_job, 3])
        list_of_jobs.append([supply_cashier_job, 3])
        list_of_jobs.append([home_improvement_cashier_job, 3])
        list_of_jobs.append([home_improvement_support_job, 3])
        list_of_jobs.append([salon_hairdresser_job, 3])
        list_of_jobs.append([store_assistant_job, 3])
        list_of_jobs.append([store_clerk_job, 3])

        list_of_jobs.append([gym_instructor_job, 3])
        list_of_jobs.append([yoga_teacher_job, 3])

        list_of_jobs.append([doctor_job, 2])
        list_of_jobs.append([nurse_job, 3])
        list_of_jobs.append([night_nurse_job, 3])
        list_of_jobs.append([office_worker_job, 3])
        list_of_jobs.append([lawyer_job, 2])
        list_of_jobs.append([architect_job, 2])
        list_of_jobs.append([interior_decorator_job, 2])
        list_of_jobs.append([fashion_designer_job, 2])
        list_of_jobs.append([pro_gamer_job, 2])
        list_of_jobs.append([university_professor_job, 2])
    return
