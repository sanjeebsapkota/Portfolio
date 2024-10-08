from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


# Create your views here.
def home(request):
    return render (request,"home.html")


def about (request):
    return render (request,"about.html")


def projects(request):
    projects_show = [
        {
            'title': 'Todo List',
            'path': 'images/todo.jpg',
            'link': 'https://github.com/sanjeebsapkota/TODO',  # actual link
            'description': 'A simple todo list application to manage tasks efficiently.',
        },
        {
            'title': 'Recipe Website with CRUD',
            'path': 'images/recipe.PNG',
            'link': 'https://github.com/sanjeebsapkota/Recipe_Project',  # actual link
            'description': 'A recipe website allowing users to create, read, update, and delete recipes.',
        },
        {
            'title': 'Weather App',
            'path': 'images/weather.PNG',
            'link': 'https://github.com/sanjeebsapkota/Weather_app',  #  actual link
            'description': 'An application that provides weather forecasts and updates.',
        },
        {
            'title': 'Library Management System',
            'path': 'images/lms.PNG',
            'link': 'https://github.com/sanjeebsapkota/Library-Management-System',  # actual link
            'description': 'A system for managing library resources and user transactions.',
        },
        {
            'title': 'Django Login System',
            'path': 'images/login.jpg',
            'link': 'https://github.com/sanjeebsapkota/Django_Login_System',  # actual link
            'description': 'A user authentication system built with Django.',
        },
        {
            'title': 'Inventory Management System',
            'path': 'images/ims.PNG',
            'link': 'https://github.com/sanjeebsapkota/Inventory-Management-System',  # Replace with actual link
            'description': 'A system for tracking inventory levels and orders.',
        },
        {
            'title': 'Portfolio',
            'path': 'images/portfolio.jpg',
            'link': 'https://github.com/sanjeebsapkota/Portfolio-website',  # Replace with actual link
            'description': 'A personal portfolio showcasing projects and skills.',
        },
        {
            'title': 'Hospital Management System',
            'path': 'images/hms.jpg',
            'link': 'https://github.com/sanjeebsapkota/HMSAPI',  # Replace with actual link
            'description': 'A system for managing hospital operations and patient records.',
        },
    ]

    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experience = [
        {
            "company": "IT Department Chandika Distillery Pvt. Ltd",
            "position": "Junior Executive (SAP Consultant)",
            "location": "Kathmandu",
            "start_date": "Sep, 2022",
            "end_date": "Present",
            "description": [
                "Successfully implemented SAP Business One ERP Software, enhancing operational efficiency.",
                "Experienced in various modules within SAP-ERP, including Production, Accounting, and Inventory Management.",
                "Handling the SAP Issues and resolving them.",
                "Proficient in SAP Data Visualization Tools, particularly Microsoft Power BI.",
                "Experienced in SAP modules such as Sales, Production, Finance, and Inventory, with expertise in tasks such as GRPO, Purchase Order processing, outgoing and incoming payments, and internal reconciliation."
            ]
        },
        {
            "company": "Deurali Janta Pharmaceuticals Pvt. Ltd",
            "position": "Senior IT Assistant",
            "location": "Bashbari, Kathmandu",
            "start_date": "Oct, 2021",
            "end_date": "May, 2022",
            "description": [
                "Administered Windows Server 2016 and managed Hyper-V for virtualization.",
                "Conducted thorough issue verification and reported solutions promptly.",
                "Installing the Open Source Application as per the company’s requirements.",
                "System data Backup and Recovery.",
                "User account management."
            ]
        },
        {
            "company": "Retail Monitoring Department WorldLink Communications Ltd",
            "position": "Junior Assistant",
            "location": "Jawalakhel",
            "start_date": "Aug, 2019",
            "end_date": "Sep, 2021",
            "description": [
                "Assigned outages to the respective branch’s ONM (Outage Network Management) team members.",
                "Coordinated updates from nationwide deployed ONM team members, particularly for OLT and GPON-related issues.",
                "Monitoring the OLT and BRAS Traffic and verifying L2 Level Issue.",
                "Collect and analyze data related to network performance and customer issues.",
                "Generating reports to track trends and suggest improvements to prevent recurring issues.",
                "Ensuring the quality of service."
            ]
        },
        {
            "company": "WorldLink Communications Ltd",
            "position": "Technical Support Representative | CSR",
            "location": "Jawalakhel",
            "start_date": "Jan, 2019",
            "end_date": "Aug, 2019",
            "description": [
                "Provide step-by-step instructions to customers on setting up and configuring their internet equipment, including modems, routers, and other devices.",
                "Resolved system, hardware, and telephone issues improving efficiency among departments.",
                "IP phone, CCTV configuration and Troubleshooting.",
                "Escalate further technical issues to higher-level support or network engineering teams for quicker resolution."
            ]
        }
    ]
    return render(request, "experience.html", {"experience": experience})



def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

# def resume(request):
#     resume_path="myapp/resume.pdf"
#     resume_path=staticfiles_storage.path(resume_path)
#     if staticfiles_storage.exists(resume_path):
#         with open(resume_path,"rb") as resume_file:
#             response=HttpResponse(resume_file.read(),content_type="application/pdf")
#             response['Content-Disposition']= 'attachment'; filename="resume.pdf"
#             return response
#     else:
#         return HttpResponse("resume not found", status=404)

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']= 'attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)

