

pages = [
        {
            "filename": "content/index.html", #Input file
            "output": "docs/index.html",       #output file after templating
            "title": "Welcome to PB site - Pradeep B.", 
        },
        {
            "filename": "content/portfolio.html",
            "output": "docs/portfolio.html",
            "title": "My Portfolio - Pradeep B.",
        },
        {
            "filename": "content/about.html",
            "output": "docs/about.html",
            "title": "About the site - Pradeep B.",
        },
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "Contact Us - Pradeep B.",
        },
            
            ] 
 

def generate_html():   
    for page in pages:
        file_name = page["filename"]
        file_output = page["output"]
        template = open("templates/base.html").read()
        page_title = page["title"]
        html_content = open(page["filename"]).read()
        templated_html = replace_template(html_content, template, page_title)
        open(file_output, "w+").write(templated_html)
        print("The file " + file_name + " has been created successfully")
    return

def replace_template(html_content, template, page_title):
    templated_html = template.replace("{{content}}", html_content).replace("{{title}}", page_title)        
    return templated_html
def main():
    
        generate_html()
    
if __name__ == "__main__":
    main()


#Working code
# pages = [
#         {
#             "filename": "content/index.html",
#             "output": "docs/index.html",
#             "title": "Welcome to PB site - Pradeep B.",
#         },
#         {
#             "filename": "content/portfolio.html",
#             "output": "docs/portfolio.html",
#             "title": "My Portfolio - Pradeep B.",
#         },
#         {
#             "filename": "content/about.html",
#             "output": "docs/about.html",
#             "title": "About the site - Pradeep B.",
#         },
#         {
#             "filename": "content/contact.html",
#             "output": "docs/contact.html",
#             "title": "Contact Us - Pradeep B.",
#         },
            
#             ] 
# def generate_html():   
#     for page in pages:
#         file_name = page["filename"]
#         file_output = page["output"]
#         template = open("templates/base.html").read()
#         html_content = open(file_name).read()
#         finished_html= template.replace("{{content}}", html_content)
#         open(file_output, "w+").write(finished_html)
#         print("The file " + file_name + " has been created successfully")
#     return




    # index_filenames = ["templates/top.html", "content/index.html", "templates/bottom.html"] #Input file list
    # with open('docs/index.html', 'w') as outfile:
    #     for fname in index_filenames:
    #         with open(fname) as infile:
    #             outfile.write(infile.read()) #Output single file
    # index_filenames = ["templates/top.html", "content/portfolio.html", "templates/bottom.html"] #Input file list
    # with open('docs/portfolio.html', 'w') as outfile:
    #     for fname in index_filenames:
    #         with open(fname) as infile:
    #             outfile.write(infile.read()) #Output single file
    # index_filenames = ["templates/top.html", "content/about.html", "templates/bottom.html"] #Input file list
    # with open('docs/about.html', 'w') as outfile:
    #     for fname in index_filenames:
    #         with open(fname) as infile:
    #             outfile.write(infile.read()) #Output single file
    # index_filenames = ["templates/top.html", "content/contact.html", "templates/bottom.html"] #Input file list
    # with open('docs/contact.html', 'w') as outfile:
    #     for fname in index_filenames:
    #         with open(fname) as infile:
    #             outfile.write(infile.read()) #Output single file