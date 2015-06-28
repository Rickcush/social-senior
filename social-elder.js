Router.route('/', function(){
  this.render('home');
});
Router.route('/settings', function(){
  this.render('settings',{
    data: {
      name: "battlehacker",
      phoneNumber: "520-321-5592",
      trustedNumbers: [
        {name: "Clark", number: '444-444-4444'},
        {name: "Derek", number: '555-555-5555'},
        {name: "Ricky", number: '333-333-3333'},
      ]
    }
  });
});

Router.route('/request', function(){
  var data = {
    userName: 'Clark',
    type: 1,
    _id: this.params._id
  };
  this.render('request', {
    data: data
  });
});
Router.route('/request/:_id/:_type', 'POST', function(){
  var data = {
    piNumber: this.params._id,
    userName: 'Clark', // find user name
  };
  console.log(parseInt(this.params._type));
  switch(parseInt(this.params._type)){
    case(1):
      data.type = "groceries";
      break;
    case(2):
      data.type = "a conversation";
      break;
    case(3):
      data.type = "help";
      break;
    default:
      window.alert('This route is not supported!');
      break;
  }

  this.render('request', {
    data: data
  });
});

if (Meteor.isClient) {

  Template.hero.onCreated(function(){
    Accounts.ui.config({
    }, function(){
      console.log("wut");
    });


    Accounts.onLogin(function(){
      console.log(Meteor.user());
      // redirect to settings on login
      window.location.href = "./settings";
    });
  });

  Template.hero.events({
    'click .button': function(){
      $("html,body").animate({scrollTop: window.innerHeight}, 600);
    }
  });

  Template.services.helpers({
    service: function(){
      return [{
        name: 'food',
        tagline: 'Grocery delivery in under a hour.',
        logo: '/imgs/instacart.png',
        attribution: 'InstaCart',
        disabled: true,
        attributionLink: 'https://www.instacart.com/',
        background: '/imgs/grocery-shopping.jpg'
      },
      {
        name: 'help',
        tagline: 'Moving, cleaning, and repair work.',
        logo: '/imgs/taskrabbit.png',
        attribution: 'TaskRabbit',
        disabled: true,
        attributionLink: 'https://www.taskrabbit.com/',
        background: '/imgs/help.jpg'
      },
      {
        name: 'conversation',
        tagline: 'Contact family and friends for some company.',
        logo: '/imgs/twilio.svg',
        attribution: 'Twilio',
        disabled: false,
        attributionLink: 'https://www.twilio.com/',
        background: '/imgs/conversation.jpg'
      }];
    }
  });

}


if (Meteor.isServer) {

  Meteor.startup(function () {
    Accounts.onCreateUser(function(options, user){
      //this.redirect('settings');
      return user;
    });
    // code to run on server at startup
  });
}
