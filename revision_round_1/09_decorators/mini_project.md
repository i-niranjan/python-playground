# Mini Project: Function Logger

Build decorators for a tiny application.

Create these decorators:

- `log_call`: prints when a function starts and ends
- `require_login`: blocks function if `is_logged_in` is false
- `uppercase_result`: converts a string return value to uppercase

Use them on functions like:

- view_profile()
- edit_profile()
- get_welcome_message()

Extra:

- Make decorators work with arguments.
- Use `functools.wraps`.

