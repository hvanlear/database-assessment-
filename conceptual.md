### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  - open-source relational database management system emphasizing extensibility and SQL compliance

- What is the difference between SQL and PostgreSQL?

* PostgreSQL is an advanced object-relational database management system that uses Structured Query Language (SQL) in addition to its own procedural language

- In `psql`, how do you connect to a database?

  - \c 'database name'

- What is the difference between `HAVING` and `WHERE`?

  - The main difference between WHERE and HAVING clause comes when used together with GROUP BY clause, In that case WHERE is used to filter rows before grouping and HAVING is used to exclude records after grouping.

- What is the difference between an `INNER` and `OUTER` join?

* Inner joins don’t include non-matching rows; whereas, outer joins do include them.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

* LEFT JOIN: returns all rows from the left table, even if there are no matches in the right table. RIGHT JOIN: returns all rows from the right table, even if there are no matches in the left table.

- What is an ORM? What do they do?

* Object-relational-mapping is the idea of being able to write queries like the one above, as well as much more complicated ones, using the object-oriented paradigm of your preferred programming language.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?

  - In traditional HTTP situations, your browser loads a page that it receives from a server. For example, when you submit a form, your page usually refreshes to show a new page that confirms the information was submitted. With AJAX, however, you can update a page without reloading it entirely.

- What is CSRF? What is the purpose of the CSRF token?

* This token, called a CSRF Token or a Synchronizer Token, works as follows: The client requests an HTML page that contains a form. ... When the client submits the form, it must send both tokens back to the server. The client sends the cookie token as a cookie, and it sends the form token inside the form data.

- What is the purpose of `form.hidden_tag()`?

* The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks.
