init -2 python:
    class Job(): # A job is just a title displayed on the screen and a name that is displayed. A person can only have one job at a time (if it's not a full time job it's just a Role).
        def __init__(self, job_title, job_roles = None, job_location = None, hire_function = None, quit_function = None, work_days = None, work_times = None,
            seniority_level = 1, wage_adjustment = 1.0, productivity_adjustment = 1.0, promotion_function = None,
            mandatory_duties = None, available_duties = None):
            self.job_title = job_title # The string that is displayed on the hud
            if job_roles is None:
                self.job_roles = [unimportant_job_role]
            elif isinstance(job_roles, list):
                self.job_roles = job_roles # Roles that are added and removed when a person is hired onto or fired from this job.
            else:
                self.job_roles = [job_roles] #Job role i

            self._job_location = None
            self.job_location = job_location # If job location is None than the character is allowed in to spend their job time in any of the public spaces.


            self.hire_function = hire_function # Called when a role is give to a character. Should take a Person as a parameter.
            self.quit_function = quit_function #Function called when a character quits this job. Should take a Person as a parameter

            if work_days is None:
                work_days = [0,1,2,3,4]
            if work_times is None:
                work_times = [1,2,3]
            self.work_days = work_days
            self.work_times = work_times
            self.schedule = Schedule()
            self.schedule.set_schedule(self.job_location, self.work_days, self.work_times)

            self.seniority_level = seniority_level # How experienced or far up the career ladder this job is. Girls will be unhappy or unwilling to take jobs with lower seniority levels.
            self.wage_adjustment = wage_adjustment #How much more or less than basic income this job demands.
            self.productivity_adjustment = productivity_adjustment #How much more or less this job produces compared to normal.

            self.promotion_function = promotion_function #Takes a Person and returns True if they can be promoted to that job, False if that promotion should be hidden, or a string if it is disabled.
            #TODO: Add passive drain to girls expected seniority levels.

            if mandatory_duties is None:
                self.mandatory_duties = []
            elif not isinstance(mandatory_duties, list):
                self.mandatory_duties = [mandatory_duties]
            else:
                self.mandatory_duties = mandatory_duties

            if available_duties is None:
                self.available_duties = []
            elif not isinstance(available_duties, list):
                self.available_duties = [available_duties]
            else:
                self.available_duties = available_duties

            self.identifier = hash((self.job_title, self.job_location,
                tuple(x for x in map(hash, self.work_days)),
                tuple(x for x in map(hash, self.work_times))
                ))

        def resume_job_schedule(self):
            self.schedule.set_schedule(self.job_location, self.work_days, self.work_times)

        def pause_job_schedule(self):
            self.schedule.set_schedule(None, self.work_days, self.work_times)

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.job_title == other.job_title and self.job_location == other.job_location and self.work_days == other.work_days and self.work_times == other.work_times:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return self.identifier

        @property
        def job_location(self):
            return next((x for x in list_of_places if x.identifier == self._job_location), None)

        @job_location.setter
        def job_location(self, value):
            if isinstance(value, Room):
                self._job_location = value.identifier
