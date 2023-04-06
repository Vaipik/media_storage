### Here will be actions
___
# Media storage web application
___

This is a fullstack PET project with `FastAPI` as backend and `Vue.js` as frontend.
The idea is to make application where users can store their memories such as photos and videos from their trips
or events.  \
Developing will be performed by TDD ideology with attention to clean architecture(at least i will try)
___
At the first approach user will be able to create event and add media to this event.
Each media will have an optional description and will be downloaded directly to cloud storage `GoogleDrive`.  
`Celery` will be used for uploading files in background  
`Redis` will be used to cache files
