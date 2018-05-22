# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:26:45 2018

@author: admin
"""
import random
import json
import datetime
import dateutil.parser as parser
now = datetime.datetime.now()
current_year=now.year
#from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
with open('parseResponse.json', 'r',encoding='utf-8-sig') as myfile:
  txt = myfile.read()
dd=json.loads(txt)
Work_Period=[]
companies_worked_for=[]
functional_blocks_of=[]
per=[]
Technical=[]
months_of_experience=[]
skillset=[]
skill_last_used=[]
skills = ['Apache Ant','Apache POI','Apache POI','Apache POI','AWT','Design Patterns','Easy Mock','Eclipse','EJB','Guava','Hibernate','iBATIS','Jackson','JasperReports','JavaXML','Java','Jbpm5','Java.ioPackage','JavaInterviewQuestions','Java.lang Package','Java.math Package','Java.util Package','Java-8','Java Examples','Java Mail API','JDB','JDBC','JFree Chart','jMeter','JOGL','JPA','JSON','JSP','JUnit','log4j','Lucene','Maven','PDFbox','Servlets','Spring','Struts2.x','Swing','TestNG','Apache Tika','Apache Xerces','XStream', 'Apache Presto','CouchDB','DB2','Document DB','DocumentDB SQL','HSQLDB','IMS DB','Memcached','MariaDB','MongoDB','MySQL','Neo4J','OBIEE','OrientDB','PL/SQL','PouchDB','PostgreSQL','Redis','SQLCertification','SQL','T-SQL','SQLite', 'Git', 'Apex','Arduino','ASP.Net','ASP.Net MVC','ASP.Net WP', 'Assembly','Awk','CStandardLibrary','C++ Standard Library','COBOL','C++','C','Computer Programming','CbyExamples','C#','Clojure','Data Structure & Algorithms','D','Elixir','Erlang','Euphoria','F#','Fortran','GoPrograming','Groovy','Java','Java-8','JCL','LISP','MATLAB','Node.js','ObjectiveC','Pascal','R Programming','Rexx Programming','Socket.io','Swift','Scala','VB.Net','VBA', 'Apache Flume','Apache Impala','Apache Pig','Apache Tajo','Apache Spark','Apache Storm','Spark SQL','Avro','Couch DB','Cassandra','Cognos','Google Charts','Hadoop','HCatalog','Hive','Highcharts','HBase','JFree   Chart','Apache Kafka','Map Reduce','Mahout','Pentaho','Qlik View','R Programming','SAS','Sqoop','Statistics','Teradata','Tableau','Zookeeper', 'CICS','COBOL','DB2','IMSDB','JCL','VSAM', 'Batch Script','C#','Excel','Advanced Excel','Excel Charts','Entity Framework','F#','NHibernate','LinQ','MFC','Microsoft Azure','Powerpoint','Microsoft Access','Microsoft Project','Micro Strategy','MicrosoftCRM','MS SQl Server','MVVM','Sharepoint','Silverlight','VBA','VB.Net','WCF','Word','WPF','XAML','Windows 10 Development','Windows 10', 'Android','Cordova','iOS','jQueryMobile','Ionic','Meteor','PhoneGap','ReactNative','SL4A', 'Ajax','Angular2','AngularJS','Angular Material','ASP.Net','Aurelia','Backbone JS','Bootstrap','CherryPy','CSS','Codeigniter','Coffee Script','CPanel','Drupal','Django','EmberJS','ExtJS','ExpressJS','Firebase','Framework7','Flask','Adobe Flex','Foundation','Grav','Grunt','Gulp','GWT','Google Maps','HTML','HTML5','HTTP','Highcharts','JasmineJS','JavaScript','Joomla','jQuery','jQuery UI','JSF','KnockoutJS','KoaJS','Laravel','LESS','Magento Framework','MaterialDesignLite','Materialize','Mootools','MVC Framework','Prototype','Pure.CSS','React JS','RubyonRails-2.1','RubyonRails','SASS','script.aculo.us','SVG','TurboGears','VB Script','Web Developers Guide','Web Services','RESTful Web Services','W3CSS','Web Icons','Web Sockets','Web2Py','WebGL','WebRTC','Wordpress','XHTML','Yii', 'JavaScript','jQuery','jQueryUI','Lua','Perl','PHP','Python','Python-3','PyGTK','PyQt','WxPython','Ruby','RSpec','Sed','Tcl/Tk','Unix','VBScript']
r=[]
months_used_for=[]
designation_worked_at=[]
number_of_works=len(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"])
functional_area=[]
top_skills=[]
from_period=[]
questions={}
work_experience_null='Not NULL'
n=0
q=[]
com='Not Done'
job_difference=[]
number_of_degrees=len(dd["data"]["CandidateData"][0]["QualificationsDetails"]["QualificationData"])
ques=[]
tq=['What programming languages are you most familiar with?','Describe the troubleshooting process you’d follow for a crashing program.','How can you debug a program while it’s being used?','What is your field of expertise and what would you like to learn more about?','Have you implemented significant improvements to an IT infrastructure? What were they, and how did you implement them?','What’s the most effective way to gather user and system requirements?','Describe a time you had to explain technical details to a non-technical audience.','How did you modify your presentation?','Where do you place most of your focus when reviewing somebody else’s code?']
specific_tq=['Tell me about this project. Who did you work with and what was your specific contribution?','What did you find most challenging about this assignment?','What resources did you use to complete the assignment?','In which of your previous positions/past projects did you use [X] software?','Describe the timeframe and how you worked within it.','What did you learn from the project?','What would you have done differently if you had more time?','What would you do differently if you were under a strict deadline and you couldn’t meet the project scope? Which features would you prioritize?']
for i in range(0,number_of_works):
    if len(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"])==0:
        work_experience_null='Yes'
    elif len(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["DesignationList"])==0:
        work_experience_null='Yes'
if(work_experience_null!='Yes'):
    for i in range(0,number_of_works):
        fp=(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["FromPeriod"]["Date"])

        tp=(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["ToPeriod"]["Date"])
        per.append(fp)
        per.append(tp)
        Work_Period.append(per)
        per=[]
        months_of_experience.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["totalMonthsOfExperience"])
        companies_worked_for.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]['Organization'])
        designation_worked_at.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["DesignationList"])
        functional_area.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["FunctionalArea"])
    for i in range(0,number_of_works):
        from_period.append(dd["data"]["CandidateData"][0]["EmployementsHistoryDetails"]["EmployementHistoryData"][i]["WorkExperience"][0]["FromPeriod"]['Date'])
    for i in range(0,number_of_works):
        fpm1=parser.parse(from_period[i]).month
        fpy1=parser.parse(from_period[i]).year
        for j in range(i+1,number_of_works):
            fpm2=parser.parse(from_period[j]).month
            fpy2=parser.parse(from_period[j]).year
            if(fpy1<fpy2):
                Work_Period[i],Work_Period[j]=Work_Period[j],Work_Period[i]
                months_of_experience[i],months_of_experience[j]=months_of_experience[j],months_of_experience[i]
                companies_worked_for[i],companies_worked_for[j]=companies_worked_for[j],companies_worked_for[i]
                functional_area[i],functional_area[j]=functional_area[j],functional_area[i]
                designation_worked_at[i],designation_worked_at[j]=designation_worked_at[j],designation_worked_at[i]
            elif(fpy1==fpy2):
                    if(fpm1<fpm2):
                        Work_Period[i],Work_Period[j]=Work_Period[j],Work_Period[i]
                        
                        months_of_experience[i],months_of_experience[j]=months_of_experience[j],months_of_experience[i]
                        companies_worked_for[i],companies_worked_for[j]=companies_worked_for[j],companies_worked_for[i]
                        functional_area[i],functional_area[j]=functional_area[j],functional_area[i]
                        designation_worked_at[i],designation_worked_at[j]=designation_worked_at[j],designation_worked_at[i]
                        
    number_of_skills=len(dd["data"]["CandidateData"][0]["SkillSetDetails"])
    for i in range(0,number_of_skills):
        skillset.append(dd["data"]["CandidateData"][0]["SkillSetDetails"][i]["skillname"])
        skill_last_used.append(dd["data"]["CandidateData"][0]["SkillSetDetails"][i]["Skillused"]["lastused"])
        months_used_for.append(dd["data"]["CandidateData"][0]["SkillSetDetails"][i]["Skillused"]["months"])
        '''    
                for i in range(0,number_of_works):
                    print("The candidate worked at",companies_worked_for[i],"for a period of",months_of_experience[i],"months between", Work_Period[i][0],'and',Work_Period[i][1],'\n')
                    '''
                                
    month=['Jan-','Feb-','Mar-','Apr-','May-','Jun-','Jul-','Aug-','Sep-','Oct-','Nov-','Dec-']            
    for i in range(0,number_of_works-2):
        c=0    
        for k in range(0,len(month)-2):
            if month[k] in Work_Period[i][0] and month[k+1] in Work_Period[i+1][1]:
                c=1
                                            
        if c==0:
                s='What did you do after leaving '+companies_worked_for[i]+" in "+ Work_Period[i][1]+'?'
                ques.append(s)
                k='3.)Gap'
                n+=1
        pair={k:ques}
        questions.update(pair)
    
    if(n>=2):
        s="Why are there so many gaps in your Employment History?"
        ques.append(s)
        k='3.)Gap'
    pair={k:ques}
    questions.update(pair)
    ques=[]
    for i in range(0,number_of_works):
        if(months_of_experience[i]<24):
            s='Why did you leave '+companies_worked_for[i]+'after working for only '+str(months_of_experience[i])+' months?'
            ques.append(s)
    k='2.)Experience'
    pair={k:ques}
    questions.update(pair)
    ques=[]
    for i in range(0,number_of_works):
        s='Briefly explain the work you did as '+designation_worked_at[i][0]+' at '+companies_worked_for[i]+' ?'
        ques.append(s)
    k='4)Designation'
    pair={k:ques}
    questions.update(pair)
    ques=[]
                                                                
    for i in range(0,number_of_works-1):
        if(functional_area[i]!=functional_area[i+1]):
            ques.append("Why did you change your functional area from "+functional_area[i+1]+' to '+functional_area[i]+' after leaving '+companies_worked_for[i+1]+' ?')
            k='5.)Functional Area'
    pair={k:ques}
    questions.update(pair)
    ques=[]
    print("Enter the number of skills reqd")
    top=int(input())
    print("Out of",skillset,"what are your top ", top ,"skills ?\n")
    print("Enter the top",top," skills given by the interviewee ")
    for i in range(0,top):
        n=input()
        top_skills.append(n)
    for j in top_skills:
        if j in skills:
            Technical.append(j)
    for i in range(0,len(Technical)):
        print("Have you executed a project in",Technical[i],'\n')
        print("Enter y if yes and n if no")
        res=input()       
        if(res=='y' or res=='Y'):
            ques.append("Briefly explain the project you have implemented in "+Technical[i]+'?')
    k='6.)Skills'
    pair={k:ques}
    print(pair)
    questions.update(pair)
    print(questions[k])
    ques=[]
    for i in range(0,number_of_degrees):
        if('M.Sc'==dd["data"]["CandidateData"][0]["QualificationsDetails"]["QualificationData"][i]["Degree"]):
            ques.append('Briefly explain the domain of the thesis done during masters at '+dd["data"]["CandidateData"][0]["QualificationsDetails"]["QualificationData"][i]["Institution"])
            k='1.)Education'                                                                                                    
            pair={k:ques}
            questions.update(pair)
            ques=[]
    for i in range(0,number_of_works-1):
        job_1_end_month=parser.parse(Work_Period[i][0]).month
        job_2_start_month=parser.parse(Work_Period[i+1][1]).month
        job_1_end_year=parser.parse(Work_Period[i][0]).year
        job_2_start_year=parser.parse(Work_Period[i+1][1]).year
        if(job_2_start_month<job_1_end_month):
            diff_in_months=abs(12*(job_2_start_year-job_1_end_year)-(job_1_end_month-job_2_start_month))
        else:
            diff_in_months=abs(12*(job_2_start_year-job_1_end_year)+(job_2_start_month-job_1_end_month))
        job_difference.append(diff_in_months)   
            
    for i in range(0, len(job_difference)):
        if(job_difference[i]>40):
            ques.append('Why is there such a big gap between leaving '+companies_worked_for[i+1]+" and joining "+companies_worked_for[i]) 
            k='9.)Inter_Work_Gap'
            pair={k:ques}
            questions.update(pair)
    ques=[]           
    for i in Technical:
        k='7.)Skills_List'
    pair={k:specific_tq}
    questions.update(pair)

    '''
    for i in questions['Skills']:
        print(i,'\n')
        print(random.sample(list(questions['Technical Skills']),4))
        print('\n')
    
    '''
    if len(Technical)>0:
        print("This is a technical Resume")
        k='8.)Basic Technical Questions'
        pair={k:tq}
        questions.update(pair)
        
    while(com.lower()!="done"):
        print('''Enter the category of question
              1. Education
              2. Experience
              3. Gap
              4. Designation
              5. Functional Area
              6. Skills
              7. Skills List
              8. Technical Questions
              9. Interwork Gap''')
        category=input()
        for i in questions.keys():
            if category in i:
                l=list(questions[i])
                print(l)
        print("Enter the number of questions not more than",len(l),'\n' )
        num=int(input())
        print(random.sample(l,num))
        print("Are you done with your questions")
        com=input()
        l=[]
            
                
                   
else:
    print("ERROR!!\nThe file may have been incorrectly parsed")

