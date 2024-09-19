# **TagLink**

## **Introduction**

The TagLink Platform allows users to register, create portfolios, and showcase their projects in an interactive community environment. Users can like and comment on other users' portfolios, manage multiple projects, and connect with professionals through an intuitive user interface.

- **Live Site**: [Deployed Site URL](#)
- **Project Blog Article**: [Final Project Blog](#)
- **Author LinkedIn**: [Your LinkedIn](www.linkedin.com/in/hassanakinade)

---

## **Installation**

To get started with the project locally, follow these steps:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/LichtCode/taglink.git
   cd taglink
   ```
2. **Create a Virtual Environment**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the Database**

    Ensure your PostgreSQL database is running, and run the following commands:

    - Migrate the database:

        ```bash
        python manage.py migrate
        ```
    - Create a superuser:

        ```bash
        python manage.py createsuperuser
        ```
5. **Run the Server**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```
6. **Access the Application**

    Navigate to ```http://127.0.0.1:8000```in your browser.

---

# **Usage**

## User Registration and Authentication

- **Register**: Users can register using their username, email, and password.
- **Profile Update**: After registration, users can log in and update their profiles with a bio, profile picture, and social links (GitHub, LinkedIn).
- **Authentication**: The platform supports secure authentication with session management and a "Remember Me" feature.

## Portfolio and Project Management

- **Create a Portfolio**: Registered users can create one or more portfolios.
- **Manage Projects**: Within each portfolio, users can add multiple projects, including details like titles, descriptions, links, and project images.
- **Track Changes**: Projects and portfolios are automatically timestamped for creation and last modification.

## Interactions

- **Like Portfolios**: Users can like or unlike portfolios.
- **Comment on Portfolios**: Users can leave comments on portfolios and engage with others.
- **Engagement Tracking**: The number of likes and comments on each portfolio is displayed.