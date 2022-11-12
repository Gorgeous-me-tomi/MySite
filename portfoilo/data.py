from blog import views as blog_data

experties = [
    {
        'color':  'gold',
        'icon': '<i class="bi bi-lightbulb-fill"></i>',
        'title': 'Inovations',
        'writeup': "According to wikipedia inovation means 'the pratical implementation of ideas that result in the introduction of new goods or services', This literally explains ME. ",
    },

    {
        'color': 'blue',
        'icon': '<i class="bi bi-code-slash"></i>',
        'title': 'Web Development',
        'writeup': "Web development is another field i really like because it encourages me to actualize my interests through innovations, designs, debugging amongst others.",
    },

    {
        'color': 'darkred',
        'icon': '<i class="bi bi-lock-fill"></i>',
        'title': 'Data Encryption',
        'writeup': 'My online tutor Dr.Angela Yu made me understand how important data encrypting is and taught me how to encrypt data to the safest.',
    },

    {
        'color': 'purple',
        'icon': '<i class="bi bi-palette"></i>',
        'title': 'Graphics Design',
        'writeup': "I also specialized in the graphics field; designing flyers, business cards and logos for different clients."
    },

    {
        'color': '#b13f44',
        'icon': '<i class="bi bi-bug-fill"></i>',
        'title': 'Debugging',
        'writeup': "Through my years of coding and creating stunning projects, have been dealing with a lot of errors and hence developed the ability to debbug.",
    },

    # {
    #     'color': 'darkred',
    #     'icon': '<i class="fa-solid fa-chart-line"></i>',
    #     'title': 'Data Analysis',
    #     'writeup': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Mollitia, explicabo! Recusandae, necessitatibus tenetur?',
    # },

]


portfolio = [
    {
        'id': 1,
        'name': 'T-Sketch',
        'link': 'https://t-sketch-app.herokuapp.com/',
        'image': 't-sketch-screenshot.PNG',
        'descriptions': 'lorem ipsum',
        'category': 'Web Application',

    },

    {
        'id': 2,
        'name': 'T-Blog',
        'link': 'https://tomisinerinle.herokuapp.com/blog',
        'image': 'T-Blog.PNG' ,
        'descriptions': 'lorem ipsum',
        'category': 'Web Application',
    },    

    # {
    #     'id': 3,
    #     'name': 'T-Blog',
    #     'link': 'https://jumia.com',
    #     'image': 't-sketch-screenshot.PNG',
    #     'descriptions': 'lorem ipsum',
    #     'category': 'Web Application',  
    # },

    {
        'id': 3,
        'name': 'DaystarChapel',
        'link': None,
        'image': 'Daystar Chapel flyer3.png',
        'descriptions': 'lorem ipsum',
        'category': 'Graphics Design(Flyer)',
    },

    
    {
        'id': 4,
        'name': 'EaglesWingsRide',
        'link': None,
        'image': 'eagleswingsrideflyer.png',
        'descriptions': 'lorem ipsum',
        'category': 'Graphics Design(Flyer)',
    },

    {
        'id': 5,
        'name': 'KanLaitan Limited',
        'link': None,
        'image': 'Kan laitan ltd.jpg',
        'descriptions': 'lorem ipsum',
        'category': 'Graphics Design(Logo)',
    },


    
]


testimonials = [

     {
        'name': 'Desmond',
        'image': 'Desmond-img.png',
        'content': 'I once taught Him, He is very good at assimilation, quick learner also filled with a lot of breath taking ideas.',
        'job': 'FullStack Developer'
    },

    {
        'name': 'Tobi',
        'image': 'Tobi-Img.png',
        'content': 'He is just from a different world.',
        'job': 'Application Developer',
    },

    {
        'name': 'Tunmise',
        'image': 'male_img.png',
        'content': 'He is a very good and talanted programmer filled with innovations, ideas, basically all what you expect from an experienced programmer.',
        'job': ''
    },  


]


blog_posts = blog_data.posts


