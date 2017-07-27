# postit

# API for postIT with Django Rest Framework 

This sample project have to do with user been able to create posts and also add comments.

## Dependencies

To setup and run the sample code, you're going to need `npm` from NodeJS available to install the frontend code.

## Setup

To setup and run the sample code you need to clone the repo
        
1. Create a virtualenv to isolate our package dependencies locally
    virtual env
    
2. Activate the virtual environment
    source env/bin/activate
    
3. Install Python Requirements

        pip install -r requirements.txt
        python setup.py develop  


## Routes

**POSTS**
----
  <_The User will be able to create posts_>

* **URL**

  <_/api/posts/create)_>
  
* **Method:**
  
  <_The request type_>

  `POST`
  
 *  **URL Params** 
 **Required:**
 `title=[CharField]`
 `content=[TextField]`
 `publish_date=[DateTime]`
 

* **URL**

  <_/api/posts/slug/edit)_>
  
* **Method:**
  
  <_The request type_>

  `PUT`
  
 *  **URL Params** 
 **Required:**
 `title=[CharField]`
 `content=[TextField]`
 `publish_date=[DateTime]`
 
 
 * **URL**

  <_/api/posts/slug/edit)_>
  
* **Method:**
  
  <_The request type_>

  `PUT`
  
 *  **URL Params** 
 **Required:**
 `title=[CharField]`
 `content=[TextField]`
 `publish_date=[DateTime]`
 
 
 * **URL**

  <_/api/posts/slug/)_>
  
* **Method:**
  
  <_The request type_>

  `GET`
  
  <_response_>
  url
  user
  id
  title
  slug
  markdown
  content
  published date
  comments(if any)
  
  * **URL**

  <_/api/posts/slug/delete)_>
  
* **Method:**
  
  <_The request type_>

  `DELETE`
  
  
  **COMMENTS**
----
  <_The User will be able to ADD COMMENTS_>

* **URL**

  <_/api/comments/create)_>
  
* **Method:**
  
  <_The request type_>

  `POST`
  
 *  **URL Params** 
 **Required:**
 `content=[TextField]`
 
 * **URL**

  <_/api/comments/?type=post&slug=my-title)_>
  
* **Method:**
  
  <_The request type_>

  `GET`
  
 <_response_>
 `url`
 `id`
 `content`
 `reply_count`
 `timestamp`
 
 
 * **URL**

  <_/api/comments/id)_>
  
* **Method:**
  
  <_The request type_>

  `PUT`
  
 *  **URL Params** 
 **Required:**
 `content=[TextField]`
 
 
 * **URL**

  <_/api/comments/id)_>
  
* **Method:**
  
  <_The request type_>

  `DELETE`
  
  
  
  **USERS**
----
  <_The User will be able to register and login_>

* **URL**

  <_/api/users/register)_>
  
* **Method:**
  
  <_The request type_>

  `POST`
  
 *  **URL Params** 
 **Required:**
 `username=[TextField]`
 `email=[TextField]`
 `password=[TextField]`
 
 * **URL**

  <_/api/users/login)_>
  
* **Method:**
  
  <_The request type_>

  `POST`
  
 *  **URL Params** 
 **Required:**
 `email=[TextField]`
 `password=[TextField]`
 
  
 
 
 
 
 
 

  
  
  
  

 
 

    
  


