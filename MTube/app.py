from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__ug__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mtube.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    youtube_url = db.Column(db.String(200), nullable=False)
    thumbnail_url = db.Column(db.String(200))
    category = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)

# Routes
@app.route('/')
def index():
    videos = Video.query.order_by(Video.date_added.desc()).all()
    return render_template('index.html', videos=videos)

@app.route('/video/<int:id>')
def video(id):
    video = Video.query.get_or_404(id)
    video.views += 1
    db.session.commit()
    related_videos = Video.query.filter_by(category=video.category).limit(4).all()
    return render_template('video.html', video=video, related_videos=related_videos)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and check_password_hash(admin.password_hash, password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    videos = Video.query.order_by(Video.date_added.desc()).all()
    return render_template('admin.html', videos=videos)

@app.route('/admin/add_video', methods=['POST'])
def add_video():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    title = request.form.get('title')
    description = request.form.get('description')
    youtube_url = request.form.get('youtube_url')
    thumbnail_url = request.form.get('thumbnail_url')
    category = request.form.get('category')
    
    video = Video(
        title=title,
        description=description,
        youtube_url=youtube_url,
        thumbnail_url=thumbnail_url,
        category=category
    )
    
    db.session.add(video)
    db.session.commit()
    flash('Video added successfully')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete_video/<int:id>', methods=['POST'])
def delete_video(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    video = Video.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash('Video deleted successfully')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create default admin user if it doesn't exist
        existing_admin = Admin.query.filter_by(username='admin').first()
        if not existing_admin:
            admin_user = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin_user)
            db.session.commit()
    
    # For deployment (Heroku, Railway, etc.)
    import os
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
