import { createRequire } from 'module';
const require = createRequire(import.meta.url);

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://feen:feen@cluster0.mo20d.mongodb.net/Song?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("MusicDataReporter");
  dbo.collection("Artists").find({}, { projection: { _id: 0, artist: 1, number_of_fans: 1 } }).toArray(function(err, result) {
    if (err) throw err;
    console.log(result[0]['artist']);

    var dps = [];

    var chart = new CanvasJS.Chart("chartContainer", {
		title:{
			text: "Music Data API : List of Fans"              
		},
		data: [              
		  {
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "column",
			dataPoints: dps,  
      }]
    });

    $.each(result, function(key, value){
      dps.push({x: value[0]['artist'], y: parseInt(value[0]['number_of_fans'])});
      console.log("Artist Name")
      console.log(value[0])
    });
    
    chart.render();
    
    db.close();
  });
});