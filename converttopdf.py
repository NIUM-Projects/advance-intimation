
from tokenize import Number
import pdfkit
from jinja2 import Template
from datetime import date,time
from timeit import timeit
def prog():
   
    #open letter template as a read file.
    html_template = open ("./templates/letter.html",'r').read()
    # print(html_template)
     # importing present date
    todays_date= date.today()
    #variables to be put on the letter
    name="ayush mohril"
    application_no= ["50","23","4453","37464","8476876","76869769","87678765","76547654","76585458756","86t76"] 
    application_no_length=len(application_no)
    # template = Template("Hello {{Name}}")
    #import file as html template in jinja2
    template = Template(html_template)
    #render temolate with given variables
    template_for_render = template.render(todays_date= todays_date ,Name= name,application_no= application_no)

    #print(template_for_render)
    #write the template as a html.
    with open("C:/Users/admin/Desktop/web page letter/templates/temp.html", "w") as fh:
        fh.write(template_for_render)
        fh.close()
    #conerting html as pdf with pdfkit
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    options = {'enable-local-file-access': None}
    pdfkit.from_file('./templates/temp.html','C:/Users/admin/Desktop/web page letter/letter for output.pdf', configuration=config,options=options)

if __name__=="__main__":
    #it is for testing the time taken to render multiple pdf files
    #a=timeit(lambda:prog(),number=100)
    #print(a)
    prog()
