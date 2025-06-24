# MTube - YouTube-like Entertainment Website

A modern, admin-managed entertainment website with YouTube-like interface for curated content.

## Features

- 🎥 **Admin Content Management** - Upload and manage YouTube videos
- 🎨 **YouTube-like Interface** - Modern, responsive design
- 🔐 **Admin Authentication** - Secure login system
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🗂️ **Content Categories** - Entertainment, Music, Gaming, Sports, Education, Comedy, News
- 📊 **View Tracking** - Track video views and engagement
- 🎬 **Video Player** - Embedded YouTube player with custom styling

## Screenshots

### Homepage
- Clean, modern interface with video grid layout
- Hero section with welcome message
- Category-based content organization

### Admin Dashboard
- Easy video upload form
- Content management table
- Video analytics and controls

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/mtube.git
cd mtube
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Initialize the database:**
```bash
python setup.py
```

4. **Run the application:**
```bash
python app.py
```

5. **Access the website:**
- Homepage: http://localhost:5000
- Admin Login: http://localhost:5000/admin/login

## Default Admin Credentials

- **Username:** admin
- **Password:** admin123

⚠️ **Important:** Change these credentials in production!

## Usage

### For Admins:
1. Login with admin credentials
2. Access the dashboard to add new videos
3. Fill in video details (title, description, YouTube URL, thumbnail, category)
4. Manage existing videos (view, delete)

### For Visitors:
1. Browse videos on the homepage
2. Click on any video to watch
3. Explore different categories
4. Enjoy curated entertainment content

## Project Structure

```
mtube/
├── app.py                 # Main Flask application
├── setup.py              # Database initialization
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── admin.html        # Admin dashboard
│   ├── login.html        # Admin login
│   └── video.html        # Video player page
├── static/
│   └── css/
│       └── styles.css    # Main stylesheet
└── mtube.db             # SQLite database (created after setup)
```

## Technologies Used

- **Backend:** Python Flask
- **Database:** SQLite with Flask-SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Authentication:** Werkzeug password hashing
- **Video Integration:** YouTube embed API

## Deployment

### GitHub Pages (Static hosting)
This project requires a Python backend, so GitHub Pages won't work directly.

### Heroku Deployment
1. Create a `Procfile`:
```
web: python app.py
```

2. Update `app.py` for production:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Railway/Render Deployment
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/mtube/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## Roadmap

- [ ] User registration and profiles
- [ ] Video comments system
- [ ] Advanced search and filtering
- [ ] Video upload from local files
- [ ] Analytics dashboard
- [ ] Social media integration
- [ ] Video playlists
- [ ] Dark/light theme toggle

---

**Made with ❤️ for entertainment content creators and viewers**
