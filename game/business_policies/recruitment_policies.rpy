init 0 python:
    #Define all helper functions first
    def increase_interview_cost(amount):
        mc.business.recruitment_cost += amount

    def decrease_interview_cost(amount):
        mc.business.recruitment_cost -= amount



    recruitment_policies_list = []

    #### RECRUITMENT IMPROVEMENT POLICIES ####

    recruitment_batch_one_policy = Policy(name = "Recruitment Batch Size Improvement One",
        desc = "More efficient hiring software will allow you to review an additional resume in each recruitment batch.",
        cost = 200,
        toggleable = True,
        extra_data = {"recruitment_batch_adjust":1})

    recruitment_policies_list.append(recruitment_batch_one_policy)

    recruitment_batch_two_policy = Policy(name = "Recruitment Batch Size Improvement Two",
        desc = "Further improvements in hiring software and protocols allows you to review an additional two resumes in each recruitment batch.",
        cost = 600,
        toggleable = True,
        active_requirement = recruitment_batch_one_policy,
        dependant_policies = recruitment_batch_one_policy,
        extra_data = {"recruitment_batch_adjust":2})

    recruitment_policies_list.append(recruitment_batch_two_policy)

    recruitment_batch_three_policy = Policy(name = "Recruitment Batch Size Improvement Three",
        desc = "A complete suite of recruitment software lets you maximize the use of your time while reviewing resumes.\nAllows you to review four additional resumes in each recruitment batch.",
        cost = 1200,
        toggleable = True,
        active_requirement = recruitment_batch_two_policy,
        dependant_policies = recruitment_batch_two_policy,
        extra_data = {"recruitment_batch_adjust":4})

    recruitment_policies_list.append(recruitment_batch_three_policy)

    recruitment_knowledge_one_policy = Policy(name = "Applicant Questionnaire",
        desc = "A simple questionnaire required from each applicant reveals some of their basic information and likes and dislikes, helping to determine if they would a good fit for your company culture.\nReveals age, height, obedience and two opinions on an applicants resume.",
        cost = 400,
        toggleable = True,
        extra_data = {"reveal_count_adjust":2,"reveal_obedience":True,"reveal_age":True,"reveal_height":True})
    recruitment_policies_list.append(recruitment_knowledge_one_policy)

    recruitment_knowledge_two_policy = Policy(name = "Applicant Background Checks",
        desc = "An automated background check produces a detailed history for each applicant. This can reveal a great deal of information about a potential employee before they even step in the door.\nReveals breast size, relationship status and two more opinions on an applicants resume.",
        cost = 800,
        toggleable = True,
        active_requirement = recruitment_knowledge_one_policy,
        dependant_policies = recruitment_knowledge_one_policy,
        extra_data = {"reveal_count_adjust":2,"reveal_relationship":True,"reveal_tits":True})
    recruitment_policies_list.append(recruitment_knowledge_two_policy)

    recruitment_knowledge_three_policy = Policy(name = "Applicant History Deep Dive",
        desc = "Scrapping the web for any and all information about an applicant can reveal a startling amount of information.\nReveals suggestibility, number of kids and one more opinion on an applicants resume.\nRevealed opinions may be about sex.",
        cost = 1500,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        extra_data = {"reveal_count_adjust":2,"reveal_sex_opinion":True,"reveal_suggestibility":True,"reveal_kids":True})
    recruitment_policies_list.append(recruitment_knowledge_three_policy)

    recruitment_knowledge_four_policy = Policy(name = "Applicant Sexual History Survey",
        desc = "A detailed questionnaire focused on sex, fetishes, and kinks produces even more information about an applicants sexual preferences.\nIt can also be used as a surprisingly accurate predictor of sexual experience.\nReveals one more opinion and the sluttiness and sex skills are now displayed on an applicants resume.",
        cost = 2500,
        toggleable = True,
        active_requirement = recruitment_knowledge_three_policy,
        dependant_policies = recruitment_knowledge_three_policy,
        extra_data = {"reveal_count_adjust":2,"reveal_sex_skills":True,"reveal_sluttiness":True})
    recruitment_policies_list.append(recruitment_knowledge_four_policy)


    recruitment_skill_improvement_policy = Policy(name = "Recruitment Skill Improvement",
        desc = "Restricting your recruitment search to university and college graduates improves their skill across all disciplines.\nRaises all skill caps by 2 and lowers the average age by 5 when hiring new employees.",
        cost = 800,
        toggleable = True,
        extra_data = {"skill_ceiling_adjust":2,"age_floor_adjust":-5,"age_ceiling_adjust":-5})
    recruitment_policies_list.append(recruitment_skill_improvement_policy)

    recruitment_skill_minimums_policy = Policy(name = "Recruitment Skill Minimums",
        desc = "By carefully vetting the references of potential recruits you can weed out those with poor skills.\nRaises all skill minimums when hiring new employees by 2.\nRaises the cost of screening applicants by $100 while active.",
        cost = 800,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        extra_data = {"skill_floor_adjust":2,"interview_cost_adjust":100})
    recruitment_policies_list.append(recruitment_skill_minimums_policy)


    recruitment_stat_improvement_policy = Policy(name = "Recruitment Stat Improvement",
        desc = "A wide range of networking connections can put you in touch with the best and brightest in the industry.\nRaises all statistic caps by 2 and raises the average age by 5 when hiring new employees.",
        cost = 1500,
        toggleable = True,
        own_requirement = recruitment_skill_improvement_policy,
        dependant_policies = recruitment_skill_improvement_policy,
        extra_data = {"stat_ceiling_adjust":2,"age_floor_adjust":5,"age_ceiling_adjust":5})
    recruitment_policies_list.append(recruitment_stat_improvement_policy)

    recruitment_stat_minimums_policy = Policy(name = "Recruitment Stat Minimums",
        desc = "By introducing screening interviews with general aptitude tests you can weed out interviewees with poor abilities.\nRaises all statistic minimums when hiring new employees by two.\nRaises the cost of screening applicants by $500 while active.",
        cost = 1500,
        toggleable = True,
        own_requirement = recruitment_skill_minimums_policy,
        dependant_policies = recruitment_skill_minimums_policy,
        extra_data = {"stat_floor_adjust":2,"interview_cost_adjust":500})
    recruitment_policies_list.append(recruitment_stat_minimums_policy)

    recruitment_suggest_improvement_policy = Policy(name = "High Suggestibility Recruits",
        desc = "You change your focus to hiring younger, more impressionable employees.\nNew employees will all have a starting suggestibility of 5.\nLowers average age by 5.",
        cost = 1000,
        toggleable = True,
        active_requirement = recruitment_knowledge_three_policy,
        dependant_policies = recruitment_knowledge_three_policy,
        extra_data = {"suggestibility_floor_adjust":5,"suggestibility_ceiling_adjust":5,"age_floor_adjust":-5,"age_ceiling_adjust":-5})
    recruitment_policies_list.append(recruitment_suggest_improvement_policy)

    recruitment_obedience_improvement_policy = Policy(name = "High Obedience Recruits",
        desc = "A highly regimented business appeals to some people.\nBy improving your corporate image and stressing company stability new recruits will have a starting obedience 10 points higher than normal.",
        cost = 600,
        toggleable = True,
        extra_data = {"obedience_floor_adjust":10,"obedience_ceiling_adjust":10})
    recruitment_policies_list.append(recruitment_obedience_improvement_policy)

    recruitment_slut_improvement_policy = Policy(name = "High Sluttiness Recruits",
        desc = "Narrowing your resume search parameters to include previous experience at strip clubs, bars, and modeling agencies produces a batch of potential employees with a much higher initial sluttiness value.\nIncreases starting sluttiness by 20, lowers average age by 5.",
        cost = 1200,
        toggleable = True,
        own_requirement = [recruitment_obedience_improvement_policy],
        active_requirement = [recruitment_knowledge_four_policy],
        dependant_policies = [recruitment_knowledge_four_policy],
        extra_data = {"sluttiness_floor_adjust":20,"sluttiness_ceiling_adjust":20,"age_floor_adjust":-5,"age_ceiling_adjust":-5})
    recruitment_policies_list.append(recruitment_slut_improvement_policy)

    recruitment_sex_improvement_policy = Policy (name = "Recruitment Sex Skill Improvement",
        desc = "Extending your recruitment advertising to several pornographic sites is likely to draw people with higher than average sex skills.\nRaises all sex skill caps by two.",
        cost = 1500,
        toggleable = True,
        own_requirement = [recruitment_slut_improvement_policy],
        active_requirement = recruitment_knowledge_four_policy,
        dependant_policies = [recruitment_slut_improvement_policy, recruitment_knowledge_four_policy],
        extra_data = {"sex_skill_ceiling_adjust":2})
    recruitment_policies_list.append(recruitment_sex_improvement_policy)

    recruitment_sex_minimums_policy = Policy (name = "Recruitment Sex Skill Minimums",
        desc = "By focusing recruitment on those with prior sex work experience and careful vetting of both work experience and responses to the Applicant Sexual History Surveys, you can weed out applicants without significant sexual experience.\nRaises all sex skill minimums by two.\nRaises the cost of screening applicants by $500 while active.",
        cost = 1500,
        toggleable = True,
        own_requirement = [recruitment_sex_improvement_policy,recruitment_slut_improvement_policy, recruitment_skill_minimums_policy],
        active_requirement = [recruitment_knowledge_four_policy],
        dependant_policies=[recruitment_sex_improvement_policy,recruitment_slut_improvement_policy, recruitment_knowledge_four_policy,recruitment_skill_minimums_policy],
        extra_data = {"sex_skill_floor_adjust":2,"interview_cost_adjust":500})
    recruitment_policies_list.append(recruitment_sex_minimums_policy)


    recruitment_big_tits_policy = Policy(name = "Screening Criteria: Large Breasts",
        desc = "Only accept resumes from applicants with a D cup or larger.\nRaises the cost of screening applicants by $100 while active.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "breast_criteria",
        extra_data = {"tits_range":Person.get_large_tits_weighted_list(),"interview_cost_adjust":100})
    recruitment_policies_list.append(recruitment_big_tits_policy)

    recruitment_huge_tits_policy = Policy(name = "Screening Criteria: Huge Breasts",
        desc = "All but the most big-breasted women have their resume automatically rejected, ensuring all applicants will have an E cup or larger.\nRaises the cost of screening applicants by $500 while active.",
        cost = 4500,
        toggleable = True,
        own_requirement = [recruitment_big_tits_policy],
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "breast_criteria",
        extra_data = {"tits_range":Person.get_huge_tits_weighted_list(),"interview_cost_adjust":500})
    recruitment_policies_list.append(recruitment_huge_tits_policy)

    recruitment_small_tits_policy = Policy(name = "Screening Criteria: Small Breasts",
        desc = "Eliminates resumes from applicants with a D cup or larger, leaving only small-chested women in the application pool.\nRaises the cost of screening applicants by $100 while active.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "breast_criteria",
        extra_data = {"tits_range":Person.get_small_tits_weighted_list(),"interview_cost_adjust":100})
    recruitment_policies_list.append(recruitment_small_tits_policy)

    recruitment_tiny_tits_policy = Policy(name = "Screening Criteria: Tiny Breasts",
        desc = "Automatically removes the resume of any woman applying with more than an AA cup.\nThe smaller pool of talent raises the cost of screening applicants by $500 while active.",
        cost = 4500,
        toggleable = True,
        own_requirement = recruitment_small_tits_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "breast_criteria",
        extra_data = {"tits_range":Person.get_tiny_tits_weighted_list(),"interview_cost_adjust":500})
    recruitment_policies_list.append(recruitment_tiny_tits_policy)

    recruitment_short_policy = Policy(name = "Screening Criteria: Short",
        desc = "Only accept applications from women under 5',3\".\nRaises the cost of applicant screening by $50.",
        cost = 1500,
        toggleable = True,
        active_requirement = recruitment_knowledge_one_policy,
        dependant_policies = recruitment_knowledge_one_policy,
        exclusive_tag = "height_criteria",
        extra_data = {"height_ceiling":Person.get_short_height_ceiling(),"interview_cost_adjust":50})
    recruitment_policies_list.append(recruitment_short_policy)

    recruitment_tall_policy = Policy(name = "Screening Criteria: Tall",
        desc = "Only accept applications from women over 5',9\".\nRaises the cost of applicant screening by $50.",
        cost = 1500,
        toggleable = True,
        active_requirement = recruitment_knowledge_one_policy,
        dependant_policies = recruitment_knowledge_one_policy,
        exclusive_tag = "height_criteria",
        extra_data = {"height_floor":Person.get_tall_height_floor(),"interview_cost_adjust":50})
    recruitment_policies_list.append(recruitment_tall_policy)


    recruitment_single_policy = Policy(name = "Screening Criteria: Single",
        desc = "Take applications only from women who are currently single.\nRaise the cost of applicant screening by $200, lowers average age.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "relationship_criteria",
        extra_data = {"relationships_allowed":["Single"],"interview_cost_adjust":200})
    recruitment_policies_list.append(recruitment_single_policy)

    recruitment_married_policy = Policy(name = "Screening Criteria: Married",
        desc = "Take applications only from women who are married.\nRaise the cost of applicant screening by $200, raises average age.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_two_policy,
        dependant_policies = recruitment_knowledge_two_policy,
        exclusive_tag = "relationship_criteria",
        extra_data = {"relationships_allowed":["Married"],"interview_cost_adjust":200})
    recruitment_policies_list.append(recruitment_married_policy)

    recruitment_old_policy = Policy(name = "Screening Criteria: Old",
        desc = "Only accept applications from women 40 or older.\nRaise the cost of applicant screening by $100.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_one_policy,
        dependant_policies = recruitment_knowledge_one_policy,
        exclusive_tag = "age_criteria",
        extra_data = {"age_floor":Person.get_old_age_floor(),"interview_cost_adjust":100})
    recruitment_policies_list.append(recruitment_old_policy)

    recruitment_teen_policy = Policy(name = "Screening Criteria: Teenager",
        desc = "Only accept applications from women ages 18 or 19.\nRaise the cost of applicant screening by $400.",
        cost = 5000,
        toggleable = True,
        active_requirement = recruitment_knowledge_one_policy,
        dependant_policies = recruitment_knowledge_one_policy,
        exclusive_tag = "age_criteria",
        extra_data = {"age_ceiling":Person.get_teen_age_ceiling(),"interview_cost_adjust":400})
    recruitment_policies_list.append(recruitment_teen_policy)

    #Children depend on age, so these go last
    recruitment_mothers_policy = Policy(name = "Screening Criteria: Mother",
        desc = "Only seek applications from women who are mothers.\nRaises the cost of applicant screening by $200.",
        cost = 2000,
        toggleable = True,
        active_requirement = recruitment_knowledge_three_policy,
        dependant_policies = recruitment_knowledge_three_policy,
        exclusive_tag = "mother_criteria",
        extra_data = {"kids_floor":1,"interview_cost_adjust":200})
    recruitment_policies_list.append(recruitment_mothers_policy)

    recruitment_childless_policy = Policy(name = "Screening Criteria: Childless",
        desc = "Only seek applications from women who are not parents.\nRaise the cost of applicant screening by $50.",
        cost = 1000,
        toggleable = True,
        active_requirement = recruitment_knowledge_three_policy,
        dependant_policies = recruitment_knowledge_three_policy,
        exclusive_tag = "mother_criteria",
        extra_data = {"kids_ceiling":0,"interview_cost_adjust":50})
    recruitment_policies_list.append(recruitment_childless_policy)
