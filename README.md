# BlogPostDjango

## Setup Instructions

<ol>
  <li>Clone This Project <code>git clone https://github.com/kabilan65/BlogPostDjango.git</code></li>
  <li>Go to Project Directory <code>cd BlogPostDjango</code></li>
  <li>Create a Virtual Environment <code>python -m venv env</code></li>
  <li>Activate Virtual Environment:
    <ul>
      <li>Windows: <code>env\Scripts\activate</code></li>
      <li>macOS/Linux: <code>source env/bin/activate</code></li>
    </ul>
  </li>
  <li>Install Requirements Package <code>pip install -r requirements.txt</code></li>
  <li>Migrate Database <code>python manage.py migrate</code></li>
  <li>Create Super User <code>python manage.py createsuperuser</code></li>
  <li>Finally Run The Project <code>python manage.py runserver</code></li>
</ol>

## Project Features

- **CRUD Operations for Posts**: Authenticated users can create, edit, and delete posts. Non-authenticated users can only view posts and leave comments. Only the author of a post can edit or delete their own post.
  
- **Commenting System**: Non-authenticated users can leave comments on posts, but they cannot delete them. Only the user who made the comment can delete their comment.
  
- **Search Functionality**: Users can search for posts using tags or keywords in the title or description.
  
- **User Authentication**: Implemented login, register, and logout functionalities to manage user access.

