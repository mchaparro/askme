ping raspberrypi.mshome.net
ssh raspberrypi.mshome.net

username: pi
password: raspberry

https://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

RESET HEROKU DATABASE
heroku restart && heroku pg:reset DATABASE --confirm APP-NAME

google apps key
AIzaSyBteeZDjRtOcrEab02Wa-FHUFX_InsQibE


FLASK API led raspberry 
https://docs.dataplicity.com/docs/control-gpios-using-rest-api

RUN NGROK
 sudo -E flask run --host=0.0.0.0 --port=80
./ngrok http 80
http://d00c7686.ngrok.io


$.post( "http://4e6f0723.ngrok.io/led/green/?state=0", {'state':0}).done(function( data ) {
 console.log(data);
}));

$.post( "http://4e6f0723.ngrok.io/led/green/?state=0", { state: "0" })
  .done(function( data ) {
    console.log(data);
  });


 $.ajax({
            url: "https://cors.io/?http://4e6f0723.ngrok.io/led/green/?state=0",
            type: "POST",
            crossDomain: true,
            data: JSON.stringify({}),
            dataType: "json",
            success: function (response) {
                var resp = JSON.parse(response)
                alert(resp.status);
            },
            error: function (xhr, status) {
                alert("error");
            }
        });



heroku run python manage.py collectstatic --no-input