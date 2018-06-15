# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:41:58 2018
Similarity with [1,0.5,0]
[0,0.5,1]
Most Accurate Method
@author: admin
"""
import re
import PyPDF2
from scipy import spatial
from nltk import word_tokenize,sent_tokenize, pos_tag, ne_chunk
from nltk.corpus import words,stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import random
import json
import datetime
import dateutil.parser as parser
now = datetime.datetime.now()
from nltk.corpus import wordnet as wn
Verb_File={}
Verb_File_Vector_Technical={}
Verb_File_Vector_Management={}
VECT=[]
manage=[]
verb_in_file={}
technical=[]
File_Field_Type={}
enough=0
Categ_Prob_File={}
dist=[]
while(enough==0):
 filename = input('Enter a filename: ')
 Skill_Phrases=[]
 enough=0
 Reference={}
 categ_prob=[]
 verb_phrases=[]
 verb_list=[]
 verbs=[]
 verb_file=[]
 verb_type=[]
 z=0
 prob_phrases=[]
 skills = ['Apache Ant','Apache POI','Apache POI','Apache POI','ASP.NET','AWT','Design Patterns','Easy Mock','Eclipse','EJB','Guava','Hibernate','iBATIS','Jackson','JasperReports','JavaXML','Java','Jbpm5','Java.ioPackage','JavaInterviewQuestions','Java.lang Package','Java.math Package','Java.util Package','Java-8','Java Examples','Java Mail API','JDB','JDBC','JFree Chart','jMeter','JOGL','JPA','JSON','JSP','JUnit','log4j','Lucene','Maven','PDFbox','Servlets','Spring','Struts2.x','Swing','TestNG','Apache Tika','Apache Xerces','XStream', 'Apache Presto','CouchDB','DB2','Document DB','DocumentDB SQL','HSQLDB','IMS DB','Memcached','MariaDB','MongoDB','MySQL','Neo4J','OBIEE','OrientDB','PL/SQL','PouchDB','PostgreSQL','Redis','SQLCertification','SQL','T-SQL','SQLite', 'Git', 'Apex','Arduino','ASP.Net','ASP.Net MVC','ASP.Net WP', 'Assembly','Awk','CStandardLibrary','C++ Standard Library','COBOL','C++','C','Computer Programming','CbyExamples','C#','Clojure','Data Structure & Algorithms','D','Elixir','Erlang','Euphoria','F#','Fortran','GoPrograming','Groovy','Java','Java-8','JCL','LISP','MATLAB','Node.js','ObjectiveC','Pascal','R Programming','Rexx Programming','Socket.io','Swift','Scala','VB.Net','VBA', 'Apache Flume','Apache Impala','Apache Pig','Apache Tajo','Apache Spark','Apache Storm','Spark SQL','Avro','Couch DB','Cassandra','Cognos','Google Charts','Hadoop','HCatalog','Hive','Highcharts','HBase','JFree   Chart','Apache Kafka','Map Reduce','Mahout','Pentaho','Qlik View','R Programming','SAS','Sqoop','Statistics','Teradata','Tableau','Zookeeper', 'CICS','COBOL','DB2','IMSDB','JCL','VSAM', 'Batch Script','C#','Excel','Advanced Excel','Excel Charts','Entity Framework','F#','NHibernate','LinQ','MFC','Microsoft Azure','Powerpoint','Microsoft Access','Microsoft Project','Micro Strategy','MicrosoftCRM','MS SQl Server','MVVM','Sharepoint','Silverlight','VBA','VB.Net','WCF','Word','WPF','XAML','Windows 10 Development','Windows 10', 'Android','Cordova','iOS','jQueryMobile','Ionic','Meteor','PhoneGap','ReactNative','SL4A', 'Ajax','Angular2','AngularJS','Angular Material','ASP.Net','Aurelia','Backbone JS','Bootstrap','CherryPy','CSS','Codeigniter','Coffee Script','CPanel','Drupal','Django','EmberJS','ExtJS','ExpressJS','Firebase','Framework7','Flask','Adobe Flex','Foundation','Grav','Grunt','Gulp','GWT','Google Maps','HTML','HTML5','HTTP','Highcharts','JasmineJS','JavaScript','Joomla','jQuery','jQuery UI','JSF','KnockoutJS','KoaJS','Laravel','LESS','Magento Framework','MaterialDesignLite','Materialize','Mootools','MVC Framework','Prototype','Pure.CSS','React JS','RubyonRails-2.1','RubyonRails','SASS','script.aculo.us','SVG','TurboGears','VB Script','Web Developers Guide','Web Services','RESTful Web Services','W3CSS','Web Icons','Web Sockets','Web2Py','WebGL','WebRTC','Wordpress','XHTML','Yii', 'JavaScript','jQuery','jQueryUI','Lua','Perl','PHP','Python','Python-3','PyGTK','PyQt','WxPython','Ruby','RSpec','Sed','Tcl/Tk','Unix','VBScript']
 management=['effectively managing all essential tasks', 'managing a team', 'managing accounts', 'managing agency relationships', 'managing agents', 'managing associates', 'managing budget', 'managing budgets & p&ls', 'managing business growth', 'managing complex projects', 'managing complex sales', 'managing creative teams', 'managing crews', 'managing database', 'managing deadlines', 'managing distribution channels', 'managing employees', 'managing events', 'managing expectations', 'managing finance', 'managing finances', 'managing global operations', 'managing groups', 'managing high performance teams', 'managing international teams', 'managing it infrastructure', 'managing key accounts', 'managing large budgets', 'managing large scale projects', 'managing managers', 'managing media relations', 'managing meetings', 'managing multi-million dollar budgets', 'managing multiple locations', 'managing multiple projects', 'managing offshore teams', 'managing others', "managing p&l's", 'managing p&ls', 'managing partner relationships', 'managing partners', 'managing processes', 'managing product development', 'managing production', 'managing project budgets', 'managing rapid growth', 'managing relationships', 'managing sales team', 'managing technical personnel', 'managing the learning function', 'managing volunteers', 'managing workflow','managerial', 'managerial economics', 'managerial experience', 'managerial finance', 'managerial skills','effectively managing all essential tasks', 'managing a team', 'managing accounts', 'managing agency relationships', 'managing agents', 'managing associates', 'managing budget', 'managing budgets & p&ls', 'managing business growth', 'managing complex projects', 'managing complex sales', 'managing creative teams', 'managing crews', 'managing database', 'managing deadlines', 'managing distribution channels', 'managing employees', 'managing events', 'managing expectations', 'managing finance', 'managing finances', 'managing global operations', 'managing groups', 'managing high performance teams', 'managing international teams', 'managing it infrastructure', 'managing key accounts', 'managing large budgets', 'managing large scale projects', 'managing managers', 'managing media relations', 'managing meetings', 'managing multi-million dollar budgets', 'managing multiple locations', 'managing multiple projects', 'managing offshore teams', 'managing others', "managing p&l's", 'managing p&ls', 'managing partner relationships', 'managing partners', 'managing processes', 'managing product development', 'managing production', 'managing project budgets', 'managing rapid growth', 'managing relationships', 'managing sales team', 'managing technical personnel', 'managing the learning function', 'managing volunteers', 'managing workflow']
 marketing=['account marketing', 'acquisition marketing', 'adobe marketing cloud', 'affiliate marketing', 'african markets', 'aggressive marketing', 'agricultural marketing', 'alliance marketing', 'amazon marketplace', 'american marketing association', 'art marketing', 'article marketing', 'asian markets', 'association marketing', 'athlete marketing', 'attraction marketing', 'automotive aftermarket', 'automotive marketing', 'b2b marketing', 'b2b marketing strategy', 'b2c marketing', 'beverage marketing', 'blog marketing', 'bluetooth marketing', 'bond markets', 'book marketing', 'bootstrap marketing', 'brand marketing', 'branding & identity marketing', 'buzz marketing', 'candidate marketing', 'capital market operations', 'capital markets', 'capital markets advisory', 'capital markets analysis', 'capital markets transactions', 'carbon markets', 'casino marketing', 'catalog marketing', 'cause marketing', 'charity marketing', 'city marketing', 'closed loop marketing', 'cloud marketing', 'co-marketing', 'collaborative marketing', 'commodity markets', 'community marketing', 'comparable market analysis', 'comparative market analysis', 'competitive marketing strategies', 'consumer goods marketing', 'consumer marketing', 'consumer packaged goods marketing', 'content marketing', 'content-marketing', 'continuity marketing', 'conversational marketing', 'cooperative marketing', 'cost effective marketing', 'creative market planning & execution', 'creative marketer', 'creative marketing solutions', 'cross channel marketing', 'cross media marketing', 'cultural marketing', 'customer focused marketing', 'customer marketing', 'data-driven marketing', 'database marketing', 'dealer marketing', 'dental marketing', 'designing marketing collateral', 'destination marketing', 'developing marketing', 'developing markets', 'developing new markets', 'development & implementation of marketing plans', 'development of strategic marketing plans', 'digital direct marketing', 'digital marketing', 'digital marketing experience', 'digital music marketing', 'direct market access', 'direct marketing', 'display marketing', 'diverse market/industry', 'diversity marketing', 'drip marketing', 'e-mail-marketing', 'e.u. markets in financial instruments directive (mifid)', 'education marketing', 'educational marketing', 'electricity markets', 'electronic marketing', 'electronic markets', 'email marketing', 'email marketing software', 'emarketer', 'emerging markets', 'energy markets', 'engagement marketing', 'enterprise marketing', 'enterprise markets', 'entertainment marketing', 'equity capital markets', 'ethical marketing', 'ethnic marketing', 'european market', 'european markets', 'event based marketing', 'event marketing', 'event marketing strategy', 'event-based marketing', 'external marketing', 'face-to-face marketing', 'facebook marketing', 'fair market value', 'farmers markets', 'fashion marketing', 'field marketing', 'film marketing', 'financial market research', 'financial markets', 'food marketing', 'frontier markets', 'general market', 'geomarketing', 'global market experience', 'global marketing', 'go-to-market strategy', 'gorilla marketing', 'government markets', 'grassroots marketing', 'green marketing', 'guerrilla marketing', 'habilidades de marketing', 'health care marketing', 'health marketing', 'healthcare marketing', 'higher education marketing', 'hispanic market', 'hispanic marketing', 'home marketing', 'hospital marketing', 'housing market analysis', 'image marketing', 'implementing marketing', 'in-store marketing', 'inbound marketing', 'industrial markets', 'industry marketing', 'influencer marketing', 'information marketing', 'institutional marketing', 'insurance marketing', 'integrated brand marketing', 'integrated marketing', 'integrated marketing communications planning', 'integrated marketing plans', 'integrated marketing solutions', 'integrated multi-channel marketing', 'interactive marketing', 'interactive marketing strategy', 'internal marketing', 'international capital markets', 'international market analysis', 'international market entry', 'international marketing', 'international markets', 'international sales & marketing', 'ion marketview', 'japanese market', 'joint marketing', 'labor market', 'labour market research', 'latin american markets', 'law firm marketing', 'legal marketing', 'lifestyle marketing', 'linkedin marketing', 'local marketing', 'local store marketing', 'location based marketing', 'london insurance market', 'london market', 'london market insurance', 'loyalty marketing', 'luxury brand marketing', 'luxury marketing', 'managed markets', 'managed markets marketing', 'mark to market', 'market', 'market abuse regulations', 'market access', 'market analysis', 'market assessments', 'market basket analysis', 'market communications planning', 'market conduct', 'market data', 'market definition', 'market design', 'market development', 'market differentiation', 'market entry', 'market evaluation', 'market evaluations', 'market growth', 'market identification', 'market information', 'market insight', 'market intelligence', 'market knowledge', 'market landscape analysis', 'market launch', 'market making', 'market mapping', 'market microstructure', 'market modeling', 'market monitoring', 'market needs analysis', 'market neutral', 'market opportunities', 'market opportunity analysis', 'market opportunity assessment', 'market penetration', 'market planning', 'market pricing', 'market profile', 'market rate', 'market regulation', 'market requirements documents', 'market research', 'market research project management', 'market risk', 'market samurai', 'market sectors', 'market share', 'market share analysis', 'market sizing', 'market structure', 'market studies', 'market testing', 'market timing', 'market understanding', 'market updates', 'market validation', 'market valuation', 'market value', 'market2lead', 'marketability', 'marketaxess', 'marketing', 'marketing accountability', 'marketing activation', 'marketing agency', 'marketing agreements', 'marketing analytics', 'marketing assistance', 'marketing automation', 'marketing budget', 'marketing budget management', 'marketing coaching', 'marketing communications', 'marketing communications planning', 'marketing compliance', 'marketing concepts', 'marketing consulting', 'marketing copy', 'marketing de contenu', 'marketing documents', 'marketing effectiveness', 'marketing en ligne', 'marketing en social media', 'marketing engineering', 'marketing event planning', 'marketing for small business', 'marketing graphics', 'marketing homes', 'marketing information systems', 'marketing intelligence', 'marketing kits', 'marketing law', 'marketing leadership', 'marketing liason', 'marketing literature', 'marketing management', 'marketing material creation', 'marketing materials', 'marketing media', 'marketing messaging', 'marketing mix', 'marketing mix modeling', 'marketing mobile', 'marketing online', 'marketing operations', 'marketing par e-mail', 'marketing partnerships', 'marketing photography', 'marketing plan creation', 'marketing process', 'marketing professional', 'marketing reporting', 'marketing research', 'marketing science', 'marketing strategy', 'marketing support', 'marketing systems', 'marketing teams', 'marketing transformation', 'marketing y ventas', 'marketingkompetenz', 'marketmate', 'marketo', 'marketplace', 'marketron', 'marketsight', 'marketview', 'marketvision', 'mass email marketing', 'mass market', 'mass marketing', 'mature market', 'media marketing', 'medical marketing', 'membership marketing', 'micro marketing', 'mid-market', 'middle market', 'mobile marketing', 'mobile marketing tours', 'mobiles marketing', 'money market', 'money market accounts', 'money market funds', 'mortgage marketing', 'motorsports marketing', 'multi-channel marketing', 'multi-level marketing', 'multi-market', 'multi-market experience', 'multi-media marketing campaigns', 'multicultural marketing', 'multimedia marketing', 'multimedia marketing communications', 'music marketing', 'national marketing', 'network marketing', 'network marketing professional', 'neuromarketing', 'new market', 'new market expansion', 'new market exploration', 'new market growth', 'new markets development', 'new markets tax credits', 'new media marketing', 'niche marketing', 'nmarket', 'non-profit marketing', 'offline marketing', 'on-premise marketing', 'one-to-one marketing', 'online marketing', 'online marketing analysis', 'online marketplace', 'online video marketing', 'online-marketing', 'opening new markets', 'outbound marketing', 'outsourced marketing', 'partner marketing', 'partnership marketing', 'pay-per-click marketing', 'performance based marketing', 'permission marketing', 'pinterest marketing', 'portfolio marketing', 'post market surveillance', 'power markets', 'pragmatic marketing certification', 'precision marketing', 'prediction markets', 'premarket approval (pma)', 'print marketing', 'product marketing', 'professional services marketing', 'promotional marketing', 'property marketing', 'public markets', 'pull marketing', 'qualitative market research', 're-marketing', 'real estate marketing', 'real-time marketing', 'recruitment marketing', 'referral marketing', 'regional marketing', 'relationship marketing', 'remarketing', 'renewable energy markets', 'reputation marketing', 'restaurant marketing', 'retail marketing', 'return on marketing investment (romi)', 'reverse marketing', 'revolutionary marketing', 'routes to market', 'rural marketing', 'rural markets', 'sales & marketing', 'sales & marketing alignment', 'sales & marketing functions', 'sales & marketing leadership', 'school marketing', 'search engine marketing (sem)', 'search marketing y display marketing', 'second home market', 'secondary market', 'secondary mortgage market', 'securities market', 'self-marketing', 'seminar marketing', 'services marketing', 'shopper marketing', 'skill marketing', 'small business marketing', 'small business online marketing', 'social marketing', 'social marketing fulfillment', 'social media marketing', 'social media-marketing', 'solutions marketing', 'sponsorship marketing', 'sports marketing', 'startup marketing', 'stealth marketing', 'stock market', 'stock market analysis', 'strategic marketing', 'strategic marketing consultancy', 'street marketing', 'student marketing', 'suche und display-marketing', 'suchmaschinenmarketing (sem)', 'supermarkets', 'sustainability marketing', 'tactical marketing', 'taking new products to market', 'target market development', 'target marketing', 'technical marketing', 'technology marketing', 'telecommunications marketing', 'telemarketing', 'test marketing', 'text marketing', 'theatrical marketing', 'time to market', 'tour marketing', 'tourism marketing', 'trade marketing', 'travel marketing', 'twitter marketing', 'uk market', 'unique marketing', 'upstream marketing', 'us hispanic market', 'vehicle remarketing', 'ventes et marketing', 'vertical market', 'vertical market penetration', 'vertical marketing', 'vertrieb und marketing', 'video marketing', 'viral marketing', 'visual marketing', 'web marketing', 'web marketing strategy', 'wine marketing', 'wireless marketing', 'word of mouth marketing', 'yahoo search marketing', 'yahoo! search marketing ambassador', 'youth marketing']
 sales = ['account sales strategies', 'acquisition sales', 'ad sales', 'advertising sales', 'after sales service', 'after sales support', 'after-sales', 'aftersales', 'aircraft sales', 'annuity sales', 'art sales', 'asset sales', 'automotive sales', 'automotive sales training', 'b to b sales', 'big ticket sales', 'biotech sales', 'book sales', 'broadcast media sales', 'building sales', 'bulk sales', 'business purchases & sales', 'c-level sales', 'c-level sales experience', 'c-level sales presentations', 'c-suite sales', 'capital equipment sales', 'cash sales', 'catering sales', 'certified new home sales professional', 'certified salesforce.com consultant', 'certified salesforce.com developer', 'certified short sales', 'channel sales', 'channel sales development', 'chemical sales', 'cluster sales', 'commercial property sales', 'commercial sales', 'complex sales', 'computer sales', 'conceptual sales', 'condominium sales', 'consultative sales management', 'consultative sales professional', 'corporate sales management', 'corporate sales presentations', 'cpg sales', 'creative sales', 'cross-platform sales', 'customer-focused sales', 'dart sales manager', 'data sales', 'days sales outstanding (dso)', 'dental sales', 'development of sales', 'digital media sales', 'direct sales', 'distress sales', 'district sales management', 'domestic sales', 'driving sales performance', 'ebay sales', 'electrical sales', 'end to end sales', 'end user sales', 'enterprise sales', 'enterprise solution sales', 'enterprise technology sales', 'equity sales', 'esales', 'estate sales', 'event sales', 'exceed sales goals', 'exceeding sales goals', 'executive sales recruitment', 'existing home sales', 'experienced sales professional', 'external sales', 'face to face sales', 'face-to-face sales', 'federal government sales', 'fine art sales', 'fleet sales', 'follow-up sales activity', 'foreign military sales', 'franchise sales', 'general sales', 'general securities sales supervisor', 'global sales', 'growing sales', 'heaton moor sales', 'high performance sales teams', 'high tech sales', 'high technology sales', 'high value sales', 'high-impact sales presentation', 'high-impact sales presentations', 'high-tech sales', 'high-volume sales', 'hospital sales', 'ict sales', 'identifying sales opportunities', 'implementing sales', 'in-home sales', 'income property sales', 'increasing sales revenue', 'indirect channel sales', 'indirect sales channels', 'inside sales', 'institutional sales', 'intangible sales', 'integrated media sales', 'international sales', 'international sales & marketing', 'investment sales', 'investor sales', 'it sales', 'land & lot sales', 'land sales', 'large account sales', 'leading sales', 'loan sales', 'managing complex sales', 'managing sales team', 'manchester city centre sales', 'media sales', 'medical sales', 'medical software sales', 'membership sales', 'miller heiman sales training', 'multi-state sales tax', 'national account sales', 'national sales training', 'netapp accredited sales professional', 'new home sales', 'new media sales', 'on-line sales', 'online sales', 'online sales management', 'operating room sales', 'outside sales', 'pharmaceutical sales', 'phone sales', 'post-sales', 'post-sales support', 'pre-sales', 'pre-sales consultancy', 'pre-sales consultation', 'pre-sales consulting', 'pre-sales efforts', 'pre-sales initiatives', 'pre-sales technical consulting', 'pre-sales technical support', 'pre/post sales engineers', 'premium sales', 'print media sales', 'private sales', 'project sales', 'radio sales', 're-sales', 'real estate sales license', 'resales', 'retail sales', 'retail sales analysis', 'retail sales experience', 'sales', 'sales & distribution', 'sales & marketing', 'sales & marketing alignment', 'sales & marketing functions', 'sales & marketing leadership', 'sales & use tax', 'sales & use tax compliance', 'sales abilities', 'sales acquisition', 'sales acumen', 'sales administration', 'sales analysis', 'sales analytics', 'sales assessments', 'sales audit', 'sales automation', 'sales brochures', 'sales building', 'sales campaigns', 'sales channel', 'sales channel development', 'sales co-ordination', 'sales coach', 'sales coaching', 'sales commission', 'sales commissions', 'sales compensation', 'sales compensation design', 'sales compensation planning', 'sales compensation plans', 'sales consulting', 'sales contracts', 'sales conversion', 'sales coordination', 'sales copy', 'sales cycle management', 'sales direct', 'sales driven', 'sales education', 'sales effectiveness', 'sales enablement', 'sales enablement tools', 'sales engineering', 'sales excellence', 'sales execution', 'sales finance', 'sales force alignment', 'sales force compensation', 'sales force development', 'sales funnel optimization', 'sales funnels', 'sales genie', 'sales growth', 'sales hiring', 'sales improvement', 'sales initiatives', 'sales intelligence', 'sales kits', 'sales leadership training', 'sales leads', 'sales letters', 'sales liaison', 'sales literature', 'sales logix', 'sales management', 'sales management coaching', 'sales management consulting', 'sales material', 'sales material development', 'sales messaging', 'sales metrics', 'sales motivation', 'sales motivator', 'sales navigator', 'sales networking', 'sales online', 'sales operations', 'sales order', 'sales order processing', 'sales organization', 'sales organization leadership', 'sales organizations', 'sales performance', 'sales pipeline management', 'sales plan', 'sales practices', 'sales presentation skills', 'sales presentations', 'sales process', 'sales process development', 'sales process implementation', 'sales program development', 'sales programs', 'sales promotion', 'sales prospecting', 'sales recruitment', 'sales rep training', 'sales representatives', 'sales research', 'sales retention', 'sales services', 'sales skills training', 'sales strategy', 'sales support', 'sales support tools', 'sales targets', 'sales tax', 'sales tools development', 'sales trainings', 'sales trend analysis', 'sales turnaround', 'sales videos', 'sales workshops', 'salesforce', 'salesforce administrator', 'salesforce training', 'salesforce transformation', 'salesforce.com', 'salesforce.com admin', 'salesforce.com administration', 'salesforce.com administrator', 'salesforce.com certified', 'salesforce.com certified administrator', 'salesforce.com certified consultant', 'salesforce.com certified sales cloud consultant', 'salesforce.com consulting', 'salesforce.com development', 'salesforce.com implementation', 'salesforce.com system administrator', 'saleslogix', 'salespro', 'sap pre-sales', 'sap sales & distribution', 'security sales', 'service contract sales', 'services sales', 'short sales', 'situational sales negotiation', 'smb sales', 'software sales', 'software sales management', 'software solution sales', 'spin sales training', 'sponsorship sales', 'state & local government sales', 'strategic sales', 'strategic sales initiatives', 'strategic sales plans', 'subscription sales', 'superior sales skills', 'surgical device sales', 'system sales', 'tactical sales', 'tactical sales planning', 'tax sales', 'technical presales', 'technical product sales', 'technical sales consulting', 'technical sales presentations', 'technology pre-sales', 'telecom sales', 'telecommunications sales', 'ticket sales', 'trade sales', 'travel sales', 'vacant land sales', 'volume sales', 'web sales', 'wholesale sales', 'wine sales']
 edu_info=["university","high school","junior college","bachelor",' board ',"qualification",'degree','institute',]
 Management=['administered','analyzed','appointed','approved','assigned','attained','authorized','chaired','considered','consolidated','contracted','controlled','converted','coordinated','decided','delegated','developed','directed','eliminated','emphasized','enforced','enhanced','established','executed','generated','handled','headed','hired','hosted','improved','incorporated','increased','initiated','inspected','instituted','led','managed','merged','motivated','organized','originated','overhauled','oversaw','planned','presided','prioritized','produced','recommended','reorganized','released','replaced','restored','reviewed','scheduled streamlined','strengthened','supervised','terminated']
 #Organization=['approved','arranged','cataloged','categorized','charted','classified','collected','compiled','corresponded','distributed','executed','filed','generated','implemented','incorporated','inspected','logged','maintained','monitored','obtained','operated','ordered','organized','prepared','provided','purchased','recorded','registered','reserved','responded','reviewed','routed','scheduled','screened','set up','submitted','supplied','standardized','systematized','updated','validated','verified']
 Research=['analyzed','clarified','collected compared','conducted','critiqued','detected','determined','diagnosed','evaluated','examined','experimented','explored','extracted','formulated','gathered','identified','inspected','interpreted','interviewed','invented','investigated','located','measured','organized','researched','searched','solved','summarized','surveyed','systematized','tested']
 Technical=['adapted','assembled','built','calculated','coded','computed','conserved','constructed','converted','debugged','designed','determined','developed','engineered','fabricated','fortified','installed','maintained','operated','overhauled','printed','rectified','regulated','remodeled','repaired','replaced','restored','solved','specialized','standardized','studied','upgraded','utilized']
 for i in Management:
    Reference[lemmatizer.lemmatize(i,'v')]='management'
 for i in Research:
    Reference[lemmatizer.lemmatize(i,'v')]='research'
 for i in Technical:
    Reference[lemmatizer.lemmatize(i,'v')]='technical'
 k=[]
 q=[]
 fdict={}
 Verb={}
 Phrase_type={}
 k=list(Reference.keys())
 for i in range(0,len(k)):
      q.append(lemmatizer.lemmatize(k[i],'v'))
 not_noise=[]
 skills.extend(management)
 skills.extend(marketing)
 skills.extend(sales)
 refined_words=[]
 cand_skills=[]
 ts=[]
 noise=[]
 work=[]
 t=[] 
 if('.pdf' in filename):
    pdfFileObj = open(filename, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # creating a page object
    pageObj = pdfReader.getPage(0)
    
    # extracting text from page
    txt=pageObj.extractText()
    # closing the pdf file object
    pdfFileObj.close()
 elif ('.txt' in filename):
    f=open(filename, "r",encoding='utf-8-sig')
    txt=f.read()
 stop_words = list(stopwords.words('english'))
 txt=txt.replace("\n",". ")
 sent=sent_tokenize(txt)
 ws=word_tokenize(txt)
 for phrase in sent :
    #c=0
    tokenized_text = word_tokenize(phrase)
    for i in tokenized_text:
        if i=='@' and phrase not in noise:
            noise.append(phrase)
            #c+=1
 for j in edu_info:
    for i in sent:
        if j.lower() in i.lower() and i not in noise:
            noise.append(i)
 for i in  sent:
    if i not in noise:
        not_noise.append(i)
 for i in ws:
    if  i not in stop_words and len(i)>1:
        refined_words.append(i)
        
 t=[]
 for i in skills:
    for j in refined_words:
        if lemmatizer.lemmatize(i,'v') in lemmatizer.lemmatize(j,'v') and i not in cand_skills:
            cand_skills.append(i)
 grammar="""NP:{(<NNP>|<NNS>|<NN>)*}"""
 for i in not_noise:
    w=word_tokenize(i.lower())
    for i in w:
        if(i!='•'):
            t.append(pos_tag(word_tokenize(i)))
    ts.append(t)
    t=[]
 c=0   
 for i in ts:
    for j in range(0,len(i)):
     if(lemmatizer.lemmatize(i[j][0][0].lower(),'v') in q and not_noise[ts.index(i)] not in work and 'NNP' != pos_tag(word_tokenize(i[j][0][0]))):
        work.append((not_noise[ts.index(i)]))
        verb_phrases.append(i[j][0][0])
 for i in skills:
    for j in not_noise:
        if i.lower() in word_tokenize(j.lower()) and j not in Skill_Phrases:
            Skill_Phrases.append(j)


 for i in work:
    ws=word_tokenize(i.lower())
    Refer={}
    for j in Reference.keys():
        for k in ws:
            if j==lemmatizer.lemmatize(k,'v'):
                Refer.update({j:Reference[j]})
    Phrase_type[i]=Refer
 m=t=r=0
 categ_freq=[0,0,0]
 categ=['management','research','technical']
 for i in Phrase_type.keys():
    m,r,t=0,0,0
    v=Phrase_type[i]    
    for k in v.values():   
        if(k.lower()=='technical'):
                t+=1
        elif(k.lower()=='management'):
                m+=1
        elif(k.lower()=='research'):
                r+=1  
    summ=m+r+t
    typ_freq=[m,r,t]
    prob=[m/summ,r/summ,t/summ]
    prob_phrases.append(prob)
    m=max(prob)
    for i in prob:
        if i==m:
            categ_freq[prob.index(i)]+=1
 summ=0
 for i in categ_freq:
    summ=summ+i
 for i in range(0,len(categ_freq)):
    categ_prob.append(categ_freq[i]/summ)
 m=max(categ_prob)
 for i in categ_prob:
    if i==m:
        d=categ[categ_prob.index(i)]
 Categ_Prob_File[filename]=(categ_prob)         
 for i in Reference.keys():
    if(Reference[i]==d):
        verb_list.append(i)
 for i in Phrase_type.values():
    for j in i.keys():
            verbs.append(j)
    for j in i.values():
        verb_type.append(j)
 for i in range(0,len(verb_type)):
    Verb[verbs[i]]=verb_type[i]
 counter=0
 for i in Verb.keys():
     verb_file.append(i)
 Verb_File[filename]=verb_file
 File_Field_Type[filename]=d
 print("1 to exit, 0 to continue")
 enough=int(input())
 most_technical=[0,0.5,1]
 most_managemental=[1,0.5,0]
 dist_from_management =spatial.distance.cosine(most_managemental,categ_prob)
 dist_from_technical=spatial.distance.cosine(most_technical,categ_prob)
 print("Management:",dist_from_management,"::Technical:",dist_from_technical)
t=[]
dist=[]
for j in Categ_Prob_File.values():
        t.append(j)
d=[]
for i in range(0,len(t)):
    for j in range(0,len(t)):
                d.append(spatial.distance.cosine(t[i],t[j]))
    dist.append(d)
    d=[]
count=0
fnames=list(Verb_File.keys())
for i in Verb_File.values():
    for k in Technical:
        c=0
        for j in i:
            if j==lemmatizer.lemmatize(k,'v'):
                c+=1
            else:
                c+=0
        if(c>0):
            VECT.append(1)
        else:
            VECT.append(0)
    Verb_File_Vector_Technical[fnames[count]]=VECT
    VECT=[]
    count+=1

count=0
for i in Verb_File.values():
    for k in Management:
        c=0
        for j in i:
            if j==lemmatizer.lemmatize(k,'v'):
                c+=1
            else:
                c+=0
        if(c>0):
            VECT.append(1)
        else:
            VECT.append(0)
    Verb_File_Vector_Management[fnames[count]]=VECT
    VECT=[]
    count+=1
dft=dfm=0.0
dt={}
dm={}

Reference_Technical=[]
Reference_Management=[]
for i in range(0,len(Technical)):
    Reference_Technical.append(1)
for i in range(0,len(Management)):
    Reference_Management.append(1)
for i in Verb_File_Vector_Management.keys():
    dfm=spatial.distance.cosine(Reference_Management,Verb_File_Vector_Management[i])
    dm[i]=dfm*(len(Management)+len(Technical))/len(Management)
for i in Verb_File_Vector_Technical.keys():
    dft=spatial.distance.cosine(Reference_Technical,Verb_File_Vector_Technical[i])
    dt[i]=dft*(len(Management)+len(Technical))/len(Technical)
 
for i in dt.keys():
    ft=min(dt[i],dm[i])
    if(ft==dm[i]):
        fdict[i]='Management'
        manage.append(fdict)
    else:
        fdict[i]='Technical'
        technical.append(fdict)
    fdict={}
    