# Restaurant Offers Project

This Django project manages restaurant offers with integrated chat functionality and location-based features.

## Project Structure

### Core Configuration
- [Settings](/restaurant_offers/settings.py) - Main Django configuration file
- [URLs](/restaurant_offers/urls.py) - Main URL configuration

### Apps
- [Accounts](/accounts/) - User authentication and profiles
- [Offers](/offers/) - Restaurant offers management
- [Chat](/chat/) - Real-time chat functionality

### Configuration Files
- [Requirements](/requirements.txt) - Project dependencies
- [.env.example](/.env.example) - Environment variables template

## Settings Configuration

### Environment Variables
- Uses `python-dotenv` for environment variable management
- Loads sensitive configuration from `.env` file
- Key variables include:
  - `SECRET_KEY`
  - Database credentials
  - Google Maps API key

### Security Settings
- `SECRET_KEY`: Loaded from environment variables with a fallback default (not recommended for production)
- `DEBUG`: Currently set to `True` (should be `False` in production)
- `ALLOWED_HOSTS`: Empty list (should be configured for production)

## Applications

### Installed Apps
1. **Django Built-in Apps**
   - admin
   - auth
   - contenttypes
   - sessions
   - messages
   - staticfiles

2. **Third-party Apps**
   - rest_framework

3. **Local Apps**
   - accounts
   - offers
   - chat

## Database Configuration

- Uses PostGIS (Geographic Information System extension for PostgreSQL)
- Configuration variables:
  - `DB_NAME`: Default 'restaurant_offers'
  - `DB_USER`: Default 'postgres'
  - `DB_PASSWORD`: Default '123456'
  - `DB_HOST`: Default 'localhost'
  - `DB_PORT`: Default '5432'

## Authentication

- Custom user model: `accounts.User`
- Login redirect: 'profile'
- Logout redirect: 'login'
- Login URL: 'login'

### Password Validation
Includes standard Django password validators:
- UserAttributeSimilarityValidator
- MinimumLengthValidator
- CommonPasswordValidator
- NumericPasswordValidator

## File Management

### Static Files
- URL: '/static/'
- Root: 'staticfiles'
- Additional directories: 'static'

### Media Files
- URL: '/media/'
- Root: 'media'

## REST Framework Configuration

### Authentication Classes
- SessionAuthentication
- BasicAuthentication

### Default Permissions
- IsAuthenticated

## Additional Settings

### Internationalization
- Language: English (US)
- Timezone: UTC
- Internationalization enabled
- Localization enabled
- Timezone support enabled

### Templates
- Uses Django template backend
- Template directories configured in 'templates' folder
- Includes standard context processors plus media context processor

### Google Maps Integration
- API key loaded from environment variables

## Setup Instructions

1. Clone the repository: 