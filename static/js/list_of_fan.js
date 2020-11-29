var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://feen:feen@cluster0.mo20d.mongodb.net/Song?retryWrites=true&w=majority";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("MusicDataReporter");
  dbo.collection("Artists").find({}, { projection: { _id: 0, artist: 1, number_of_fans: 1 } }).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);

    var dps = [];

    var chart = new CanvasJS.Chart("chartContainer", {
		title:{
			text: "Music Data API : List of Fans"              
		},
		data: [              
		{
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "column",
			dataPoints: [
				function parseDataPoints () {
                    for (var i = 0; i <= result.length; i++)
                        for(var j = 0; j <= i.length; j++)
                            dps.push({label: result[i][j], y: result[i][j+1]});
                            console.log(dps)  
                };
                
			]
		}
		]
    });
    parseDataPoints();
    chart.options.data[0].dataPoints = dps;
    
    chart.render();
    
    db.close();
  });
});