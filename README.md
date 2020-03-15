# Eddie Brett WEBSITE

I want to create a dynamics, clean, user friendly website where users can navigate through a webstore, blogs and music etc with minimal clicks. This is not a corparate website and i do not want it to feel like one, nor is it a sight that will reguarly needs up dating, with that in mind i dont want to other complicate information but i want it to be easy for adminastrative users to update or add information.
 
## UX
 
The users will want to find our website from google, which is why we've added meta tags to all of our pages. 
Users will want to know what Eddie is up to, and so we will include a blog section field with easy to update stories.
Users might want to know who Eddie is and so we will include videos and work that he has previously done.
User will want to buy merchandise and so we will make an online store.
Users may wish to contact Eddie so we will include a contact form.
Users will want to get a general sense of what Eddie Brett is about and so we will make sure all styling and written represents that of an approachable, humorous street poet from east london. 

Please find my wireframes for the poject, alternatively located in /media/images/readme_pics/     :

mobile:
![Image description](/workspace/eddiewebsite2020/static/media/images/readme_pics/iPhone XR-XS Max-11 – 1.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 2.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 3.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 4.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 5.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 6.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 7.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 8.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/iPhone XR-XS Max-11 – 9.png)

desktop:
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/hi-fi wireframe.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 1.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 2.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 3.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 4.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 5.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 6.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 7.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 8.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 9.png)
![Image description](/workspace/eddiewebsite2020//static/media/images/readme_pics/Web 1920 – 10.png)


## Features

The home page is the first page that visitor will see and so i have placed a striking picture across the whole of the page to gice the user a true understanding of who Eddie Brett is imediately. 

I wanted the music page to feel like a collage. A varied mixture of the different things that Eddie has worked on. This page can easily grow and adapt as more work becomes available. Users wanting to see material are presented with various music and video options. I looked at carousel options but i wanted the user to get an instant sense of the breadth of the work rather than have to scrool through and work for it.

The shop page can easily be added to or change from the django admin page and superaccounts can be set up to access this. I refrained from including front end login pages for admin as a security caution. They aren't ever going to be more than 10 things for sale so i was quite happy to let this space be spread out and celebrate the things for sale. The language used reflect the brand of Eddie.

The contact page is very matter of fact. Not busy with infomation just a very clear box and oportunity for users to connect with the project if they want. I used the mailto: function to start a fresh page so that the user felt a personal connection with the message rather than just be subjected to another text box on a website that might go nowhere. Letting the user see an email feels personal.

 
### Existing Features
- The mental game is just a bit of additional fun to give users a reason to return to site, whilst researching other artists i couldn't see any sites with this can of quirk and so i thought it would be a cool thing to add.
### Features Left to Implement
- Once the project is in full swing and mate is touring we will also create a new page called 'touring' a gig type poster designed in photoshop to relay all of the information regarding gig dates and upcoming shows.
- the youtube videos take quite a while to load so i want to add some spinners to let the user know something is coming.

## Technologies Used

I've used the bootstrap framework https://getbootstrap.com/ because of its ease of use and clear layouts. I have used google fonts https://fonts.google.com/ to give my site some interesting asthetically pleasing fonts that tie in well with the brand. I have embedded youtube iFrames in my site because they are a fantastic video player and the format is known to the user degraphic. I have made my site with HTML5 and CSS. I have used a custom domaine name purchased from Go daddy. www.godaddy.com. I have used Javascript https://www.javascript.com/ to my an automatic slug writer to uniform the urls and blog names, and for making a card game.

- https://www.djangoproject.com/ ive used the django framework to make the website dynamics and easier to maintain.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- I've used stripe https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450310&utm_term=stripe%20payments&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQiA1-3yBRCmARIsAN7B4H3aS_G15nYFWEdGylS_fxa8PD5oqnMCz1ih70RQomw1OSRsHZZJ4ywaAsjgEALw_wcB to process the payments in my shop application.


## Testing

I tested the code using the mark up validation website https://validator.w3.org/ and addressed any errors it picked up. I used the google chrome inspect tool to check the functionality on various devices. I got friends to test the site on their devices in order to get some honest feedback on the ease of use and to pick up any problems i had over looked. I clicked on every hyperlink to ensure that i arrived at the correct destination. I clicked play on all of the videos to make sure they played and that they displayed the correct content.

Using mobile first design was a great way to ensure that the site was asthetically pleasing across all devices.

I sent test emails to the email address provided in the contact page to ensure that that feature was working.



## Deployment

When i have made a change to my website i commit the update and push it to GitHub. When i have made a change that i want to upload i type in the terminal: 'git init' Then i add the file i have updated for exaple: 'git add readme.md' I then add a note of what has been updated and commit the files staged in the local repository: 'git commit -m "updated readme file to be more specific and include UX drawings"' and then finally: 'git push -u origin master' This pushes the changes in the local repository to github. I am hosting my site on Heroku which works with databases; https://dashboard.heroku.com/ . Ive purchased the domaine www.eddiebrett.com and so that is where the site will be pointed to. I am storing all of my static files in an s3 bucket using amazon AWS cloud facilities https://aws.amazon.com/ .


## Credits

### Content
- Honest EP link to spotify- https://open.spotify.com/album/7ytgV7ClfdXbbvDhF8W9mJ?si=1U9IUXQaQDiVKUyhy6vGqg This and that album link to spotify- https://open.spotify.com/album/4V88ivH6YwYTe1w6q8wKvd?si=uDIBxPA7SJuwe3QFYB2hmA Riots music video link to youtube- https://www.youtube.com/watch?v=nqmcgX7WKdo Honest music video link to youtube- https://www.youtube.com/watch?v=gPPHRwWlGQM Lost boy poetry link to youtube- https://www.youtube.com/watch?v=0tRBmbi65zc Dirtywknd documentary link to youtube- https://www.youtube.com/watch?v=NkpMZbQsXAM

### Media
- Photographs of mate taken by BradHPhotos @MirumFilms of which Eddie Brett owns the rights to.

### Acknowledgements

- My design reference points were lifestyle fashions brands such as; adidas and supreme. Photographers suchs as AZCaptures. I also looked at poets, musicians and rappers such as Ratboy, George the poet, Rizzle Kickz, Tyler the creator/ odd future, George Ezra, Mac Demarco and Al the Native to give me a sense of what was happening, what works, what doesn't and how to avoid being a copycat.
- I followed a youtube series by web ninja to build the blog: https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc

- I used a youtube tutorial to build the card game: https://www.youtube.com/watch?v=28VfzEiJgy4&t=4s
- page loader video https://www.youtube.com/watch?v=xuA83OYTE7I

The github url is : https://eddiebrett.github.io/eddiewebsite2020/

Heroku url is : https://eddie-ecommerce2.herokuapp.com/

the web url is : eddiebrett.com