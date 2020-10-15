# Capstone
Capstone final project

## Project Overview
This will be a podcast search website. It will allow you to search for podcasts by episode, name, or genre. There will
also be a random podcast button and a best by genre area. Users will be able to favorite podcasts and episodes and 
will be able to comment on them.

## Functionality
When a user goes to the home page they will see a banner and a brief explanation of the site. There will be a top 
nav for loging in, logging out and links to the home page, categories with top tens, the user's profile, and random 
(maybe). After searching for a podcast, a paginated list of cards will appear that match the search parameters. The 
cards will have the podcast's image, a link to the podcast, the genre(s), and a link to a seperate info page. On 
the info page there will be all of the above plus a description, an audio link, and a comment section. On the user's
profile page they will be able to see the podcasts that they've favorited, and will have a field for episodes that 
defaults to unseen, that they can change to seen. This will allow them to keep track of podcasts that they've 
already enjoyed.

## Data Model
There will be 5 models for this project. 

Podcast, Episode, Genre, Comment, and User

#### Podcast(Model):
    title = <br/>
    genre = many to many field (Genre) <br/>
    image = <br/>
    thumbnail = <br/>
    audio_length_sec = <br/>
    publisher =<br/>

#### Episode(Model):
    title =
    image = 
    link =
    audio_link =
    audio_length_sec =
    explicit_content = boolean field
    description =
    podcast = foreign key (Podcast)

#### Genre(Model):
    genre = 

#### Comment(Model):
    text =
    date_created =
    user = foreign key (User)

#### User(Model):
    favorite = foreign key (Episode)

## Schedule

### Milestone 1 (Oct 21)
- Models
- Search functionality by text and genre
- Creating a profile, loging in and out
- Simple index page with search bar and top nav

### Mileston 2 (Oct 26)
- Pagination
- Info page
- Comments
- Favorite episodes and see them in your profile

### Milestone (Oct 30)
- Styling
- (Maybe) Top ten by genre page
- (Maybe) Upvotes

