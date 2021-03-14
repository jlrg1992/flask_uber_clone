var app = new Framework7({
  root: '#app',
  name: 'My App',
  id: 'com.myapp.test',
  routes: [
    // Add your routes here
    // Example:
    /*
    {
      path: '/about/',
      url: 'about.html',
    },
    */
  ],
});

var mainView = app.views.create('.view-main');

function goto(url){
  window.location.replace(url);
}


dialog = app.dialog
if(typeof messages !== 'undefined'){
  for(msg of messages){
    dialog.alert(msg);
  }
}