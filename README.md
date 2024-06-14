## Flask Application Design

**Problem Statement (Hello World):** Create a web application that displays a simple message, "Hello, World!" to the user when they visit a specific URL. 

### HTML Files

- **hello.html:** This HTML file will contain the message "Hello, World!" and the necessary markup to display it in a web browser.
    - Contents:
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
        </html>
        ```

### Routes

- **home()**: This route will render the 'hello.html' file to display the message "Hello, World!" to the user.
    - Purpose: To define the URL and associate it with the function that handles the request.
    - Functionality: Flask will map the '/' URL to the 'home()' function. When a user visits the root URL (localhost:5000/), Flask will execute the 'home()' function, which returns the rendered 'hello.html' file, displaying the message "Hello, World!" in the browser.
        - Example:
            ```python
            @app.route('/')
            def home():
                return render_template('hello.html')
            ```