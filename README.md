# Capstone
Capstone final project

## Project Overview
This will be a rock climbling web app. On it you will be able to see climbing routes at a local gym. You will be 
able to make a profile and will be able to see information on that specific route. The information 
would include rating, wall type, holds, and possibly beta (info on how to climb that route). You will also be 
able to up vote or down vote routes, check if you've completed them, and comment on them (not sure if there should
be both comments and beta). I will be using Vue and Bootstrap, and possibly open source libraries for the map 
graphics.

## Functionality
When a user goes to the home page they will see a banner and a brief explanation of the site. There will be a top 
nav for loging in, logging out and links to the home page, gyms around them, and their profile. On the profile page
you will be able to see routes you've completed and comments or beta you've given. On the gyms page you will see the
listed gyms that have a link to an overhead map of that gym's walls. On that map there will be pins that coordinate 
to route locations in that gym. The pin will be a link that will take you to an info page for that route. That is 
where you will be able to comment and see info for that specific route.

## Data Model

#### Gym(Model):
    name
    address
    map_info?

#### Route(Model):
    gym = foreign key (Gym)
    climb_type = foreign key (ClimbType)
    rating
    height
    holds = many to many (Hold)
    wall_type = foreign key (Wall)
    description
    beta
    user_beta = foreign key (User)
    comment = many to many (Comment)
    date_created 
    date_leaving

#### Hold(Model):
    hold 

#### Wall(Model):
    wall

#### ClimbType(Model):
    type
    

#### Comment(Model):
    text =
    date_created =
    user = foreign key (User)
    route = foreign key (Route)

#### User(Model):
    completed_routes = many to many (Route)


## Schedule

### Milestone 1 (Oct 23)
- Map prototype
- Models
- Creating a profile, loging in and out
- Simple index page with top nav

### Mileston 2 (Oct 26)
- Gym Page (integrating prototype)
- Route info page
- Comments


### Milestone (Oct 30)
- Styling
- Various fixing and what not




