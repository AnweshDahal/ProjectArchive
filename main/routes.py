from flask import render_template ,redirect, url_for
from main import app, db
from main.models import Projects
from main.forms import ProjectForm

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 Page Not Found")

@app.route('/')
@app.route('/home')
def home():
    project = Projects.query.all()
    languages = {
        "Java": len(Projects.query.filter_by(programming_lang="Java").all()),
        "Python": len(Projects.query.filter_by(programming_lang="Python").all()),
        "HTML": len(Projects.query.filter_by(programming_lang="HTML").all())
    }
    return render_template('home.html', projects = project, language = languages, title = "Home")

@app.route('/downloads')
def downloads():
    project = Projects.query.all()

    languages = {
        "Java": len(Projects.query.filter_by(programming_lang="Java").all()),
        "Python": len(Projects.query.filter_by(programming_lang="Python").all()),
        "HTML": len(Projects.query.filter_by(programming_lang="HTML").all())
    }
    return render_template('download.html', projects = project, language = languages, title = "Download")

@app.route('/contacts')
def contacts():
    project = Projects.query.all()

    languages = {
        "Java": len(Projects.query.filter_by(programming_lang="Java").all()),
        "Python": len(Projects.query.filter_by(programming_lang="Python").all()),
        "HTML": len(Projects.query.filter_by(programming_lang="HTML").all())
    }
    return render_template('contacts.html', projects = project, language = languages, title = "Contacts")

@app.route('/proj8@rchv-upd8+pr0j£c+/<int:id>', methods = ['GET', 'POST'])
def update_project(id):
    project = Projects.query.get_or_404(id)
    projectForm = ProjectForm()
    projectForm.project_name.data = project.project_name
    projectForm.version.data = project.version
    projectForm.language.data = project.language
    projectForm.dependency.data = project.dependency
    projectForm.script.data = project.script
    projectForm.markup.data = project.markup
    projectForm.style.data = project.style
    projectForm.github.data = project.github
    projectForm.programming_lang.data = project.programming_lang
    if projectForm.validate_on_submit():
        project.project_name=projectForm.project_name.data
        project.version=projectForm.version.data
        project.language=projectForm.language.data
        project.dependency=projectForm.dependency.data
        project.script=projectForm.script.data
        project.markup=projectForm.markup.data
        project.style=projectForm.style.data
        project.github=projectForm.github.data
        project.programming_lang=projectForm.programming_lang.data
        db.session.commit()
        return redirect(url_for('home'))

    languages = {
        "Java": len(Projects.query.filter_by(programming_lang="Java").all()),
        "Python": len(Projects.query.filter_by(programming_lang="Python").all()),
        "HTML": len(Projects.query.filter_by(programming_lang="HTML").all())
    }
    return render_template('addProject.html', language=languages, title="Add Project", form=projectForm)
    
@app.route('/dcmnt@rchv-a+pr0j£t', methods = ['GET','POST'])
def add_project():
    projectForm = ProjectForm()
    if projectForm.validate_on_submit():
        project = Projects(project_name = projectForm.project_name.data, 
        version = projectForm.version.data, 
        language = projectForm.language.data,
        dependency=projectForm.dependency.data,
        script = projectForm.script.data,
        markup = projectForm.markup.data,
        style = projectForm.style.data,
        github = projectForm.github.data,
        programming_lang=projectForm.programming_lang.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('home'))
    
    languages = {
        "Java": len(Projects.query.filter_by(programming_lang="Java").all()),
        "Python": len(Projects.query.filter_by(programming_lang="Python").all()),
        "HTML": len(Projects.query.filter_by(programming_lang="HTML").all())
    }
    return render_template('addProject.html', language = languages, title = "Add Project", form=projectForm)
