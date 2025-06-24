from app import app, db, Admin
from werkzeug.security import generate_password_hash

def setup_database():
    """Initialize the database and create default admin user"""
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user already exists
        existing_admin = Admin.query.filter_by(username='admin').first()
        if not existing_admin:
            # Create default admin user
            admin_user = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123')
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Default admin user created!")
            print("Username: admin")
            print("Password: admin123")
        else:
            print("✅ Admin user already exists!")
        
        print("✅ Database setup complete!")

if __name__ == '__main__':
    setup_database()
